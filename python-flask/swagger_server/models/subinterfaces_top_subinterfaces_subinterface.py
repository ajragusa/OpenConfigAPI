# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.subinterfaces_config import SubinterfacesConfig  # noqa: F401,E501
from swagger_server.models.subinterfaces_state import SubinterfacesState  # noqa: F401,E501
from swagger_server import util


class SubinterfacesTopSubinterfacesSubinterface(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, index: str=None, state: SubinterfacesState=None, config: SubinterfacesConfig=None):  # noqa: E501
        """SubinterfacesTopSubinterfacesSubinterface - a model defined in Swagger

        :param index: The index of this SubinterfacesTopSubinterfacesSubinterface.  # noqa: E501
        :type index: str
        :param state: The state of this SubinterfacesTopSubinterfacesSubinterface.  # noqa: E501
        :type state: SubinterfacesState
        :param config: The config of this SubinterfacesTopSubinterfacesSubinterface.  # noqa: E501
        :type config: SubinterfacesConfig
        """
        self.swagger_types = {
            'index': str,
            'state': SubinterfacesState,
            'config': SubinterfacesConfig
        }

        self.attribute_map = {
            'index': 'index',
            'state': 'state',
            'config': 'config'
        }

        self._index = index
        self._state = state
        self._config = config

    @classmethod
    def from_dict(cls, dikt) -> 'SubinterfacesTopSubinterfacesSubinterface':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SubinterfacesTop_subinterfaces_subinterface of this SubinterfacesTopSubinterfacesSubinterface.  # noqa: E501
        :rtype: SubinterfacesTopSubinterfacesSubinterface
        """
        return util.deserialize_model(dikt, cls)

    @property
    def index(self) -> str:
        """Gets the index of this SubinterfacesTopSubinterfacesSubinterface.

        The index number of the subinterface -- used to address the logical interface  # noqa: E501

        :return: The index of this SubinterfacesTopSubinterfacesSubinterface.
        :rtype: str
        """
        return self._index

    @index.setter
    def index(self, index: str):
        """Sets the index of this SubinterfacesTopSubinterfacesSubinterface.

        The index number of the subinterface -- used to address the logical interface  # noqa: E501

        :param index: The index of this SubinterfacesTopSubinterfacesSubinterface.
        :type index: str
        """

        self._index = index

    @property
    def state(self) -> SubinterfacesState:
        """Gets the state of this SubinterfacesTopSubinterfacesSubinterface.

        Operational state data for logical interfaces  # noqa: E501

        :return: The state of this SubinterfacesTopSubinterfacesSubinterface.
        :rtype: SubinterfacesState
        """
        return self._state

    @state.setter
    def state(self, state: SubinterfacesState):
        """Sets the state of this SubinterfacesTopSubinterfacesSubinterface.

        Operational state data for logical interfaces  # noqa: E501

        :param state: The state of this SubinterfacesTopSubinterfacesSubinterface.
        :type state: SubinterfacesState
        """

        self._state = state

    @property
    def config(self) -> SubinterfacesConfig:
        """Gets the config of this SubinterfacesTopSubinterfacesSubinterface.

        Configurable items at the subinterface level  # noqa: E501

        :return: The config of this SubinterfacesTopSubinterfacesSubinterface.
        :rtype: SubinterfacesConfig
        """
        return self._config

    @config.setter
    def config(self, config: SubinterfacesConfig):
        """Sets the config of this SubinterfacesTopSubinterfacesSubinterface.

        Configurable items at the subinterface level  # noqa: E501

        :param config: The config of this SubinterfacesTopSubinterfacesSubinterface.
        :type config: SubinterfacesConfig
        """

        self._config = config
