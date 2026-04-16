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

from yaparai.tools.generate import generate_image, generate_video, generate_music
from yaparai.tools.balance import check_balance
from yaparai.tools.models import list_models

mcp = FastMCP(
    "YaparAI",
    description=(
        "Generate AI images, videos, and music using YaparAI. "
        "Supports 16+ AI models including Flux, SDXL, Imagen 4 (images), "
        "Veo 3.1, Kling (videos), and Suno v4 (music). "
        "448 ready-made templates. Credit-based pricing. "
        "Get your API key at https://www.yaparai.com/settings"
    ),
)

# Register tools
mcp.tool(generate_image)
mcp.tool(generate_video)
mcp.tool(generate_music)
mcp.tool(check_balance)
mcp.tool(list_models)


def main():
    """Entry point for the yaparai CLI command."""
    mcp.run()


if __name__ == "__main__":
    main()
