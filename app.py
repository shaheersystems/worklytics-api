from flask import Flask, jsonify,request, render_template
from flask_restful import Api
from database import db
from resources import routes
from database.models import Company

dbName = "job_db"

app=Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host':'mongodb://localhost:27017/'+dbName
}

api=Api(app)

db.initialize_db(app)
routes.intialize_routes(api)
# initiallize routes
@app.route('/')
def index():
    return "<h1>Worklytics Api</h1>"


if __name__ == '__main__':
    app.run(debug=True)