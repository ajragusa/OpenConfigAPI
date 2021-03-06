# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class VlanLogicalDoubleTaggedConfig(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, inner_vlan_id: str=None, outer_vlan_id: str=None):  # noqa: E501
        """VlanLogicalDoubleTaggedConfig - a model defined in Swagger

        :param inner_vlan_id: The inner_vlan_id of this VlanLogicalDoubleTaggedConfig.  # noqa: E501
        :type inner_vlan_id: str
        :param outer_vlan_id: The outer_vlan_id of this VlanLogicalDoubleTaggedConfig.  # noqa: E501
        :type outer_vlan_id: str
        """
        self.swagger_types = {
            'inner_vlan_id': str,
            'outer_vlan_id': str
        }

        self.attribute_map = {
            'inner_vlan_id': 'innerVlanId',
            'outer_vlan_id': 'outerVlanId'
        }

        self._inner_vlan_id = inner_vlan_id
        self._outer_vlan_id = outer_vlan_id

    @classmethod
    def from_dict(cls, dikt) -> 'VlanLogicalDoubleTaggedConfig':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VlanLogicalDoubleTaggedConfig of this VlanLogicalDoubleTaggedConfig.  # noqa: E501
        :rtype: VlanLogicalDoubleTaggedConfig
        """
        return util.deserialize_model(dikt, cls)

    @property
    def inner_vlan_id(self) -> str:
        """Gets the inner_vlan_id of this VlanLogicalDoubleTaggedConfig.

        Inner VLAN identifier for double-tagged packets.  # noqa: E501

        :return: The inner_vlan_id of this VlanLogicalDoubleTaggedConfig.
        :rtype: str
        """
        return self._inner_vlan_id

    @inner_vlan_id.setter
    def inner_vlan_id(self, inner_vlan_id: str):
        """Sets the inner_vlan_id of this VlanLogicalDoubleTaggedConfig.

        Inner VLAN identifier for double-tagged packets.  # noqa: E501

        :param inner_vlan_id: The inner_vlan_id of this VlanLogicalDoubleTaggedConfig.
        :type inner_vlan_id: str
        """

        self._inner_vlan_id = inner_vlan_id

    @property
    def outer_vlan_id(self) -> str:
        """Gets the outer_vlan_id of this VlanLogicalDoubleTaggedConfig.

        Outer VLAN identifier for double-tagged packets.  # noqa: E501

        :return: The outer_vlan_id of this VlanLogicalDoubleTaggedConfig.
        :rtype: str
        """
        return self._outer_vlan_id

    @outer_vlan_id.setter
    def outer_vlan_id(self, outer_vlan_id: str):
        """Sets the outer_vlan_id of this VlanLogicalDoubleTaggedConfig.

        Outer VLAN identifier for double-tagged packets.  # noqa: E501

        :param outer_vlan_id: The outer_vlan_id of this VlanLogicalDoubleTaggedConfig.
        :type outer_vlan_id: str
        """

        self._outer_vlan_id = outer_vlan_id
