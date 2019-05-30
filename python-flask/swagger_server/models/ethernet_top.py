# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.ethernet_top_ethernet import EthernetTopEthernet  # noqa: F401,E501
from swagger_server import util


class EthernetTop(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, ethernet: EthernetTopEthernet=None):  # noqa: E501
        """EthernetTop - a model defined in Swagger

        :param ethernet: The ethernet of this EthernetTop.  # noqa: E501
        :type ethernet: EthernetTopEthernet
        """
        self.swagger_types = {
            'ethernet': EthernetTopEthernet
        }

        self.attribute_map = {
            'ethernet': 'ethernet'
        }

        self._ethernet = ethernet

    @classmethod
    def from_dict(cls, dikt) -> 'EthernetTop':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EthernetTop of this EthernetTop.  # noqa: E501
        :rtype: EthernetTop
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ethernet(self) -> EthernetTopEthernet:
        """Gets the ethernet of this EthernetTop.


        :return: The ethernet of this EthernetTop.
        :rtype: EthernetTopEthernet
        """
        return self._ethernet

    @ethernet.setter
    def ethernet(self, ethernet: EthernetTopEthernet):
        """Sets the ethernet of this EthernetTop.


        :param ethernet: The ethernet of this EthernetTop.
        :type ethernet: EthernetTopEthernet
        """

        self._ethernet = ethernet
