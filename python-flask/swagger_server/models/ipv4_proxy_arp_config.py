# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Ipv4ProxyArpConfig(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, mode: str=None):  # noqa: E501
        """Ipv4ProxyArpConfig - a model defined in Swagger

        :param mode: The mode of this Ipv4ProxyArpConfig.  # noqa: E501
        :type mode: str
        """
        self.swagger_types = {
            'mode': str
        }

        self.attribute_map = {
            'mode': 'mode'
        }

        self._mode = mode

    @classmethod
    def from_dict(cls, dikt) -> 'Ipv4ProxyArpConfig':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Ipv4ProxyArpConfig of this Ipv4ProxyArpConfig.  # noqa: E501
        :rtype: Ipv4ProxyArpConfig
        """
        return util.deserialize_model(dikt, cls)

    @property
    def mode(self) -> str:
        """Gets the mode of this Ipv4ProxyArpConfig.

        When set to a value other than DISABLE, the local system should respond to ARP requests that are for target addresses other than those that are configured on the local subinterface using its own MAC address as the target hardware address. If the REMOTE_ONLY value is specified, replies are only sent when the target address falls outside the locally configured subnets on the interface, whereas with the ALL value, all requests, regardless of their target address are replied to.  # noqa: E501

        :return: The mode of this Ipv4ProxyArpConfig.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode: str):
        """Sets the mode of this Ipv4ProxyArpConfig.

        When set to a value other than DISABLE, the local system should respond to ARP requests that are for target addresses other than those that are configured on the local subinterface using its own MAC address as the target hardware address. If the REMOTE_ONLY value is specified, replies are only sent when the target address falls outside the locally configured subnets on the interface, whereas with the ALL value, all requests, regardless of their target address are replied to.  # noqa: E501

        :param mode: The mode of this Ipv4ProxyArpConfig.
        :type mode: str
        """
        allowed_values = ["DISABLE", "REMOTE_ONLY", "ALL"]  # noqa: E501
        if mode not in allowed_values:
            raise ValueError(
                "Invalid value for `mode` ({0}), must be one of {1}"
                .format(mode, allowed_values)
            )

        self._mode = mode
