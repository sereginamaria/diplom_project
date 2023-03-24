from flask import Flask, jsonify, request, Response
import flask
from flask_cors import CORS
from database import Data_Base

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.app = flask.Flask(__name__)
        CORS(self.app)

        self.app.add_url_rule("/auth", view_func=self.get_auth)

    def run_server(self):
        return self.app.run(host=self.host, port=self.port)

    def get_auth(self):
        new_db = Data_Base()
        users = new_db.get_users()
        if not (users):
            return Response(status=404)
        return users


if __name__ == "__main__":
    server_host = "0.0.0.0"
    server_port = 8060

    server = Server(server_host, server_port)
    server.run_server()
