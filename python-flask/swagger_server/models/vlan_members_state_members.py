# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.base_interface_ref_state import BaseInterfaceRefState  # noqa: F401,E501
from swagger_server import util


class VlanMembersStateMembers(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, member: List[BaseInterfaceRefState]=None):  # noqa: E501
        """VlanMembersStateMembers - a model defined in Swagger

        :param member: The member of this VlanMembersStateMembers.  # noqa: E501
        :type member: List[BaseInterfaceRefState]
        """
        self.swagger_types = {
            'member': List[BaseInterfaceRefState]
        }

        self.attribute_map = {
            'member': 'member'
        }

        self._member = member

    @classmethod
    def from_dict(cls, dikt) -> 'VlanMembersStateMembers':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VlanMembersState_members of this VlanMembersStateMembers.  # noqa: E501
        :rtype: VlanMembersStateMembers
        """
        return util.deserialize_model(dikt, cls)

    @property
    def member(self) -> List[BaseInterfaceRefState]:
        """Gets the member of this VlanMembersStateMembers.

        List of references to interfaces / subinterfaces associated with the VLAN.  # noqa: E501

        :return: The member of this VlanMembersStateMembers.
        :rtype: List[BaseInterfaceRefState]
        """
        return self._member

    @member.setter
    def member(self, member: List[BaseInterfaceRefState]):
        """Sets the member of this VlanMembersStateMembers.

        List of references to interfaces / subinterfaces associated with the VLAN.  # noqa: E501

        :param member: The member of this VlanMembersStateMembers.
        :type member: List[BaseInterfaceRefState]
        """

        self._member = member