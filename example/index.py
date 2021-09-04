from .base import quidax

import json
# rmosvi6t
# response = quidax.markets.list_all_markets()
# response = quidax.wallets.create_payment_address_for_a_cryptocurrency("i5efm3vb", "doge")
response = quidax.wallets.fetch_payment_address("i5efm3vb", "doge")

# curr = ['btc', 'ltc', 'eth', 'xrp', 'usdt', 'dash', 'trx']
# users = quidax.users.all_sub_account()

# response = quidax.quotes.quote("trxngn", "trx", "bid", 1)
# response = quidax.withdrawal.create_a_withdrawal()
# response = quidax.orders.create_buy_or_sell_order("me", market="btcngn", side="buy", ord_type="limit", price=0.9, volume=0.0004)
# response = quidax.orders.cancel_an_order("me", "juaumj7o")
# response = quidax.instant_orders.create_instant_order("me", bid="ngn", ask="ltc", type="sell", volume="0.0001", unit="ltc")
# response = quidax.instant_orders.create_instant_order("me", bid="ngn", ask="trx", type="buy", total=5, unit="ngn")
# response = quidax.instant_orders.confirm_instant_orders("me", response['data']['id'])
# response = quidax.instant_orders.confirm_instant_orders("me", "2nv7osuf")
# response = quidax.orders.get_all_orders("me", "btcngn", "cancel", "asc")
# response = quidax.users.create(first_name="oye", last_name="lekan", email="lekann@gmail.com")
# for currency in curr:
    # response = quidax.wallets.fetch_payment_address("vf65xhxk", currency)
# for user in users['data']:
#     response = quidax.wallets.fetch_all_wallets(user['id'])
#     data_dict_data = {"data": response['data'], }
#     data_dict = {
#         "user_info": user,
#         **data_dict_data
#     }
#     print(json.dumps(data_dict, indent=4))
# response = quidax.users.all_sub_account()
# response = quidax.wallets.create_payment_address_for_a_cryptocurrency("vf65xhxk", "btc")
# response = quidax.wallets.get_payment_address_by_id("b465wwri", "trx", "lin7e743")
# response = quidax.wallets.get_payment_address_by_id("qarnq3wn", "usdt", "jfne2ogr")
# response = quidax.withdrawal.cance_a_withdrawal("b465wwri", "5hjy6tlo")

print(json.dumps(response, indent=4))
