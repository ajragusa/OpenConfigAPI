# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InterfacePhysHoldtimeConfig(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, down: str=None, up: str=None):  # noqa: E501
        """InterfacePhysHoldtimeConfig - a model defined in Swagger

        :param down: The down of this InterfacePhysHoldtimeConfig.  # noqa: E501
        :type down: str
        :param up: The up of this InterfacePhysHoldtimeConfig.  # noqa: E501
        :type up: str
        """
        self.swagger_types = {
            'down': str,
            'up': str
        }

        self.attribute_map = {
            'down': 'down',
            'up': 'up'
        }

        self._down = down
        self._up = up

    @classmethod
    def from_dict(cls, dikt) -> 'InterfacePhysHoldtimeConfig':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InterfacePhysHoldtimeConfig of this InterfacePhysHoldtimeConfig.  # noqa: E501
        :rtype: InterfacePhysHoldtimeConfig
        """
        return util.deserialize_model(dikt, cls)

    @property
    def down(self) -> str:
        """Gets the down of this InterfacePhysHoldtimeConfig.

        Dampens advertisement when the interface transitions from up to down.  A zero value means dampening is turned off, i.e., immediate notification.  # noqa: E501

        :return: The down of this InterfacePhysHoldtimeConfig.
        :rtype: str
        """
        return self._down

    @down.setter
    def down(self, down: str):
        """Sets the down of this InterfacePhysHoldtimeConfig.

        Dampens advertisement when the interface transitions from up to down.  A zero value means dampening is turned off, i.e., immediate notification.  # noqa: E501

        :param down: The down of this InterfacePhysHoldtimeConfig.
        :type down: str
        """

        self._down = down

    @property
    def up(self) -> str:
        """Gets the up of this InterfacePhysHoldtimeConfig.

        Dampens advertisement when the interface transitions from down to up.  A zero value means dampening is turned off, i.e., immediate notification.  # noqa: E501

        :return: The up of this InterfacePhysHoldtimeConfig.
        :rtype: str
        """
        return self._up

    @up.setter
    def up(self, up: str):
        """Sets the up of this InterfacePhysHoldtimeConfig.

        Dampens advertisement when the interface transitions from down to up.  A zero value means dampening is turned off, i.e., immediate notification.  # noqa: E501

        :param up: The up of this InterfacePhysHoldtimeConfig.
        :type up: str
        """

        self._up = up
