from fastmcp import FastMCP

mcp = FastMCP(title="Addition Service", description="A simple service to add two integers.")


@mcp.tool
def add(x: int, y: int) -> int:
    """Add two integers."""
    return x + y

@mcp.tool
def subtract(x: int, y: int) -> int:
    """Subtract two integers."""
    return x - y

@mcp.tool
def multiply(x: int, y: int) -> int:
    """Multiply two integers."""
    return x * y

@mcp.tool
def divide(x: int, y: int) -> float:
    """Divide two integers."""
    if y == 0:
        return float("inf")
    return x / y

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
