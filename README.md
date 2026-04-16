# YaparAI MCP Server

Generate AI images, videos, and music directly from **Claude Desktop**, **Cursor**, **Windsurf**, and other MCP-compatible AI assistants.

[![PyPI](https://img.shields.io/pypi/v/yaparai)](https://pypi.org/project/yaparai/)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/pypi/pyversions/yaparai)](https://pypi.org/project/yaparai/)

## What is YaparAI?

[YaparAI](https://www.yaparai.com) is an all-in-one AI content creation platform with 16+ AI models:

- **Image Generation** — Flux, SDXL, Imagen 4 (text-to-image, image-to-image)
- **Video Generation** — Veo 3.1, Kling (text-to-video, image-to-video)
- **Music Generation** — Suno v4 (full songs with vocals, instrumentals)
- **Image Editing** — Background removal, face swap, style transfer
- **E-commerce** — Virtual try-on, AI mannequin for product photos
- **Avatar** — Lip sync talking avatars from photos

## Quick Start

### 1. Install

```bash
pip install yaparai
```

### 2. Get your API Key

1. Sign up at [yaparai.com](https://www.yaparai.com) (100 free credits)
2. Go to **Settings > API Keys**
3. Create a new key — copy it (shown only once!)

### 3. Configure Claude Desktop

Edit your Claude Desktop config (`Settings > Developer > Edit Config`):

```json
{
  "mcpServers": {
    "yaparai": {
      "command": "yaparai",
      "env": {
        "YAPARAI_API_KEY": "yap_live_your_key_here"
      }
    }
  }
}
```

### 4. Use it!

In Claude Desktop, just ask:

> "Generate an image of a sunset over Istanbul"

> "Create a 30-second lo-fi music track"

> "Make a video of a cat walking on a beach"

> "Remove the background from this image: https://example.com/photo.jpg"

> "Check my credit balance"

## Available Tools (13)

### Generation

| Tool | Description | Cost |
|------|-------------|------|
| `generate_image` | Generate images from text prompts (Flux, SDXL, Imagen 4) | ~6 credits |
| `generate_video` | Generate videos from text or images (Veo 3.1, Kling) | ~350 credits |
| `generate_music` | Generate music from text descriptions (Suno v4) | ~14 credits |
| `generate_music_video` | Generate music + matching video combined | ~364 credits |

### Image Editing

| Tool | Description | Cost |
|------|-------------|------|
| `transform_image` | Transform an image using AI (img2img style transfer) | ~6 credits |
| `remove_background` | Remove background from any image | ~2 credits |
| `swap_face` | Swap faces in an image | ~6 credits |

### E-commerce

| Tool | Description | Cost |
|------|-------------|------|
| `virtual_try_on` | Virtual clothing try-on on a person's photo | ~6 credits |
| `generate_mannequin` | Generate AI mannequin/model for product photos | ~6 credits |

### Avatar

| Tool | Description | Cost |
|------|-------------|------|
| `lip_sync` | Create talking avatar from a photo | ~14 credits |

### Utility

| Tool | Description | Cost |
|------|-------------|------|
| `check_balance` | Check your credit balance | Free |
| `list_models` | List all available models and costs | Free |
| `get_job_status` | Check status of a running job | Free |

## Configuration

| Env Variable | Description | Default |
|-------------|-------------|---------|
| `YAPARAI_API_KEY` | Your API key (required) | — |
| `YAPARAI_BASE_URL` | API base URL | `https://api.yaparai.com` |

## Cursor / Windsurf

Same configuration format — add to your MCP settings:

```json
{
  "yaparai": {
    "command": "yaparai",
    "env": {
      "YAPARAI_API_KEY": "yap_live_your_key_here"
    }
  }
}
```

## Claude Code

Add to your `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "yaparai": {
      "command": "yaparai",
      "env": {
        "YAPARAI_API_KEY": "yap_live_your_key_here"
      }
    }
  }
}
```

## Python SDK Usage

You can also use YaparAI as a Python library:

```python
import asyncio
from yaparai.client import YaparAIClient

async def main():
    client = YaparAIClient(api_key="yap_live_your_key_here")

    # Generate an image
    job = await client.generate({
        "type": "image",
        "prompt": "A futuristic city at sunset",
    })

    # Wait for result
    result = await client.wait_for_result(job["job_id"])
    print(result["result_url"])

    # Check balance
    balance = await client.get_balance()
    print(f"Credits: {balance['balance']}")

asyncio.run(main())
```

## Pricing

Credits are deducted from your YaparAI account balance:

- **100 free credits** on signup (no credit card required)
- Image generation: ~6 credits (~$0.50)
- Video generation: ~350 credits (~$3-5)
- Music generation: ~14 credits (~$1)
- Background removal: ~2 credits (~$0.15)
- Credits never expire

[View pricing](https://www.yaparai.com/pricing)

## Links

- **Website**: [yaparai.com](https://www.yaparai.com)
- **Gallery**: [yaparai.com/gallery](https://www.yaparai.com/gallery)
- **API Keys**: [yaparai.com/settings](https://www.yaparai.com/settings)
- **Support**: destek@yaparai.com

## License

Apache 2.0 — see [LICENSE](LICENSE)
