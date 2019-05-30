# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class VlanLogicalSingleTaggedRangeConfig(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, high_vlan_id: str=None, low_vlan_id: str=None):  # noqa: E501
        """VlanLogicalSingleTaggedRangeConfig - a model defined in Swagger

        :param high_vlan_id: The high_vlan_id of this VlanLogicalSingleTaggedRangeConfig.  # noqa: E501
        :type high_vlan_id: str
        :param low_vlan_id: The low_vlan_id of this VlanLogicalSingleTaggedRangeConfig.  # noqa: E501
        :type low_vlan_id: str
        """
        self.swagger_types = {
            'high_vlan_id': str,
            'low_vlan_id': str
        }

        self.attribute_map = {
            'high_vlan_id': 'highVlanId',
            'low_vlan_id': 'lowVlanId'
        }

        self._high_vlan_id = high_vlan_id
        self._low_vlan_id = low_vlan_id

    @classmethod
    def from_dict(cls, dikt) -> 'VlanLogicalSingleTaggedRangeConfig':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VlanLogicalSingleTaggedRangeConfig of this VlanLogicalSingleTaggedRangeConfig.  # noqa: E501
        :rtype: VlanLogicalSingleTaggedRangeConfig
        """
        return util.deserialize_model(dikt, cls)

    @property
    def high_vlan_id(self) -> str:
        """Gets the high_vlan_id of this VlanLogicalSingleTaggedRangeConfig.

        The high-value VLAN identifier in a range for single-tagged packets. The range is matched inclusively.  # noqa: E501

        :return: The high_vlan_id of this VlanLogicalSingleTaggedRangeConfig.
        :rtype: str
        """
        return self._high_vlan_id

    @high_vlan_id.setter
    def high_vlan_id(self, high_vlan_id: str):
        """Sets the high_vlan_id of this VlanLogicalSingleTaggedRangeConfig.

        The high-value VLAN identifier in a range for single-tagged packets. The range is matched inclusively.  # noqa: E501

        :param high_vlan_id: The high_vlan_id of this VlanLogicalSingleTaggedRangeConfig.
        :type high_vlan_id: str
        """

        self._high_vlan_id = high_vlan_id

    @property
    def low_vlan_id(self) -> str:
        """Gets the low_vlan_id of this VlanLogicalSingleTaggedRangeConfig.

        The low-value VLAN identifier in a range for single-tagged packets. The range is matched inclusively.  # noqa: E501

        :return: The low_vlan_id of this VlanLogicalSingleTaggedRangeConfig.
        :rtype: str
        """
        return self._low_vlan_id

    @low_vlan_id.setter
    def low_vlan_id(self, low_vlan_id: str):
        """Sets the low_vlan_id of this VlanLogicalSingleTaggedRangeConfig.

        The low-value VLAN identifier in a range for single-tagged packets. The range is matched inclusively.  # noqa: E501

        :param low_vlan_id: The low_vlan_id of this VlanLogicalSingleTaggedRangeConfig.
        :type low_vlan_id: str
        """

        self._low_vlan_id = low_vlan_id
