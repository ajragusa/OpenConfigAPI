# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class EthernetInterfaceStateCounters(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, in_crc_errors: str=None, out_mac_control_frames: str=None, in_block_errors: str=None, in_jabber_frames: str=None, in_mac_control_frames: str=None, out_mac_pause_frames: str=None, out8021q_frames: str=None, in_mac_pause_frames: str=None, in8021q_frames: str=None, in_fragment_frames: str=None, in_undersize_frames: str=None, in_oversize_frames: str=None):  # noqa: E501
        """EthernetInterfaceStateCounters - a model defined in Swagger

        :param in_crc_errors: The in_crc_errors of this EthernetInterfaceStateCounters.  # noqa: E501
        :type in_crc_errors: str
        :param out_mac_control_frames: The out_mac_control_frames of this EthernetInterfaceStateCounters.  # noqa: E501
        :type out_mac_control_frames: str
        :param in_block_errors: The in_block_errors of this EthernetInterfaceStateCounters.  # noqa: E501
        :type in_block_errors: str
        :param in_jabber_frames: The in_jabber_frames of this EthernetInterfaceStateCounters.  # noqa: E501
        :type in_jabber_frames: str
        :param in_mac_control_frames: The in_mac_control_frames of this EthernetInterfaceStateCounters.  # noqa: E501
        :type in_mac_control_frames: str
        :param out_mac_pause_frames: The out_mac_pause_frames of this EthernetInterfaceStateCounters.  # noqa: E501
        :type out_mac_pause_frames: str
        :param out8021q_frames: The out8021q_frames of this EthernetInterfaceStateCounters.  # noqa: E501
        :type out8021q_frames: str
        :param in_mac_pause_frames: The in_mac_pause_frames of this EthernetInterfaceStateCounters.  # noqa: E501
        :type in_mac_pause_frames: str
        :param in8021q_frames: The in8021q_frames of this EthernetInterfaceStateCounters.  # noqa: E501
        :type in8021q_frames: str
        :param in_fragment_frames: The in_fragment_frames of this EthernetInterfaceStateCounters.  # noqa: E501
        :type in_fragment_frames: str
        :param in_undersize_frames: The in_undersize_frames of this EthernetInterfaceStateCounters.  # noqa: E501
        :type in_undersize_frames: str
        :param in_oversize_frames: The in_oversize_frames of this EthernetInterfaceStateCounters.  # noqa: E501
        :type in_oversize_frames: str
        """
        self.swagger_types = {
            'in_crc_errors': str,
            'out_mac_control_frames': str,
            'in_block_errors': str,
            'in_jabber_frames': str,
            'in_mac_control_frames': str,
            'out_mac_pause_frames': str,
            'out8021q_frames': str,
            'in_mac_pause_frames': str,
            'in8021q_frames': str,
            'in_fragment_frames': str,
            'in_undersize_frames': str,
            'in_oversize_frames': str
        }

        self.attribute_map = {
            'in_crc_errors': 'inCrcErrors',
            'out_mac_control_frames': 'outMacControlFrames',
            'in_block_errors': 'inBlockErrors',
            'in_jabber_frames': 'inJabberFrames',
            'in_mac_control_frames': 'inMacControlFrames',
            'out_mac_pause_frames': 'outMacPauseFrames',
            'out8021q_frames': 'out8021qFrames',
            'in_mac_pause_frames': 'inMacPauseFrames',
            'in8021q_frames': 'in8021qFrames',
            'in_fragment_frames': 'inFragmentFrames',
            'in_undersize_frames': 'inUndersizeFrames',
            'in_oversize_frames': 'inOversizeFrames'
        }

        self._in_crc_errors = in_crc_errors
        self._out_mac_control_frames = out_mac_control_frames
        self._in_block_errors = in_block_errors
        self._in_jabber_frames = in_jabber_frames
        self._in_mac_control_frames = in_mac_control_frames
        self._out_mac_pause_frames = out_mac_pause_frames
        self._out8021q_frames = out8021q_frames
        self._in_mac_pause_frames = in_mac_pause_frames
        self._in8021q_frames = in8021q_frames
        self._in_fragment_frames = in_fragment_frames
        self._in_undersize_frames = in_undersize_frames
        self._in_oversize_frames = in_oversize_frames

    @classmethod
    def from_dict(cls, dikt) -> 'EthernetInterfaceStateCounters':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EthernetInterfaceStateCounters of this EthernetInterfaceStateCounters.  # noqa: E501
        :rtype: EthernetInterfaceStateCounters
        """
        return util.deserialize_model(dikt, cls)

    @property
    def in_crc_errors(self) -> str:
        """Gets the in_crc_errors of this EthernetInterfaceStateCounters.

        The total number of frames received that had a length (excluding framing bits, but including FCS octets) of between 64 and 1518 octets, inclusive, but had either a bad Frame Check Sequence (FCS) with an integral number of octets (FCS Error) or a bad FCS with a non-integral number of octets (Alignment Error)  # noqa: E501

        :return: The in_crc_errors of this EthernetInterfaceStateCounters.
        :rtype: str
        """
        return self._in_crc_errors

    @in_crc_errors.setter
    def in_crc_errors(self, in_crc_errors: str):
        """Sets the in_crc_errors of this EthernetInterfaceStateCounters.

        The total number of frames received that had a length (excluding framing bits, but including FCS octets) of between 64 and 1518 octets, inclusive, but had either a bad Frame Check Sequence (FCS) with an integral number of octets (FCS Error) or a bad FCS with a non-integral number of octets (Alignment Error)  # noqa: E501

        :param in_crc_errors: The in_crc_errors of this EthernetInterfaceStateCounters.
        :type in_crc_errors: str
        """

        self._in_crc_errors = in_crc_errors

    @property
    def out_mac_control_frames(self) -> str:
        """Gets the out_mac_control_frames of this EthernetInterfaceStateCounters.

        MAC layer control frames sent on the interface  # noqa: E501

        :return: The out_mac_control_frames of this EthernetInterfaceStateCounters.
        :rtype: str
        """
        return self._out_mac_control_frames

    @out_mac_control_frames.setter
    def out_mac_control_frames(self, out_mac_control_frames: str):
        """Sets the out_mac_control_frames of this EthernetInterfaceStateCounters.

        MAC layer control frames sent on the interface  # noqa: E501

        :param out_mac_control_frames: The out_mac_control_frames of this EthernetInterfaceStateCounters.
        :type out_mac_control_frames: str
        """

        self._out_mac_control_frames = out_mac_control_frames

    @property
    def in_block_errors(self) -> str:
        """Gets the in_block_errors of this EthernetInterfaceStateCounters.

        The number of received errored blocks. Error detection codes are capable of detecting whether one or more errors have occurred in a given sequence of bits – the block. It is normally not possible to determine the exact number of errored bits within the block  # noqa: E501

        :return: The in_block_errors of this EthernetInterfaceStateCounters.
        :rtype: str
        """
        return self._in_block_errors

    @in_block_errors.setter
    def in_block_errors(self, in_block_errors: str):
        """Sets the in_block_errors of this EthernetInterfaceStateCounters.

        The number of received errored blocks. Error detection codes are capable of detecting whether one or more errors have occurred in a given sequence of bits – the block. It is normally not possible to determine the exact number of errored bits within the block  # noqa: E501

        :param in_block_errors: The in_block_errors of this EthernetInterfaceStateCounters.
        :type in_block_errors: str
        """

        self._in_block_errors = in_block_errors

    @property
    def in_jabber_frames(self) -> str:
        """Gets the in_jabber_frames of this EthernetInterfaceStateCounters.

        Number of jabber frames received on the interface.  Jabber frames are typically defined as oversize frames which also have a bad CRC.  Implementations may use slightly different definitions of what constitutes a jabber frame.  Often indicative of a NIC hardware problem.  # noqa: E501

        :return: The in_jabber_frames of this EthernetInterfaceStateCounters.
        :rtype: str
        """
        return self._in_jabber_frames

    @in_jabber_frames.setter
    def in_jabber_frames(self, in_jabber_frames: str):
        """Sets the in_jabber_frames of this EthernetInterfaceStateCounters.

        Number of jabber frames received on the interface.  Jabber frames are typically defined as oversize frames which also have a bad CRC.  Implementations may use slightly different definitions of what constitutes a jabber frame.  Often indicative of a NIC hardware problem.  # noqa: E501

        :param in_jabber_frames: The in_jabber_frames of this EthernetInterfaceStateCounters.
        :type in_jabber_frames: str
        """

        self._in_jabber_frames = in_jabber_frames

    @property
    def in_mac_control_frames(self) -> str:
        """Gets the in_mac_control_frames of this EthernetInterfaceStateCounters.

        MAC layer control frames received on the interface  # noqa: E501

        :return: The in_mac_control_frames of this EthernetInterfaceStateCounters.
        :rtype: str
        """
        return self._in_mac_control_frames

    @in_mac_control_frames.setter
    def in_mac_control_frames(self, in_mac_control_frames: str):
        """Sets the in_mac_control_frames of this EthernetInterfaceStateCounters.

        MAC layer control frames received on the interface  # noqa: E501

        :param in_mac_control_frames: The in_mac_control_frames of this EthernetInterfaceStateCounters.
        :type in_mac_control_frames: str
        """

        self._in_mac_control_frames = in_mac_control_frames

    @property
    def out_mac_pause_frames(self) -> str:
        """Gets the out_mac_pause_frames of this EthernetInterfaceStateCounters.

        MAC layer PAUSE frames sent on the interface  # noqa: E501

        :return: The out_mac_pause_frames of this EthernetInterfaceStateCounters.
        :rtype: str
        """
        return self._out_mac_pause_frames

    @out_mac_pause_frames.setter
    def out_mac_pause_frames(self, out_mac_pause_frames: str):
        """Sets the out_mac_pause_frames of this EthernetInterfaceStateCounters.

        MAC layer PAUSE frames sent on the interface  # noqa: E501

        :param out_mac_pause_frames: The out_mac_pause_frames of this EthernetInterfaceStateCounters.
        :type out_mac_pause_frames: str
        """

        self._out_mac_pause_frames = out_mac_pause_frames

    @property
    def out8021q_frames(self) -> str:
        """Gets the out8021q_frames of this EthernetInterfaceStateCounters.

        Number of 802.1q tagged frames sent on the interface  # noqa: E501

        :return: The out8021q_frames of this EthernetInterfaceStateCounters.
        :rtype: str
        """
        return self._out8021q_frames

    @out8021q_frames.setter
    def out8021q_frames(self, out8021q_frames: str):
        """Sets the out8021q_frames of this EthernetInterfaceStateCounters.

        Number of 802.1q tagged frames sent on the interface  # noqa: E501

        :param out8021q_frames: The out8021q_frames of this EthernetInterfaceStateCounters.
        :type out8021q_frames: str
        """

        self._out8021q_frames = out8021q_frames

    @property
    def in_mac_pause_frames(self) -> str:
        """Gets the in_mac_pause_frames of this EthernetInterfaceStateCounters.

        MAC layer PAUSE frames received on the interface  # noqa: E501

        :return: The in_mac_pause_frames of this EthernetInterfaceStateCounters.
        :rtype: str
        """
        return self._in_mac_pause_frames

    @in_mac_pause_frames.setter
    def in_mac_pause_frames(self, in_mac_pause_frames: str):
        """Sets the in_mac_pause_frames of this EthernetInterfaceStateCounters.

        MAC layer PAUSE frames received on the interface  # noqa: E501

        :param in_mac_pause_frames: The in_mac_pause_frames of this EthernetInterfaceStateCounters.
        :type in_mac_pause_frames: str
        """

        self._in_mac_pause_frames = in_mac_pause_frames

    @property
    def in8021q_frames(self) -> str:
        """Gets the in8021q_frames of this EthernetInterfaceStateCounters.

        Number of 802.1q tagged frames received on the interface  # noqa: E501

        :return: The in8021q_frames of this EthernetInterfaceStateCounters.
        :rtype: str
        """
        return self._in8021q_frames

    @in8021q_frames.setter
    def in8021q_frames(self, in8021q_frames: str):
        """Sets the in8021q_frames of this EthernetInterfaceStateCounters.

        Number of 802.1q tagged frames received on the interface  # noqa: E501

        :param in8021q_frames: The in8021q_frames of this EthernetInterfaceStateCounters.
        :type in8021q_frames: str
        """

        self._in8021q_frames = in8021q_frames

    @property
    def in_fragment_frames(self) -> str:
        """Gets the in_fragment_frames of this EthernetInterfaceStateCounters.

        The total number of frames received that were less than 64 octets in length (excluding framing bits but including FCS octets) and had either a bad Frame Check Sequence (FCS) with an integral number of octets (FCS Error) or a bad FCS with a non-integral number of octets (Alignment Error).  # noqa: E501

        :return: The in_fragment_frames of this EthernetInterfaceStateCounters.
        :rtype: str
        """
        return self._in_fragment_frames

    @in_fragment_frames.setter
    def in_fragment_frames(self, in_fragment_frames: str):
        """Sets the in_fragment_frames of this EthernetInterfaceStateCounters.

        The total number of frames received that were less than 64 octets in length (excluding framing bits but including FCS octets) and had either a bad Frame Check Sequence (FCS) with an integral number of octets (FCS Error) or a bad FCS with a non-integral number of octets (Alignment Error).  # noqa: E501

        :param in_fragment_frames: The in_fragment_frames of this EthernetInterfaceStateCounters.
        :type in_fragment_frames: str
        """

        self._in_fragment_frames = in_fragment_frames

    @property
    def in_undersize_frames(self) -> str:
        """Gets the in_undersize_frames of this EthernetInterfaceStateCounters.

        The total number of frames received that were less than 64 octets long (excluding framing bits, but including FCS octets) and were otherwise well formed.  # noqa: E501

        :return: The in_undersize_frames of this EthernetInterfaceStateCounters.
        :rtype: str
        """
        return self._in_undersize_frames

    @in_undersize_frames.setter
    def in_undersize_frames(self, in_undersize_frames: str):
        """Sets the in_undersize_frames of this EthernetInterfaceStateCounters.

        The total number of frames received that were less than 64 octets long (excluding framing bits, but including FCS octets) and were otherwise well formed.  # noqa: E501

        :param in_undersize_frames: The in_undersize_frames of this EthernetInterfaceStateCounters.
        :type in_undersize_frames: str
        """

        self._in_undersize_frames = in_undersize_frames

    @property
    def in_oversize_frames(self) -> str:
        """Gets the in_oversize_frames of this EthernetInterfaceStateCounters.

        The total number of frames received that were longer than 1518 octets (excluding framing bits, but including FCS octets) and were otherwise well formed.  # noqa: E501

        :return: The in_oversize_frames of this EthernetInterfaceStateCounters.
        :rtype: str
        """
        return self._in_oversize_frames

    @in_oversize_frames.setter
    def in_oversize_frames(self, in_oversize_frames: str):
        """Sets the in_oversize_frames of this EthernetInterfaceStateCounters.

        The total number of frames received that were longer than 1518 octets (excluding framing bits, but including FCS octets) and were otherwise well formed.  # noqa: E501

        :param in_oversize_frames: The in_oversize_frames of this EthernetInterfaceStateCounters.
        :type in_oversize_frames: str
        """

        self._in_oversize_frames = in_oversize_frames
