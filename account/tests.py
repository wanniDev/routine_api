from django.test import TestCase, Client
import json

class UserTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_sign_up_with_wrong_password_format(self) :
        payload = {'email':'test@test.com', 'password':'aaaaaa123'}
        json_load = json.dumps(payload);
        response = self.client.post('/account/signup/', json_load, content_type="application/x-www-form-urlencoded")
        self.assertNotEqual(response.status_code, 200)
    
    def test_sign_up_with_short_password_format(self) :
        payload = {'email':'test@test.com', 'password':'aB@#!1'}
        json_load = json.dumps(payload);
        response = self.client.post('/account/signup/', json_load, content_type="application/x-www-form-urlencoded")
        self.assertNotEqual(response.status_code, 200)