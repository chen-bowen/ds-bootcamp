from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/bowen_hello")
    def hello_world():
        return "Hello, World", 200
    
    @app.route("/bowen_bye")
    def goodbye_world():
        return "Goodbye, World", 200

    return app