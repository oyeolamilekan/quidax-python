from quidaxapi.base import QuidaxBase

class Withdrawal(QuidaxBase):

    @classmethod
    def create_a_withdrawal(cls, user_id, **kwargs):
        return cls().requests.post(f"users/{user_id}/withdraws/", data=kwargs)
    

    @classmethod
    def cancel_a_withdrawal(cls, user_id, withdraw_id):
        return cls().requests.post(f"users/{user_id}/withdraws/{withdraw_id}/cancel")
    
    @classmethod
    def fetch_a_withdrawal_details(cls, user_id, withdraw_id):
        return cls().requests.get(f"users/{user_id}/withdraws/{withdraw_id}")
    

    @classmethod
    def fetch_a_withdrawal_details(cls, user_id, currency, state):
        return cls().requests.get(f"users/{user_id}/withdraws?currency={currency}&state={state}")