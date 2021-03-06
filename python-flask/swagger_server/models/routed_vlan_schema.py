# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.sub_unnumbered_top import SubUnnumberedTop  # noqa: F401,E501
from swagger_server.models.vlan_routed_config import VlanRoutedConfig  # noqa: F401,E501
from swagger_server.models.vlan_routed_state import VlanRoutedState  # noqa: F401,E501
from swagger_server import util


class RoutedVlanSchema(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, state: VlanRoutedState=None, config: VlanRoutedConfig=None, ipv4: SubUnnumberedTop=None, ipv6: SubUnnumberedTop=None):  # noqa: E501
        """RoutedVlanSchema - a model defined in Swagger

        :param state: The state of this RoutedVlanSchema.  # noqa: E501
        :type state: VlanRoutedState
        :param config: The config of this RoutedVlanSchema.  # noqa: E501
        :type config: VlanRoutedConfig
        :param ipv4: The ipv4 of this RoutedVlanSchema.  # noqa: E501
        :type ipv4: SubUnnumberedTop
        :param ipv6: The ipv6 of this RoutedVlanSchema.  # noqa: E501
        :type ipv6: SubUnnumberedTop
        """
        self.swagger_types = {
            'state': VlanRoutedState,
            'config': VlanRoutedConfig,
            'ipv4': SubUnnumberedTop,
            'ipv6': SubUnnumberedTop
        }

        self.attribute_map = {
            'state': 'state',
            'config': 'config',
            'ipv4': 'ipv4',
            'ipv6': 'ipv6'
        }

        self._state = state
        self._config = config
        self._ipv4 = ipv4
        self._ipv6 = ipv6

    @classmethod
    def from_dict(cls, dikt) -> 'RoutedVlanSchema':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RoutedVlanSchema of this RoutedVlanSchema.  # noqa: E501
        :rtype: RoutedVlanSchema
        """
        return util.deserialize_model(dikt, cls)

    @property
    def state(self) -> VlanRoutedState:
        """Gets the state of this RoutedVlanSchema.

        Operational state data   # noqa: E501

        :return: The state of this RoutedVlanSchema.
        :rtype: VlanRoutedState
        """
        return self._state

    @state.setter
    def state(self, state: VlanRoutedState):
        """Sets the state of this RoutedVlanSchema.

        Operational state data   # noqa: E501

        :param state: The state of this RoutedVlanSchema.
        :type state: VlanRoutedState
        """

        self._state = state

    @property
    def config(self) -> VlanRoutedConfig:
        """Gets the config of this RoutedVlanSchema.

        Configuration data for routed vlan interfaces  # noqa: E501

        :return: The config of this RoutedVlanSchema.
        :rtype: VlanRoutedConfig
        """
        return self._config

    @config.setter
    def config(self, config: VlanRoutedConfig):
        """Sets the config of this RoutedVlanSchema.

        Configuration data for routed vlan interfaces  # noqa: E501

        :param config: The config of this RoutedVlanSchema.
        :type config: VlanRoutedConfig
        """

        self._config = config

    @property
    def ipv4(self) -> SubUnnumberedTop:
        """Gets the ipv4 of this RoutedVlanSchema.

        Parameters for the IPv4 address family.  # noqa: E501

        :return: The ipv4 of this RoutedVlanSchema.
        :rtype: SubUnnumberedTop
        """
        return self._ipv4

    @ipv4.setter
    def ipv4(self, ipv4: SubUnnumberedTop):
        """Sets the ipv4 of this RoutedVlanSchema.

        Parameters for the IPv4 address family.  # noqa: E501

        :param ipv4: The ipv4 of this RoutedVlanSchema.
        :type ipv4: SubUnnumberedTop
        """

        self._ipv4 = ipv4

    @property
    def ipv6(self) -> SubUnnumberedTop:
        """Gets the ipv6 of this RoutedVlanSchema.

        Parameters for the IPv6 address family.  # noqa: E501

        :return: The ipv6 of this RoutedVlanSchema.
        :rtype: SubUnnumberedTop
        """
        return self._ipv6

    @ipv6.setter
    def ipv6(self, ipv6: SubUnnumberedTop):
        """Sets the ipv6 of this RoutedVlanSchema.

        Parameters for the IPv6 address family.  # noqa: E501

        :param ipv6: The ipv6 of this RoutedVlanSchema.
        :type ipv6: SubUnnumberedTop
        """

        self._ipv6 = ipv6
