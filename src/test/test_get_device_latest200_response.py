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

from notehub_py.models.get_device_latest200_response import GetDeviceLatest200Response

class TestGetDeviceLatest200Response(unittest.TestCase):
    """GetDeviceLatest200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetDeviceLatest200Response:
        """Test GetDeviceLatest200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetDeviceLatest200Response`
        """
        model = GetDeviceLatest200Response()
        if include_optional:
            return GetDeviceLatest200Response(
                latest_events = [
                    notehub_py.models.event.Event(
                        event = '', 
                        session = '', 
                        tls = True, 
                        best_id = '', 
                        device = '', 
                        sn = '', 
                        product = '', 
                        app = '', 
                        received = 1.337, 
                        req = '', 
                        when = 1.337, 
                        file = '', 
                        note = '', 
                        updates = 1.337, 
                        body = notehub_py.models.body.body(), 
                        payload = '', 
                        best_location_type = '', 
                        best_location_when = 1.337, 
                        best_lat = 1.337, 
                        best_lon = 1.337, 
                        best_location = '', 
                        best_country = '', 
                        best_timezone = '', 
                        where_olc = '', 
                        where_when = 1.337, 
                        where_lat = 1.337, 
                        where_lon = 1.337, 
                        where_location = '', 
                        where_country = '', 
                        where_timezone = '', 
                        tower_when = 1.337, 
                        tower_lat = 1.337, 
                        tower_lon = 1.337, 
                        tower_country = '', 
                        tower_location = '', 
                        tower_timezone = '', 
                        tower_id = '', 
                        tri_when = 1.337, 
                        tri_lat = 1.337, 
                        tri_lon = 1.337, 
                        tri_location = '', 
                        tri_country = '', 
                        tri_timezone = '', 
                        tri_points = 1.337, 
                        moved = 1.337, 
                        orientation = '', 
                        rssi = 1.337, 
                        sinr = 1.337, 
                        rsrp = 1.337, 
                        rsrq = 1.337, 
                        rat = '', 
                        bars = 1.337, 
                        voltage = 1.337, 
                        temp = 1.337, 
                        environment = notehub_py.models.environment.environment(), )
                    ]
            )
        else:
            return GetDeviceLatest200Response(
        )
        """

    def testGetDeviceLatest200Response(self):
        """Test GetDeviceLatest200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
