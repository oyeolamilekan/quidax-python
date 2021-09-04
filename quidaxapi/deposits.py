from quidaxapi.base import QuidaxBase


class Deposits(QuidaxBase):

    @classmethod
    def fetch_all_deposits(cls, user_id, currency, state):
        """
        List all deposits
        """
        return cls().requests.get(f'users/{user_id}/deposits?currency={currency}&state={state}')
    
    @classmethod
    def fetch_a_deposit(cls, user_id, desposit_id):
        """
        Fetch a deposit
        """
        return cls().requests.get(f'users/{user_id}/deposits/{desposit_id}')