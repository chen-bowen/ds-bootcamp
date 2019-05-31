from flask import Flask
import yaml
import os
from flask import Flask, jsonify

dir_path = os.path.dirname(os.path.realpath(__file__))

def create_app():
    app = Flask(__name__)

    with open(os.path.join(dir_path, 'yamls/simple_model.yaml'), 'r') as f:
       simple_model = yaml.load(f, Loader=yaml.SafeLoader)

    @app.route("/bowen_hello")
    def hello_world():
        return "Hello, World", 200

    @app.route("/simple_model/<submodel>/<x_1>")
    def yaml_model(submodel, x_1):
        try:
            model = simple_model[submodel]
        except KeyError:
            return "Model Not Found", 404
        dict_ = {'score': model['a1'] + model['b1']*int(x_1)}
        return jsonify(dict_)

    @app.route("/bowen_bye")
    def goodbye_world():
        return "Goodbye, World", 200

    return app