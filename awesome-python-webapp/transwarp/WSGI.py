from wsgiref.simple_server import make_server

URL_PATTERNS= (
    ('hi','say_hi'),
    ('hello','say_hello'),
    )


class Dispatcher(object):

    def _match(self, path):
        path = path.split('/')[1]
        for url, fun_txt in URL_PATTERNS:
            if path in url:
                return fun_txt

    def __call__(self, environ, start_response):
        path = environ.get('PATH_INFO','/')
        print path.split('/')[1]
        fun_txt = self._match(path)
        if fun_txt:
            fun = globals()[fun_txt]
            return fun(environ, start_response)
        else:
            start_response("404 NOT FOUND",[('Content-type', 'text/plain')])
            return ["Page dose not exists!\n 404 NOT FOUND"]


def say_hi(environ, start_response):
    start_response("200 OK", [('Content-type', 'text/html')])
    return ["kenshin say hi to you!"]


def say_hello(environ, start_response):
    start_response("200 OK", [('Content-type', 'text/html')])
    return ["kenshin say hello to you!"]


def say_heihei(start_response):
    start_response("200 OK", [('Content-type', 'text/html')])
    return ["kenshin say heihei to you!"]


class Auth(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        #TODO
        return self.app(environ, start_response)


bpp = Dispatcher()
auth_app = Auth(bpp)

httpd = make_server('', 8000, auth_app)
print "Serving on port 8000..."
httpd.serve_forever()

