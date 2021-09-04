"""Script defined to test the Class instance."""

import httpretty

from quidaxapi.tests.base_test_case import BaseTestCase
from quidaxapi.withdrawals import Withdrawal

class TestWithdrawal(BaseTestCase):
    """Method defined to test transaction instance."""

    @httpretty.activate
    def test_create_a_withdrawal(self):

        httpretty.register_uri(
            httpretty.POST,
            self.endpoint_url(
                "users/3en4nf/withdraws/"),
            content_type='text/json',
            body='{"status": "success", "message": "Successful", "data": []}',
            status=200,
        )

        response = Withdrawal.create_a_withdrawal(
            "3en4nf",)

        self.assertEquals(response['status'], 'success')

    @httpretty.activate
    def test_cancel_a_withdrawal(self):

        httpretty.register_uri(
            httpretty.POST,
            self.endpoint_url("users/3mdmnf/withdraws/jfmnn4mnm3/cancel"),
            content_type='text/json',
            body='{"status": "success", "message": "Successful", "data": "{}"}',
            status=200,
        )

        response = Withdrawal.cancel_a_withdrawal("3mdmnf", "jfmnn4mnm3",)
        self.assertEquals(response['status'], 'success')
    
    @httpretty.activate
    def test_fetch_a_withdrawal_details(self):

        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("users/3ermnv/withdraws/emn4mdn"),
            content_type='text/json',
            body='{"status": "success", "message": "Successful", "data": "{}"}',
            status=200,
        )

        response = Withdrawal.cancel_a_withdrawal("3mdmnf", "jfmnn4mnm3",)
        self.assertEquals(response['status'], 'success')

    @httpretty.activate
    def test_fetch_a_withdrawal_details(self):

        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("users/9ooini/withdraws?currency=btc&state=submitting"),
            content_type='text/json',
            body='{"status": "success", "message": "Successful", "data": "{}"}',
            status=200,
        )

        response = Withdrawal.fetch_a_withdrawal_details("9ooini", "btc", "submitting")
        self.assertEquals(response['status'], 'success')
