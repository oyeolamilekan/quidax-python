from ..base import quidax

response = quidax.wallets.create_payment_address_for_a_cryptocurrency("<account_id>", 'btc')

print(response)