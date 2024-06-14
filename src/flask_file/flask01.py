#new
from flask import Flask,request, jsonify, make_response, render_template, session,send_file
import routes as router
from flask_cors import CORS
from quart_cors import cors
from quart import Quart, Blueprint
import os

def create_app():
    app = Quart(__name__)
    cors(app, allow_origin="*", allow_headers=["Content-Type", "Authorization",
         "Access-Control-Allow-Credentials"], allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
    #CORS(app ,origins= "*" )



    app.register_blueprint(router.router)

    # app.config['UPLOAD_FOLDER']  = 'uploads'
    return app
    # if __name__ == "__main__":
    #     app.run( host="172.20.11.47",port=3000 ,debug=True) #host="172.20.11.47"





