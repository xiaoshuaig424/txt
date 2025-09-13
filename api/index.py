from flask import Flask, make_response
import requests

app = Flask(__name__)

# Vercel 会将所有请求路由到这个函数
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    try:
        url = "https://v1.hitokoto.cn/"
        res = requests.get(url).json()
        
        # 获取一言内容
        hitokoto_text = res.get("hitokoto", "获取一言失败")
        
        # 创建一个纯文本响应
        response = make_response(hitokoto_text, 200)
        response.mimetype = "text/plain; charset=utf-8"
        return response
        
    except Exception as e:
        # 增加错误处理
        error_message = f"发生错误: {e}"
        response = make_response(error_message, 500)
        response.mimetype = "text/plain; charset=utf-8"
        return response
