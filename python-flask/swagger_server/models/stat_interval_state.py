# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class StatIntervalState(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, interval: str=None):  # noqa: E501
        """StatIntervalState - a model defined in Swagger

        :param interval: The interval of this StatIntervalState.  # noqa: E501
        :type interval: str
        """
        self.swagger_types = {
            'interval': str
        }

        self.attribute_map = {
            'interval': 'interval'
        }

        self._interval = interval

    @classmethod
    def from_dict(cls, dikt) -> 'StatIntervalState':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The StatIntervalState of this StatIntervalState.  # noqa: E501
        :rtype: StatIntervalState
        """
        return util.deserialize_model(dikt, cls)

    @property
    def interval(self) -> str:
        """Gets the interval of this StatIntervalState.

        If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system.  # noqa: E501

        :return: The interval of this StatIntervalState.
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval: str):
        """Sets the interval of this StatIntervalState.

        If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system.  # noqa: E501

        :param interval: The interval of this StatIntervalState.
        :type interval: str
        """

        self._interval = interval
