from quidaxapi.base import QuidaxBase


class Users(QuidaxBase):

    @classmethod
    def create(cls, **kwargs):
        """
        Creates account for user
        """
        return cls().requests.post('users', data=kwargs)

    @classmethod
    def all_sub_account(cls):
        """
        Get all sub account
        """

        return cls().requests.get('users')

    @classmethod
    def get_account_details(cls, account_id):
        """
        Get account details
        """

        return cls().requests.get(f'users/{account_id}')

    @classmethod
    def edit_account(cls, account_id, **kwargs):
        """
        Edit account
        """

        return cls().requests.put(f'users/{account_id}', data=kwargs)
