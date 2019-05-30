# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.vlan_logical_double_tagged_config import VlanLogicalDoubleTaggedConfig  # noqa: F401,E501
from swagger_server import util


class VlanLogicalMatchTopMatchDoubleTagged(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, state: VlanLogicalDoubleTaggedConfig=None, config: VlanLogicalDoubleTaggedConfig=None):  # noqa: E501
        """VlanLogicalMatchTopMatchDoubleTagged - a model defined in Swagger

        :param state: The state of this VlanLogicalMatchTopMatchDoubleTagged.  # noqa: E501
        :type state: VlanLogicalDoubleTaggedConfig
        :param config: The config of this VlanLogicalMatchTopMatchDoubleTagged.  # noqa: E501
        :type config: VlanLogicalDoubleTaggedConfig
        """
        self.swagger_types = {
            'state': VlanLogicalDoubleTaggedConfig,
            'config': VlanLogicalDoubleTaggedConfig
        }

        self.attribute_map = {
            'state': 'state',
            'config': 'config'
        }

        self._state = state
        self._config = config

    @classmethod
    def from_dict(cls, dikt) -> 'VlanLogicalMatchTopMatchDoubleTagged':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VlanLogicalMatchTop_match_doubleTagged of this VlanLogicalMatchTopMatchDoubleTagged.  # noqa: E501
        :rtype: VlanLogicalMatchTopMatchDoubleTagged
        """
        return util.deserialize_model(dikt, cls)

    @property
    def state(self) -> VlanLogicalDoubleTaggedConfig:
        """Gets the state of this VlanLogicalMatchTopMatchDoubleTagged.

        State for matching double-tagged packets against inner exact and outer exact VLAN identifiers.  # noqa: E501

        :return: The state of this VlanLogicalMatchTopMatchDoubleTagged.
        :rtype: VlanLogicalDoubleTaggedConfig
        """
        return self._state

    @state.setter
    def state(self, state: VlanLogicalDoubleTaggedConfig):
        """Sets the state of this VlanLogicalMatchTopMatchDoubleTagged.

        State for matching double-tagged packets against inner exact and outer exact VLAN identifiers.  # noqa: E501

        :param state: The state of this VlanLogicalMatchTopMatchDoubleTagged.
        :type state: VlanLogicalDoubleTaggedConfig
        """

        self._state = state

    @property
    def config(self) -> VlanLogicalDoubleTaggedConfig:
        """Gets the config of this VlanLogicalMatchTopMatchDoubleTagged.

        Configuration for matching double-tagged packets against inner exact and outer exact VLAN identifiers.  # noqa: E501

        :return: The config of this VlanLogicalMatchTopMatchDoubleTagged.
        :rtype: VlanLogicalDoubleTaggedConfig
        """
        return self._config

    @config.setter
    def config(self, config: VlanLogicalDoubleTaggedConfig):
        """Sets the config of this VlanLogicalMatchTopMatchDoubleTagged.

        Configuration for matching double-tagged packets against inner exact and outer exact VLAN identifiers.  # noqa: E501

        :param config: The config of this VlanLogicalMatchTopMatchDoubleTagged.
        :type config: VlanLogicalDoubleTaggedConfig
        """

        self._config = config