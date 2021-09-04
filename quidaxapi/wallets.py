from quidaxapi.base import QuidaxBase

# rmosvi6t
class Wallets(QuidaxBase):

    @classmethod
    def fetch_all_wallets(cls, user_id):
        """
        Fetch all wallets
        """
        return cls().requests.get(f'users/{user_id}/wallets')

    @classmethod
    def fetch_a_specific_currency_wallet(cls, user_id, currency):
        """
        Fetch a specific wallet
        """
        return cls().requests.get(f'users/{user_id}/wallets/{currency}')

    @classmethod
    def fetch_payment_addresses(cls, user_id, currency):
        """
        Fetch payment addresses
        """
        return cls().requests.get(f'users/{user_id}/wallets/{currency}/addresses')

    @classmethod
    def fetch_payment_address(cls, user_id, currency):
        """
        Fetch payment addresses
        """
        return cls().requests.get(f'users/{user_id}/wallets/{currency}/address')

    @classmethod
    def create_payment_address_for_a_cryptocurrency(cls, user_id, currency):
        """
        Create payment address for a cryptocurrency
        """
        return cls().requests.post(f'users/{user_id}/wallets/{currency}/addresses')

    @classmethod
    def get_payment_address_by_id(cls, user_id, currency, address_id):
        """
        Create payment address for a cryptocurrency
        """
        return cls().requests.get(f'users/{user_id}/wallets/{currency}/addresses/{address_id}')
