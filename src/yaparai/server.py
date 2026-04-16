"""
YaparAI MCP Server — Generate images, videos, and music with AI.

Usage with Claude Desktop:
    Add to claude_desktop_config.json:
    {
        "mcpServers": {
            "yaparai": {
                "command": "yaparai",
                "env": {
                    "YAPARAI_API_KEY": "yap_live_xxxxxxxxxxxxx"
                }
            }
        }
    }

Usage with Cursor/Windsurf:
    Same configuration format in their MCP settings.
"""

from fastmcp import FastMCP

# Generation tools
from yaparai.tools.generate import (
    generate_image,
    generate_video,
    generate_music,
    generate_music_video,
)

# Image editing tools
from yaparai.tools.edit import (
    transform_image,
    remove_background,
    swap_face,
)

# E-commerce tools
from yaparai.tools.ecommerce import (
    virtual_try_on,
    generate_mannequin,
)

# Avatar tools
from yaparai.tools.avatar import lip_sync

# Utility tools
from yaparai.tools.balance import check_balance
from yaparai.tools.models import list_models
from yaparai.tools.jobs import get_job_status

mcp = FastMCP(
    "YaparAI",
    description=(
        "Generate AI images, videos, and music using YaparAI. "
        "13 tools covering image generation, video creation, music, "
        "image editing (background removal, face swap), e-commerce "
        "(virtual try-on, AI mannequin), lip sync avatars, and more. "
        "Powered by 16+ AI models: Flux, SDXL, Imagen 4, Veo 3.1, "
        "Kling, Suno v4. Credit-based pricing — 100 free credits on signup. "
        "Get your API key at https://www.yaparai.com/settings"
    ),
)

# --- Generation ---
mcp.tool(generate_image)
mcp.tool(generate_video)
mcp.tool(generate_music)
mcp.tool(generate_music_video)

# --- Image Editing ---
mcp.tool(transform_image)
mcp.tool(remove_background)
mcp.tool(swap_face)

# --- E-commerce ---
mcp.tool(virtual_try_on)
mcp.tool(generate_mannequin)

# --- Avatar ---
mcp.tool(lip_sync)

# --- Utility ---
mcp.tool(check_balance)
mcp.tool(list_models)
mcp.tool(get_job_status)


def main():
    """Entry point for the yaparai CLI command."""
    mcp.run()


if __name__ == "__main__":
    main()
