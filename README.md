# quidax-python


Python plugin for [Quidax](https://www.quidax.com/)
View on [pypi.python.org](https://pypi.org/project/quidax-python/)

## Installation

```shell
pip install quidax-python
```

## Instantiate Quidax

```python
from quidaxapi.quidax import Quidax
quidax_secret_key = "5om3secretK3y"
quidax = Quidax(secret_key=quidax_secret_key)

# to use users class
quidax.users.all_sub_account()

# to list all markets
quidax.markets.list_all_markets()

# to fetch user trades
quidax.trades.trades(user_id)

# to fetch wallets from a user and a specific wallet.
quidax.wallets.fetch_a_specific_currency_wallet(user_id, currency)
```

## DOC Reference: <https://developer.quidax.com/>

### Other methods can be found in the docs folder


### Available resources

```Python

Users
Orders
InstantOrders
Markets
Wallets
Withdrawal
Deposits
Trades
Quotes
```

Please reference the **docs** folder for usage,

This repo won't be possible without the hard work of [andela-sjames](https://github.com/andela-sjames).