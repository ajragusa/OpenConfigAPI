# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.vlan_top_vlans import VlanTopVlans  # noqa: F401,E501
from swagger_server import util


class VlanTop(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, vlans: VlanTopVlans=None):  # noqa: E501
        """VlanTop - a model defined in Swagger

        :param vlans: The vlans of this VlanTop.  # noqa: E501
        :type vlans: VlanTopVlans
        """
        self.swagger_types = {
            'vlans': VlanTopVlans
        }

        self.attribute_map = {
            'vlans': 'vlans'
        }

        self._vlans = vlans

    @classmethod
    def from_dict(cls, dikt) -> 'VlanTop':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VlanTop of this VlanTop.  # noqa: E501
        :rtype: VlanTop
        """
        return util.deserialize_model(dikt, cls)

    @property
    def vlans(self) -> VlanTopVlans:
        """Gets the vlans of this VlanTop.


        :return: The vlans of this VlanTop.
        :rtype: VlanTopVlans
        """
        return self._vlans

    @vlans.setter
    def vlans(self, vlans: VlanTopVlans):
        """Sets the vlans of this VlanTop.


        :param vlans: The vlans of this VlanTop.
        :type vlans: VlanTopVlans
        """

        self._vlans = vlans
