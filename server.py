from flask import Flask


class Server:
    def __init__(self, name):
        self.app = Flask(name)
        self.routes()

    def routes(self):
        @self.app.route('/')
        def home():
            return 'Test server!'

    def run(self, host='127.0.0.1', port=5000, debug=True):
        self.app.run(host=host, port=port, debug=debug)


app = Server(__name__)

if __name__ == '__main__':
    app.run()
