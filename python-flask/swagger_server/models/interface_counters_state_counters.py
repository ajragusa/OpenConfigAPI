# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InterfaceCountersStateCounters(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, out_octets: str=None, out_unicast_pkts: str=None, carrier_transitions: str=None, in_multicast_pkts: str=None, in_pkts: str=None, out_errors: str=None, in_broadcast_pkts: str=None, out_pkts: str=None, in_octets: str=None, out_discards: str=None, in_unknown_protos: str=None, last_clear: str=None, in_errors: str=None, out_multicast_pkts: str=None, in_fcs_errors: str=None, in_discards: str=None, out_broadcast_pkts: str=None, in_unicast_pkts: str=None):  # noqa: E501
        """InterfaceCountersStateCounters - a model defined in Swagger

        :param out_octets: The out_octets of this InterfaceCountersStateCounters.  # noqa: E501
        :type out_octets: str
        :param out_unicast_pkts: The out_unicast_pkts of this InterfaceCountersStateCounters.  # noqa: E501
        :type out_unicast_pkts: str
        :param carrier_transitions: The carrier_transitions of this InterfaceCountersStateCounters.  # noqa: E501
        :type carrier_transitions: str
        :param in_multicast_pkts: The in_multicast_pkts of this InterfaceCountersStateCounters.  # noqa: E501
        :type in_multicast_pkts: str
        :param in_pkts: The in_pkts of this InterfaceCountersStateCounters.  # noqa: E501
        :type in_pkts: str
        :param out_errors: The out_errors of this InterfaceCountersStateCounters.  # noqa: E501
        :type out_errors: str
        :param in_broadcast_pkts: The in_broadcast_pkts of this InterfaceCountersStateCounters.  # noqa: E501
        :type in_broadcast_pkts: str
        :param out_pkts: The out_pkts of this InterfaceCountersStateCounters.  # noqa: E501
        :type out_pkts: str
        :param in_octets: The in_octets of this InterfaceCountersStateCounters.  # noqa: E501
        :type in_octets: str
        :param out_discards: The out_discards of this InterfaceCountersStateCounters.  # noqa: E501
        :type out_discards: str
        :param in_unknown_protos: The in_unknown_protos of this InterfaceCountersStateCounters.  # noqa: E501
        :type in_unknown_protos: str
        :param last_clear: The last_clear of this InterfaceCountersStateCounters.  # noqa: E501
        :type last_clear: str
        :param in_errors: The in_errors of this InterfaceCountersStateCounters.  # noqa: E501
        :type in_errors: str
        :param out_multicast_pkts: The out_multicast_pkts of this InterfaceCountersStateCounters.  # noqa: E501
        :type out_multicast_pkts: str
        :param in_fcs_errors: The in_fcs_errors of this InterfaceCountersStateCounters.  # noqa: E501
        :type in_fcs_errors: str
        :param in_discards: The in_discards of this InterfaceCountersStateCounters.  # noqa: E501
        :type in_discards: str
        :param out_broadcast_pkts: The out_broadcast_pkts of this InterfaceCountersStateCounters.  # noqa: E501
        :type out_broadcast_pkts: str
        :param in_unicast_pkts: The in_unicast_pkts of this InterfaceCountersStateCounters.  # noqa: E501
        :type in_unicast_pkts: str
        """
        self.swagger_types = {
            'out_octets': str,
            'out_unicast_pkts': str,
            'carrier_transitions': str,
            'in_multicast_pkts': str,
            'in_pkts': str,
            'out_errors': str,
            'in_broadcast_pkts': str,
            'out_pkts': str,
            'in_octets': str,
            'out_discards': str,
            'in_unknown_protos': str,
            'last_clear': str,
            'in_errors': str,
            'out_multicast_pkts': str,
            'in_fcs_errors': str,
            'in_discards': str,
            'out_broadcast_pkts': str,
            'in_unicast_pkts': str
        }

        self.attribute_map = {
            'out_octets': 'outOctets',
            'out_unicast_pkts': 'outUnicastPkts',
            'carrier_transitions': 'carrierTransitions',
            'in_multicast_pkts': 'inMulticastPkts',
            'in_pkts': 'inPkts',
            'out_errors': 'outErrors',
            'in_broadcast_pkts': 'inBroadcastPkts',
            'out_pkts': 'outPkts',
            'in_octets': 'inOctets',
            'out_discards': 'outDiscards',
            'in_unknown_protos': 'inUnknownProtos',
            'last_clear': 'lastClear',
            'in_errors': 'inErrors',
            'out_multicast_pkts': 'outMulticastPkts',
            'in_fcs_errors': 'inFcsErrors',
            'in_discards': 'inDiscards',
            'out_broadcast_pkts': 'outBroadcastPkts',
            'in_unicast_pkts': 'inUnicastPkts'
        }

        self._out_octets = out_octets
        self._out_unicast_pkts = out_unicast_pkts
        self._carrier_transitions = carrier_transitions
        self._in_multicast_pkts = in_multicast_pkts
        self._in_pkts = in_pkts
        self._out_errors = out_errors
        self._in_broadcast_pkts = in_broadcast_pkts
        self._out_pkts = out_pkts
        self._in_octets = in_octets
        self._out_discards = out_discards
        self._in_unknown_protos = in_unknown_protos
        self._last_clear = last_clear
        self._in_errors = in_errors
        self._out_multicast_pkts = out_multicast_pkts
        self._in_fcs_errors = in_fcs_errors
        self._in_discards = in_discards
        self._out_broadcast_pkts = out_broadcast_pkts
        self._in_unicast_pkts = in_unicast_pkts

    @classmethod
    def from_dict(cls, dikt) -> 'InterfaceCountersStateCounters':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InterfaceCountersState_counters of this InterfaceCountersStateCounters.  # noqa: E501
        :rtype: InterfaceCountersStateCounters
        """
        return util.deserialize_model(dikt, cls)

    @property
    def out_octets(self) -> str:
        """Gets the out_octets of this InterfaceCountersStateCounters.

        The total number of octets transmitted out of the interface, including framing characters.  Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of 'last-clear'.  # noqa: E501

        :return: The out_octets of this InterfaceCountersStateCounters.
        :rtype: str
        """
        return self._out_octets

    @out_octets.setter
    def out_octets(self, out_octets: str):
        """Sets the out_octets of this InterfaceCountersStateCounters.

        The total number of octets transmitted out of the interface, including framing characters.  Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of 'last-clear'.  # noqa: E501

        :param out_octets: The out_octets of this InterfaceCountersStateCounters.
        :type out_octets: str
        """

        self._out_octets = out_octets

    @property
    def out_unicast_pkts(self) -> str:
        """Gets the out_unicast_pkts of this InterfaceCountersStateCounters.

        The total number of packets that higher-level protocols requested be transmitted, and that were not addressed to a multicast or broadcast address at this sub-layer, including those that were discarded or not sent.  Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of 'last-clear'.  # noqa: E501

        :return: The out_unicast_pkts of this InterfaceCountersStateCounters.
        :rtype: str
        """
        return self._out_unicast_pkts

    @out_unicast_pkts.setter
    def out_unicast_pkts(self, out_unicast_pkts: str):
        """Sets the out_unicast_pkts of this InterfaceCountersStateCounters.

        The total number of packets that higher-level protocols requested be transmitted, and that were not addressed to a multicast or broadcast address at this sub-layer, including those that were discarded or not sent.  Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of 'last-clear'.  # noqa: E501

        :param out_unicast_pkts: The out_unicast_pkts of this InterfaceCountersStateCounters.
        :type out_unicast_pkts: str
        """

        self._out_unicast_pkts = out_unicast_pkts

    @property
    def carrier_transitions(self) -> str:
        """Gets the carrier_transitions of this InterfaceCountersStateCounters.

        Number of times the interface state has transitioned between up and down since the time the device restarted or the last-clear time, whichever is most recent.  # noqa: E501

        :return: The carrier_transitions of this InterfaceCountersStateCounters.
        :rtype: str
        """
        return self._carrier_transitions

    @carrier_transitions.setter
    def carrier_transitions(self, carrier_transitions: str):
        """Sets the carrier_transitions of this InterfaceCountersStateCounters.

        Number of times the interface state has transitioned between up and down since the time the device restarted or the last-clear time, whichever is most recent.  # noqa: E501

        :param carrier_transitions: The carrier_transitions of this InterfaceCountersStateCounters.
        :type carrier_transitions: str
        """

        self._carrier_transitions = carrier_transitions

    @property
    def in_multicast_pkts(self) -> str:
        """Gets the in_multicast_pkts of this InterfaceCountersStateCounters.

        The number of packets, delivered by this sub-layer to a higher (sub-)layer, that were addressed to a multicast address at this sub-layer.  For a MAC-layer protocol, this includes both Group and Functional addresses.  Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of 'last-clear'.  # noqa: E501

        :return: The in_multicast_pkts of this InterfaceCountersStateCounters.
        :rtype: str
        """
        return self._in_multicast_pkts

    @in_multicast_pkts.setter
    def in_multicast_pkts(self, in_multicast_pkts: str):
        """Sets the in_multicast_pkts of this InterfaceCountersStateCounters.

        The number of packets, delivered by this sub-layer to a higher (sub-)layer, that were addressed to a multicast address at this sub-layer.  For a MAC-layer protocol, this includes both Group and Functional addresses.  Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of 'last-clear'.  # noqa: E501

        :param in_multicast_pkts: The in_multicast_pkts of this InterfaceCountersStateCounters.
        :type in_multicast_pkts: str
        """

        self._in_multicast_pkts = in_multicast_pkts

    @property
    def in_pkts(self) -> str:
        """Gets the in_pkts of this InterfaceCountersStateCounters.

        The total number of packets received on the interface, including all unicast, multicast, broadcast and bad packets etc.  # noqa: E501

        :return: The in_pkts of this InterfaceCountersStateCounters.
        :rtype: str
        """
        return self._in_pkts

    @in_pkts.setter
    def in_pkts(self, in_pkts: str):
        """Sets the in_pkts of this InterfaceCountersStateCounters.

        The total number of packets received on the interface, including all unicast, multicast, broadcast and bad packets etc.  # noqa: E501

        :param in_pkts: The in_pkts of this InterfaceCountersStateCounters.
        :type in_pkts: str
        """

        self._in_pkts = in_pkts

    @property
    def out_errors(self) -> str:
        """Gets the out_errors of this InterfaceCountersStateCounters.

        For packet-oriented interfaces, the number of outbound packets that could not be transmitted because of errors. For character-oriented or fixed-length interfaces, the number of outbound transmission units that could not be transmitted because of errors.  Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of 'last-clear'.  # noqa: E501

        :return: The out_errors of this InterfaceCountersStateCounters.
        :rtype: str
        """
        return self._out_errors

    @out_errors.setter
    def out_errors(self, out_errors: str):
        """Sets the out_errors of this InterfaceCountersStateCounters.

        For packet-oriented interfaces, the number of outbound packets that could not be transmitted because of errors. For character-oriented or fixed-length interfaces, the number of outbound transmission units that could not be transmitted because of errors.  Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of 'last-clear'.  # noqa: E501

        :param out_errors: The out_errors of this InterfaceCountersStateCounters.
        :type out_errors: str
        """

        self._out_errors = out_errors

    @property
    def in_broadcast_pkts(self) -> str:
        """Gets the in_broadcast_pkts of this InterfaceCountersStateCounters.

        The number of packets, delivered by this sub-layer to a higher (sub-)layer, that were addressed to a broadcast address at this sub-layer.  Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of 'last-clear'.  # noqa: E501

        :return: The in_broadcast_pkts of this InterfaceCountersStateCounters.
        :rtype: str
        """
        return self._in_broadcast_pkts

    @in_broadcast_pkts.setter
    def in_broadcast_pkts(self, in_broadcast_pkts: str):
        """Sets the in_broadcast_pkts of this InterfaceCountersStateCounters.

        The number of packets, delivered by this sub-layer to a higher (sub-)layer, that were addressed to a broadcast address at this sub-layer.  Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of 'last-clear'.  # noqa: E501

        :param in_broadcast_pkts: The in_broadcast_pkts of this InterfaceCountersStateCounters.
        :type in_broadcast_pkts: str
        """

        self._in_broadcast_pkts = in_broadcast_pkts

    @property
    def out_pkts(self) -> str:
        """Gets the out_pkts of this InterfaceCountersStateCounters.

        The total number of packets transmitted out of the interface, including all unicast, multicast, broadcast, and bad packets etc.  # noqa: E501

        :return: The out_pkts of this InterfaceCountersStateCounters.
        :rtype: str
        """
        return self._out_pkts

    @out_pkts.setter
    def out_pkts(self, out_pkts: str):
        """Sets the out_pkts of this InterfaceCountersStateCounters.

        The total number of packets transmitted out of the interface, including all unicast, multicast, broadcast, and bad packets etc.  # noqa: E501

        :param out_pkts: The out_pkts of this InterfaceCountersStateCounters.
        :type out_pkts: str
        """

        self._out_pkts = out_pkts

    @property
    def in_octets(self) -> str:
        """Gets the in_octets of this InterfaceCountersStateCounters.

        The total number of octets received on the interface, including framing characters.  Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of 'last-clear'.  # noqa: E501

        :return: The in_octets of this InterfaceCountersStateCounters.
        :rtype: str
        """
        return self._in_octets

    @in_octets.setter
    def in_octets(self, in_octets: str):
        """Sets the in_octets of this InterfaceCountersStateCounters.

        The total number of octets received on the interface, including framing characters.  Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of 'last-clear'.  # noqa: E501

        :param in_octets: The in_octets of this InterfaceCountersStateCounters.
        :type in_octets: str
        """

        self._in_octets = in_octets

    @property
    def out_discards(self) -> str:
        """Gets the out_discards of this InterfaceCountersStateCounters.

        The number of outbound packets that were chosen to be discarded even though no errors had been detected to prevent their being transmitted.  One possible reason for discarding such a packet could be to free up buffer space.  Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of 'last-clear'.  # noqa: E501

        :return: The out_discards of this InterfaceCountersStateCounters.
        :rtype: str
        """
        return self._out_discards

    @out_discards.setter
    def out_discards(self, out_discards: str):
        """Sets the out_discards of this InterfaceCountersStateCounters.

        The number of outbound packets that were chosen to be discarded even though no errors had been detected to prevent their being transmitted.  One possible reason for discarding such a packet could be to free up buffer space.  Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of 'last-clear'.  # noqa: E501

        :param out_discards: The out_discards of this InterfaceCountersStateCounters.
        :type out_discards: str
        """

        self._out_discards = out_discards

    @property
    def in_unknown_protos(self) -> str:
        """Gets the in_unknown_protos of this InterfaceCountersStateCounters.

        For packet-oriented interfaces, the number of packets received via the interface that were discarded because of an unknown or unsupported protocol.  For character-oriented or fixed-length interfaces that support protocol multiplexing, the number of transmission units received via the interface that were discarded because of an unknown or unsupported protocol. For any interface that does not support protocol multiplexing, this counter is not present.  Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of 'last-clear'.  # noqa: E501

        :return: The in_unknown_protos of this InterfaceCountersStateCounters.
        :rtype: str
        """
        return self._in_unknown_protos

    @in_unknown_protos.setter
    def in_unknown_protos(self, in_unknown_protos: str):
        """Sets the in_unknown_protos of this InterfaceCountersStateCounters.

        For packet-oriented interfaces, the number of packets received via the interface that were discarded because of an unknown or unsupported protocol.  For character-oriented or fixed-length interfaces that support protocol multiplexing, the number of transmission units received via the interface that were discarded because of an unknown or unsupported protocol. For any interface that does not support protocol multiplexing, this counter is not present.  Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of 'last-clear'.  # noqa: E501

        :param in_unknown_protos: The in_unknown_protos of this InterfaceCountersStateCounters.
        :type in_unknown_protos: str
        """

        self._in_unknown_protos = in_unknown_protos

    @property
    def last_clear(self) -> str:
        """Gets the last_clear of this InterfaceCountersStateCounters.

        Timestamp of the last time the interface counters were cleared.  The value is the timestamp in nanoseconds relative to the Unix Epoch (Jan 1, 1970 00:00:00 UTC).  # noqa: E501

        :return: The last_clear of this InterfaceCountersStateCounters.
        :rtype: str
        """
        return self._last_clear

    @last_clear.setter
    def last_clear(self, last_clear: str):
        """Sets the last_clear of this InterfaceCountersStateCounters.

        Timestamp of the last time the interface counters were cleared.  The value is the timestamp in nanoseconds relative to the Unix Epoch (Jan 1, 1970 00:00:00 UTC).  # noqa: E501

        :param last_clear: The last_clear of this InterfaceCountersStateCounters.
        :type last_clear: str
        """

        self._last_clear = last_clear

    @property
    def in_errors(self) -> str:
        """Gets the in_errors of this InterfaceCountersStateCounters.

        For packet-oriented interfaces, the number of inbound packets that contained errors preventing them from being deliverable to a higher-layer protocol.  For character- oriented or fixed-length interfaces, the number of inbound transmission units that contained errors preventing them from being deliverable to a higher-layer protocol.  Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of 'last-clear'.  # noqa: E501

        :return: The in_errors of this InterfaceCountersStateCounters.
        :rtype: str
        """
        return self._in_errors

    @in_errors.setter
    def in_errors(self, in_errors: str):
        """Sets the in_errors of this InterfaceCountersStateCounters.

        For packet-oriented interfaces, the number of inbound packets that contained errors preventing them from being deliverable to a higher-layer protocol.  For character- oriented or fixed-length interfaces, the number of inbound transmission units that contained errors preventing them from being deliverable to a higher-layer protocol.  Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of 'last-clear'.  # noqa: E501

        :param in_errors: The in_errors of this InterfaceCountersStateCounters.
        :type in_errors: str
        """

        self._in_errors = in_errors

    @property
    def out_multicast_pkts(self) -> str:
        """Gets the out_multicast_pkts of this InterfaceCountersStateCounters.

        The total number of packets that higher-level protocols requested be transmitted, and that were addressed to a multicast address at this sub-layer, including those that were discarded or not sent.  For a MAC-layer protocol, this includes both Group and Functional addresses.  Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of 'last-clear'.  # noqa: E501

        :return: The out_multicast_pkts of this InterfaceCountersStateCounters.
        :rtype: str
        """
        return self._out_multicast_pkts

    @out_multicast_pkts.setter
    def out_multicast_pkts(self, out_multicast_pkts: str):
        """Sets the out_multicast_pkts of this InterfaceCountersStateCounters.

        The total number of packets that higher-level protocols requested be transmitted, and that were addressed to a multicast address at this sub-layer, including those that were discarded or not sent.  For a MAC-layer protocol, this includes both Group and Functional addresses.  Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of 'last-clear'.  # noqa: E501

        :param out_multicast_pkts: The out_multicast_pkts of this InterfaceCountersStateCounters.
        :type out_multicast_pkts: str
        """

        self._out_multicast_pkts = out_multicast_pkts

    @property
    def in_fcs_errors(self) -> str:
        """Gets the in_fcs_errors of this InterfaceCountersStateCounters.

        Number of received packets which had errors in the frame check sequence (FCS), i.e., framing errors.  Discontinuities in the value of this counter can occur when the device is re-initialization as indicated by the value of 'last-clear'.  # noqa: E501

        :return: The in_fcs_errors of this InterfaceCountersStateCounters.
        :rtype: str
        """
        return self._in_fcs_errors

    @in_fcs_errors.setter
    def in_fcs_errors(self, in_fcs_errors: str):
        """Sets the in_fcs_errors of this InterfaceCountersStateCounters.

        Number of received packets which had errors in the frame check sequence (FCS), i.e., framing errors.  Discontinuities in the value of this counter can occur when the device is re-initialization as indicated by the value of 'last-clear'.  # noqa: E501

        :param in_fcs_errors: The in_fcs_errors of this InterfaceCountersStateCounters.
        :type in_fcs_errors: str
        """

        self._in_fcs_errors = in_fcs_errors

    @property
    def in_discards(self) -> str:
        """Gets the in_discards of this InterfaceCountersStateCounters.

        The number of inbound packets that were chosen to be discarded even though no errors had been detected to prevent their being deliverable to a higher-layer protocol.  One possible reason for discarding such a packet could be to free up buffer space.  Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of 'last-clear'.  # noqa: E501

        :return: The in_discards of this InterfaceCountersStateCounters.
        :rtype: str
        """
        return self._in_discards

    @in_discards.setter
    def in_discards(self, in_discards: str):
        """Sets the in_discards of this InterfaceCountersStateCounters.

        The number of inbound packets that were chosen to be discarded even though no errors had been detected to prevent their being deliverable to a higher-layer protocol.  One possible reason for discarding such a packet could be to free up buffer space.  Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of 'last-clear'.  # noqa: E501

        :param in_discards: The in_discards of this InterfaceCountersStateCounters.
        :type in_discards: str
        """

        self._in_discards = in_discards

    @property
    def out_broadcast_pkts(self) -> str:
        """Gets the out_broadcast_pkts of this InterfaceCountersStateCounters.

        The total number of packets that higher-level protocols requested be transmitted, and that were addressed to a broadcast address at this sub-layer, including those that were discarded or not sent.  Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of 'last-clear'.  # noqa: E501

        :return: The out_broadcast_pkts of this InterfaceCountersStateCounters.
        :rtype: str
        """
        return self._out_broadcast_pkts

    @out_broadcast_pkts.setter
    def out_broadcast_pkts(self, out_broadcast_pkts: str):
        """Sets the out_broadcast_pkts of this InterfaceCountersStateCounters.

        The total number of packets that higher-level protocols requested be transmitted, and that were addressed to a broadcast address at this sub-layer, including those that were discarded or not sent.  Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of 'last-clear'.  # noqa: E501

        :param out_broadcast_pkts: The out_broadcast_pkts of this InterfaceCountersStateCounters.
        :type out_broadcast_pkts: str
        """

        self._out_broadcast_pkts = out_broadcast_pkts

    @property
    def in_unicast_pkts(self) -> str:
        """Gets the in_unicast_pkts of this InterfaceCountersStateCounters.

        The number of packets, delivered by this sub-layer to a higher (sub-)layer, that were not addressed to a multicast or broadcast address at this sub-layer.  Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of 'last-clear'.  # noqa: E501

        :return: The in_unicast_pkts of this InterfaceCountersStateCounters.
        :rtype: str
        """
        return self._in_unicast_pkts

    @in_unicast_pkts.setter
    def in_unicast_pkts(self, in_unicast_pkts: str):
        """Sets the in_unicast_pkts of this InterfaceCountersStateCounters.

        The number of packets, delivered by this sub-layer to a higher (sub-)layer, that were not addressed to a multicast or broadcast address at this sub-layer.  Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of 'last-clear'.  # noqa: E501

        :param in_unicast_pkts: The in_unicast_pkts of this InterfaceCountersStateCounters.
        :type in_unicast_pkts: str
        """

        self._in_unicast_pkts = in_unicast_pkts