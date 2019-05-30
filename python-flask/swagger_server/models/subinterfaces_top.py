# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.subinterfaces_top_subinterfaces import SubinterfacesTopSubinterfaces  # noqa: F401,E501
from swagger_server import util


class SubinterfacesTop(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, subinterfaces: SubinterfacesTopSubinterfaces=None):  # noqa: E501
        """SubinterfacesTop - a model defined in Swagger

        :param subinterfaces: The subinterfaces of this SubinterfacesTop.  # noqa: E501
        :type subinterfaces: SubinterfacesTopSubinterfaces
        """
        self.swagger_types = {
            'subinterfaces': SubinterfacesTopSubinterfaces
        }

        self.attribute_map = {
            'subinterfaces': 'subinterfaces'
        }

        self._subinterfaces = subinterfaces

    @classmethod
    def from_dict(cls, dikt) -> 'SubinterfacesTop':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SubinterfacesTop of this SubinterfacesTop.  # noqa: E501
        :rtype: SubinterfacesTop
        """
        return util.deserialize_model(dikt, cls)

    @property
    def subinterfaces(self) -> SubinterfacesTopSubinterfaces:
        """Gets the subinterfaces of this SubinterfacesTop.


        :return: The subinterfaces of this SubinterfacesTop.
        :rtype: SubinterfacesTopSubinterfaces
        """
        return self._subinterfaces

    @subinterfaces.setter
    def subinterfaces(self, subinterfaces: SubinterfacesTopSubinterfaces):
        """Sets the subinterfaces of this SubinterfacesTop.


        :param subinterfaces: The subinterfaces of this SubinterfacesTop.
        :type subinterfaces: SubinterfacesTopSubinterfaces
        """

        self._subinterfaces = subinterfaces
