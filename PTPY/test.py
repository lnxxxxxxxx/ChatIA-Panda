import unittest
from chatbot import get_response, model

class TestChatbot(unittest.TestCase):
    def test_saludo(self):
        response = get_response(model, "Hola")
        self.assertIn(response, ["Hola"])

    def test_respuestas_predeterminadas(self):
        response = get_response(model, "cualquier cosa")
        self.assertIn(response, ["Lo siento, no entiendo el mensaje."])

if __name__ == '__main__':
    unittest.main()
