from django.test import TestCase, Client
import json

class UserTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_sigh_up_with_wrong_password_format(self) :
        payload = {'email':'test@test.com', 'password':'a123'}
        jLoad = json.dumps(payload);
        response = self.client.post('http://localhost:8000/account/signup/', jLoad, content_type="application/x-www-form-urlencoded")
        self.assertNotEqual(response.status_code, 200)