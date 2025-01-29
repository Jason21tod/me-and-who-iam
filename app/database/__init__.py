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
        try:
            with current_app.app_context():
                new_kid = self.projects_model(
                    name=data.title, link=data.link,
                    description=data.description, image_link=image_link.image_link
                    )
                db.session.add(new_kid)
                db.session.commit()
        except:
            print('não foi possivel enviar os dados')