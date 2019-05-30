from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return "Hello, World", 200
    
    @app.route("/bye")
    def goodbye_world():
        raise Exception ("blah")
        return "Goodbye, World", 200

    return app