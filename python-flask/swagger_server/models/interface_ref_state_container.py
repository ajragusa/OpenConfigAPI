# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.interface_ref_common import InterfaceRefCommon  # noqa: F401,E501
from swagger_server import util


class InterfaceRefStateContainer(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, state: InterfaceRefCommon=None):  # noqa: E501
        """InterfaceRefStateContainer - a model defined in Swagger

        :param state: The state of this InterfaceRefStateContainer.  # noqa: E501
        :type state: InterfaceRefCommon
        """
        self.swagger_types = {
            'state': InterfaceRefCommon
        }

        self.attribute_map = {
            'state': 'state'
        }

        self._state = state

    @classmethod
    def from_dict(cls, dikt) -> 'InterfaceRefStateContainer':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InterfaceRefStateContainer of this InterfaceRefStateContainer.  # noqa: E501
        :rtype: InterfaceRefStateContainer
        """
        return util.deserialize_model(dikt, cls)

    @property
    def state(self) -> InterfaceRefCommon:
        """Gets the state of this InterfaceRefStateContainer.

        Operational state for interface-ref  # noqa: E501

        :return: The state of this InterfaceRefStateContainer.
        :rtype: InterfaceRefCommon
        """
        return self._state

    @state.setter
    def state(self, state: InterfaceRefCommon):
        """Sets the state of this InterfaceRefStateContainer.

        Operational state for interface-ref  # noqa: E501

        :param state: The state of this InterfaceRefStateContainer.
        :type state: InterfaceRefCommon
        """

        self._state = state
