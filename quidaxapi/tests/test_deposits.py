"""Script defined to test the Class instance."""

import httpretty

from quidaxapi.tests.base_test_case import BaseTestCase
from quidaxapi.deposits import Deposits


class TestDeposits(BaseTestCase):
    """Method defined to test transaction instance."""

    @httpretty.activate
    def test_fetch_all_deposits(self):

        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url(
                "users/2wnnmenrbe/deposits?currency=btc&state=submitting"),
            content_type='text/json',
            body='{"status": "success", "message": "Successful", "data": []}',
            status=200,
        )

        response = Deposits.fetch_all_deposits(
            "2wnnmenrbe", "btcng", "pending",)

        self.assertEquals(response['status'], 'success')

    @httpretty.activate
    def test_fetch_a_deposit(self):

        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url("users/23jdhb/deposits/zd5kkocy"),
            content_type='text/json',
            body='{"status": "success", "message": "Successful", "data": "{}"}',
            status=200,
        )

        response = Deposits.fetch_a_deposit("23jdhb", "zd5kkocy",)
        self.assertEquals(response['status'], 'success')
