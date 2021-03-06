# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Ipv6AddressConfig(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, ip: str=None, prefix_length: str=None):  # noqa: E501
        """Ipv6AddressConfig - a model defined in Swagger

        :param ip: The ip of this Ipv6AddressConfig.  # noqa: E501
        :type ip: str
        :param prefix_length: The prefix_length of this Ipv6AddressConfig.  # noqa: E501
        :type prefix_length: str
        """
        self.swagger_types = {
            'ip': str,
            'prefix_length': str
        }

        self.attribute_map = {
            'ip': 'ip',
            'prefix_length': 'prefixLength'
        }

        self._ip = ip
        self._prefix_length = prefix_length

    @classmethod
    def from_dict(cls, dikt) -> 'Ipv6AddressConfig':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Ipv6AddressConfig of this Ipv6AddressConfig.  # noqa: E501
        :rtype: Ipv6AddressConfig
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ip(self) -> str:
        """Gets the ip of this Ipv6AddressConfig.

        The IPv6 address on the interface.  # noqa: E501

        :return: The ip of this Ipv6AddressConfig.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip: str):
        """Sets the ip of this Ipv6AddressConfig.

        The IPv6 address on the interface.  # noqa: E501

        :param ip: The ip of this Ipv6AddressConfig.
        :type ip: str
        """

        self._ip = ip

    @property
    def prefix_length(self) -> str:
        """Gets the prefix_length of this Ipv6AddressConfig.

        The length of the subnet prefix.  # noqa: E501

        :return: The prefix_length of this Ipv6AddressConfig.
        :rtype: str
        """
        return self._prefix_length

    @prefix_length.setter
    def prefix_length(self, prefix_length: str):
        """Sets the prefix_length of this Ipv6AddressConfig.

        The length of the subnet prefix.  # noqa: E501

        :param prefix_length: The prefix_length of this Ipv6AddressConfig.
        :type prefix_length: str
        """

        self._prefix_length = prefix_length
