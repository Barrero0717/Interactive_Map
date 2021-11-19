from wsgiref.simple_server import make_server

HTML = """
<!DOCTYPE html>
<html>
  <head>
    <title>Título</title>
  </head>
  <body>
    <h1>Hola gente de códigofacilito</h1>
  </body>
</html>
"""

def application(environ, start_response):
    headers = [ ('Content-type', 'text/html; charset=utf-8') ]

    start_response('200 OK', headers)

    return [bytes(HTML, 'utf-8')]

server = make_server('localhost', 8000, application)
server.serve_forever()