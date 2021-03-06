# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.interface_phys_holdtime_config import InterfacePhysHoldtimeConfig  # noqa: F401,E501
from swagger_server.models.interface_phys_holdtime_state import InterfacePhysHoldtimeState  # noqa: F401,E501
from swagger_server import util


class InterfacePhysHoldtimeTopHoldTime(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, state: InterfacePhysHoldtimeState=None, config: InterfacePhysHoldtimeConfig=None):  # noqa: E501
        """InterfacePhysHoldtimeTopHoldTime - a model defined in Swagger

        :param state: The state of this InterfacePhysHoldtimeTopHoldTime.  # noqa: E501
        :type state: InterfacePhysHoldtimeState
        :param config: The config of this InterfacePhysHoldtimeTopHoldTime.  # noqa: E501
        :type config: InterfacePhysHoldtimeConfig
        """
        self.swagger_types = {
            'state': InterfacePhysHoldtimeState,
            'config': InterfacePhysHoldtimeConfig
        }

        self.attribute_map = {
            'state': 'state',
            'config': 'config'
        }

        self._state = state
        self._config = config

    @classmethod
    def from_dict(cls, dikt) -> 'InterfacePhysHoldtimeTopHoldTime':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InterfacePhysHoldtimeTop_holdTime of this InterfacePhysHoldtimeTopHoldTime.  # noqa: E501
        :rtype: InterfacePhysHoldtimeTopHoldTime
        """
        return util.deserialize_model(dikt, cls)

    @property
    def state(self) -> InterfacePhysHoldtimeState:
        """Gets the state of this InterfacePhysHoldtimeTopHoldTime.

        Operational state data for interface hold-time.  # noqa: E501

        :return: The state of this InterfacePhysHoldtimeTopHoldTime.
        :rtype: InterfacePhysHoldtimeState
        """
        return self._state

    @state.setter
    def state(self, state: InterfacePhysHoldtimeState):
        """Sets the state of this InterfacePhysHoldtimeTopHoldTime.

        Operational state data for interface hold-time.  # noqa: E501

        :param state: The state of this InterfacePhysHoldtimeTopHoldTime.
        :type state: InterfacePhysHoldtimeState
        """

        self._state = state

    @property
    def config(self) -> InterfacePhysHoldtimeConfig:
        """Gets the config of this InterfacePhysHoldtimeTopHoldTime.

        Configuration data for interface hold-time settings.  # noqa: E501

        :return: The config of this InterfacePhysHoldtimeTopHoldTime.
        :rtype: InterfacePhysHoldtimeConfig
        """
        return self._config

    @config.setter
    def config(self, config: InterfacePhysHoldtimeConfig):
        """Sets the config of this InterfacePhysHoldtimeTopHoldTime.

        Configuration data for interface hold-time settings.  # noqa: E501

        :param config: The config of this InterfacePhysHoldtimeTopHoldTime.
        :type config: InterfacePhysHoldtimeConfig
        """

        self._config = config
