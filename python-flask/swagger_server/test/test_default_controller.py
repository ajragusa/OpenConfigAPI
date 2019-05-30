# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.counters_schema import CountersSchema  # noqa: E501
from swagger_server.models.hold_time_schema import HoldTimeSchema  # noqa: E501
from swagger_server.models.interface_counters_state import InterfaceCountersState  # noqa: E501
from swagger_server.models.interface_phys_config import InterfacePhysConfig  # noqa: E501
from swagger_server.models.interface_phys_holdtime_config import InterfacePhysHoldtimeConfig  # noqa: E501
from swagger_server.models.interface_phys_holdtime_state import InterfacePhysHoldtimeState  # noqa: E501
from swagger_server.models.interfaces_schema import InterfacesSchema  # noqa: E501
from swagger_server.models.subinterface_schema import SubinterfaceSchema  # noqa: E501
from swagger_server.models.subinterfaces_config import SubinterfacesConfig  # noqa: E501
from swagger_server.models.subinterfaces_schema import SubinterfacesSchema  # noqa: E501
from swagger_server.models.subinterfaces_state import SubinterfacesState  # noqa: E501
from swagger_server.models.subinterfaces_top import SubinterfacesTop  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_create_interfaces_by_id(self):
        """Test case for create_interfaces_by_id

        Create interfaces by ID
        """
        interfaces = InterfacesSchema()
        response = self.client.open(
            '/restconf/config/interfaces/',
            method='POST',
            data=json.dumps(interfaces),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_interfaces_interface_config_config_by_id(self):
        """Test case for create_interfaces_interface_config_config_by_id

        Create config by ID
        """
        config = InterfacePhysConfig()
        response = self.client.open(
            '/restconf/config/interfaces/interface/{name}/config/'.format(name='name_example'),
            method='POST',
            data=json.dumps(config),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_interfaces_interface_hold_time_config_config_by_id(self):
        """Test case for create_interfaces_interface_hold_time_config_config_by_id

        Create config by ID
        """
        config = InterfacePhysHoldtimeConfig()
        response = self.client.open(
            '/restconf/config/interfaces/interface/{name}/hold-time/config/'.format(name='name_example'),
            method='POST',
            data=json.dumps(config),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_interfaces_interface_hold_time_hold_time_by_id(self):
        """Test case for create_interfaces_interface_hold_time_hold_time_by_id

        Create hold-time by ID
        """
        hold_time = HoldTimeSchema()
        response = self.client.open(
            '/restconf/config/interfaces/interface/{name}/hold-time/'.format(name='name_example'),
            method='POST',
            data=json.dumps(hold_time),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_interfaces_interface_interface_by_id(self):
        """Test case for create_interfaces_interface_interface_by_id

        Create interface by ID
        """
        interface = SubinterfacesTop()
        response = self.client.open(
            '/restconf/config/interfaces/interface/{name}/'.format(name='name_example'),
            method='POST',
            data=json.dumps(interface),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_interfaces_interface_subinterfaces_subinterface_config_config_by_id(self):
        """Test case for create_interfaces_interface_subinterfaces_subinterface_config_config_by_id

        Create config by ID
        """
        config = SubinterfacesConfig()
        response = self.client.open(
            '/restconf/config/interfaces/interface/{name}/subinterfaces/subinterface/{index}/config/'.format(name='name_example', index='index_example'),
            method='POST',
            data=json.dumps(config),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_interfaces_interface_subinterfaces_subinterface_subinterface_by_id(self):
        """Test case for create_interfaces_interface_subinterfaces_subinterface_subinterface_by_id

        Create subinterface by ID
        """
        subinterface = SubinterfaceSchema()
        response = self.client.open(
            '/restconf/config/interfaces/interface/{name}/subinterfaces/subinterface/{index}/'.format(name='name_example', index='index_example'),
            method='POST',
            data=json.dumps(subinterface),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_interfaces_interface_subinterfaces_subinterfaces_by_id(self):
        """Test case for create_interfaces_interface_subinterfaces_subinterfaces_by_id

        Create subinterfaces by ID
        """
        subinterfaces = SubinterfacesSchema()
        response = self.client.open(
            '/restconf/config/interfaces/interface/{name}/subinterfaces/'.format(name='name_example'),
            method='POST',
            data=json.dumps(subinterfaces),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_interfaces_by_id(self):
        """Test case for delete_interfaces_by_id

        Delete interfaces by ID
        """
        response = self.client.open(
            '/restconf/config/interfaces/',
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_interfaces_interface_config_config_by_id(self):
        """Test case for delete_interfaces_interface_config_config_by_id

        Delete config by ID
        """
        response = self.client.open(
            '/restconf/config/interfaces/interface/{name}/config/'.format(name='name_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_interfaces_interface_hold_time_config_config_by_id(self):
        """Test case for delete_interfaces_interface_hold_time_config_config_by_id

        Delete config by ID
        """
        response = self.client.open(
            '/restconf/config/interfaces/interface/{name}/hold-time/config/'.format(name='name_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_interfaces_interface_hold_time_hold_time_by_id(self):
        """Test case for delete_interfaces_interface_hold_time_hold_time_by_id

        Delete hold-time by ID
        """
        response = self.client.open(
            '/restconf/config/interfaces/interface/{name}/hold-time/'.format(name='name_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_interfaces_interface_interface_by_id(self):
        """Test case for delete_interfaces_interface_interface_by_id

        Delete interface by ID
        """
        response = self.client.open(
            '/restconf/config/interfaces/interface/{name}/'.format(name='name_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_interfaces_interface_subinterfaces_subinterface_config_config_by_id(self):
        """Test case for delete_interfaces_interface_subinterfaces_subinterface_config_config_by_id

        Delete config by ID
        """
        response = self.client.open(
            '/restconf/config/interfaces/interface/{name}/subinterfaces/subinterface/{index}/config/'.format(name='name_example', index='index_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_interfaces_interface_subinterfaces_subinterface_subinterface_by_id(self):
        """Test case for delete_interfaces_interface_subinterfaces_subinterface_subinterface_by_id

        Delete subinterface by ID
        """
        response = self.client.open(
            '/restconf/config/interfaces/interface/{name}/subinterfaces/subinterface/{index}/'.format(name='name_example', index='index_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_interfaces_interface_subinterfaces_subinterfaces_by_id(self):
        """Test case for delete_interfaces_interface_subinterfaces_subinterfaces_by_id

        Delete subinterfaces by ID
        """
        response = self.client.open(
            '/restconf/config/interfaces/interface/{name}/subinterfaces/'.format(name='name_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_interfaces(self):
        """Test case for retrieve_interfaces

        Retrieve interfaces
        """
        response = self.client.open(
            '/restconf/config/interfaces/',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_interfaces_interface_config_config_by_id(self):
        """Test case for retrieve_interfaces_interface_config_config_by_id

        Retrieve config by ID
        """
        response = self.client.open(
            '/restconf/config/interfaces/interface/{name}/config/'.format(name='name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_interfaces_interface_hold_time_config_config_by_id(self):
        """Test case for retrieve_interfaces_interface_hold_time_config_config_by_id

        Retrieve config by ID
        """
        response = self.client.open(
            '/restconf/config/interfaces/interface/{name}/hold-time/config/'.format(name='name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_interfaces_interface_hold_time_hold_time_by_id(self):
        """Test case for retrieve_interfaces_interface_hold_time_hold_time_by_id

        Retrieve hold-time by ID
        """
        response = self.client.open(
            '/restconf/config/interfaces/interface/{name}/hold-time/'.format(name='name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_interfaces_interface_hold_time_state_state_by_id(self):
        """Test case for retrieve_interfaces_interface_hold_time_state_state_by_id

        Retrieve state by ID
        """
        response = self.client.open(
            '/restconf/config/interfaces/interface/{name}/hold-time/state/'.format(name='name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_interfaces_interface_interface_by_id(self):
        """Test case for retrieve_interfaces_interface_interface_by_id

        Retrieve interface by ID
        """
        response = self.client.open(
            '/restconf/config/interfaces/interface/{name}/'.format(name='name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_interfaces_interface_state_counters_counters_by_id(self):
        """Test case for retrieve_interfaces_interface_state_counters_counters_by_id

        Retrieve counters by ID
        """
        response = self.client.open(
            '/restconf/config/interfaces/interface/{name}/state/counters/'.format(name='name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_interfaces_interface_state_state_by_id(self):
        """Test case for retrieve_interfaces_interface_state_state_by_id

        Retrieve state by ID
        """
        response = self.client.open(
            '/restconf/config/interfaces/interface/{name}/state/'.format(name='name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_interfaces_interface_subinterfaces_subinterface_config_config_by_id(self):
        """Test case for retrieve_interfaces_interface_subinterfaces_subinterface_config_config_by_id

        Retrieve config by ID
        """
        response = self.client.open(
            '/restconf/config/interfaces/interface/{name}/subinterfaces/subinterface/{index}/config/'.format(name='name_example', index='index_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_interfaces_interface_subinterfaces_subinterface_state_counters_counters_by_id(self):
        """Test case for retrieve_interfaces_interface_subinterfaces_subinterface_state_counters_counters_by_id

        Retrieve counters by ID
        """
        response = self.client.open(
            '/restconf/config/interfaces/interface/{name}/subinterfaces/subinterface/{index}/state/counters/'.format(name='name_example', index='index_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_interfaces_interface_subinterfaces_subinterface_state_state_by_id(self):
        """Test case for retrieve_interfaces_interface_subinterfaces_subinterface_state_state_by_id

        Retrieve state by ID
        """
        response = self.client.open(
            '/restconf/config/interfaces/interface/{name}/subinterfaces/subinterface/{index}/state/'.format(name='name_example', index='index_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_interfaces_interface_subinterfaces_subinterface_subinterface_by_id(self):
        """Test case for retrieve_interfaces_interface_subinterfaces_subinterface_subinterface_by_id

        Retrieve subinterface by ID
        """
        response = self.client.open(
            '/restconf/config/interfaces/interface/{name}/subinterfaces/subinterface/{index}/'.format(name='name_example', index='index_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_interfaces_interface_subinterfaces_subinterfaces_by_id(self):
        """Test case for retrieve_interfaces_interface_subinterfaces_subinterfaces_by_id

        Retrieve subinterfaces by ID
        """
        response = self.client.open(
            '/restconf/config/interfaces/interface/{name}/subinterfaces/'.format(name='name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_interfaces_by_id(self):
        """Test case for update_interfaces_by_id

        Update interfaces by ID
        """
        interfaces = InterfacesSchema()
        response = self.client.open(
            '/restconf/config/interfaces/',
            method='PUT',
            data=json.dumps(interfaces),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_interfaces_interface_config_config_by_id(self):
        """Test case for update_interfaces_interface_config_config_by_id

        Update config by ID
        """
        config = InterfacePhysConfig()
        response = self.client.open(
            '/restconf/config/interfaces/interface/{name}/config/'.format(name='name_example'),
            method='PUT',
            data=json.dumps(config),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_interfaces_interface_hold_time_config_config_by_id(self):
        """Test case for update_interfaces_interface_hold_time_config_config_by_id

        Update config by ID
        """
        config = InterfacePhysHoldtimeConfig()
        response = self.client.open(
            '/restconf/config/interfaces/interface/{name}/hold-time/config/'.format(name='name_example'),
            method='PUT',
            data=json.dumps(config),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_interfaces_interface_hold_time_hold_time_by_id(self):
        """Test case for update_interfaces_interface_hold_time_hold_time_by_id

        Update hold-time by ID
        """
        hold_time = HoldTimeSchema()
        response = self.client.open(
            '/restconf/config/interfaces/interface/{name}/hold-time/'.format(name='name_example'),
            method='PUT',
            data=json.dumps(hold_time),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_interfaces_interface_interface_by_id(self):
        """Test case for update_interfaces_interface_interface_by_id

        Update interface by ID
        """
        interface = SubinterfacesTop()
        response = self.client.open(
            '/restconf/config/interfaces/interface/{name}/'.format(name='name_example'),
            method='PUT',
            data=json.dumps(interface),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_interfaces_interface_subinterfaces_subinterface_config_config_by_id(self):
        """Test case for update_interfaces_interface_subinterfaces_subinterface_config_config_by_id

        Update config by ID
        """
        config = SubinterfacesConfig()
        response = self.client.open(
            '/restconf/config/interfaces/interface/{name}/subinterfaces/subinterface/{index}/config/'.format(name='name_example', index='index_example'),
            method='PUT',
            data=json.dumps(config),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_interfaces_interface_subinterfaces_subinterface_subinterface_by_id(self):
        """Test case for update_interfaces_interface_subinterfaces_subinterface_subinterface_by_id

        Update subinterface by ID
        """
        subinterface = SubinterfaceSchema()
        response = self.client.open(
            '/restconf/config/interfaces/interface/{name}/subinterfaces/subinterface/{index}/'.format(name='name_example', index='index_example'),
            method='PUT',
            data=json.dumps(subinterface),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_interfaces_interface_subinterfaces_subinterfaces_by_id(self):
        """Test case for update_interfaces_interface_subinterfaces_subinterfaces_by_id

        Update subinterfaces by ID
        """
        subinterfaces = SubinterfacesSchema()
        response = self.client.open(
            '/restconf/config/interfaces/interface/{name}/subinterfaces/'.format(name='name_example'),
            method='PUT',
            data=json.dumps(subinterfaces),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
