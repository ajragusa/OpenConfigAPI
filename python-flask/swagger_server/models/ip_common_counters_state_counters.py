# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IpCommonCountersStateCounters(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, out_error_pkts: str=None, in_pkts: str=None, out_forwarded_pkts: str=None, in_forwarded_octets: str=None, in_forwarded_pkts: str=None, in_octets: str=None, out_octets: str=None, in_discarded_pkts: str=None, out_pkts: str=None, in_error_pkts: str=None, out_discarded_pkts: str=None, out_forwarded_octets: str=None):  # noqa: E501
        """IpCommonCountersStateCounters - a model defined in Swagger

        :param out_error_pkts: The out_error_pkts of this IpCommonCountersStateCounters.  # noqa: E501
        :type out_error_pkts: str
        :param in_pkts: The in_pkts of this IpCommonCountersStateCounters.  # noqa: E501
        :type in_pkts: str
        :param out_forwarded_pkts: The out_forwarded_pkts of this IpCommonCountersStateCounters.  # noqa: E501
        :type out_forwarded_pkts: str
        :param in_forwarded_octets: The in_forwarded_octets of this IpCommonCountersStateCounters.  # noqa: E501
        :type in_forwarded_octets: str
        :param in_forwarded_pkts: The in_forwarded_pkts of this IpCommonCountersStateCounters.  # noqa: E501
        :type in_forwarded_pkts: str
        :param in_octets: The in_octets of this IpCommonCountersStateCounters.  # noqa: E501
        :type in_octets: str
        :param out_octets: The out_octets of this IpCommonCountersStateCounters.  # noqa: E501
        :type out_octets: str
        :param in_discarded_pkts: The in_discarded_pkts of this IpCommonCountersStateCounters.  # noqa: E501
        :type in_discarded_pkts: str
        :param out_pkts: The out_pkts of this IpCommonCountersStateCounters.  # noqa: E501
        :type out_pkts: str
        :param in_error_pkts: The in_error_pkts of this IpCommonCountersStateCounters.  # noqa: E501
        :type in_error_pkts: str
        :param out_discarded_pkts: The out_discarded_pkts of this IpCommonCountersStateCounters.  # noqa: E501
        :type out_discarded_pkts: str
        :param out_forwarded_octets: The out_forwarded_octets of this IpCommonCountersStateCounters.  # noqa: E501
        :type out_forwarded_octets: str
        """
        self.swagger_types = {
            'out_error_pkts': str,
            'in_pkts': str,
            'out_forwarded_pkts': str,
            'in_forwarded_octets': str,
            'in_forwarded_pkts': str,
            'in_octets': str,
            'out_octets': str,
            'in_discarded_pkts': str,
            'out_pkts': str,
            'in_error_pkts': str,
            'out_discarded_pkts': str,
            'out_forwarded_octets': str
        }

        self.attribute_map = {
            'out_error_pkts': 'outErrorPkts',
            'in_pkts': 'inPkts',
            'out_forwarded_pkts': 'outForwardedPkts',
            'in_forwarded_octets': 'inForwardedOctets',
            'in_forwarded_pkts': 'inForwardedPkts',
            'in_octets': 'inOctets',
            'out_octets': 'outOctets',
            'in_discarded_pkts': 'inDiscardedPkts',
            'out_pkts': 'outPkts',
            'in_error_pkts': 'inErrorPkts',
            'out_discarded_pkts': 'outDiscardedPkts',
            'out_forwarded_octets': 'outForwardedOctets'
        }

        self._out_error_pkts = out_error_pkts
        self._in_pkts = in_pkts
        self._out_forwarded_pkts = out_forwarded_pkts
        self._in_forwarded_octets = in_forwarded_octets
        self._in_forwarded_pkts = in_forwarded_pkts
        self._in_octets = in_octets
        self._out_octets = out_octets
        self._in_discarded_pkts = in_discarded_pkts
        self._out_pkts = out_pkts
        self._in_error_pkts = in_error_pkts
        self._out_discarded_pkts = out_discarded_pkts
        self._out_forwarded_octets = out_forwarded_octets

    @classmethod
    def from_dict(cls, dikt) -> 'IpCommonCountersStateCounters':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The IpCommonCountersState_counters of this IpCommonCountersStateCounters.  # noqa: E501
        :rtype: IpCommonCountersStateCounters
        """
        return util.deserialize_model(dikt, cls)

    @property
    def out_error_pkts(self) -> str:
        """Gets the out_error_pkts of this IpCommonCountersStateCounters.

        Number of IP packets for the specified address family locally generated and discarded due to errors, including no route found to the IP destination.  # noqa: E501

        :return: The out_error_pkts of this IpCommonCountersStateCounters.
        :rtype: str
        """
        return self._out_error_pkts

    @out_error_pkts.setter
    def out_error_pkts(self, out_error_pkts: str):
        """Sets the out_error_pkts of this IpCommonCountersStateCounters.

        Number of IP packets for the specified address family locally generated and discarded due to errors, including no route found to the IP destination.  # noqa: E501

        :param out_error_pkts: The out_error_pkts of this IpCommonCountersStateCounters.
        :type out_error_pkts: str
        """

        self._out_error_pkts = out_error_pkts

    @property
    def in_pkts(self) -> str:
        """Gets the in_pkts of this IpCommonCountersStateCounters.

        The total number of IP packets received for the specified address family, including those received in error  # noqa: E501

        :return: The in_pkts of this IpCommonCountersStateCounters.
        :rtype: str
        """
        return self._in_pkts

    @in_pkts.setter
    def in_pkts(self, in_pkts: str):
        """Sets the in_pkts of this IpCommonCountersStateCounters.

        The total number of IP packets received for the specified address family, including those received in error  # noqa: E501

        :param in_pkts: The in_pkts of this IpCommonCountersStateCounters.
        :type in_pkts: str
        """

        self._in_pkts = in_pkts

    @property
    def out_forwarded_pkts(self) -> str:
        """Gets the out_forwarded_pkts of this IpCommonCountersStateCounters.

        The number of packets for which this entity was not their final IP destination and for which it was successful in finding a path to their final destination.  # noqa: E501

        :return: The out_forwarded_pkts of this IpCommonCountersStateCounters.
        :rtype: str
        """
        return self._out_forwarded_pkts

    @out_forwarded_pkts.setter
    def out_forwarded_pkts(self, out_forwarded_pkts: str):
        """Sets the out_forwarded_pkts of this IpCommonCountersStateCounters.

        The number of packets for which this entity was not their final IP destination and for which it was successful in finding a path to their final destination.  # noqa: E501

        :param out_forwarded_pkts: The out_forwarded_pkts of this IpCommonCountersStateCounters.
        :type out_forwarded_pkts: str
        """

        self._out_forwarded_pkts = out_forwarded_pkts

    @property
    def in_forwarded_octets(self) -> str:
        """Gets the in_forwarded_octets of this IpCommonCountersStateCounters.

        The number of octets received in input IP packets for the specified address family for which the device was not their final IP destination and for which the device attempted to find a route to forward them to that final destination.  # noqa: E501

        :return: The in_forwarded_octets of this IpCommonCountersStateCounters.
        :rtype: str
        """
        return self._in_forwarded_octets

    @in_forwarded_octets.setter
    def in_forwarded_octets(self, in_forwarded_octets: str):
        """Sets the in_forwarded_octets of this IpCommonCountersStateCounters.

        The number of octets received in input IP packets for the specified address family for which the device was not their final IP destination and for which the device attempted to find a route to forward them to that final destination.  # noqa: E501

        :param in_forwarded_octets: The in_forwarded_octets of this IpCommonCountersStateCounters.
        :type in_forwarded_octets: str
        """

        self._in_forwarded_octets = in_forwarded_octets

    @property
    def in_forwarded_pkts(self) -> str:
        """Gets the in_forwarded_pkts of this IpCommonCountersStateCounters.

        The number of input packets for which the device was not their final IP destination and for which the device attempted to find a route to forward them to that final destination.  # noqa: E501

        :return: The in_forwarded_pkts of this IpCommonCountersStateCounters.
        :rtype: str
        """
        return self._in_forwarded_pkts

    @in_forwarded_pkts.setter
    def in_forwarded_pkts(self, in_forwarded_pkts: str):
        """Sets the in_forwarded_pkts of this IpCommonCountersStateCounters.

        The number of input packets for which the device was not their final IP destination and for which the device attempted to find a route to forward them to that final destination.  # noqa: E501

        :param in_forwarded_pkts: The in_forwarded_pkts of this IpCommonCountersStateCounters.
        :type in_forwarded_pkts: str
        """

        self._in_forwarded_pkts = in_forwarded_pkts

    @property
    def in_octets(self) -> str:
        """Gets the in_octets of this IpCommonCountersStateCounters.

        The total number of octets received in input IP packets for the specified address family, including those received in error.  # noqa: E501

        :return: The in_octets of this IpCommonCountersStateCounters.
        :rtype: str
        """
        return self._in_octets

    @in_octets.setter
    def in_octets(self, in_octets: str):
        """Sets the in_octets of this IpCommonCountersStateCounters.

        The total number of octets received in input IP packets for the specified address family, including those received in error.  # noqa: E501

        :param in_octets: The in_octets of this IpCommonCountersStateCounters.
        :type in_octets: str
        """

        self._in_octets = in_octets

    @property
    def out_octets(self) -> str:
        """Gets the out_octets of this IpCommonCountersStateCounters.

        The total number of octets in IP packets for the specified address family that the device supplied to the lower layers for transmission.  This includes packets generated locally and those forwarded by the device.  # noqa: E501

        :return: The out_octets of this IpCommonCountersStateCounters.
        :rtype: str
        """
        return self._out_octets

    @out_octets.setter
    def out_octets(self, out_octets: str):
        """Sets the out_octets of this IpCommonCountersStateCounters.

        The total number of octets in IP packets for the specified address family that the device supplied to the lower layers for transmission.  This includes packets generated locally and those forwarded by the device.  # noqa: E501

        :param out_octets: The out_octets of this IpCommonCountersStateCounters.
        :type out_octets: str
        """

        self._out_octets = out_octets

    @property
    def in_discarded_pkts(self) -> str:
        """Gets the in_discarded_pkts of this IpCommonCountersStateCounters.

        The number of input IP packets for the specified address family, for which no problems were encountered to prevent their continued processing, but were discarded (e.g., for lack of buffer space).  # noqa: E501

        :return: The in_discarded_pkts of this IpCommonCountersStateCounters.
        :rtype: str
        """
        return self._in_discarded_pkts

    @in_discarded_pkts.setter
    def in_discarded_pkts(self, in_discarded_pkts: str):
        """Sets the in_discarded_pkts of this IpCommonCountersStateCounters.

        The number of input IP packets for the specified address family, for which no problems were encountered to prevent their continued processing, but were discarded (e.g., for lack of buffer space).  # noqa: E501

        :param in_discarded_pkts: The in_discarded_pkts of this IpCommonCountersStateCounters.
        :type in_discarded_pkts: str
        """

        self._in_discarded_pkts = in_discarded_pkts

    @property
    def out_pkts(self) -> str:
        """Gets the out_pkts of this IpCommonCountersStateCounters.

        The total number of IP packets for the specified address family that the device supplied to the lower layers for transmission.  This includes packets generated locally and those forwarded by the device.  # noqa: E501

        :return: The out_pkts of this IpCommonCountersStateCounters.
        :rtype: str
        """
        return self._out_pkts

    @out_pkts.setter
    def out_pkts(self, out_pkts: str):
        """Sets the out_pkts of this IpCommonCountersStateCounters.

        The total number of IP packets for the specified address family that the device supplied to the lower layers for transmission.  This includes packets generated locally and those forwarded by the device.  # noqa: E501

        :param out_pkts: The out_pkts of this IpCommonCountersStateCounters.
        :type out_pkts: str
        """

        self._out_pkts = out_pkts

    @property
    def in_error_pkts(self) -> str:
        """Gets the in_error_pkts of this IpCommonCountersStateCounters.

        Number of IP packets discarded due to errors for the specified address family, including errors in the IP header, no route found to the IP destination, invalid address, unknown protocol, etc.  # noqa: E501

        :return: The in_error_pkts of this IpCommonCountersStateCounters.
        :rtype: str
        """
        return self._in_error_pkts

    @in_error_pkts.setter
    def in_error_pkts(self, in_error_pkts: str):
        """Sets the in_error_pkts of this IpCommonCountersStateCounters.

        Number of IP packets discarded due to errors for the specified address family, including errors in the IP header, no route found to the IP destination, invalid address, unknown protocol, etc.  # noqa: E501

        :param in_error_pkts: The in_error_pkts of this IpCommonCountersStateCounters.
        :type in_error_pkts: str
        """

        self._in_error_pkts = in_error_pkts

    @property
    def out_discarded_pkts(self) -> str:
        """Gets the out_discarded_pkts of this IpCommonCountersStateCounters.

        The number of output IP packets for the specified address family for which no problem was encountered to prevent their transmission to their destination, but were discarded (e.g., for lack of buffer space).  # noqa: E501

        :return: The out_discarded_pkts of this IpCommonCountersStateCounters.
        :rtype: str
        """
        return self._out_discarded_pkts

    @out_discarded_pkts.setter
    def out_discarded_pkts(self, out_discarded_pkts: str):
        """Sets the out_discarded_pkts of this IpCommonCountersStateCounters.

        The number of output IP packets for the specified address family for which no problem was encountered to prevent their transmission to their destination, but were discarded (e.g., for lack of buffer space).  # noqa: E501

        :param out_discarded_pkts: The out_discarded_pkts of this IpCommonCountersStateCounters.
        :type out_discarded_pkts: str
        """

        self._out_discarded_pkts = out_discarded_pkts

    @property
    def out_forwarded_octets(self) -> str:
        """Gets the out_forwarded_octets of this IpCommonCountersStateCounters.

        The number of octets in packets for which this entity was not their final IP destination and for which it was successful in finding a path to their final destination.  # noqa: E501

        :return: The out_forwarded_octets of this IpCommonCountersStateCounters.
        :rtype: str
        """
        return self._out_forwarded_octets

    @out_forwarded_octets.setter
    def out_forwarded_octets(self, out_forwarded_octets: str):
        """Sets the out_forwarded_octets of this IpCommonCountersStateCounters.

        The number of octets in packets for which this entity was not their final IP destination and for which it was successful in finding a path to their final destination.  # noqa: E501

        :param out_forwarded_octets: The out_forwarded_octets of this IpCommonCountersStateCounters.
        :type out_forwarded_octets: str
        """

        self._out_forwarded_octets = out_forwarded_octets
