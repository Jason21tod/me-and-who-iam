from flask import blueprints
from .database import DataHandler

project_exibition = blueprints.Blueprint('project exibition', __name__, url_prefix='/projects')
data_handler = DataHandler()

@project_exibition.route('/', methods=['GET'])
def project_exibition_endpoint():
    print('test_case -> getting data')
    data = data_handler.retrieve_project_in_db()
    return {'projects':data}

