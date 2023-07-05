from .resources import TestApi, CompanyAuthApi, CompanyLoginApi, CompaniesApi,SearchJobApi


def intialize_routes(api):
    api.add_resource(TestApi, '/api/tests')
    api.add_resource(CompanyAuthApi, '/api/company/auth')
    api.add_resource(CompanyLoginApi, '/api/company/login')
    api.add_resource(CompaniesApi, '/api/companies')
    api.add_resource(SearchJobApi,'/api/searchjob')

