from flask import request, Response, jsonify, make_response, json
from flask_restful import Resource
from database.models import Test, User, Company,Jobs, Application
from mongoengine.queryset.visitor import Q
# from database.models [models]

# @apis

class TestApi(Resource):
    def get(self):
        try:
            tests = Test.objects().to_json()
            return Response(tests, mimetype="application/json", status=200)
        except Exception as e:
            return Response(e, mimetype="application/json", status=500)
    def post(self):
        try:
            body = request.get_json()
            test = Test(**body).save()
            id = test.id
            return {'id': str(id)}, 200
        except Exception as e:
            return Response(e, mimetype="application/json", status=500)

# Nabeel
class CompanyAuthApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            email = body.get('email')
            password=body.get('password')
            user = User(email=email, password=password).save()
            company_data = {key: value for key, value in body.items() if key in Company._fields}
            company = Company(user_id=user.id, **company_data)
            company.save()
            return Response(company.to_json(), mimetype="application/json", status=200)
        except Exception as e:
            return Response(str(e), mimetype="application/json", status=500)

# Nabeel 
class CompanyLoginApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            email = body.get('email')
            password = body.get('password')
            user = User.objects.get(email=email)
            companyData = Company.objects.get(user_id=user.id)
            if not user.check_password(password=password):
                return jsonify({'error': 'Email or password invalid', "auth": False}), 401
            response_data = {
                "company": companyData,
                "auth": True
            }
            return make_response(jsonify(response_data), 200)
        except Exception as e:
            response_data = {
                "error": str(e),
                "auth": False
            }
            print(str(response_data))
            return make_response(jsonify(response_data), 500)

# Nabeel
class CompaniesApi(Resource):
    def get(self):
        try:
            companies = None
            location=request.args.get('location')
            if location != None:
                companies = Company.objects(location=location).to_json()
            else:
                companies = Company.objects().to_json()
            return Response(companies, mimetype="application/json", status=200)
        except Exception as e:
            return Response(e, mimetype="application/json", status=500)
# Nabeel
class CompanyApi(Resource):
     
    def get(self, id):
        try:
            company = Company.objects.get(id=id).to_json()
            return Response(company, mimetype="application/json", status=200)
        except Exception as e:
            return Response(e, mimetype="application/json", status=500)
# Bakhtawar, Areesha
class JobsApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            job = Jobs(**body).save()
            id = job.id
            return {'id': str(id)}, 200
        except Exception as e:
            return Response(e, mimetype="application/json", status=500)
# Ehtisham
class SearchJobApi(Resource):
    def get(self):
        try:
            # query=request.args.get('query')
            # location=request.args.get('location')
            jobtype=request.args.get("jobtype")
            jobs=None
            if (jobtype != None and jobtype != "All"):
                jobs = Jobs.objects(jobtype=jobtype, status="Open")
            elif jobtype=="All":
                jobs=Jobs.objects(status="Open")
            else:
                jobs=Jobs.objects(status="Open")
            # if (query == None and location == None  and jobtype==None):
            #     jobs=Jobs.objects(status="Open")
            # elif(query == None and location !=None  and jobtype==None):
            #     jobs=Jobs.objects(location=location)  
            # elif(location != None and jobtype==None):
            #     jobs=Jobs.objects(Q(title__icontains=query) | Q(description__icontains=query) | Q(jobtype__icontains=query), status="Open" , location=location  )
            # else:
            #     jobs=Jobs.objects(Q(title__icontains=query) | Q(description__icontains=query) | Q(jobtype__icontains=query) )
            return Response(jobs.to_json(), mimetype="application/json", status=200)
        except Exception as e:
            return Response(str(e), mimetype="application/json", status=500)

# Bakhtawar, Areesha
class JobsByCompany(Resource):
    def get(self):
        try:
            company_id=request.args.get('company_id')
            jobs=Jobs.objects(company_id=company_id)
            return Response(jobs.to_json(), mimetype="application/json", status=200)
        except Exception as e:
            return Response(e, mimetype="application/json", status=500)

# Ehtisham
class JobApi(Resource):
    def get(self, id):
        try:
            # job and related company data
            job = Jobs.objects.get(id=id).to_json() 
            # get related company too
           
            return Response(job, mimetype="application/json", status=200)
        except Exception as e:
            return Response(e, mimetype="application/json", status=500)
        
# Shaheer
class ApplicationApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            application = Application(**body).save()
            id = application.id
            return {'id': str(id)}, 200
        except Exception as e:
            return Response(e, mimetype="application/json", status=500)
    def get(self):
        try:
            job_id=request.args.get('job_id')
            applications=Application.objects(job_id=job_id)
            return Response(applications.to_json(), mimetype="application/json", status=200)
        except Exception as e:
            return Response(e, mimetype="application/json", status=500)
class SingleApplicationApi(Resource):
    def get(self,id):
        try:
            application=Application.objects.get(id=id)
            return Response(application.to_json(), mimetype="application/json", status=200)
        except Exception as e:
            return Response(e, mimetype="application/json", status=500)        
# shaheer        
class ApplicationStatusApi(Resource):
    def put(self):
        try:
            body = request.get_json()
            application_id=body.get('application_id')
            status=body.get('status')
            application=Application.objects.get(id=application_id)
            application.update(status=status)
            return Response(application.to_json(), mimetype="application/json", status=200)
        except Exception as e:
            return Response(e, mimetype="application/json", status=500)

# shaheer
class ApplicationsToCompanyApi(Resource):
    def get(self):
        try:
            company_id=request.args.get('company_id')
            company = Company.objects.get(id=company_id)
            # Find all the jobs associated with the company
            jobs = Jobs.objects(company_id=company)
            # Retrieve all the applications for each job and combine them into a list
            all_applications = []
            for job in jobs:
                applications = Application.objects(job_id=job)
                all_applications.extend(applications)
            return make_response(jsonify(all_applications), 200)
        except Exception as e:
            print(str(e))
            return make_response(jsonify({"error":str(e)}), 500)