"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaa16m7avj5o488amgg-a.oregon-postgres.render.com",
        database="todo_u6yc",
        user="todo_u6yc_user",
        password="hO5DKI0RJDTFm0QVBWOY40vzpVFHl9Z2")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
