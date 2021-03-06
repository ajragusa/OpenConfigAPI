# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.interface_counters_state_counters import InterfaceCountersStateCounters  # noqa: F401,E501
from swagger_server import util


class InterfaceCountersState(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, counters: InterfaceCountersStateCounters=None):  # noqa: E501
        """InterfaceCountersState - a model defined in Swagger

        :param counters: The counters of this InterfaceCountersState.  # noqa: E501
        :type counters: InterfaceCountersStateCounters
        """
        self.swagger_types = {
            'counters': InterfaceCountersStateCounters
        }

        self.attribute_map = {
            'counters': 'counters'
        }

        self._counters = counters

    @classmethod
    def from_dict(cls, dikt) -> 'InterfaceCountersState':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InterfaceCountersState of this InterfaceCountersState.  # noqa: E501
        :rtype: InterfaceCountersState
        """
        return util.deserialize_model(dikt, cls)

    @property
    def counters(self) -> InterfaceCountersStateCounters:
        """Gets the counters of this InterfaceCountersState.


        :return: The counters of this InterfaceCountersState.
        :rtype: InterfaceCountersStateCounters
        """
        return self._counters

    @counters.setter
    def counters(self, counters: InterfaceCountersStateCounters):
        """Sets the counters of this InterfaceCountersState.


        :param counters: The counters of this InterfaceCountersState.
        :type counters: InterfaceCountersStateCounters
        """

        self._counters = counters
