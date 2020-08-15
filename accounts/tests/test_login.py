from django.test import TestCase
from django.contrib.auth import authenticate

from django.contrib.auth.models import User

class LoginTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('user1', 'user1@domain.com', 'user1pass')

    def test_login_ok(self):

        credentials = {'username': 'user1', 'password': 'user1pass'}
        authenticated_user1 = authenticate(**credentials)

        self.assertTrue(authenticated_user1) # user terá o objeto

    def test_login_fail(self):

        credentials = {'username': 'user1', 'password': 'user1wrongpass'}
        authenticated_user1 = authenticate(**credentials)

        self.assertFalse(authenticated_user1) # user será None

