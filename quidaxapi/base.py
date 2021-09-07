import requests
import quidaxapi as api
HEADERS = {'Authorization': 'Bearer {}'}
API_URL = 'https://www.quidax.com/api/v1/'


class Borg:
    """Borg class making class attributes global"""
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class QuidaxBase(Borg):
    """Base Class used across defined."""

    def __init__(self, **kwargs):
        """Initialize Quidax with secret key."""
        Borg.__init__(self)
        secret_key = kwargs.get('secret_key', api.SECRET_KEY)
        authorization = kwargs.get(
            'authorization',
            f"{HEADERS['Authorization'].format(secret_key)}",)
        headers = dict(Authorization=authorization)
        arguments = dict(api_url=API_URL, headers=headers)
        if not hasattr(self, 'requests'):
            req = QuidaxRequests(**arguments)
            self._shared_state.update(requests=req)


class QuidaxRequests(object):

    def __init__(self, api_url='https://www.quidax.com/api/v1/',
                 headers=None):
        """Initialize Quidax Request object for browsing resource.
        Args:
                api_url: str
                headers: dict
        """
        self.API_BASE_URL = f"{api_url}"
        self.headers = headers

    def _request(self, method, resource_uri, **kwargs):
        """Perform a method on a resource.
        Args:
                method: requests.`method`
                resource_uri: resource endpoint
        Raises:
                HTTPError
        Returns:
                JSON Response
        """
        data = kwargs.get('data')
        qs = kwargs.get('qs')

        response = method(
            self.API_BASE_URL + resource_uri,
            json=data, headers=self.headers,
            params=qs
        )
        try:
            if "InvalidSecretKeyError" in response.text:
                return {"status": "error", "message": "Invalid secret key"}
            return response.json()
        except:
            return {"status": "error", "message": response.text}

    def get(self, endpoint, **kwargs):
        """Get a resource.
        Args:
                endpoint: resource endpoint.
        """
        return self._request(requests.get, endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        """Create a resource.
        Args:
                endpoint: resource endpoint.
        """
        return self._request(requests.post, endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        """Update a resource.
        Args:
                endpoint: resource endpoint.
        """
        return self._request(requests.put, endpoint, **kwargs)
