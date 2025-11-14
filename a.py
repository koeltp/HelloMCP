from fastmcp import FastMCP
mcp=FastMCP("Demo")

@mcp.tool
def add(a:int,b:int)->int:
    """
    Add two numbers

    Args:
        a (int): _description_
        b (int): _description_

    Returns:
        int: _description_
    """

    return a+b

if __name__ == "__main__":
    mcp.run()