# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class VlanLogicalConfig(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, vlan_id: str=None):  # noqa: E501
        """VlanLogicalConfig - a model defined in Swagger

        :param vlan_id: The vlan_id of this VlanLogicalConfig.  # noqa: E501
        :type vlan_id: str
        """
        self.swagger_types = {
            'vlan_id': str
        }

        self.attribute_map = {
            'vlan_id': 'vlanId'
        }

        self._vlan_id = vlan_id

    @classmethod
    def from_dict(cls, dikt) -> 'VlanLogicalConfig':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VlanLogicalConfig of this VlanLogicalConfig.  # noqa: E501
        :rtype: VlanLogicalConfig
        """
        return util.deserialize_model(dikt, cls)

    @property
    def vlan_id(self) -> str:
        """Gets the vlan_id of this VlanLogicalConfig.

        VLAN id for the subinterface -- specified inline for the case of a local VLAN.  The id is scoped to the subinterface, and could be repeated on different subinterfaces. Deprecation note: See adjacent elements in the 'vlan' container for making more expressive VLAN matches.  # noqa: E501

        :return: The vlan_id of this VlanLogicalConfig.
        :rtype: str
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id: str):
        """Sets the vlan_id of this VlanLogicalConfig.

        VLAN id for the subinterface -- specified inline for the case of a local VLAN.  The id is scoped to the subinterface, and could be repeated on different subinterfaces. Deprecation note: See adjacent elements in the 'vlan' container for making more expressive VLAN matches.  # noqa: E501

        :param vlan_id: The vlan_id of this VlanLogicalConfig.
        :type vlan_id: str
        """

        self._vlan_id = vlan_id