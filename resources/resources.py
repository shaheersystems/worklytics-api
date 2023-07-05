from flask import request, Response, jsonify
from flask_restful import Resource
from database.models import Test, User, Company,Jobs
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
            id = str(company.id)
            return Response({"id":id}, mimetype="application/json", status=200)
        except Exception as e:
            return Response(str(e), mimetype="application/json", status=500) 
class CompanyLoginApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            email = body.get('email')
            password = body.get('password')
            user = User.objects.get(email=email)
            if not user.check_password(password=password):
                return {'error': 'Email or password invalid', "auth":False}, 401
            return {'id': str(user.id), "auth":True}, 200
        except Exception as e:
            return Response({"error":str(e), "auth":False}, mimetype="application/json", status=500)

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

class SearchJobApi(Resource):
    def get(self):
        try:
            query=request.args.get('query')
            location=request.args.get('location')

            if(location != None):
                jobs=Jobs.objects(Q(title__icontains=query) | Q(description__icontains=query) | Q(jobtype__icontains=query) , location=location  )
            else:
                jobs=Jobs.objects(Q(title__icontains=query) | Q(description__icontains=query) | Q(jobtype__icontains=query) )
           
            return Response(jobs.to_json(), mimetype="application/json", status=200)
        except Exception as e:
            return Response(e, mimetype="application/json", status=500)
