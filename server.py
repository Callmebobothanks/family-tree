#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
简单的HTTP服务器，用于运行家谱网页
使用方法：python server.py
然后在浏览器中访问 http://localhost:8000
"""

import http.server
import socketserver
import webbrowser
import os

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # 添加CORS头，允许跨域请求
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        # 设置UTF-8编码
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        super().end_headers()

    def log_message(self, format, *args):
        # 自定义日志格式
        print(f"[{self.address_string()}] {args[0]}")

if __name__ == "__main__":
    # 切换到脚本所在目录
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    Handler = MyHTTPRequestHandler
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}/index.html"
        print("=" * 60)
        print("杨氏家族家谱网页服务器已启动！")
        print("=" * 60)
        print(f"服务器地址: http://localhost:{PORT}")
        print(f"网页地址: {url}")
        print("=" * 60)
        print("按 Ctrl+C 停止服务器")
        print("=" * 60)
        
        # 自动打开浏览器
        try:
            webbrowser.open(url)
        except:
            pass
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n服务器已停止")


