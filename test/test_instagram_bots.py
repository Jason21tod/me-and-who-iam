from unittest import TestCase, main
from app import instagram_bots as insta_bots

class TestGetLongDurationToken(TestCase):
    def test_get_new_long_duration_token(self):
        """Teste principal pra ver se tudo está nos conformes - o token usado deve ser um de curta duração"""
        print(insta_bots.get_new_long_duration_token(
            'bbd2b3d2eca79ca839f29f4d070cff21','AQCVh4_J8X_qDje6qNh-HhywquxUBl7LvWsVaBLlt5mqjuXUYgxUTQBCi6i2Lnhf_GaMVXk4nzfbFlvs0S4OKyerpfyInwqagPoulSdvaXuwYmfZvlGEwDfKhhRG2DnEb7KDdFFp1x_cbHotMlGBsKhnQtENMDGTPnLdoTpCXcuw9IFPYaJJ-uMi23_-qn_w9E9mK5cMiBGOAqKBMwdIpbgnsbbxtveihCZtAXnp-u-R8Q'
                )
            )


class TestScrapBots(TestCase):
    test_scrap_bot = insta_bots.ScrapBot()
    def test_get_base_data(self):
        """AVISO: ao executar este teste é necessário verificar o token de acesso"""
        mock_data = {
            'user_id':17919768758730247,
            'access_token':'IGQVJWRDZAOcWRKcUxveHFGOUJnQ1ZAKbk9sNllBLTB5NnZAJaFY4UXc5WGtCdlJVVnNVTlBvNmFWaVUzYndlSllyVkotcWtlZAGkzZAjdBU2xZAVzR1X1F2UXBHNmgtbkpkakJmNlk1akdn'
                     }
        print(self.test_scrap_bot.get_simple_base_data(mock_data).text)
