from ..base import quidax

response = quidax.wallets.fetch_payment_address("<address_id>", "<currency>")

print(response)
