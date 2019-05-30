# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.min_max_time import MinMaxTime  # noqa: F401,E501
from swagger_server import util


class AvgMinMaxStatsPrecision1(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, min_time: str=None, max_time: str=None, max: float=None, avg: float=None, min: float=None):  # noqa: E501
        """AvgMinMaxStatsPrecision1 - a model defined in Swagger

        :param min_time: The min_time of this AvgMinMaxStatsPrecision1.  # noqa: E501
        :type min_time: str
        :param max_time: The max_time of this AvgMinMaxStatsPrecision1.  # noqa: E501
        :type max_time: str
        :param max: The max of this AvgMinMaxStatsPrecision1.  # noqa: E501
        :type max: float
        :param avg: The avg of this AvgMinMaxStatsPrecision1.  # noqa: E501
        :type avg: float
        :param min: The min of this AvgMinMaxStatsPrecision1.  # noqa: E501
        :type min: float
        """
        self.swagger_types = {
            'min_time': str,
            'max_time': str,
            'max': float,
            'avg': float,
            'min': float
        }

        self.attribute_map = {
            'min_time': 'minTime',
            'max_time': 'maxTime',
            'max': 'max',
            'avg': 'avg',
            'min': 'min'
        }

        self._min_time = min_time
        self._max_time = max_time
        self._max = max
        self._avg = avg
        self._min = min

    @classmethod
    def from_dict(cls, dikt) -> 'AvgMinMaxStatsPrecision1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AvgMinMaxStatsPrecision1 of this AvgMinMaxStatsPrecision1.  # noqa: E501
        :rtype: AvgMinMaxStatsPrecision1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def min_time(self) -> str:
        """Gets the min_time of this AvgMinMaxStatsPrecision1.

        The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00:00:00 UTC).  # noqa: E501

        :return: The min_time of this AvgMinMaxStatsPrecision1.
        :rtype: str
        """
        return self._min_time

    @min_time.setter
    def min_time(self, min_time: str):
        """Sets the min_time of this AvgMinMaxStatsPrecision1.

        The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00:00:00 UTC).  # noqa: E501

        :param min_time: The min_time of this AvgMinMaxStatsPrecision1.
        :type min_time: str
        """

        self._min_time = min_time

    @property
    def max_time(self) -> str:
        """Gets the max_time of this AvgMinMaxStatsPrecision1.

        The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00:00:00 UTC).  # noqa: E501

        :return: The max_time of this AvgMinMaxStatsPrecision1.
        :rtype: str
        """
        return self._max_time

    @max_time.setter
    def max_time(self, max_time: str):
        """Sets the max_time of this AvgMinMaxStatsPrecision1.

        The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00:00:00 UTC).  # noqa: E501

        :param max_time: The max_time of this AvgMinMaxStatsPrecision1.
        :type max_time: str
        """

        self._max_time = max_time

    @property
    def max(self) -> float:
        """Gets the max of this AvgMinMaxStatsPrecision1.

        The maximum value of the statitic over the time interval.  # noqa: E501

        :return: The max of this AvgMinMaxStatsPrecision1.
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max: float):
        """Sets the max of this AvgMinMaxStatsPrecision1.

        The maximum value of the statitic over the time interval.  # noqa: E501

        :param max: The max of this AvgMinMaxStatsPrecision1.
        :type max: float
        """

        self._max = max

    @property
    def avg(self) -> float:
        """Gets the avg of this AvgMinMaxStatsPrecision1.

        The arithmetic mean value of the statistic over the time interval.  # noqa: E501

        :return: The avg of this AvgMinMaxStatsPrecision1.
        :rtype: float
        """
        return self._avg

    @avg.setter
    def avg(self, avg: float):
        """Sets the avg of this AvgMinMaxStatsPrecision1.

        The arithmetic mean value of the statistic over the time interval.  # noqa: E501

        :param avg: The avg of this AvgMinMaxStatsPrecision1.
        :type avg: float
        """

        self._avg = avg

    @property
    def min(self) -> float:
        """Gets the min of this AvgMinMaxStatsPrecision1.

        The minimum value of the statistic over the time interval.  # noqa: E501

        :return: The min of this AvgMinMaxStatsPrecision1.
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min: float):
        """Sets the min of this AvgMinMaxStatsPrecision1.

        The minimum value of the statistic over the time interval.  # noqa: E501

        :param min: The min of this AvgMinMaxStatsPrecision1.
        :type min: float
        """

        self._min = min
