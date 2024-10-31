# coding: utf-8

"""
    Notehub API

    The OpenAPI definition for the Notehub.io API. 

    The version of the OpenAPI document: 1.2.0
    Contact: engineering@blues.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from notehub_py.models.user_db_route import UserDbRoute

class TestUserDbRoute(unittest.TestCase):
    """UserDbRoute unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserDbRoute:
        """Test UserDbRoute
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserDbRoute`
        """
        model = UserDbRoute()
        if include_optional:
            return UserDbRoute(
                uid = 'route:8d65a087d5d290ce5bdf03aeff2becc0',
                label = 'success route',
                type = 'http',
                modified = '2020-03-09T17:58:37Z',
                disabled = True
            )
        else:
            return UserDbRoute(
        )
        """

    def testUserDbRoute(self):
        """Test UserDbRoute"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
