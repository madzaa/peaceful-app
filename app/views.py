from math import pow
from flask import jsonify, request, Response
from app import app, db
from app.models import ItemsModel
from app.utils import add_column, email

ip_ban_list = []


@app.route("/")
def handle_item():
    if request.method == "GET":
        item = request.args.get("n", default=None, type=float)
        if item is None:
            return "Argument not provided, please provide a parameter n"
        return jsonify(f"{item} ^ 2 is : {(pow(item, 2))}")


@app.route("/blacklisted", methods=["GET"])
def handle_blacklisted():
    status_code = Response(response="Error code 444", status=444, mimetype="text/plain")
    if request.method == "GET":
        try:
            ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)  # get original IP if behind a proxy
            if ip not in ip_ban_list:
                ip_ban_list.append(ip)
                email(ip, app)
                db.create_all()
                add_column(db, ItemsModel, ip, request.path)
            else:
                return status_code
        finally:
            return status_code
