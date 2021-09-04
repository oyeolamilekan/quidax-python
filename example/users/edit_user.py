from ..base import quidax

response = quidax.users.edit_account(
    "<account_id>", first_name="oye", last_name="lekan", email="lekann@gmail.com",)

print(response)
