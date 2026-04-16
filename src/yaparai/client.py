"""HTTP client for YaparAI Public API."""

from __future__ import annotations

import asyncio
import httpx

from yaparai.config import YAPARAI_API_KEY, YAPARAI_BASE_URL

# Module-level client for connection reuse across tool calls
_shared_client: httpx.AsyncClient | None = None


def _get_headers(api_key: str) -> dict:
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "User-Agent": "yaparai-mcp/0.2.0",
    }


class YaparAIClient:
    """Async HTTP wrapper around the YaparAI Public API.

    Reuses a shared httpx.AsyncClient across calls for connection pooling.
    """

    def __init__(
        self,
        api_key: str | None = None,
        base_url: str | None = None,
    ):
        self.api_key = api_key or YAPARAI_API_KEY
        self.base_url = (base_url or YAPARAI_BASE_URL).rstrip("/")

        if not self.api_key:
            raise ValueError(
                "YAPARAI_API_KEY is not set. "
                "Get your API key at https://www.yaparai.com/settings "
                "and set the YAPARAI_API_KEY environment variable."
            )

        self.headers = _get_headers(self.api_key)

    async def _client(self) -> httpx.AsyncClient:
        """Return a shared async client for connection reuse."""
        global _shared_client
        if _shared_client is None or _shared_client.is_closed:
            _shared_client = httpx.AsyncClient(
                base_url=self.base_url,
                headers=self.headers,
                timeout=httpx.Timeout(30.0, connect=10.0),
            )
        return _shared_client

    async def _request(self, method: str, path: str, **kwargs) -> dict:
        """Make an HTTP request with error handling."""
        client = await self._client()
        try:
            resp = await client.request(method, path, **kwargs)
        except httpx.ConnectError:
            raise ConnectionError(
                f"Cannot connect to YaparAI API at {self.base_url}. "
                "Check your internet connection."
            )
        except httpx.TimeoutException:
            raise TimeoutError(
                "YaparAI API request timed out. The service may be busy — try again."
            )

        if resp.status_code == 401:
            raise PermissionError(
                "Invalid API key. Check your YAPARAI_API_KEY or generate "
                "a new one at https://www.yaparai.com/settings"
            )
        if resp.status_code == 402:
            raise RuntimeError(
                "Insufficient credits. Top up at https://www.yaparai.com/pricing"
            )
        if resp.status_code == 429:
            raise RuntimeError(
                "Rate limit exceeded. Please wait a moment and try again."
            )

        resp.raise_for_status()
        return resp.json()

    async def generate(self, request: dict) -> dict:
        """Start a generation job. Returns job info with job_id."""
        return await self._request("POST", "/v1/public/generate", json=request)

    async def get_job(self, job_id: str) -> dict:
        """Get job status and result."""
        return await self._request("GET", f"/v1/public/jobs/{job_id}")

    async def get_balance(self) -> dict:
        """Get credit balance."""
        return await self._request("GET", "/v1/public/balance")

    async def get_models(self) -> dict:
        """List available models and their credit costs."""
        return await self._request("GET", "/v1/public/models")

    async def wait_for_result(
        self,
        job_id: str,
        timeout: int = 120,
        poll_interval: int = 3,
    ) -> dict:
        """Poll job status until completed or timeout.

        Returns the final job status dict with result_url.
        Raises RuntimeError on failure, TimeoutError on timeout.
        """
        elapsed = 0
        while elapsed < timeout:
            job = await self.get_job(job_id)
            status = job.get("status", "")

            if status == "succeeded":
                return job
            if status == "failed":
                error = job.get("error_message") or job.get("error") or "Unknown error"
                raise RuntimeError(f"Generation failed: {error}")

            await asyncio.sleep(poll_interval)
            elapsed += poll_interval

        raise TimeoutError(
            f"Job {job_id} is still processing after {timeout}s. "
            f"Use get_job_status('{job_id}') to check later."
        )
