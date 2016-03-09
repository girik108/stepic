from html import escape

def hello(env , start_response):
    status = '200 OK'
    data = b"Hello\n"
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    resp = bytes(env['QUERY_STRING'], encoding = 'utf-8')
    resp = [res + b'\n' for res in resp.split(b'&')]
    return resp
