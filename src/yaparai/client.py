"""HTTP client for YaparAI Public API."""

from __future__ import annotations

import asyncio
import httpx

from yaparai.config import YAPARAI_API_KEY, YAPARAI_BASE_URL


class YaparAIClient:
    """Thin async HTTP wrapper around the YaparAI Public API."""

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
                "Set it as an environment variable or pass it to the constructor."
            )

        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "User-Agent": "yaparai-mcp/0.1.0",
        }

    async def generate(self, request: dict) -> dict:
        """Start a generation job. Returns job info."""
        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.post(
                f"{self.base_url}/v1/public/generate",
                json=request,
                headers=self.headers,
            )
            resp.raise_for_status()
            return resp.json()

    async def get_job(self, job_id: str) -> dict:
        """Get job status and result."""
        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.get(
                f"{self.base_url}/v1/public/jobs/{job_id}",
                headers=self.headers,
            )
            resp.raise_for_status()
            return resp.json()

    async def get_balance(self) -> dict:
        """Get credit balance."""
        async with httpx.AsyncClient(timeout=10) as client:
            resp = await client.get(
                f"{self.base_url}/v1/public/balance",
                headers=self.headers,
            )
            resp.raise_for_status()
            return resp.json()

    async def get_models(self) -> dict:
        """List available models and their credit costs."""
        async with httpx.AsyncClient(timeout=10) as client:
            resp = await client.get(
                f"{self.base_url}/v1/public/models",
                headers=self.headers,
            )
            resp.raise_for_status()
            return resp.json()

    async def wait_for_result(
        self,
        job_id: str,
        timeout: int = 120,
        poll_interval: int = 3,
    ) -> dict:
        """
        Poll job status until completed or timeout.

        Returns the final job status dict with result_url.
        """
        elapsed = 0
        while elapsed < timeout:
            job = await self.get_job(job_id)
            status = job.get("status", "")

            if status == "succeeded":
                return job
            if status == "failed":
                error = job.get("error_message", "Unknown error")
                raise RuntimeError(f"Job failed: {error}")

            await asyncio.sleep(poll_interval)
            elapsed += poll_interval

        raise TimeoutError(f"Job {job_id} did not complete within {timeout}s")
