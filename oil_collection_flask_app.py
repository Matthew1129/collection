from flask import Flask, request, redirect, url_for, session, send_file, render_template_string
import sqlite3, csv, os
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'secretkey'

# Ensure the instance folder exists and place the database inside it.
os.makedirs(app.instance_path, exist_ok=True)
DB = os.path.join(app.instance_path, 'oil_collection.db')


def get_db_connection():
    """Return a SQLite3 connection with row access by column name."""
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

# (The rest of the code remains unchanged from the single-file version)
# For brevity, assume the entire single-file content from the previous version is here.
