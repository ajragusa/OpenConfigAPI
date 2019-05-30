# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.vlan_logical_single_tagged_list_config import VlanLogicalSingleTaggedListConfig  # noqa: F401,E501
from swagger_server import util


class SingleTaggedListSchema(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, state: VlanLogicalSingleTaggedListConfig=None, config: VlanLogicalSingleTaggedListConfig=None):  # noqa: E501
        """SingleTaggedListSchema - a model defined in Swagger

        :param state: The state of this SingleTaggedListSchema.  # noqa: E501
        :type state: VlanLogicalSingleTaggedListConfig
        :param config: The config of this SingleTaggedListSchema.  # noqa: E501
        :type config: VlanLogicalSingleTaggedListConfig
        """
        self.swagger_types = {
            'state': VlanLogicalSingleTaggedListConfig,
            'config': VlanLogicalSingleTaggedListConfig
        }

        self.attribute_map = {
            'state': 'state',
            'config': 'config'
        }

        self._state = state
        self._config = config

    @classmethod
    def from_dict(cls, dikt) -> 'SingleTaggedListSchema':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SingleTaggedListSchema of this SingleTaggedListSchema.  # noqa: E501
        :rtype: SingleTaggedListSchema
        """
        return util.deserialize_model(dikt, cls)

    @property
    def state(self) -> VlanLogicalSingleTaggedListConfig:
        """Gets the state of this SingleTaggedListSchema.

        State for matching single-tagged packets with a list of VLAN identifiers.  # noqa: E501

        :return: The state of this SingleTaggedListSchema.
        :rtype: VlanLogicalSingleTaggedListConfig
        """
        return self._state

    @state.setter
    def state(self, state: VlanLogicalSingleTaggedListConfig):
        """Sets the state of this SingleTaggedListSchema.

        State for matching single-tagged packets with a list of VLAN identifiers.  # noqa: E501

        :param state: The state of this SingleTaggedListSchema.
        :type state: VlanLogicalSingleTaggedListConfig
        """

        self._state = state

    @property
    def config(self) -> VlanLogicalSingleTaggedListConfig:
        """Gets the config of this SingleTaggedListSchema.

        Configuration for matching single-tagged packets with a list of VLAN identifiers.  # noqa: E501

        :return: The config of this SingleTaggedListSchema.
        :rtype: VlanLogicalSingleTaggedListConfig
        """
        return self._config

    @config.setter
    def config(self, config: VlanLogicalSingleTaggedListConfig):
        """Sets the config of this SingleTaggedListSchema.

        Configuration for matching single-tagged packets with a list of VLAN identifiers.  # noqa: E501

        :param config: The config of this SingleTaggedListSchema.
        :type config: VlanLogicalSingleTaggedListConfig
        """

        self._config = config