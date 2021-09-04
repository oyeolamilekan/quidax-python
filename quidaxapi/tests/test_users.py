import httpretty

from quidaxapi.tests.base_test_case import BaseTestCase
from quidaxapi.users import Users

class TestUsers(BaseTestCase):
    @httpretty.activate
    def test_create_user(self):

        httpretty.register_uri(
            httpretty.POST,
            self.endpoint_url(
                'users'),
            content_type='text/json',
            body='{"status": "success", "message": "Successful", "data": []}',
            status=200,
        )

        response = Users.create(first_name="oye", last_name="lekan", email="lekann@gmail.com")
        self.assertTrue(response['status'], 'success')
    
    @httpretty.activate
    def test_all_sub_account(self):

        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url(
                'users'),
            content_type='text/json',
            body='{"status": "success", "message": "Successful", "data": []}',
            status=200,
        )

        response = Users.all_sub_account()
        self.assertTrue(response['status'], 'success')
    
    @httpretty.activate
    def test_account_details(self):

        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url(
                'users/3ej4nf'),
            content_type='text/json',
            body='{"status": "success", "message": "Successful", "data": []}',
            status=200,
        )

        response = Users.get_account_details("3ej4nf")
        self.assertTrue(response['status'], 'success')
    
    @httpretty.activate
    def test_edit_account(self):

        httpretty.register_uri(
            httpretty.PUT,
            self.endpoint_url(
                'users/3ej4nf'),
            content_type='text/json',
            body='{"status": "success", "message": "Successful", "data": []}',
            status=200,
        )

        response = Users.edit_account("3ej4nf", first_name="oye", last_name="lekan", email="lekann@gmail.com")
        self.assertTrue(response['status'], 'success')