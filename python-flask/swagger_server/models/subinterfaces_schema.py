# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.subinterfaces_schema_subinterface import SubinterfacesSchemaSubinterface  # noqa: F401,E501
from swagger_server import util


class SubinterfacesSchema(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, subinterface: List[SubinterfacesSchemaSubinterface]=None):  # noqa: E501
        """SubinterfacesSchema - a model defined in Swagger

        :param subinterface: The subinterface of this SubinterfacesSchema.  # noqa: E501
        :type subinterface: List[SubinterfacesSchemaSubinterface]
        """
        self.swagger_types = {
            'subinterface': List[SubinterfacesSchemaSubinterface]
        }

        self.attribute_map = {
            'subinterface': 'subinterface'
        }

        self._subinterface = subinterface

    @classmethod
    def from_dict(cls, dikt) -> 'SubinterfacesSchema':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SubinterfacesSchema of this SubinterfacesSchema.  # noqa: E501
        :rtype: SubinterfacesSchema
        """
        return util.deserialize_model(dikt, cls)

    @property
    def subinterface(self) -> List[SubinterfacesSchemaSubinterface]:
        """Gets the subinterface of this SubinterfacesSchema.

        The list of subinterfaces (logical interfaces) associated with a physical interface  # noqa: E501

        :return: The subinterface of this SubinterfacesSchema.
        :rtype: List[SubinterfacesSchemaSubinterface]
        """
        return self._subinterface

    @subinterface.setter
    def subinterface(self, subinterface: List[SubinterfacesSchemaSubinterface]):
        """Sets the subinterface of this SubinterfacesSchema.

        The list of subinterfaces (logical interfaces) associated with a physical interface  # noqa: E501

        :param subinterface: The subinterface of this SubinterfacesSchema.
        :type subinterface: List[SubinterfacesSchemaSubinterface]
        """

        self._subinterface = subinterface
