import unittest
from app import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client() 

    def tearDown(self):
        pass

    def test_indexNoAcceptHeader(self):
        response = self.app.get('/', headers={})
        self.assertEqual(response.data, b'<p>Hello, World</p>\n')
        self.assertEqual(response.status_code, 200)

    def test_indexJSON(self):
        response = self.app.get('/', headers={'Accept': 'application/json'})
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.data, b'{"message":"Good morning"}\n')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
