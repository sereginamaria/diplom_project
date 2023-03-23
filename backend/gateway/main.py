#!D:\Python\python.exe
import flask
from flask import request, jsonify, Response
from flask_cors import CORS
import requests

class Server:
    def __init__(self, host, port, tickets_port, auth_port, bonuses_port):
        self.host = host
        self.port = port
        self.Tickets = tickets_port
        self.auth = auth_port
        self.Bonuses = bonuses_port
        self.app = flask.Flask(__name__)
        CORS(self.app)

        self.app.add_url_rule("/auth", view_func=self.post_auth, methods=['POST'])


    def post_auth(self):
        buy_inf = request.json
        url1 = "http://auth:" + str(self.auth)

        response_auth = requests.get(url1, headers={"login": buy_inf["login"], "password": buy_inf["password"]})
        if response_auth.status_code == 404:
            return Response(status=404)
        response_auth = response_auth.json()

        return response_auth


if __name__ == "__main__":
    server_host = "0.0.0.0"
    server_port = 8080
    tickets_port = 8070
    auth_port = 8060
    bonuses_port = 8050

    server = Server(server_host, server_port, tickets_port, auth_port, bonuses_port)
    server.run_server()
