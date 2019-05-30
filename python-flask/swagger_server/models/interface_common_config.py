# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InterfaceCommonConfig(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, enabled: bool=None, description: str=None):  # noqa: E501
        """InterfaceCommonConfig - a model defined in Swagger

        :param enabled: The enabled of this InterfaceCommonConfig.  # noqa: E501
        :type enabled: bool
        :param description: The description of this InterfaceCommonConfig.  # noqa: E501
        :type description: str
        """
        self.swagger_types = {
            'enabled': bool,
            'description': str
        }

        self.attribute_map = {
            'enabled': 'enabled',
            'description': 'description'
        }

        self._enabled = enabled
        self._description = description

    @classmethod
    def from_dict(cls, dikt) -> 'InterfaceCommonConfig':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InterfaceCommonConfig of this InterfaceCommonConfig.  # noqa: E501
        :rtype: InterfaceCommonConfig
        """
        return util.deserialize_model(dikt, cls)

    @property
    def enabled(self) -> bool:
        """Gets the enabled of this InterfaceCommonConfig.

        This leaf contains the configured, desired state of the interface.  Systems that implement the IF-MIB use the value of this leaf in the 'running' datastore to set IF-MIB.ifAdminStatus to 'up' or 'down' after an ifEntry has been initialized, as described in RFC 2863.  Changes in this leaf in the 'running' datastore are reflected in ifAdminStatus, but if ifAdminStatus is changed over SNMP, this leaf is not affected.  # noqa: E501

        :return: The enabled of this InterfaceCommonConfig.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled: bool):
        """Sets the enabled of this InterfaceCommonConfig.

        This leaf contains the configured, desired state of the interface.  Systems that implement the IF-MIB use the value of this leaf in the 'running' datastore to set IF-MIB.ifAdminStatus to 'up' or 'down' after an ifEntry has been initialized, as described in RFC 2863.  Changes in this leaf in the 'running' datastore are reflected in ifAdminStatus, but if ifAdminStatus is changed over SNMP, this leaf is not affected.  # noqa: E501

        :param enabled: The enabled of this InterfaceCommonConfig.
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def description(self) -> str:
        """Gets the description of this InterfaceCommonConfig.

        A textual description of the interface.  A server implementation MAY map this leaf to the ifAlias MIB object.  Such an implementation needs to use some mechanism to handle the differences in size and characters allowed between this leaf and ifAlias.  The definition of such a mechanism is outside the scope of this document.  Since ifAlias is defined to be stored in non-volatile storage, the MIB implementation MUST map ifAlias to the value of 'description' in the persistently stored datastore.  Specifically, if the device supports ':startup', when ifAlias is read the device MUST return the value of 'description' in the 'startup' datastore, and when it is written, it MUST be written to the 'running' and 'startup' datastores.  Note that it is up to the implementation to  decide whether to modify this single leaf in 'startup' or perform an implicit copy-config from 'running' to 'startup'.  If the device does not support ':startup', ifAlias MUST be mapped to the 'description' leaf in the 'running' datastore.  # noqa: E501

        :return: The description of this InterfaceCommonConfig.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this InterfaceCommonConfig.

        A textual description of the interface.  A server implementation MAY map this leaf to the ifAlias MIB object.  Such an implementation needs to use some mechanism to handle the differences in size and characters allowed between this leaf and ifAlias.  The definition of such a mechanism is outside the scope of this document.  Since ifAlias is defined to be stored in non-volatile storage, the MIB implementation MUST map ifAlias to the value of 'description' in the persistently stored datastore.  Specifically, if the device supports ':startup', when ifAlias is read the device MUST return the value of 'description' in the 'startup' datastore, and when it is written, it MUST be written to the 'running' and 'startup' datastores.  Note that it is up to the implementation to  decide whether to modify this single leaf in 'startup' or perform an implicit copy-config from 'running' to 'startup'.  If the device does not support ':startup', ifAlias MUST be mapped to the 'description' leaf in the 'running' datastore.  # noqa: E501

        :param description: The description of this InterfaceCommonConfig.
        :type description: str
        """

        self._description = description