# YaparAI MCP Server

Generate AI images, videos, and music directly from **Claude Desktop**, **Cursor**, **Windsurf**, and other MCP-compatible AI assistants.

[![PyPI](https://img.shields.io/pypi/v/yaparai)](https://pypi.org/project/yaparai/)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

## What is YaparAI?

[YaparAI](https://www.yaparai.com) is an all-in-one AI content creation platform with 16+ AI models:

- **Image Generation** — Flux, SDXL, Imagen 4 (text-to-image, image-to-image)
- **Video Generation** — Veo 3.1, Kling (text-to-video, image-to-video)
- **Music Generation** — Suno v4 (full songs with vocals)
- **And more** — Lip sync, virtual try-on, AI mannequin, ad creation

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

> "Check my credit balance"

## Available Tools

| Tool | Description | Cost |
|------|-------------|------|
| `generate_image` | Generate images from text prompts | ~6 credits |
| `generate_video` | Generate videos from text or images | ~350 credits |
| `generate_music` | Generate music from text descriptions | ~14 credits |
| `check_balance` | Check your credit balance | Free |
| `list_models` | List available models and costs | Free |

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

## Pricing

Credits are deducted from your YaparAI account balance:

- **100 free credits** on signup (no credit card required)
- Image: ~6 credits (~$0.50)
- Video: ~350 credits (~$3-5)
- Music: ~14 credits (~$1)
- Credits never expire

[View pricing](https://www.yaparai.com/pricing)

## Links

- **Website**: [yaparai.com](https://www.yaparai.com)
- **Gallery**: [yaparai.com/gallery](https://www.yaparai.com/gallery)
- **API Docs**: [yaparai.com/settings](https://www.yaparai.com/settings) (API key management)
- **Support**: destek@yaparai.com

## License

Apache 2.0 — see [LICENSE](LICENSE)
