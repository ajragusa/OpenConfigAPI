# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.neighbors_schema_neighbor import NeighborsSchemaNeighbor  # noqa: F401,E501
from swagger_server import util


class NeighborsSchema(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, neighbor: List[NeighborsSchemaNeighbor]=None):  # noqa: E501
        """NeighborsSchema - a model defined in Swagger

        :param neighbor: The neighbor of this NeighborsSchema.  # noqa: E501
        :type neighbor: List[NeighborsSchemaNeighbor]
        """
        self.swagger_types = {
            'neighbor': List[NeighborsSchemaNeighbor]
        }

        self.attribute_map = {
            'neighbor': 'neighbor'
        }

        self._neighbor = neighbor

    @classmethod
    def from_dict(cls, dikt) -> 'NeighborsSchema':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NeighborsSchema of this NeighborsSchema.  # noqa: E501
        :rtype: NeighborsSchema
        """
        return util.deserialize_model(dikt, cls)

    @property
    def neighbor(self) -> List[NeighborsSchemaNeighbor]:
        """Gets the neighbor of this NeighborsSchema.

        List of IPv6 neighbors  # noqa: E501

        :return: The neighbor of this NeighborsSchema.
        :rtype: List[NeighborsSchemaNeighbor]
        """
        return self._neighbor

    @neighbor.setter
    def neighbor(self, neighbor: List[NeighborsSchemaNeighbor]):
        """Sets the neighbor of this NeighborsSchema.

        List of IPv6 neighbors  # noqa: E501

        :param neighbor: The neighbor of this NeighborsSchema.
        :type neighbor: List[NeighborsSchemaNeighbor]
        """

        self._neighbor = neighbor
