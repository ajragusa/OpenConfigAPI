# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class VlanLogicalEgressMappingConfig(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, vlan_stack_action: str=None, vlan_id: str=None, tpid: str=None):  # noqa: E501
        """VlanLogicalEgressMappingConfig - a model defined in Swagger

        :param vlan_stack_action: The vlan_stack_action of this VlanLogicalEgressMappingConfig.  # noqa: E501
        :type vlan_stack_action: str
        :param vlan_id: The vlan_id of this VlanLogicalEgressMappingConfig.  # noqa: E501
        :type vlan_id: str
        :param tpid: The tpid of this VlanLogicalEgressMappingConfig.  # noqa: E501
        :type tpid: str
        """
        self.swagger_types = {
            'vlan_stack_action': str,
            'vlan_id': str,
            'tpid': str
        }

        self.attribute_map = {
            'vlan_stack_action': 'vlanStackAction',
            'vlan_id': 'vlanId',
            'tpid': 'tpid'
        }

        self._vlan_stack_action = vlan_stack_action
        self._vlan_id = vlan_id
        self._tpid = tpid

    @classmethod
    def from_dict(cls, dikt) -> 'VlanLogicalEgressMappingConfig':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VlanLogicalEgressMappingConfig of this VlanLogicalEgressMappingConfig.  # noqa: E501
        :rtype: VlanLogicalEgressMappingConfig
        """
        return util.deserialize_model(dikt, cls)

    @property
    def vlan_stack_action(self) -> str:
        """Gets the vlan_stack_action of this VlanLogicalEgressMappingConfig.

        The action to take on the VLAN stack of a packet. This is optionally used in conjunction with adjacent leaves to override the values of the action.  # noqa: E501

        :return: The vlan_stack_action of this VlanLogicalEgressMappingConfig.
        :rtype: str
        """
        return self._vlan_stack_action

    @vlan_stack_action.setter
    def vlan_stack_action(self, vlan_stack_action: str):
        """Sets the vlan_stack_action of this VlanLogicalEgressMappingConfig.

        The action to take on the VLAN stack of a packet. This is optionally used in conjunction with adjacent leaves to override the values of the action.  # noqa: E501

        :param vlan_stack_action: The vlan_stack_action of this VlanLogicalEgressMappingConfig.
        :type vlan_stack_action: str
        """

        self._vlan_stack_action = vlan_stack_action

    @property
    def vlan_id(self) -> str:
        """Gets the vlan_id of this VlanLogicalEgressMappingConfig.

        Optionally specifies a fixed VLAN identifier that is used by the action configured in 'vlan-stack-action'. For example, if the action is 'POP' then a VLAN identifier is removed from the stack but the value of this leaf is used instead. This value must be non-zero if the 'vlan-stack-action' is one of 'PUSH' or 'SWAP'.  # noqa: E501

        :return: The vlan_id of this VlanLogicalEgressMappingConfig.
        :rtype: str
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id: str):
        """Sets the vlan_id of this VlanLogicalEgressMappingConfig.

        Optionally specifies a fixed VLAN identifier that is used by the action configured in 'vlan-stack-action'. For example, if the action is 'POP' then a VLAN identifier is removed from the stack but the value of this leaf is used instead. This value must be non-zero if the 'vlan-stack-action' is one of 'PUSH' or 'SWAP'.  # noqa: E501

        :param vlan_id: The vlan_id of this VlanLogicalEgressMappingConfig.
        :type vlan_id: str
        """

        self._vlan_id = vlan_id

    @property
    def tpid(self) -> str:
        """Gets the tpid of this VlanLogicalEgressMappingConfig.

        Optionally override the tag protocol identifier field (TPID) that is used by the action configured by 'vlan-stack-action' when modifying the VLAN stack.  # noqa: E501

        :return: The tpid of this VlanLogicalEgressMappingConfig.
        :rtype: str
        """
        return self._tpid

    @tpid.setter
    def tpid(self, tpid: str):
        """Sets the tpid of this VlanLogicalEgressMappingConfig.

        Optionally override the tag protocol identifier field (TPID) that is used by the action configured by 'vlan-stack-action' when modifying the VLAN stack.  # noqa: E501

        :param tpid: The tpid of this VlanLogicalEgressMappingConfig.
        :type tpid: str
        """

        self._tpid = tpid
