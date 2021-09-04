from quidaxapi.base import QuidaxBase

class Trades(QuidaxBase):

    @classmethod
    def trades(cls, user_id):
        """
        Fetch trades for the authenticated user or a subaccount tethered to the authenticated user
        """
        return cls().requests.get(f'users/{user_id}/trades')