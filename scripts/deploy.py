from flask import Flask, request, redirect
from flask_restful import Resource, Api
from flask_cors import CORS
import os
import prediction

app = Flask(_name_)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)



class GetPredictionOutput(Resource):

    def post(self):
        try:
            image_path = request.data.decode('utf-8')
            predict = prediction.predict_funct(image_path)
            return {'predict': predict}

        except Exception as error:
            return {'error': str(error)}

api.add_resource(GetPredictionOutput,'/getPredictionOutput')

if _name_ == "_main_":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)