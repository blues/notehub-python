# coding: utf-8

"""
    Notehub API

    The OpenAPI definition for the Notehub.io API. 

    The version of the OpenAPI document: 1.0.0
    Contact: engineering@blues.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from notehub_py.models.route_schema import RouteSchema

class TestRouteSchema(unittest.TestCase):
    """RouteSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RouteSchema:
        """Test RouteSchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RouteSchema`
        """
        model = RouteSchema()
        if include_optional:
            return RouteSchema(
                fleets = [
                    ''
                    ],
                filter = notehub_py.models.http_filter.http_filter(
                    type = 'all', 
                    system_notefiles = True, 
                    files = [
                        ''
                        ], ),
                transform = notehub_py.models.snowflake_transform.snowflake_transform(
                    format = 'jsonata', 
                    jsonata = '', ),
                throttle_ms = 56,
                url = '',
                http_headers = {headerName1=headerValue1, headerName2=headerValue2},
                disable_http_headers = True,
                timeout = 56,
                token = '',
                alias = '',
                broker = '',
                port = 56,
                username = '',
                password = '',
                topic = '',
                certificate = '-----BEGIN CERTIFICATE-----\nMIIBpTCCA...JgVLttUY=\n-----END CERTIFICATE-----',
                certificate_name = '',
                key = '-----BEGIN PRIVATE KEY-----\nMIIEvwIBA...SleBlvA==\n-----END PRIVATE KEY-----',
                private_key_name = 'present',
                region = '',
                access_key_id = '',
                access_key_secret = '',
                message_group_id = '',
                message_deduplication_id = '',
                channel = 'C8675309',
                test_api = True,
                data_feed_key = '',
                client_id = '',
                client_secret = '',
                functions_key_secret = '',
                sas_policy_name = '',
                sas_policy_key = '',
                app_key = '',
                organization_name = '',
                account_name = '',
                user_name = '',
                pem = '-----BEGIN PRIVATE KEY-----\nMIIEvwIBA...SleBlvA==\n-----END PRIVATE KEY-----',
                slack_type = '',
                bearer = 'xoxb-1234-56789abcdefghijklmnop',
                webhook_url = 'https://hooks.slack.com/services/FOO4BAR/THIS4THAT/123xYzaBC456',
                text = '[.device] reported temp(s) of [.body.temp] at [.body.location]',
                blocks = ''
            )
        else:
            return RouteSchema(
        )
        """

    def testRouteSchema(self):
        """Test RouteSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()