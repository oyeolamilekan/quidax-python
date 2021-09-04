from quidaxapi.base import QuidaxBase


class InstantOrders(QuidaxBase):

    @classmethod
    def fetch_all_instant_orders(cls, user_id, market, state, order_by):
        return cls().requests.get(f'users/{user_id}/instant_orders?market={market}&state={state}&order_by={order_by}',)
    
    @classmethod
    def fetch_a_particular_instant_order(cls, user_id, instant_order_id):
        return cls().requests.get(f'users/{user_id}/instant_orders/{instant_order_id}',)

    @classmethod
    def create_instant_order(cls, account_id, **kwargs):
        return cls().requests.post(f'users/{account_id}/instant_orders', data=kwargs)

    @classmethod
    def requote_instant_order(cls, account_id, instant_order_id):
        return cls().requests.post(f'users/{account_id}/instant_orders/{instant_order_id}/requote')

    @classmethod
    def confirm_instant_orders(cls, account_id, instant_order_id):
        return cls().requests.post(f'users/{account_id}/instant_orders/{instant_order_id}/confirm')
