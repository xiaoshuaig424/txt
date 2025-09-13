from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Vercel 会将所有请求路由到这个函数
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    try:
        url = "https://v1.hitokoto.cn/"
        res = requests.get(url).json()
        
        # 最好返回 JSON 格式，更通用
        response_data = {
            "hitokoto": res.get("hitokoto", "获取失败"),
            "from": res.get("from", "未知来源"),
            "text": f'{res.get("hitokoto", "")}    ----{res.get("from", "")}'
        }
        
        return jsonify(response_data)
    except Exception as e:
        # 增加错误处理
        return jsonify({"error": str(e)}), 500
