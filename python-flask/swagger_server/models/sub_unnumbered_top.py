# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SubUnnumberedTop(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, unnumbered: object=None):  # noqa: E501
        """SubUnnumberedTop - a model defined in Swagger

        :param unnumbered: The unnumbered of this SubUnnumberedTop.  # noqa: E501
        :type unnumbered: object
        """
        self.swagger_types = {
            'unnumbered': object
        }

        self.attribute_map = {
            'unnumbered': 'unnumbered'
        }

        self._unnumbered = unnumbered

    @classmethod
    def from_dict(cls, dikt) -> 'SubUnnumberedTop':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SubUnnumberedTop of this SubUnnumberedTop.  # noqa: E501
        :rtype: SubUnnumberedTop
        """
        return util.deserialize_model(dikt, cls)

    @property
    def unnumbered(self) -> object:
        """Gets the unnumbered of this SubUnnumberedTop.

        Top-level container for setting unnumbered interfaces. Includes reference the interface that provides the address information  # noqa: E501

        :return: The unnumbered of this SubUnnumberedTop.
        :rtype: object
        """
        return self._unnumbered

    @unnumbered.setter
    def unnumbered(self, unnumbered: object):
        """Sets the unnumbered of this SubUnnumberedTop.

        Top-level container for setting unnumbered interfaces. Includes reference the interface that provides the address information  # noqa: E501

        :param unnumbered: The unnumbered of this SubUnnumberedTop.
        :type unnumbered: object
        """

        self._unnumbered = unnumbered
