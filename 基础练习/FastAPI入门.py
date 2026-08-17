from fastapi import FastAPI

# 创建  FastAPI 实例
app = FastAPI()

# 定义 API 接口 ---> 该函数返回值表示 API 接口的返回的数据，接口访问路径 /，请求方式 GET
@app.get("/")
def root():
	return{"message": "Hello World"}

# 定义 API 接口
@app.get("/users")
def get_users():
	return [
		{"id": 1, "name": "Alice"},
		{"id": 2, "name": "Bob"},
    ]

# 启动服务 ----> uvicorn: Python中的轻量级web服务器
if __name__ == "__main__":
	import uvicorn
	uvicorn.run(app, host="0.0.0.0", port=8000) 
	
"""
uvicorn 命令行启动方式
方式一： python3 FastAPI入门.py
方式二： uvicorn FastAPI入门:app --reload
"""