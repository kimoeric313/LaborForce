import sys
import time
import socketserver
import http.server
from http.server import SimpleHTTPRequestHandler as RequestHandler
import subprocess
from urllib.parse import urlparse   #轉換URL用
import urllib



#函式-------------------------------------------------------------

class MyHandler(RequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type","text/html")

        self.end_headers()
        #取得並解析完整的URL
        query=urlparse(self.path).query
        #反轉URL格式
        query=urllib.parse.unquote(query)

        html='無資料';

        # 當HTTP GET有收到值的時候作動
        if query!="":
            html = subprocess.check_output(['python', 'LaborForce.py',query])

        print('Get query=',query)

        output = b""
        output += b"<html><body>"
        output += html
        output += b"</body></html>"




        
        self.wfile.write(output)


#主要程式內容--------------------------------------------------------


if sys.argv[1:]:
    port=int(sys.argv[1])
else:
    port = 8888


print('Server Listening on port %s'% port)
socketserver.TCPServer.allow_reuse_address=True

httpd=socketserver.TCPServer(('0.0.0.0',port),MyHandler)

try:
    httpd.serve_forever()
except:
    print('關閉伺服器')
    httpd.server_close()
