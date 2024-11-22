from flask import Blueprint, current_app

scrapbot_page = Blueprint('jason scrapbot', __name__, url_prefix='/scrapbot')

@scrapbot_page.route('/', methods=['GET', 'POST'])
def scrap_bot():
    """Endpoint of redirect"""
    return current_app.redirect("https://scrap-bot-smoky.vercel.app/")