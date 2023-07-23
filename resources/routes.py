from .resources import TestApi, CompanyAuthApi, CompanyLoginApi, CompaniesApi,SearchJobApi, JobsApi, JobsByCompany, JobApi, CompanyApi, ApplicationApi


def intialize_routes(api):
    api.add_resource(TestApi, '/api/tests')
    api.add_resource(CompanyAuthApi, '/api/company/auth')
    api.add_resource(CompanyLoginApi, '/api/company/login')
    api.add_resource(CompaniesApi, '/api/companies')
    api.add_resource(CompanyApi, '/api/companies/<id>')
    api.add_resource(SearchJobApi,'/api/searchjob')
    api.add_resource(JobsApi, '/api/jobs')
    api.add_resource(JobsByCompany, '/api/company/jobs')
    api.add_resource(JobApi, '/api/jobs/<id>')
    api.add_resource(ApplicationApi, '/api/applications')
