# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IpCommonGlobalConfig(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, dhcp_client: bool=None):  # noqa: E501
        """IpCommonGlobalConfig - a model defined in Swagger

        :param dhcp_client: The dhcp_client of this IpCommonGlobalConfig.  # noqa: E501
        :type dhcp_client: bool
        """
        self.swagger_types = {
            'dhcp_client': bool
        }

        self.attribute_map = {
            'dhcp_client': 'dhcpClient'
        }

        self._dhcp_client = dhcp_client

    @classmethod
    def from_dict(cls, dikt) -> 'IpCommonGlobalConfig':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The IpCommonGlobalConfig of this IpCommonGlobalConfig.  # noqa: E501
        :rtype: IpCommonGlobalConfig
        """
        return util.deserialize_model(dikt, cls)

    @property
    def dhcp_client(self) -> bool:
        """Gets the dhcp_client of this IpCommonGlobalConfig.

        Enables a DHCP client on the interface in order to request an address  # noqa: E501

        :return: The dhcp_client of this IpCommonGlobalConfig.
        :rtype: bool
        """
        return self._dhcp_client

    @dhcp_client.setter
    def dhcp_client(self, dhcp_client: bool):
        """Sets the dhcp_client of this IpCommonGlobalConfig.

        Enables a DHCP client on the interface in order to request an address  # noqa: E501

        :param dhcp_client: The dhcp_client of this IpCommonGlobalConfig.
        :type dhcp_client: bool
        """

        self._dhcp_client = dhcp_client