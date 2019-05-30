# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.vlan_members_state_members import VlanMembersStateMembers  # noqa: F401,E501
from swagger_server import util


class VlanMembersState(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, members: VlanMembersStateMembers=None):  # noqa: E501
        """VlanMembersState - a model defined in Swagger

        :param members: The members of this VlanMembersState.  # noqa: E501
        :type members: VlanMembersStateMembers
        """
        self.swagger_types = {
            'members': VlanMembersStateMembers
        }

        self.attribute_map = {
            'members': 'members'
        }

        self._members = members

    @classmethod
    def from_dict(cls, dikt) -> 'VlanMembersState':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VlanMembersState of this VlanMembersState.  # noqa: E501
        :rtype: VlanMembersState
        """
        return util.deserialize_model(dikt, cls)

    @property
    def members(self) -> VlanMembersStateMembers:
        """Gets the members of this VlanMembersState.


        :return: The members of this VlanMembersState.
        :rtype: VlanMembersStateMembers
        """
        return self._members

    @members.setter
    def members(self, members: VlanMembersStateMembers):
        """Sets the members of this VlanMembersState.


        :param members: The members of this VlanMembersState.
        :type members: VlanMembersStateMembers
        """

        self._members = members
