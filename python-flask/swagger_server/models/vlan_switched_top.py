# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.vlan_switched_top_switched_vlan import VlanSwitchedTopSwitchedVlan  # noqa: F401,E501
from swagger_server import util


class VlanSwitchedTop(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, switched_vlan: VlanSwitchedTopSwitchedVlan=None):  # noqa: E501
        """VlanSwitchedTop - a model defined in Swagger

        :param switched_vlan: The switched_vlan of this VlanSwitchedTop.  # noqa: E501
        :type switched_vlan: VlanSwitchedTopSwitchedVlan
        """
        self.swagger_types = {
            'switched_vlan': VlanSwitchedTopSwitchedVlan
        }

        self.attribute_map = {
            'switched_vlan': 'switchedVlan'
        }

        self._switched_vlan = switched_vlan

    @classmethod
    def from_dict(cls, dikt) -> 'VlanSwitchedTop':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VlanSwitchedTop of this VlanSwitchedTop.  # noqa: E501
        :rtype: VlanSwitchedTop
        """
        return util.deserialize_model(dikt, cls)

    @property
    def switched_vlan(self) -> VlanSwitchedTopSwitchedVlan:
        """Gets the switched_vlan of this VlanSwitchedTop.


        :return: The switched_vlan of this VlanSwitchedTop.
        :rtype: VlanSwitchedTopSwitchedVlan
        """
        return self._switched_vlan

    @switched_vlan.setter
    def switched_vlan(self, switched_vlan: VlanSwitchedTopSwitchedVlan):
        """Sets the switched_vlan of this VlanSwitchedTop.


        :param switched_vlan: The switched_vlan of this VlanSwitchedTop.
        :type switched_vlan: VlanSwitchedTopSwitchedVlan
        """

        self._switched_vlan = switched_vlan
