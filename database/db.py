from flask_mongoengine import MongoEngine
# instantiate mongo engine
db=MongoEngine()
def initialize_db(app):
    db.init_app(app)