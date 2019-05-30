# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class MinMaxTime(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, min_time: str=None, max_time: str=None):  # noqa: E501
        """MinMaxTime - a model defined in Swagger

        :param min_time: The min_time of this MinMaxTime.  # noqa: E501
        :type min_time: str
        :param max_time: The max_time of this MinMaxTime.  # noqa: E501
        :type max_time: str
        """
        self.swagger_types = {
            'min_time': str,
            'max_time': str
        }

        self.attribute_map = {
            'min_time': 'minTime',
            'max_time': 'maxTime'
        }

        self._min_time = min_time
        self._max_time = max_time

    @classmethod
    def from_dict(cls, dikt) -> 'MinMaxTime':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MinMaxTime of this MinMaxTime.  # noqa: E501
        :rtype: MinMaxTime
        """
        return util.deserialize_model(dikt, cls)

    @property
    def min_time(self) -> str:
        """Gets the min_time of this MinMaxTime.

        The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00:00:00 UTC).  # noqa: E501

        :return: The min_time of this MinMaxTime.
        :rtype: str
        """
        return self._min_time

    @min_time.setter
    def min_time(self, min_time: str):
        """Sets the min_time of this MinMaxTime.

        The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00:00:00 UTC).  # noqa: E501

        :param min_time: The min_time of this MinMaxTime.
        :type min_time: str
        """

        self._min_time = min_time

    @property
    def max_time(self) -> str:
        """Gets the max_time of this MinMaxTime.

        The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00:00:00 UTC).  # noqa: E501

        :return: The max_time of this MinMaxTime.
        :rtype: str
        """
        return self._max_time

    @max_time.setter
    def max_time(self, max_time: str):
        """Sets the max_time of this MinMaxTime.

        The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00:00:00 UTC).  # noqa: E501

        :param max_time: The max_time of this MinMaxTime.
        :type max_time: str
        """

        self._max_time = max_time