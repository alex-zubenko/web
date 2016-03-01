def app(environ, start_response):
    path = environ.get('PATH_INFO')
    query = environ.get('QUERY_STRING')
    query = query.replace('&',"\r\n")
    response_body = query
    status = "200 OK"
    response_headers = [("Content-Type", "text/plain"),("Content-Length", str(len(response_body)))]
    start_response(status, response_headers)
    return [response_body]
