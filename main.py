import random
from fastmcp import FastMCP

mcp = FastMCP("Remote Calculator Server")

# ----------------------
# In-memory storage
# ----------------------
random_history = []

# ----------------------
# Tools
# ----------------------

@mcp.tool
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


@mcp.tool
def random_in_range(min_value: int, max_value: int) -> int:
    """Generate a random integer within a given range (inclusive)."""
    if min_value > max_value:
        return "Error: min_value must be <= max_value"

    value = random.randint(min_value, max_value)
    random_history.append(value)
    return value


# ----------------------
# Resources
# ----------------------

@mcp.resource("info://server")
def server_info() -> dict:
    """Basic metadata about the MCP server."""
    return {
        "name": "Remote Calculator Server",
        "version": "1.0.0",
        "tools_available": ["add", "random_in_range"],
    }


@mcp.resource("data://random-history")
def get_random_history() -> list:
    """Return history of generated random numbers."""
    return random_history


@mcp.resource("info://operations")
def supported_operations() -> list:
    """Return list of supported operations."""
    return ["addition", "random number generation"]

# ----------------------
# Run as HTTP Server
# ----------------------

if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=8000
    )