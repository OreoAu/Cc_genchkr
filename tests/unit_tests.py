import unittest
from app import app, card_processing, get_response




class TestCardProcessing(unittest.TestCase):
    def test_valid_card(self):
        self.assertTrue(card_processing('4111111111111111', '02/26', '123'))

    def test_invalid_card(self):
        self.assertFalse(card_processing('4111111111111112', '02/26', '123'))

class TestAppRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_app_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_app_success(self):
        response = self.app.post('/', data=dict(cardNumber='4111111111111111', expDate='02/26', cvv='123'))
        self.assertIn(b'Successful Transaction', response.data)

    def test_app_error(self):
        response = self.app.post('/', data=dict(cardNumber='4111111111111112', expDate='02/26', cvv='123'))
        self.assertIn(b'Error processing card', response.data)

if __name__ == '__main__':
    unittest.main()
