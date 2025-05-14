from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    # 获取请求的 Host 头部，例如 ipv1.4:192.168.0.5
    host = request.host
    if ":" in host:
        try:
            protocol, ip = host.split(":")
            # 输出 HTML 演示页面
            return f"""
            <h2>🌐 IPv4.1 Demo Server</h2>
            <p>🔗 你通过 <code>{protocol}</code> 协议访问了地址 <code>{ip}</code></p>
            <p>✅ IPv4.1 格式解析成功：<b>{ip}</b></p>
            <p>（这里可以实现重定向、API请求、身份识别等）</p>
            """
        except:
            return "<h3>⚠️ 地址解析失败，请使用 ipv1.4:IP 格式</h3>"
    return "<h3>欢迎来到 IPv4.1 演示服务</h3>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
