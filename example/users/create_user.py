from ..base import quidax

response = quidax.users.create(first_name="oye", last_name="lekan", email="lekann@gmail.com")

print(response)