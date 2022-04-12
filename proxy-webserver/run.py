from proxy import app # IMPORTED FROM THE INIT MODULE (__INIT__.PY) IN THIS PACKAGE

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    

#from http.server import BaseHTTPRequestHandler, HTTPServer
#import time
#
#hostName = "localhost"
#serverPort = 3000
#
#class videoStreaming(BaseHTTPRequestHandler):
#    def do_GET(self):
#        self.send_response(200)
#        self.send_header("Content-type", "video/mp4")
#        self.end_headers()
#        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
#        self.wfile.write(bytes("<video>src=4330e84be1734f3b8f9bcc9df3bef1c8.mp4</video>", "video/mp4"))
#        self.wfile.read(bytes("<video>src=4330e84be1734f3b8f9bcc9df3bef1c8.mp4</video>", "video/mp4"))
#       
#if __name__ == "__main__":        
#    webServer = HTTPServer((hostName, serverPort), videoStreaming)
#    print("Microservice online, point your browser at http://%s:%s" % (hostName, serverPort))
#
#    try:
#        webServer.serve_forever()
#    except KeyboardInterrupt:
#        pass
#
#    webServer.server_close()
#    print("Microservice stopped.")
