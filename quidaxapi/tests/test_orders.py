"""Script defined to test the Class instance."""

import httpretty

from quidaxapi.tests.base_test_case import BaseTestCase
from quidaxapi.orders import Orders


class TestOrders(BaseTestCase):
    """Method defined to test transaction instance."""

    @httpretty.activate
    def test_get_an_order_details(self):

        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url(
                'users/237847/orders/end8enh3'),
            content_type='text/json',
            body='{"status": "success", "message": "Successful", "data": []}',
            status=200,
        )

        response = Orders.get_an_order_details(
            "237847", "end8enh3",)

        self.assertEquals(response['status'], 'success')

    @httpretty.activate
    def test_get_all_orders(self):

        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("users/2ndmncd/orders?market=btcngn&state=wait&order_by=desc"),
            content_type='text/json',
            body='{"status": "success", "message": "Successful", "data": "{}"}',
            status=200,
        )

        response = Orders.get_all_orders("2ndmncd", "btcngn", "wait", "desc")
        self.assertEquals(response['status'], 'success')
    
    @httpretty.activate
    def test_cancel_an_order(self):

        httpretty.register_uri(
            httpretty.POST,
            self.endpoint_url('users/2ndmncd/orders/ndmnnd/cancel'),
            content_type='text/json',
            body='{"status": "success", "message": "Successful", "data": "{}"}',
            status=200,
        )

        response = Orders.cancel_an_order("2ndmncd", "ndmnnd",)
        self.assertEquals(response['status'], 'success')
    
    @httpretty.activate
    def test_create_buy_or_sell_order(self):

        httpretty.register_uri(
            httpretty.POST,
            self.endpoint_url("users/23jdhb/orders"),
            content_type='text/json',
            body='{"status": "success", "message": "Successful", "data": "{}"}',
            status=200,
        )

        response = Orders.create_buy_or_sell_order("23jdhb",)
        self.assertEquals(response['status'], 'success')
