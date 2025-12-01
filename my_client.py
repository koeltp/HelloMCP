# 测试一下你的客户端代码是否可行
import asyncio
from fastmcp import Client

async def test_client():
    try:
        # 创建客户端实例
        client = Client("http://127.0.0.1:8000/mcp")
        
        # 连接并调用工具
        async with client:
            # 列出可用工具
            tools = await client.list_tools()
            print("可用工具:", tools)
            
            # 调用 greet 工具
            result = await client.call_tool("greet", {"name": "Ford"})
            print("调用结果:", result)
    except Exception as e:
        print(f"错误: {e}")
        print("检查以下可能的问题...")

if __name__ == "__main__":
    asyncio.run(test_client())