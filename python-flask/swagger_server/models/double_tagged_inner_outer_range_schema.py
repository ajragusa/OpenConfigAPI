# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.vlan_logical_double_tagged_inner_outer_range_config import VlanLogicalDoubleTaggedInnerOuterRangeConfig  # noqa: F401,E501
from swagger_server import util


class DoubleTaggedInnerOuterRangeSchema(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, state: VlanLogicalDoubleTaggedInnerOuterRangeConfig=None, config: VlanLogicalDoubleTaggedInnerOuterRangeConfig=None):  # noqa: E501
        """DoubleTaggedInnerOuterRangeSchema - a model defined in Swagger

        :param state: The state of this DoubleTaggedInnerOuterRangeSchema.  # noqa: E501
        :type state: VlanLogicalDoubleTaggedInnerOuterRangeConfig
        :param config: The config of this DoubleTaggedInnerOuterRangeSchema.  # noqa: E501
        :type config: VlanLogicalDoubleTaggedInnerOuterRangeConfig
        """
        self.swagger_types = {
            'state': VlanLogicalDoubleTaggedInnerOuterRangeConfig,
            'config': VlanLogicalDoubleTaggedInnerOuterRangeConfig
        }

        self.attribute_map = {
            'state': 'state',
            'config': 'config'
        }

        self._state = state
        self._config = config

    @classmethod
    def from_dict(cls, dikt) -> 'DoubleTaggedInnerOuterRangeSchema':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DoubleTaggedInnerOuterRangeSchema of this DoubleTaggedInnerOuterRangeSchema.  # noqa: E501
        :rtype: DoubleTaggedInnerOuterRangeSchema
        """
        return util.deserialize_model(dikt, cls)

    @property
    def state(self) -> VlanLogicalDoubleTaggedInnerOuterRangeConfig:
        """Gets the state of this DoubleTaggedInnerOuterRangeSchema.

        State for matching double-tagged packets against an inner range and an outer range of VLAN identifiers.  # noqa: E501

        :return: The state of this DoubleTaggedInnerOuterRangeSchema.
        :rtype: VlanLogicalDoubleTaggedInnerOuterRangeConfig
        """
        return self._state

    @state.setter
    def state(self, state: VlanLogicalDoubleTaggedInnerOuterRangeConfig):
        """Sets the state of this DoubleTaggedInnerOuterRangeSchema.

        State for matching double-tagged packets against an inner range and an outer range of VLAN identifiers.  # noqa: E501

        :param state: The state of this DoubleTaggedInnerOuterRangeSchema.
        :type state: VlanLogicalDoubleTaggedInnerOuterRangeConfig
        """

        self._state = state

    @property
    def config(self) -> VlanLogicalDoubleTaggedInnerOuterRangeConfig:
        """Gets the config of this DoubleTaggedInnerOuterRangeSchema.

        Configuration for matching double-tagged packets against an inner range and an outer range of VLAN identifiers.  # noqa: E501

        :return: The config of this DoubleTaggedInnerOuterRangeSchema.
        :rtype: VlanLogicalDoubleTaggedInnerOuterRangeConfig
        """
        return self._config

    @config.setter
    def config(self, config: VlanLogicalDoubleTaggedInnerOuterRangeConfig):
        """Sets the config of this DoubleTaggedInnerOuterRangeSchema.

        Configuration for matching double-tagged packets against an inner range and an outer range of VLAN identifiers.  # noqa: E501

        :param config: The config of this DoubleTaggedInnerOuterRangeSchema.
        :type config: VlanLogicalDoubleTaggedInnerOuterRangeConfig
        """

        self._config = config
