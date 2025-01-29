from flask import blueprints

project_exibition = blueprints.Blueprint('project exibition', __name__, url_prefix='/projects')


@project_exibition.route('/', methods=['GET'])
def project_exibition_endpoint():
    print('test_case -> getting data')
    return {'projects':['']}

