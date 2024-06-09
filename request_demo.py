# 计划：模型持续运行并监控一个文件夹是否有图片，如果有图片就识别，没有就等待
# 问题：怎么把识别结果传递给系统服务器
# 如果发送一个http请求，需要跳转至 controller ，但是我不希望跳转

from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    response_content = ""

    def do_GET(self):
        # 获取请求路径和查询参数
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)

        print("Received GET request:")
        print("Path:", parsed_url.path)
        if query_params.get("flag")[0] == "true":
            print("query_params: ",query_params.get("fileName")[0])
            print("处理你自己的业务")
            print("处理处理好了把结果赋值给 response_content 返回")
        else:
            print("不用处理业务")

        # 使用类变量赋值给response_content
        self.response_content = plate

        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(self.response_content.encode('utf-8'))

if __name__ == '__main__':
    print('Starting server...')
    server_address = ('127.0.0.1', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    plate = "粤bbbbccc"
    print('Serving at port 8000')
    httpd.serve_forever()