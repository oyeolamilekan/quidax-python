from unittest import TestCase

class BaseTestCase(TestCase):

    def endpoint_url(self, path):
        if path[0] == '/':
            return f'https://www.quidax.com/api/v1{path}'
        return f'https://www.quidax.com/api/v1/{path}'