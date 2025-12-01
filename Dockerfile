# 使用 Python 3.10 基础镜像
FROM python:3.11.14

# 设置工作目录
WORKDIR /app

# 复制依赖文件并安装
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY . .

# 暴露端口
EXPOSE 8000

# 设置环境变量
ENV PORT=8000

# 启动应用
CMD ["python", "main.py"]