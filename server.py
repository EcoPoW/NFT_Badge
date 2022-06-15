import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options


application = tornado.web.Application([
    (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "."}),
])

if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application, ssl_options={
        "certfile": "/root/.acme.sh/www.w3connect.org/fullchain.cer",
        "keyfile": "/root/.acme.sh/www.w3connect.org/www.w3connect.org.key",
    })
    http_server.listen(443)
    tornado.ioloop.IOLoop.instance().start()

