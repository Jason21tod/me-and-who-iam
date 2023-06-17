from requests import get


class ScrapBot:
    def get_simple_base_data(self, data: dict):
        return get(f'https://graph.instagram.com/data[{data["user_id"]}]?fields=id,username&access_token=[{data["access_token"]}]')
