"""Script defined to test the Class instance."""

import httpretty

from quidaxapi.tests.base_test_case import BaseTestCase
from quidaxapi.quote import Quotes


class TestDeposits(BaseTestCase):
    """Method defined to test transaction instance."""

    @httpretty.activate
    def test_quote(self):

        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url(
                'quotes?market=btcngn&unit=btc&kind=bid&volume=1',),
            content_type='text/json',
            body='{"status": "success", "message": "Successful", "data": []}',
            status=200,
        )

        response = Quotes.quote(
            "btcngn", "btc", "bid", 1)

        self.assertEqual(response['status'], 'success')
