from flask import request, Response, jsonify
from flask_restful import Resource
from database.models import Test, User, Company
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
                return {'error': 'Email or password invalid'}, 401
            return {'id': str(user.id)}, 200
        except Exception as e:
            return Response(str(e), mimetype="application/json", status=500)
