"""Script defined to test the Class instance."""

import httpretty

from quidaxapi.tests.base_test_case import BaseTestCase
from quidaxapi.trades import Trades

class TestTrades(BaseTestCase):
    """Method defined to test transaction instance."""

    @httpretty.activate
    def test_trades(self):

        httpretty.register_uri(
            httpretty.GET,
            self.endpoint_url(
                'users/3ej4nf/trades'),
            content_type='text/json',
            body='{"status": "success", "message": "Successful", "data": []}',
            status=200,
        )

        response = Trades.trades("3ej4nf")
        self.assertTrue(response['status'], 'success')