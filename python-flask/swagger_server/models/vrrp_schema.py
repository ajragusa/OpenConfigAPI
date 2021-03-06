# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.ip_vrrp_tracking_top import IpVrrpTrackingTop  # noqa: F401,E501
from swagger_server import util


class VrrpSchema(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, vrrp_group: List[IpVrrpTrackingTop]=None):  # noqa: E501
        """VrrpSchema - a model defined in Swagger

        :param vrrp_group: The vrrp_group of this VrrpSchema.  # noqa: E501
        :type vrrp_group: List[IpVrrpTrackingTop]
        """
        self.swagger_types = {
            'vrrp_group': List[IpVrrpTrackingTop]
        }

        self.attribute_map = {
            'vrrp_group': 'vrrpGroup'
        }

        self._vrrp_group = vrrp_group

    @classmethod
    def from_dict(cls, dikt) -> 'VrrpSchema':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VrrpSchema of this VrrpSchema.  # noqa: E501
        :rtype: VrrpSchema
        """
        return util.deserialize_model(dikt, cls)

    @property
    def vrrp_group(self) -> List[IpVrrpTrackingTop]:
        """Gets the vrrp_group of this VrrpSchema.

        List of VRRP groups, keyed by virtual router id  # noqa: E501

        :return: The vrrp_group of this VrrpSchema.
        :rtype: List[IpVrrpTrackingTop]
        """
        return self._vrrp_group

    @vrrp_group.setter
    def vrrp_group(self, vrrp_group: List[IpVrrpTrackingTop]):
        """Sets the vrrp_group of this VrrpSchema.

        List of VRRP groups, keyed by virtual router id  # noqa: E501

        :param vrrp_group: The vrrp_group of this VrrpSchema.
        :type vrrp_group: List[IpVrrpTrackingTop]
        """

        self._vrrp_group = vrrp_group
