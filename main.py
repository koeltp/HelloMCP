from fastmcp import FastMCP

mcp = FastMCP("ByteEpoch MCP Server")

@mcp.tool
def greet(name: str) -> str:
    """
    向指定用户打招呼。
    Args:
        name (str): 用户名
    """
    return f"Hello,{name}@!"

@mcp.tool
def add(a:int,b:int)->int:
    """
    求两个整数的和。
    Args:
        a (int): 整数1
        b (int): 整数2

    Returns:
        int: 合計値
    """

    return a+b


if __name__ == "__main__":
    mcp.run(transport="http", port=8000)
