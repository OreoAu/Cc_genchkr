
import unittest
import sys
sys.path.append('/home/ubuntu/projects/cc_Genckr')
from app import app

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page_loads(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_invalid_card(self):
        response = self.app.post('/', data=dict(card_number='1234567890123456'))
        self.assertIn('Invalid Card', response.data.decode())

    def test_valid_card(self):
        response = self.app.post('/', data=dict(card_number='4242424242424242'))
        self.assertIn('Valid Card', response.data.decode())

if __name__ == '__main__':
    unittest.main()

