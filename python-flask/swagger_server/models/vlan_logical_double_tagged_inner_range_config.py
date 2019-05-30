# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class VlanLogicalDoubleTaggedInnerRangeConfig(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, inner_low_vlan_id: str=None, inner_high_vlan_id: str=None, outer_vlan_id: List[str]=None):  # noqa: E501
        """VlanLogicalDoubleTaggedInnerRangeConfig - a model defined in Swagger

        :param inner_low_vlan_id: The inner_low_vlan_id of this VlanLogicalDoubleTaggedInnerRangeConfig.  # noqa: E501
        :type inner_low_vlan_id: str
        :param inner_high_vlan_id: The inner_high_vlan_id of this VlanLogicalDoubleTaggedInnerRangeConfig.  # noqa: E501
        :type inner_high_vlan_id: str
        :param outer_vlan_id: The outer_vlan_id of this VlanLogicalDoubleTaggedInnerRangeConfig.  # noqa: E501
        :type outer_vlan_id: List[str]
        """
        self.swagger_types = {
            'inner_low_vlan_id': str,
            'inner_high_vlan_id': str,
            'outer_vlan_id': List[str]
        }

        self.attribute_map = {
            'inner_low_vlan_id': 'innerLowVlanId',
            'inner_high_vlan_id': 'innerHighVlanId',
            'outer_vlan_id': 'outerVlanId'
        }

        self._inner_low_vlan_id = inner_low_vlan_id
        self._inner_high_vlan_id = inner_high_vlan_id
        self._outer_vlan_id = outer_vlan_id

    @classmethod
    def from_dict(cls, dikt) -> 'VlanLogicalDoubleTaggedInnerRangeConfig':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VlanLogicalDoubleTaggedInnerRangeConfig of this VlanLogicalDoubleTaggedInnerRangeConfig.  # noqa: E501
        :rtype: VlanLogicalDoubleTaggedInnerRangeConfig
        """
        return util.deserialize_model(dikt, cls)

    @property
    def inner_low_vlan_id(self) -> str:
        """Gets the inner_low_vlan_id of this VlanLogicalDoubleTaggedInnerRangeConfig.

        The low-value inner VLAN identifier in a range for double-tagged packets. The range is matched inclusively.  # noqa: E501

        :return: The inner_low_vlan_id of this VlanLogicalDoubleTaggedInnerRangeConfig.
        :rtype: str
        """
        return self._inner_low_vlan_id

    @inner_low_vlan_id.setter
    def inner_low_vlan_id(self, inner_low_vlan_id: str):
        """Sets the inner_low_vlan_id of this VlanLogicalDoubleTaggedInnerRangeConfig.

        The low-value inner VLAN identifier in a range for double-tagged packets. The range is matched inclusively.  # noqa: E501

        :param inner_low_vlan_id: The inner_low_vlan_id of this VlanLogicalDoubleTaggedInnerRangeConfig.
        :type inner_low_vlan_id: str
        """

        self._inner_low_vlan_id = inner_low_vlan_id

    @property
    def inner_high_vlan_id(self) -> str:
        """Gets the inner_high_vlan_id of this VlanLogicalDoubleTaggedInnerRangeConfig.

        The high-value inner VLAN identifier in a range for double-tagged packets. The range is matched inclusively.  # noqa: E501

        :return: The inner_high_vlan_id of this VlanLogicalDoubleTaggedInnerRangeConfig.
        :rtype: str
        """
        return self._inner_high_vlan_id

    @inner_high_vlan_id.setter
    def inner_high_vlan_id(self, inner_high_vlan_id: str):
        """Sets the inner_high_vlan_id of this VlanLogicalDoubleTaggedInnerRangeConfig.

        The high-value inner VLAN identifier in a range for double-tagged packets. The range is matched inclusively.  # noqa: E501

        :param inner_high_vlan_id: The inner_high_vlan_id of this VlanLogicalDoubleTaggedInnerRangeConfig.
        :type inner_high_vlan_id: str
        """

        self._inner_high_vlan_id = inner_high_vlan_id

    @property
    def outer_vlan_id(self) -> List[str]:
        """Gets the outer_vlan_id of this VlanLogicalDoubleTaggedInnerRangeConfig.


        :return: The outer_vlan_id of this VlanLogicalDoubleTaggedInnerRangeConfig.
        :rtype: List[str]
        """
        return self._outer_vlan_id

    @outer_vlan_id.setter
    def outer_vlan_id(self, outer_vlan_id: List[str]):
        """Sets the outer_vlan_id of this VlanLogicalDoubleTaggedInnerRangeConfig.


        :param outer_vlan_id: The outer_vlan_id of this VlanLogicalDoubleTaggedInnerRangeConfig.
        :type outer_vlan_id: List[str]
        """

        self._outer_vlan_id = outer_vlan_id
