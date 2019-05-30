# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.base_interface_ref_state_state import BaseInterfaceRefStateState  # noqa: F401,E501
from swagger_server import util


class BaseInterfaceRefState(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, state: BaseInterfaceRefStateState=None):  # noqa: E501
        """BaseInterfaceRefState - a model defined in Swagger

        :param state: The state of this BaseInterfaceRefState.  # noqa: E501
        :type state: BaseInterfaceRefStateState
        """
        self.swagger_types = {
            'state': BaseInterfaceRefStateState
        }

        self.attribute_map = {
            'state': 'state'
        }

        self._state = state

    @classmethod
    def from_dict(cls, dikt) -> 'BaseInterfaceRefState':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BaseInterfaceRefState of this BaseInterfaceRefState.  # noqa: E501
        :rtype: BaseInterfaceRefState
        """
        return util.deserialize_model(dikt, cls)

    @property
    def state(self) -> BaseInterfaceRefStateState:
        """Gets the state of this BaseInterfaceRefState.


        :return: The state of this BaseInterfaceRefState.
        :rtype: BaseInterfaceRefStateState
        """
        return self._state

    @state.setter
    def state(self, state: BaseInterfaceRefStateState):
        """Sets the state of this BaseInterfaceRefState.


        :param state: The state of this BaseInterfaceRefState.
        :type state: BaseInterfaceRefStateState
        """

        self._state = state
