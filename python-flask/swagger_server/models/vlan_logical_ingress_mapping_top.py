# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.vlan_logical_ingress_mapping_top_ingress_mapping import VlanLogicalIngressMappingTopIngressMapping  # noqa: F401,E501
from swagger_server import util


class VlanLogicalIngressMappingTop(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, ingress_mapping: VlanLogicalIngressMappingTopIngressMapping=None):  # noqa: E501
        """VlanLogicalIngressMappingTop - a model defined in Swagger

        :param ingress_mapping: The ingress_mapping of this VlanLogicalIngressMappingTop.  # noqa: E501
        :type ingress_mapping: VlanLogicalIngressMappingTopIngressMapping
        """
        self.swagger_types = {
            'ingress_mapping': VlanLogicalIngressMappingTopIngressMapping
        }

        self.attribute_map = {
            'ingress_mapping': 'ingressMapping'
        }

        self._ingress_mapping = ingress_mapping

    @classmethod
    def from_dict(cls, dikt) -> 'VlanLogicalIngressMappingTop':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VlanLogicalIngressMappingTop of this VlanLogicalIngressMappingTop.  # noqa: E501
        :rtype: VlanLogicalIngressMappingTop
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ingress_mapping(self) -> VlanLogicalIngressMappingTopIngressMapping:
        """Gets the ingress_mapping of this VlanLogicalIngressMappingTop.


        :return: The ingress_mapping of this VlanLogicalIngressMappingTop.
        :rtype: VlanLogicalIngressMappingTopIngressMapping
        """
        return self._ingress_mapping

    @ingress_mapping.setter
    def ingress_mapping(self, ingress_mapping: VlanLogicalIngressMappingTopIngressMapping):
        """Sets the ingress_mapping of this VlanLogicalIngressMappingTop.


        :param ingress_mapping: The ingress_mapping of this VlanLogicalIngressMappingTop.
        :type ingress_mapping: VlanLogicalIngressMappingTopIngressMapping
        """

        self._ingress_mapping = ingress_mapping
