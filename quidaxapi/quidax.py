from quidaxapi.base import QuidaxBase
from quidaxapi.deposits import Deposits
from quidaxapi.instant_orders import InstantOrders
from quidaxapi.markets import Markets
from quidaxapi.orders import Orders
from quidaxapi.trades import Trades
from quidaxapi.users import Users
from quidaxapi.wallets import Wallets
from quidaxapi.withdrawals import Withdrawal
from quidaxapi.quote import Quotes


class Quidax(QuidaxBase):

    def __init__(self, secret_key=None):
        """Instantiate Basic Classes to call here."""
        QuidaxBase.__init__(self, secret_key=secret_key)
        self.users = Users
        self.orders = Orders
        self.instant_orders = InstantOrders
        self.markets = Markets
        self.wallets = Wallets
        self.withdrawal = Withdrawal
        self.deposits = Deposits
        self.trades = Trades
        self.quotes = Quotes
