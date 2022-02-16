# coding=utf-8
import uvicorn
from fastapi import FastAPI

app = FastAPI()  # 创建 api 对象


@app.get("/")  # 根路由
def root():
    return {"武汉": "加油！！！"}


@app.get("/say/{data}")
def say(data: str, q: int):
    return {"data": data, "item": q}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

