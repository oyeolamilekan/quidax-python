import httpretty

from quidaxapi.tests.base_test_case import BaseTestCase
from quidaxapi.wallets import Wallets

class TestWallets(BaseTestCase):
    
    @httpretty.activate
    def test_fetch_all_wallets(self):

        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url(
                'users/ekjdnf/wallets'),
            content_type='text/json',
            body='{"status": "success", "message": "Successful", "data": []}',
            status=200,
        )

        response = Wallets.fetch_all_wallets("ekjdnf")
        self.assertTrue(response['status'], 'success')
    
    @httpretty.activate
    def test_fetch_a_specific_currency_wallet(self):

        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url(
                'users/ekjdnf/wallets/btc'),
            content_type='text/json',
            body='{"status": "success", "message": "Successful", "data": []}',
            status=200,
        )

        response = Wallets.fetch_a_specific_currency_wallet("ekjdnf", "btc")
        self.assertTrue(response['status'], 'success')
    
    @httpretty.activate
    def test_fetch_payment_addresses(self):

        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url(
                'users/fffmmf/wallets/btc/addresses'),
            content_type='text/json',
            body='{"status": "success", "message": "Successful", "data": []}',
            status=200,
        )

        response = Wallets.fetch_payment_addresses("fffmmf", "btc")
        self.assertTrue(response['status'], 'success')
    
    @httpretty.activate
    def test_fetch_payment_address(self):

        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url(
                'users/fffmmf/wallets/btc/address'),
            content_type='text/json',
            body='{"status": "success", "message": "Successful", "data": []}',
            status=200,
        )

        response = Wallets.fetch_payment_address("fffmmf", "btc")
        self.assertTrue(response['status'], 'success')
    

    @httpretty.activate
    def test_create_payment_address_for_a_cryptocurrency(self):

        httpretty.register_uri(
            httpretty.POST,
            self.endpoint_url(
                'users/vf65xhxk/wallets/btc/addresses'),
            content_type='text/json',
            body='{"status": "success", "message": "Successful", "data": []}',
            status=200,
        )


        response = Wallets.create_payment_address_for_a_cryptocurrency("vf65xhxk", "btc")
        self.assertTrue(response['status'], 'success')

    @httpretty.activate
    def test_get_payment_address_by_id(self):


        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url(
                'users/qarnq3wn/wallets/btc/addresses/jfne2ogr'),
            content_type='text/json',
            body='{"status": "success", "message": "Successful", "data": []}',
            status=200,
        )


        response = Wallets.get_payment_address_by_id("qarnq3wn", "btc", "jfne2ogr")
        self.assertTrue(response['status'], 'success')