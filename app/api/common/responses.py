from abc import ABC


class _Response(ABC):
    """Class that represents a response in chat context. Its the most commom type of response."""
    def __init__(self, text: str ='', content_type: str = '', user: bool = False) -> None:
        super().__init__()
        self.text: str = text
        self.content_type: str = content_type
        self.user = user

        self.content: dict = {}

    def build_response_json(self):
        data = {
            'text':self.text,
            'user': self.user,
            'content': self.content,
            'content_type': self.content_type
        }

        return data

no_processed_message_response: _Response = _Response(
    text="I don't understand what you're saying, sorry... Maybe, you could digit ''Help'' and i Help you with it",
    content_type="no_response_found"
)