def hello(env , start_response):
    status = '200 OK'
    data = "Hello\n"
    headers = [
		('Content-Type', 'text/plain'),
		('Content-Length', str(len(data)))]
    start_response(status, headers)
    return [body]
