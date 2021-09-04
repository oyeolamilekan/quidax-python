from quidaxapi.base import QuidaxBase


class Orders(QuidaxBase):

    @classmethod
    def get_an_order_details(cls, account_id, order_id):
        """
        Fetch an order details for the authenticated user (/me) or a sub account (/user_id).
        """
        return cls().requests.get(f'users/{account_id}/orders/{order_id}')

    @classmethod
    def get_all_orders(cls, account_id, market, state, order_by):
        """
        Fetch an order for the authenticated user (/me) or a sub account (/user_id) i.e. user_id_or_reference can either be 'me' for a merchant order and for sub-account linked to a merchant, it refers to the sub-account id.
        """
        return cls().requests.get(f'users/{account_id}/orders?market={market}&state={state}&order_by={order_by}')

    @classmethod
    def cancel_an_order(cls, account_id, order_id):
        """
        Cancel an order linked to the authenticated user or a subaccount tethered to the authenticated user
        """
        return cls().requests.post(f'users/{account_id}/orders/{order_id}/cancel')

    @classmethod
    def create_buy_or_sell_order(cls, user_id, **kwargs):
        """
        Create a sell or buy order for the authenticated user or a subaccount tethered to authenticated user.
        """
        return cls().requests.post(f"users/{user_id}/orders", data=kwargs)
