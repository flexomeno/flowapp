def hello_world(environ, start_response):
    status = '200 ok'
    headers = [('Content-type','text/plain')]
    start_response(status, headers)
    
    return ['Hello World']

def run():
    httpd = make_server('', 8006, hello_world)
    print 'Serving on port 8006...'
    httpd.serve_forever()

if __name__ == '__main__':
    run()