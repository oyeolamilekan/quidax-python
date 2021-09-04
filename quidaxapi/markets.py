from quidaxapi.base import QuidaxBase


class Markets(QuidaxBase):

    @classmethod
    def list_all_markets(cls):
        """
        List all markets
        """
        return cls().requests.get('markets')

    @classmethod
    def list_market_tickers(cls):
        """
        List all market tickers
        """
        return cls().requests.get('markets/tickers')

    @classmethod
    def fetch_market_ticker(cls, market):
        """
        fetch a market ticker
        """
        return cls().requests.get(f'markets/tickers/{market}')
