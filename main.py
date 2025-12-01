from fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import PlainTextResponse

mcp = FastMCP("ByteEpoch MCP Server")

@mcp.tool
def greet(name: str) -> str:
    """
    向指定用户打招呼。
    Args:
        name (str): 用户名
    """
    return f"Hello,{name}@!"
@mcp.custom_route("/health", methods=["GET"])
async def health_check(request: Request) -> PlainTextResponse:
    return PlainTextResponse("OK")
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
    mcp.run(transport="streamable-http", port=8000)
