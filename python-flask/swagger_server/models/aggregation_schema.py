# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.aggregation_logical_config import AggregationLogicalConfig  # noqa: F401,E501
from swagger_server.models.aggregation_logical_state import AggregationLogicalState  # noqa: F401,E501
from swagger_server.models.vlan_switched_top_switched_vlan import VlanSwitchedTopSwitchedVlan  # noqa: F401,E501
from swagger_server import util


class AggregationSchema(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, switched_vlan: VlanSwitchedTopSwitchedVlan=None, state: AggregationLogicalState=None, config: AggregationLogicalConfig=None):  # noqa: E501
        """AggregationSchema - a model defined in Swagger

        :param switched_vlan: The switched_vlan of this AggregationSchema.  # noqa: E501
        :type switched_vlan: VlanSwitchedTopSwitchedVlan
        :param state: The state of this AggregationSchema.  # noqa: E501
        :type state: AggregationLogicalState
        :param config: The config of this AggregationSchema.  # noqa: E501
        :type config: AggregationLogicalConfig
        """
        self.swagger_types = {
            'switched_vlan': VlanSwitchedTopSwitchedVlan,
            'state': AggregationLogicalState,
            'config': AggregationLogicalConfig
        }

        self.attribute_map = {
            'switched_vlan': 'switchedVlan',
            'state': 'state',
            'config': 'config'
        }

        self._switched_vlan = switched_vlan
        self._state = state
        self._config = config

    @classmethod
    def from_dict(cls, dikt) -> 'AggregationSchema':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AggregationSchema of this AggregationSchema.  # noqa: E501
        :rtype: AggregationSchema
        """
        return util.deserialize_model(dikt, cls)

    @property
    def switched_vlan(self) -> VlanSwitchedTopSwitchedVlan:
        """Gets the switched_vlan of this AggregationSchema.


        :return: The switched_vlan of this AggregationSchema.
        :rtype: VlanSwitchedTopSwitchedVlan
        """
        return self._switched_vlan

    @switched_vlan.setter
    def switched_vlan(self, switched_vlan: VlanSwitchedTopSwitchedVlan):
        """Sets the switched_vlan of this AggregationSchema.


        :param switched_vlan: The switched_vlan of this AggregationSchema.
        :type switched_vlan: VlanSwitchedTopSwitchedVlan
        """

        self._switched_vlan = switched_vlan

    @property
    def state(self) -> AggregationLogicalState:
        """Gets the state of this AggregationSchema.

        Operational state variables for logical aggregate / LAG interfaces  # noqa: E501

        :return: The state of this AggregationSchema.
        :rtype: AggregationLogicalState
        """
        return self._state

    @state.setter
    def state(self, state: AggregationLogicalState):
        """Sets the state of this AggregationSchema.

        Operational state variables for logical aggregate / LAG interfaces  # noqa: E501

        :param state: The state of this AggregationSchema.
        :type state: AggregationLogicalState
        """

        self._state = state

    @property
    def config(self) -> AggregationLogicalConfig:
        """Gets the config of this AggregationSchema.

        Configuration variables for logical aggregate / LAG interfaces  # noqa: E501

        :return: The config of this AggregationSchema.
        :rtype: AggregationLogicalConfig
        """
        return self._config

    @config.setter
    def config(self, config: AggregationLogicalConfig):
        """Sets the config of this AggregationSchema.

        Configuration variables for logical aggregate / LAG interfaces  # noqa: E501

        :param config: The config of this AggregationSchema.
        :type config: AggregationLogicalConfig
        """

        self._config = config