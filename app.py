from flask import Flask, jsonify,request, render_template
from flask_restful import Api
from database import db

DB_NAME = ""

app=Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host':'mongodb://localhost:27017/'+DB_NAME
}

api=Api(app)

db.initialize_db(app)

# initiallize routes
@app.route('/')
def index():
    return "<h1>Worklytics Api</h1>"


if __name__ == '__main__':
    app.run(debug=True)