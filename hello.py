def application(environ, start_response):
    path = environ.get('PATH_INFO')
    query = environ.get('QUERY_STRING')
    print(query)
    response_body = "Index"
    status = "200 OK"
    response_headers = [("Content-Length", str(len(response_body)))]
    start_response(status, response_headers)
    return [response_body]