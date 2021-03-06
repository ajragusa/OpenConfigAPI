# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.aggregation_logical_top_aggregation import AggregationLogicalTopAggregation  # noqa: F401,E501
from swagger_server import util


class AggregationLogicalTop(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, aggregation: AggregationLogicalTopAggregation=None):  # noqa: E501
        """AggregationLogicalTop - a model defined in Swagger

        :param aggregation: The aggregation of this AggregationLogicalTop.  # noqa: E501
        :type aggregation: AggregationLogicalTopAggregation
        """
        self.swagger_types = {
            'aggregation': AggregationLogicalTopAggregation
        }

        self.attribute_map = {
            'aggregation': 'aggregation'
        }

        self._aggregation = aggregation

    @classmethod
    def from_dict(cls, dikt) -> 'AggregationLogicalTop':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AggregationLogicalTop of this AggregationLogicalTop.  # noqa: E501
        :rtype: AggregationLogicalTop
        """
        return util.deserialize_model(dikt, cls)

    @property
    def aggregation(self) -> AggregationLogicalTopAggregation:
        """Gets the aggregation of this AggregationLogicalTop.


        :return: The aggregation of this AggregationLogicalTop.
        :rtype: AggregationLogicalTopAggregation
        """
        return self._aggregation

    @aggregation.setter
    def aggregation(self, aggregation: AggregationLogicalTopAggregation):
        """Sets the aggregation of this AggregationLogicalTop.


        :param aggregation: The aggregation of this AggregationLogicalTop.
        :type aggregation: AggregationLogicalTopAggregation
        """

        self._aggregation = aggregation
