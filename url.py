from mdblog.app import *

from flask import url_for


with app.test_request_context():

    print(url_for("text"))
    print(url_for("admin"))
    print(url_for("admin_name", name="Franta"))
