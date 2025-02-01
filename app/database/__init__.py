from flask_sqlalchemy import SQLAlchemy
from flask import current_app


db: SQLAlchemy = SQLAlchemy()


class ProjectsModel(db.Model):
    title = db.Column(db.String, primary_key=False)
    link = db.Column(db.String(4000), primary_key=True, nullable=False)
    description = db.Column(db.String(800), nullable=False)
    image_link = db.Column(db.String(4000))


class DataHandler():
    projects_model = ProjectsModel
    def add_project_in_db(self, data):
        current_app.logger.info('Adding new project')
        new_project = self.projects_model(
            title=data['title'], link=data['link'],
            description=data['description'], image_link=data['image_link']
            )
        db.session.add(new_project)
        db.session.commit()

    def retrieve_project_in_db(self):
        projects = ProjectsModel.query.all()
        projects_formated = []
        for project in projects:
            projects_formated.append({
                'title':project.title,
                'link': project.link,
                'description': project.description,
                'image_link': project.image_link
                })
        current_app.logger.info(projects_formated)
        return projects_formated

