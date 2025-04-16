import app.database as database
import app

handler = database.DataHandler()

with app.create_app().app_context():
    handler.add_project_in_db({
        'title': 'Jason Scrapbot',
        'link': '/scrapbot',
        'description_en': 'A bot used in WebScrap and Prototypes.',
        'description_pt': 'Um robô usado para web scraping e prototipação.',
        'image_link': 'https://i.ibb.co/Vc21f8Q4/jason-scrapbot.png'
    }
)
