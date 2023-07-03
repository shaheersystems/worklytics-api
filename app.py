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

@app.route('/api/companies', methods=['POST'])
def return_companies():
    companies = Company.objects().all()
    company_list = []
    for company in companies:
        company_data = {
            'name': company.name,
            'location': company.location,
            'industry': company.industry,
            'user':company.user_id,
            'website': company.website,
            'founded_year': company.founded_year,
            'hrName': company.hrName
        }
        company_list.append(company_data)
    return jsonify(company_list)

if __name__ == '__main__':
    app.run(debug=True)