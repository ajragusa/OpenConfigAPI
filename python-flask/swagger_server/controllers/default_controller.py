import connexion
import six

from swagger_server.models.address_schema import AddressSchema  # noqa: E501
from swagger_server.models.addresses_schema import AddressesSchema  # noqa: E501
from swagger_server.models.aggregation_logical_config import AggregationLogicalConfig  # noqa: E501
from swagger_server.models.aggregation_logical_state import AggregationLogicalState  # noqa: E501
from swagger_server.models.aggregation_schema import AggregationSchema  # noqa: E501
from swagger_server.models.counters_schema import CountersSchema  # noqa: E501
from swagger_server.models.double_tagged_inner_list_schema import DoubleTaggedInnerListSchema  # noqa: E501
from swagger_server.models.double_tagged_inner_outer_range_schema import DoubleTaggedInnerOuterRangeSchema  # noqa: E501
from swagger_server.models.double_tagged_inner_range_schema import DoubleTaggedInnerRangeSchema  # noqa: E501
from swagger_server.models.double_tagged_outer_list_schema import DoubleTaggedOuterListSchema  # noqa: E501
from swagger_server.models.double_tagged_outer_range_schema import DoubleTaggedOuterRangeSchema  # noqa: E501
from swagger_server.models.double_tagged_schema import DoubleTaggedSchema  # noqa: E501
from swagger_server.models.egress_mapping_schema import EgressMappingSchema  # noqa: E501
from swagger_server.models.ethernet_interface_config import EthernetInterfaceConfig  # noqa: E501
from swagger_server.models.ethernet_interface_state import EthernetInterfaceState  # noqa: E501
from swagger_server.models.ethernet_interface_state_counters import EthernetInterfaceStateCounters  # noqa: E501
from swagger_server.models.ethernet_schema import EthernetSchema  # noqa: E501
from swagger_server.models.hold_time_schema import HoldTimeSchema  # noqa: E501
from swagger_server.models.ingress_mapping_schema import IngressMappingSchema  # noqa: E501
from swagger_server.models.interface_counters_state import InterfaceCountersState  # noqa: E501
from swagger_server.models.interface_phys_config import InterfacePhysConfig  # noqa: E501
from swagger_server.models.interface_phys_holdtime_config import InterfacePhysHoldtimeConfig  # noqa: E501
from swagger_server.models.interface_phys_holdtime_state import InterfacePhysHoldtimeState  # noqa: E501
from swagger_server.models.interface_ref import InterfaceRef  # noqa: E501
from swagger_server.models.interface_ref_common import InterfaceRefCommon  # noqa: E501
from swagger_server.models.interface_ref_state_container import InterfaceRefStateContainer  # noqa: E501
from swagger_server.models.interface_tracking_schema import InterfaceTrackingSchema  # noqa: E501
from swagger_server.models.interfaces_schema import InterfacesSchema  # noqa: E501
from swagger_server.models.ip_common_counters_state import IpCommonCountersState  # noqa: E501
from swagger_server.models.ip_vrrp_config import IpVrrpConfig  # noqa: E501
from swagger_server.models.ip_vrrp_state import IpVrrpState  # noqa: E501
from swagger_server.models.ip_vrrp_tracking_config import IpVrrpTrackingConfig  # noqa: E501
from swagger_server.models.ip_vrrp_tracking_state import IpVrrpTrackingState  # noqa: E501
from swagger_server.models.ip_vrrp_tracking_top import IpVrrpTrackingTop  # noqa: E501
from swagger_server.models.ipv4_address_config import Ipv4AddressConfig  # noqa: E501
from swagger_server.models.ipv4_address_state import Ipv4AddressState  # noqa: E501
from swagger_server.models.ipv4_global_config import Ipv4GlobalConfig  # noqa: E501
from swagger_server.models.ipv4_neighbor_config import Ipv4NeighborConfig  # noqa: E501
from swagger_server.models.ipv4_neighbor_state import Ipv4NeighborState  # noqa: E501
from swagger_server.models.ipv4_proxy_arp_config import Ipv4ProxyArpConfig  # noqa: E501
from swagger_server.models.ipv6_address_config import Ipv6AddressConfig  # noqa: E501
from swagger_server.models.ipv6_address_state import Ipv6AddressState  # noqa: E501
from swagger_server.models.ipv6_global_config import Ipv6GlobalConfig  # noqa: E501
from swagger_server.models.ipv6_neighbor_config import Ipv6NeighborConfig  # noqa: E501
from swagger_server.models.ipv6_neighbor_state import Ipv6NeighborState  # noqa: E501
from swagger_server.models.ipv6_ra_config import Ipv6RaConfig  # noqa: E501
from swagger_server.models.match_schema import MatchSchema  # noqa: E501
from swagger_server.models.neighbor_schema import NeighborSchema  # noqa: E501
from swagger_server.models.neighbors_schema import NeighborsSchema  # noqa: E501
from swagger_server.models.proxy_arp_schema import ProxyArpSchema  # noqa: E501
from swagger_server.models.routed_vlan_schema import RoutedVlanSchema  # noqa: E501
from swagger_server.models.router_advertisement_schema import RouterAdvertisementSchema  # noqa: E501
from swagger_server.models.single_tagged_list_schema import SingleTaggedListSchema  # noqa: E501
from swagger_server.models.single_tagged_range_schema import SingleTaggedRangeSchema  # noqa: E501
from swagger_server.models.single_tagged_schema import SingleTaggedSchema  # noqa: E501
from swagger_server.models.sub_unnumbered_config import SubUnnumberedConfig  # noqa: E501
from swagger_server.models.sub_unnumbered_state import SubUnnumberedState  # noqa: E501
from swagger_server.models.sub_unnumbered_top import SubUnnumberedTop  # noqa: E501
from swagger_server.models.subinterface_schema import SubinterfaceSchema  # noqa: E501
from swagger_server.models.subinterfaces_config import SubinterfacesConfig  # noqa: E501
from swagger_server.models.subinterfaces_schema import SubinterfacesSchema  # noqa: E501
from swagger_server.models.subinterfaces_state import SubinterfacesState  # noqa: E501
from swagger_server.models.subinterfaces_top import SubinterfacesTop  # noqa: E501
from swagger_server.models.switched_vlan_schema import SwitchedVlanSchema  # noqa: E501
from swagger_server.models.vlan_logical_config import VlanLogicalConfig  # noqa: E501
from swagger_server.models.vlan_logical_double_tagged_config import VlanLogicalDoubleTaggedConfig  # noqa: E501
from swagger_server.models.vlan_logical_double_tagged_inner_list_config import VlanLogicalDoubleTaggedInnerListConfig  # noqa: E501
from swagger_server.models.vlan_logical_double_tagged_inner_outer_range_config import VlanLogicalDoubleTaggedInnerOuterRangeConfig  # noqa: E501
from swagger_server.models.vlan_logical_double_tagged_inner_range_config import VlanLogicalDoubleTaggedInnerRangeConfig  # noqa: E501
from swagger_server.models.vlan_logical_double_tagged_outer_list_config import VlanLogicalDoubleTaggedOuterListConfig  # noqa: E501
from swagger_server.models.vlan_logical_double_tagged_outer_range_config import VlanLogicalDoubleTaggedOuterRangeConfig  # noqa: E501
from swagger_server.models.vlan_logical_egress_mapping_config import VlanLogicalEgressMappingConfig  # noqa: E501
from swagger_server.models.vlan_logical_egress_mapping_top import VlanLogicalEgressMappingTop  # noqa: E501
from swagger_server.models.vlan_logical_ingress_mapping_config import VlanLogicalIngressMappingConfig  # noqa: E501
from swagger_server.models.vlan_logical_single_tagged_config import VlanLogicalSingleTaggedConfig  # noqa: E501
from swagger_server.models.vlan_logical_single_tagged_list_config import VlanLogicalSingleTaggedListConfig  # noqa: E501
from swagger_server.models.vlan_logical_single_tagged_range_config import VlanLogicalSingleTaggedRangeConfig  # noqa: E501
from swagger_server.models.vlan_logical_state import VlanLogicalState  # noqa: E501
from swagger_server.models.vlan_routed_config import VlanRoutedConfig  # noqa: E501
from swagger_server.models.vlan_routed_state import VlanRoutedState  # noqa: E501
from swagger_server.models.vlan_switched_config import VlanSwitchedConfig  # noqa: E501
from swagger_server.models.vlan_switched_state import VlanSwitchedState  # noqa: E501
from swagger_server.models.vrrp_schema import VrrpSchema  # noqa: E501
from swagger_server import util


def create_interfaces_by_id(interfaces):  # noqa: E501
    """Create interfaces by ID

    Create operation of resource: interfaces # noqa: E501

    :param interfaces: interfacesbody object
    :type interfaces: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        interfaces = InterfacesSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_aggregation_aggregation_by_id(name, aggregation):  # noqa: E501
    """Create aggregation by ID

    Create operation of resource: aggregation # noqa: E501

    :param name: ID of name
    :type name: str
    :param aggregation: aggregationbody object
    :type aggregation: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        aggregation = AggregationSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_aggregation_config_config_by_id(name, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = AggregationLogicalConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_aggregation_switched_vlan_config_config_by_id(name, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = VlanSwitchedConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_aggregation_switched_vlan_switched_vlan_by_id(name, switched_vlan):  # noqa: E501
    """Create switched-vlan by ID

    Create operation of resource: switched-vlan # noqa: E501

    :param name: ID of name
    :type name: str
    :param switched_vlan: switched-vlanbody object
    :type switched_vlan: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        switched_vlan = SwitchedVlanSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_config_config_by_id(name, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = InterfacePhysConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_ethernet_config_config_by_id(name, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = EthernetInterfaceConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_ethernet_ethernet_by_id(name, ethernet):  # noqa: E501
    """Create ethernet by ID

    Create operation of resource: ethernet # noqa: E501

    :param name: ID of name
    :type name: str
    :param ethernet: ethernetbody object
    :type ethernet: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        ethernet = EthernetSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_ethernet_switched_vlan_config_config_by_id(name, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = VlanSwitchedConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_ethernet_switched_vlan_switched_vlan_by_id(name, switched_vlan):  # noqa: E501
    """Create switched-vlan by ID

    Create operation of resource: switched-vlan # noqa: E501

    :param name: ID of name
    :type name: str
    :param switched_vlan: switched-vlanbody object
    :type switched_vlan: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        switched_vlan = SwitchedVlanSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_hold_time_config_config_by_id(name, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = InterfacePhysHoldtimeConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_hold_time_hold_time_by_id(name, hold_time):  # noqa: E501
    """Create hold-time by ID

    Create operation of resource: hold-time # noqa: E501

    :param name: ID of name
    :type name: str
    :param hold_time: hold-timebody object
    :type hold_time: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        hold_time = HoldTimeSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_interface_by_id(name, interface):  # noqa: E501
    """Create interface by ID

    Create operation of resource: interface # noqa: E501

    :param name: ID of name
    :type name: str
    :param interface: interfacebody object
    :type interface: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        interface = SubinterfacesTop.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_config_config_by_id(name, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = VlanRoutedConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_ipv4_addresses_address_address_by_id(name, ip, address):  # noqa: E501
    """Create address by ID

    Create operation of resource: address # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param address: addressbody object
    :type address: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        address = AddressSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_ipv4_addresses_address_config_config_by_id(name, ip, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = Ipv4AddressConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_ipv4_addresses_address_vrrp_vrrp_by_id(name, ip, vrrp):  # noqa: E501
    """Create vrrp by ID

    Create operation of resource: vrrp # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param vrrp: vrrpbody object
    :type vrrp: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        vrrp = VrrpSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_ipv4_addresses_address_vrrp_vrrp_group_config_config_by_id(name, ip, virtualRouterId, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = IpVrrpConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_ipv4_addresses_address_vrrp_vrrp_group_interface_tracking_config_config_by_id(name, ip, virtualRouterId, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = IpVrrpTrackingConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_ipv4_addresses_address_vrrp_vrrp_group_interface_tracking_interface_tracking_by_id(name, ip, virtualRouterId, interface_tracking):  # noqa: E501
    """Create interface-tracking by ID

    Create operation of resource: interface-tracking # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str
    :param interface_tracking: interface-trackingbody object
    :type interface_tracking: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        interface_tracking = InterfaceTrackingSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_ipv4_addresses_address_vrrp_vrrp_group_vrrp_group_by_id(name, ip, virtualRouterId, vrrp_group):  # noqa: E501
    """Create vrrp-group by ID

    Create operation of resource: vrrp-group # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str
    :param vrrp_group: vrrp-groupbody object
    :type vrrp_group: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        vrrp_group = IpVrrpTrackingTop.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_ipv4_addresses_addresses_by_id(name, addresses):  # noqa: E501
    """Create addresses by ID

    Create operation of resource: addresses # noqa: E501

    :param name: ID of name
    :type name: str
    :param addresses: addressesbody object
    :type addresses: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        addresses = AddressesSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_ipv4_config_config_by_id(name, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = Ipv4GlobalConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_ipv4_ipv4_by_id(name, ipv4):  # noqa: E501
    """Create ipv4 by ID

    Create operation of resource: ipv4 # noqa: E501

    :param name: ID of name
    :type name: str
    :param ipv4: ipv4body object
    :type ipv4: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        ipv4 = SubUnnumberedTop.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_ipv4_neighbors_neighbor_config_config_by_id(name, ip, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = Ipv4NeighborConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_ipv4_neighbors_neighbor_neighbor_by_id(name, ip, neighbor):  # noqa: E501
    """Create neighbor by ID

    Create operation of resource: neighbor # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param neighbor: neighborbody object
    :type neighbor: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        neighbor = NeighborSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_ipv4_neighbors_neighbors_by_id(name, neighbors):  # noqa: E501
    """Create neighbors by ID

    Create operation of resource: neighbors # noqa: E501

    :param name: ID of name
    :type name: str
    :param neighbors: neighborsbody object
    :type neighbors: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        neighbors = NeighborsSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_ipv4_proxy_arp_config_config_by_id(name, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = Ipv4ProxyArpConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_ipv4_proxy_arp_proxy_arp_by_id(name, proxy_arp):  # noqa: E501
    """Create proxy-arp by ID

    Create operation of resource: proxy-arp # noqa: E501

    :param name: ID of name
    :type name: str
    :param proxy_arp: proxy-arpbody object
    :type proxy_arp: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        proxy_arp = ProxyArpSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_ipv4_unnumbered_config_config_by_id(name, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = SubUnnumberedConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_ipv4_unnumbered_interface_ref_config_config_by_id(name, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = InterfaceRefCommon.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_ipv4_unnumbered_interface_ref_interface_ref_by_id(name, interface_ref):  # noqa: E501
    """Create interface-ref by ID

    Create operation of resource: interface-ref # noqa: E501

    :param name: ID of name
    :type name: str
    :param interface_ref: interface-refbody object
    :type interface_ref: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        interface_ref = InterfaceRefStateContainer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_ipv4_unnumbered_unnumbered_by_id(name, unnumbered):  # noqa: E501
    """Create unnumbered by ID

    Create operation of resource: unnumbered # noqa: E501

    :param name: ID of name
    :type name: str
    :param unnumbered: unnumberedbody object
    :type unnumbered: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        unnumbered = InterfaceRef.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_ipv6_addresses_address_address_by_id(name, ip, address):  # noqa: E501
    """Create address by ID

    Create operation of resource: address # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param address: addressbody object
    :type address: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        address = AddressSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_ipv6_addresses_address_config_config_by_id(name, ip, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = Ipv6AddressConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_ipv6_addresses_address_vrrp_vrrp_by_id(name, ip, vrrp):  # noqa: E501
    """Create vrrp by ID

    Create operation of resource: vrrp # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param vrrp: vrrpbody object
    :type vrrp: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        vrrp = VrrpSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_ipv6_addresses_address_vrrp_vrrp_group_config_config_by_id(name, ip, virtualRouterId, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = IpVrrpConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_ipv6_addresses_address_vrrp_vrrp_group_interface_tracking_config_config_by_id(name, ip, virtualRouterId, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = IpVrrpTrackingConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_ipv6_addresses_address_vrrp_vrrp_group_interface_tracking_interface_tracking_by_id(name, ip, virtualRouterId, interface_tracking):  # noqa: E501
    """Create interface-tracking by ID

    Create operation of resource: interface-tracking # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str
    :param interface_tracking: interface-trackingbody object
    :type interface_tracking: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        interface_tracking = InterfaceTrackingSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_ipv6_addresses_address_vrrp_vrrp_group_vrrp_group_by_id(name, ip, virtualRouterId, vrrp_group):  # noqa: E501
    """Create vrrp-group by ID

    Create operation of resource: vrrp-group # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str
    :param vrrp_group: vrrp-groupbody object
    :type vrrp_group: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        vrrp_group = IpVrrpTrackingTop.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_ipv6_addresses_addresses_by_id(name, addresses):  # noqa: E501
    """Create addresses by ID

    Create operation of resource: addresses # noqa: E501

    :param name: ID of name
    :type name: str
    :param addresses: addressesbody object
    :type addresses: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        addresses = AddressesSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_ipv6_config_config_by_id(name, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = Ipv6GlobalConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_ipv6_ipv6_by_id(name, ipv6):  # noqa: E501
    """Create ipv6 by ID

    Create operation of resource: ipv6 # noqa: E501

    :param name: ID of name
    :type name: str
    :param ipv6: ipv6body object
    :type ipv6: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        ipv6 = SubUnnumberedTop.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_ipv6_neighbors_neighbor_config_config_by_id(name, ip, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = Ipv6NeighborConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_ipv6_neighbors_neighbor_neighbor_by_id(name, ip, neighbor):  # noqa: E501
    """Create neighbor by ID

    Create operation of resource: neighbor # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param neighbor: neighborbody object
    :type neighbor: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        neighbor = NeighborSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_ipv6_neighbors_neighbors_by_id(name, neighbors):  # noqa: E501
    """Create neighbors by ID

    Create operation of resource: neighbors # noqa: E501

    :param name: ID of name
    :type name: str
    :param neighbors: neighborsbody object
    :type neighbors: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        neighbors = NeighborsSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_ipv6_router_advertisement_config_config_by_id(name, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = Ipv6RaConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_ipv6_router_advertisement_router_advertisement_by_id(name, router_advertisement):  # noqa: E501
    """Create router-advertisement by ID

    Create operation of resource: router-advertisement # noqa: E501

    :param name: ID of name
    :type name: str
    :param router_advertisement: router-advertisementbody object
    :type router_advertisement: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        router_advertisement = RouterAdvertisementSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_ipv6_unnumbered_config_config_by_id(name, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = SubUnnumberedConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_ipv6_unnumbered_interface_ref_config_config_by_id(name, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = InterfaceRefCommon.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_ipv6_unnumbered_interface_ref_interface_ref_by_id(name, interface_ref):  # noqa: E501
    """Create interface-ref by ID

    Create operation of resource: interface-ref # noqa: E501

    :param name: ID of name
    :type name: str
    :param interface_ref: interface-refbody object
    :type interface_ref: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        interface_ref = InterfaceRefStateContainer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_ipv6_unnumbered_unnumbered_by_id(name, unnumbered):  # noqa: E501
    """Create unnumbered by ID

    Create operation of resource: unnumbered # noqa: E501

    :param name: ID of name
    :type name: str
    :param unnumbered: unnumberedbody object
    :type unnumbered: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        unnumbered = InterfaceRef.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_routed_vlan_routed_vlan_by_id(name, routed_vlan):  # noqa: E501
    """Create routed-vlan by ID

    Create operation of resource: routed-vlan # noqa: E501

    :param name: ID of name
    :type name: str
    :param routed_vlan: routed-vlanbody object
    :type routed_vlan: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        routed_vlan = RoutedVlanSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_config_config_by_id(name, index, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = SubinterfacesConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_ipv4_addresses_address_address_by_id(name, index, ip, address):  # noqa: E501
    """Create address by ID

    Create operation of resource: address # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param address: addressbody object
    :type address: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        address = AddressSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_ipv4_addresses_address_config_config_by_id(name, index, ip, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = Ipv4AddressConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_ipv4_addresses_address_vrrp_vrrp_by_id(name, index, ip, vrrp):  # noqa: E501
    """Create vrrp by ID

    Create operation of resource: vrrp # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param vrrp: vrrpbody object
    :type vrrp: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        vrrp = VrrpSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_ipv4_addresses_address_vrrp_vrrp_group_config_config_by_id(name, index, ip, virtualRouterId, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = IpVrrpConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_ipv4_addresses_address_vrrp_vrrp_group_interface_tracking_config_config_by_id(name, index, ip, virtualRouterId, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = IpVrrpTrackingConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_ipv4_addresses_address_vrrp_vrrp_group_interface_tracking_interface_tracking_by_id(name, index, ip, virtualRouterId, interface_tracking):  # noqa: E501
    """Create interface-tracking by ID

    Create operation of resource: interface-tracking # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str
    :param interface_tracking: interface-trackingbody object
    :type interface_tracking: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        interface_tracking = InterfaceTrackingSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_ipv4_addresses_address_vrrp_vrrp_group_vrrp_group_by_id(name, index, ip, virtualRouterId, vrrp_group):  # noqa: E501
    """Create vrrp-group by ID

    Create operation of resource: vrrp-group # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str
    :param vrrp_group: vrrp-groupbody object
    :type vrrp_group: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        vrrp_group = IpVrrpTrackingTop.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_ipv4_addresses_addresses_by_id(name, index, addresses):  # noqa: E501
    """Create addresses by ID

    Create operation of resource: addresses # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param addresses: addressesbody object
    :type addresses: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        addresses = AddressesSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_ipv4_config_config_by_id(name, index, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = Ipv4GlobalConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_ipv4_ipv4_by_id(name, index, ipv4):  # noqa: E501
    """Create ipv4 by ID

    Create operation of resource: ipv4 # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ipv4: ipv4body object
    :type ipv4: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        ipv4 = SubUnnumberedTop.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_ipv4_neighbors_neighbor_config_config_by_id(name, index, ip, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = Ipv4NeighborConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_ipv4_neighbors_neighbor_neighbor_by_id(name, index, ip, neighbor):  # noqa: E501
    """Create neighbor by ID

    Create operation of resource: neighbor # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param neighbor: neighborbody object
    :type neighbor: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        neighbor = NeighborSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_ipv4_neighbors_neighbors_by_id(name, index, neighbors):  # noqa: E501
    """Create neighbors by ID

    Create operation of resource: neighbors # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param neighbors: neighborsbody object
    :type neighbors: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        neighbors = NeighborsSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_ipv4_proxy_arp_config_config_by_id(name, index, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = Ipv4ProxyArpConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_ipv4_proxy_arp_proxy_arp_by_id(name, index, proxy_arp):  # noqa: E501
    """Create proxy-arp by ID

    Create operation of resource: proxy-arp # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param proxy_arp: proxy-arpbody object
    :type proxy_arp: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        proxy_arp = ProxyArpSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_ipv4_unnumbered_config_config_by_id(name, index, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = SubUnnumberedConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_ipv4_unnumbered_interface_ref_config_config_by_id(name, index, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = InterfaceRefCommon.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_ipv4_unnumbered_interface_ref_interface_ref_by_id(name, index, interface_ref):  # noqa: E501
    """Create interface-ref by ID

    Create operation of resource: interface-ref # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param interface_ref: interface-refbody object
    :type interface_ref: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        interface_ref = InterfaceRefStateContainer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_ipv4_unnumbered_unnumbered_by_id(name, index, unnumbered):  # noqa: E501
    """Create unnumbered by ID

    Create operation of resource: unnumbered # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param unnumbered: unnumberedbody object
    :type unnumbered: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        unnumbered = InterfaceRef.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_ipv6_addresses_address_address_by_id(name, index, ip, address):  # noqa: E501
    """Create address by ID

    Create operation of resource: address # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param address: addressbody object
    :type address: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        address = AddressSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_ipv6_addresses_address_config_config_by_id(name, index, ip, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = Ipv6AddressConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_ipv6_addresses_address_vrrp_vrrp_by_id(name, index, ip, vrrp):  # noqa: E501
    """Create vrrp by ID

    Create operation of resource: vrrp # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param vrrp: vrrpbody object
    :type vrrp: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        vrrp = VrrpSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_ipv6_addresses_address_vrrp_vrrp_group_config_config_by_id(name, index, ip, virtualRouterId, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = IpVrrpConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_ipv6_addresses_address_vrrp_vrrp_group_interface_tracking_config_config_by_id(name, index, ip, virtualRouterId, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = IpVrrpTrackingConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_ipv6_addresses_address_vrrp_vrrp_group_interface_tracking_interface_tracking_by_id(name, index, ip, virtualRouterId, interface_tracking):  # noqa: E501
    """Create interface-tracking by ID

    Create operation of resource: interface-tracking # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str
    :param interface_tracking: interface-trackingbody object
    :type interface_tracking: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        interface_tracking = InterfaceTrackingSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_ipv6_addresses_address_vrrp_vrrp_group_vrrp_group_by_id(name, index, ip, virtualRouterId, vrrp_group):  # noqa: E501
    """Create vrrp-group by ID

    Create operation of resource: vrrp-group # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str
    :param vrrp_group: vrrp-groupbody object
    :type vrrp_group: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        vrrp_group = IpVrrpTrackingTop.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_ipv6_addresses_addresses_by_id(name, index, addresses):  # noqa: E501
    """Create addresses by ID

    Create operation of resource: addresses # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param addresses: addressesbody object
    :type addresses: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        addresses = AddressesSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_ipv6_config_config_by_id(name, index, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = Ipv6GlobalConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_ipv6_ipv6_by_id(name, index, ipv6):  # noqa: E501
    """Create ipv6 by ID

    Create operation of resource: ipv6 # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ipv6: ipv6body object
    :type ipv6: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        ipv6 = SubUnnumberedTop.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_ipv6_neighbors_neighbor_config_config_by_id(name, index, ip, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = Ipv6NeighborConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_ipv6_neighbors_neighbor_neighbor_by_id(name, index, ip, neighbor):  # noqa: E501
    """Create neighbor by ID

    Create operation of resource: neighbor # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param neighbor: neighborbody object
    :type neighbor: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        neighbor = NeighborSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_ipv6_neighbors_neighbors_by_id(name, index, neighbors):  # noqa: E501
    """Create neighbors by ID

    Create operation of resource: neighbors # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param neighbors: neighborsbody object
    :type neighbors: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        neighbors = NeighborsSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_ipv6_router_advertisement_config_config_by_id(name, index, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = Ipv6RaConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_ipv6_router_advertisement_router_advertisement_by_id(name, index, router_advertisement):  # noqa: E501
    """Create router-advertisement by ID

    Create operation of resource: router-advertisement # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param router_advertisement: router-advertisementbody object
    :type router_advertisement: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        router_advertisement = RouterAdvertisementSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_ipv6_unnumbered_config_config_by_id(name, index, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = SubUnnumberedConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_ipv6_unnumbered_interface_ref_config_config_by_id(name, index, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = InterfaceRefCommon.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_ipv6_unnumbered_interface_ref_interface_ref_by_id(name, index, interface_ref):  # noqa: E501
    """Create interface-ref by ID

    Create operation of resource: interface-ref # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param interface_ref: interface-refbody object
    :type interface_ref: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        interface_ref = InterfaceRefStateContainer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_ipv6_unnumbered_unnumbered_by_id(name, index, unnumbered):  # noqa: E501
    """Create unnumbered by ID

    Create operation of resource: unnumbered # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param unnumbered: unnumberedbody object
    :type unnumbered: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        unnumbered = InterfaceRef.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_subinterface_by_id(name, index, subinterface):  # noqa: E501
    """Create subinterface by ID

    Create operation of resource: subinterface # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param subinterface: subinterfacebody object
    :type subinterface: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        subinterface = SubinterfaceSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_vlan_config_config_by_id(name, index, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = VlanLogicalConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_vlan_egress_mapping_config_config_by_id(name, index, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = VlanLogicalEgressMappingConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_vlan_egress_mapping_egress_mapping_by_id(name, index, egress_mapping):  # noqa: E501
    """Create egress-mapping by ID

    Create operation of resource: egress-mapping # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param egress_mapping: egress-mappingbody object
    :type egress_mapping: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        egress_mapping = EgressMappingSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_vlan_ingress_mapping_config_config_by_id(name, index, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = VlanLogicalIngressMappingConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_vlan_ingress_mapping_ingress_mapping_by_id(name, index, ingress_mapping):  # noqa: E501
    """Create ingress-mapping by ID

    Create operation of resource: ingress-mapping # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ingress_mapping: ingress-mappingbody object
    :type ingress_mapping: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        ingress_mapping = IngressMappingSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_config_config_by_id(name, index, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = VlanLogicalDoubleTaggedConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_double_tagged_by_id(name, index, double_tagged):  # noqa: E501
    """Create double-tagged by ID

    Create operation of resource: double-tagged # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param double_tagged: double-taggedbody object
    :type double_tagged: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        double_tagged = DoubleTaggedSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_inner_list_config_config_by_id(name, index, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = VlanLogicalDoubleTaggedInnerListConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_inner_list_double_tagged_inner_list_by_id(name, index, double_tagged_inner_list):  # noqa: E501
    """Create double-tagged-inner-list by ID

    Create operation of resource: double-tagged-inner-list # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param double_tagged_inner_list: double-tagged-inner-listbody object
    :type double_tagged_inner_list: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        double_tagged_inner_list = DoubleTaggedInnerListSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_inner_outer_range_config_config_by_id(name, index, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = VlanLogicalDoubleTaggedInnerOuterRangeConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_inner_outer_range_double_tagged_inner_outer_range_by_id(name, index, double_tagged_inner_outer_range):  # noqa: E501
    """Create double-tagged-inner-outer-range by ID

    Create operation of resource: double-tagged-inner-outer-range # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param double_tagged_inner_outer_range: double-tagged-inner-outer-rangebody object
    :type double_tagged_inner_outer_range: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        double_tagged_inner_outer_range = DoubleTaggedInnerOuterRangeSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_inner_range_config_config_by_id(name, index, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = VlanLogicalDoubleTaggedInnerRangeConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_inner_range_double_tagged_inner_range_by_id(name, index, double_tagged_inner_range):  # noqa: E501
    """Create double-tagged-inner-range by ID

    Create operation of resource: double-tagged-inner-range # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param double_tagged_inner_range: double-tagged-inner-rangebody object
    :type double_tagged_inner_range: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        double_tagged_inner_range = DoubleTaggedInnerRangeSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_outer_list_config_config_by_id(name, index, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = VlanLogicalDoubleTaggedOuterListConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_outer_list_double_tagged_outer_list_by_id(name, index, double_tagged_outer_list):  # noqa: E501
    """Create double-tagged-outer-list by ID

    Create operation of resource: double-tagged-outer-list # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param double_tagged_outer_list: double-tagged-outer-listbody object
    :type double_tagged_outer_list: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        double_tagged_outer_list = DoubleTaggedOuterListSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_outer_range_config_config_by_id(name, index, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = VlanLogicalDoubleTaggedOuterRangeConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_outer_range_double_tagged_outer_range_by_id(name, index, double_tagged_outer_range):  # noqa: E501
    """Create double-tagged-outer-range by ID

    Create operation of resource: double-tagged-outer-range # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param double_tagged_outer_range: double-tagged-outer-rangebody object
    :type double_tagged_outer_range: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        double_tagged_outer_range = DoubleTaggedOuterRangeSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_vlan_match_match_by_id(name, index, match):  # noqa: E501
    """Create match by ID

    Create operation of resource: match # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param match: matchbody object
    :type match: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        match = MatchSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_vlan_match_single_tagged_config_config_by_id(name, index, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = VlanLogicalSingleTaggedConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_vlan_match_single_tagged_list_config_config_by_id(name, index, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = VlanLogicalSingleTaggedListConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_vlan_match_single_tagged_list_single_tagged_list_by_id(name, index, single_tagged_list):  # noqa: E501
    """Create single-tagged-list by ID

    Create operation of resource: single-tagged-list # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param single_tagged_list: single-tagged-listbody object
    :type single_tagged_list: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        single_tagged_list = SingleTaggedListSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_vlan_match_single_tagged_range_config_config_by_id(name, index, config):  # noqa: E501
    """Create config by ID

    Create operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = VlanLogicalSingleTaggedRangeConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_vlan_match_single_tagged_range_single_tagged_range_by_id(name, index, single_tagged_range):  # noqa: E501
    """Create single-tagged-range by ID

    Create operation of resource: single-tagged-range # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param single_tagged_range: single-tagged-rangebody object
    :type single_tagged_range: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        single_tagged_range = SingleTaggedRangeSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_vlan_match_single_tagged_single_tagged_by_id(name, index, single_tagged):  # noqa: E501
    """Create single-tagged by ID

    Create operation of resource: single-tagged # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param single_tagged: single-taggedbody object
    :type single_tagged: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        single_tagged = SingleTaggedSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterface_vlan_vlan_by_id(name, index, vlan):  # noqa: E501
    """Create vlan by ID

    Create operation of resource: vlan # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param vlan: vlanbody object
    :type vlan: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        vlan = VlanLogicalEgressMappingTop.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_interfaces_interface_subinterfaces_subinterfaces_by_id(name, subinterfaces):  # noqa: E501
    """Create subinterfaces by ID

    Create operation of resource: subinterfaces # noqa: E501

    :param name: ID of name
    :type name: str
    :param subinterfaces: subinterfacesbody object
    :type subinterfaces: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        subinterfaces = SubinterfacesSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_interfaces_by_id():  # noqa: E501
    """Delete interfaces by ID

    Delete operation of resource: interfaces # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_aggregation_aggregation_by_id(name):  # noqa: E501
    """Delete aggregation by ID

    Delete operation of resource: aggregation # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_aggregation_config_config_by_id(name):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_aggregation_switched_vlan_config_config_by_id(name):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_aggregation_switched_vlan_switched_vlan_by_id(name):  # noqa: E501
    """Delete switched-vlan by ID

    Delete operation of resource: switched-vlan # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_config_config_by_id(name):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_ethernet_config_config_by_id(name):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_ethernet_ethernet_by_id(name):  # noqa: E501
    """Delete ethernet by ID

    Delete operation of resource: ethernet # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_ethernet_switched_vlan_config_config_by_id(name):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_ethernet_switched_vlan_switched_vlan_by_id(name):  # noqa: E501
    """Delete switched-vlan by ID

    Delete operation of resource: switched-vlan # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_hold_time_config_config_by_id(name):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_hold_time_hold_time_by_id(name):  # noqa: E501
    """Delete hold-time by ID

    Delete operation of resource: hold-time # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_interface_by_id(name):  # noqa: E501
    """Delete interface by ID

    Delete operation of resource: interface # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_config_config_by_id(name):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_ipv4_addresses_address_address_by_id(name, ip):  # noqa: E501
    """Delete address by ID

    Delete operation of resource: address # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_ipv4_addresses_address_config_config_by_id(name, ip):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_ipv4_addresses_address_vrrp_vrrp_by_id(name, ip):  # noqa: E501
    """Delete vrrp by ID

    Delete operation of resource: vrrp # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_ipv4_addresses_address_vrrp_vrrp_group_config_config_by_id(name, ip, virtualRouterId):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_ipv4_addresses_address_vrrp_vrrp_group_interface_tracking_config_config_by_id(name, ip, virtualRouterId):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_ipv4_addresses_address_vrrp_vrrp_group_interface_tracking_interface_tracking_by_id(name, ip, virtualRouterId):  # noqa: E501
    """Delete interface-tracking by ID

    Delete operation of resource: interface-tracking # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_ipv4_addresses_address_vrrp_vrrp_group_vrrp_group_by_id(name, ip, virtualRouterId):  # noqa: E501
    """Delete vrrp-group by ID

    Delete operation of resource: vrrp-group # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_ipv4_addresses_addresses_by_id(name):  # noqa: E501
    """Delete addresses by ID

    Delete operation of resource: addresses # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_ipv4_config_config_by_id(name):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_ipv4_ipv4_by_id(name):  # noqa: E501
    """Delete ipv4 by ID

    Delete operation of resource: ipv4 # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_ipv4_neighbors_neighbor_config_config_by_id(name, ip):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_ipv4_neighbors_neighbor_neighbor_by_id(name, ip):  # noqa: E501
    """Delete neighbor by ID

    Delete operation of resource: neighbor # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_ipv4_neighbors_neighbors_by_id(name):  # noqa: E501
    """Delete neighbors by ID

    Delete operation of resource: neighbors # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_ipv4_proxy_arp_config_config_by_id(name):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_ipv4_proxy_arp_proxy_arp_by_id(name):  # noqa: E501
    """Delete proxy-arp by ID

    Delete operation of resource: proxy-arp # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_ipv4_unnumbered_config_config_by_id(name):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_ipv4_unnumbered_interface_ref_config_config_by_id(name):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_ipv4_unnumbered_interface_ref_interface_ref_by_id(name):  # noqa: E501
    """Delete interface-ref by ID

    Delete operation of resource: interface-ref # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_ipv4_unnumbered_unnumbered_by_id(name):  # noqa: E501
    """Delete unnumbered by ID

    Delete operation of resource: unnumbered # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_ipv6_addresses_address_address_by_id(name, ip):  # noqa: E501
    """Delete address by ID

    Delete operation of resource: address # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_ipv6_addresses_address_config_config_by_id(name, ip):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_ipv6_addresses_address_vrrp_vrrp_by_id(name, ip):  # noqa: E501
    """Delete vrrp by ID

    Delete operation of resource: vrrp # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_ipv6_addresses_address_vrrp_vrrp_group_config_config_by_id(name, ip, virtualRouterId):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_ipv6_addresses_address_vrrp_vrrp_group_interface_tracking_config_config_by_id(name, ip, virtualRouterId):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_ipv6_addresses_address_vrrp_vrrp_group_interface_tracking_interface_tracking_by_id(name, ip, virtualRouterId):  # noqa: E501
    """Delete interface-tracking by ID

    Delete operation of resource: interface-tracking # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_ipv6_addresses_address_vrrp_vrrp_group_vrrp_group_by_id(name, ip, virtualRouterId):  # noqa: E501
    """Delete vrrp-group by ID

    Delete operation of resource: vrrp-group # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_ipv6_addresses_addresses_by_id(name):  # noqa: E501
    """Delete addresses by ID

    Delete operation of resource: addresses # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_ipv6_config_config_by_id(name):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_ipv6_ipv6_by_id(name):  # noqa: E501
    """Delete ipv6 by ID

    Delete operation of resource: ipv6 # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_ipv6_neighbors_neighbor_config_config_by_id(name, ip):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_ipv6_neighbors_neighbor_neighbor_by_id(name, ip):  # noqa: E501
    """Delete neighbor by ID

    Delete operation of resource: neighbor # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_ipv6_neighbors_neighbors_by_id(name):  # noqa: E501
    """Delete neighbors by ID

    Delete operation of resource: neighbors # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_ipv6_router_advertisement_config_config_by_id(name):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_ipv6_router_advertisement_router_advertisement_by_id(name):  # noqa: E501
    """Delete router-advertisement by ID

    Delete operation of resource: router-advertisement # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_ipv6_unnumbered_config_config_by_id(name):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_ipv6_unnumbered_interface_ref_config_config_by_id(name):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_ipv6_unnumbered_interface_ref_interface_ref_by_id(name):  # noqa: E501
    """Delete interface-ref by ID

    Delete operation of resource: interface-ref # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_ipv6_unnumbered_unnumbered_by_id(name):  # noqa: E501
    """Delete unnumbered by ID

    Delete operation of resource: unnumbered # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_routed_vlan_routed_vlan_by_id(name):  # noqa: E501
    """Delete routed-vlan by ID

    Delete operation of resource: routed-vlan # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_config_config_by_id(name, index):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_ipv4_addresses_address_address_by_id(name, index, ip):  # noqa: E501
    """Delete address by ID

    Delete operation of resource: address # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_ipv4_addresses_address_config_config_by_id(name, index, ip):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_ipv4_addresses_address_vrrp_vrrp_by_id(name, index, ip):  # noqa: E501
    """Delete vrrp by ID

    Delete operation of resource: vrrp # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_ipv4_addresses_address_vrrp_vrrp_group_config_config_by_id(name, index, ip, virtualRouterId):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_ipv4_addresses_address_vrrp_vrrp_group_interface_tracking_config_config_by_id(name, index, ip, virtualRouterId):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_ipv4_addresses_address_vrrp_vrrp_group_interface_tracking_interface_tracking_by_id(name, index, ip, virtualRouterId):  # noqa: E501
    """Delete interface-tracking by ID

    Delete operation of resource: interface-tracking # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_ipv4_addresses_address_vrrp_vrrp_group_vrrp_group_by_id(name, index, ip, virtualRouterId):  # noqa: E501
    """Delete vrrp-group by ID

    Delete operation of resource: vrrp-group # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_ipv4_addresses_addresses_by_id(name, index):  # noqa: E501
    """Delete addresses by ID

    Delete operation of resource: addresses # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_ipv4_config_config_by_id(name, index):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_ipv4_ipv4_by_id(name, index):  # noqa: E501
    """Delete ipv4 by ID

    Delete operation of resource: ipv4 # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_ipv4_neighbors_neighbor_config_config_by_id(name, index, ip):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_ipv4_neighbors_neighbor_neighbor_by_id(name, index, ip):  # noqa: E501
    """Delete neighbor by ID

    Delete operation of resource: neighbor # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_ipv4_neighbors_neighbors_by_id(name, index):  # noqa: E501
    """Delete neighbors by ID

    Delete operation of resource: neighbors # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_ipv4_proxy_arp_config_config_by_id(name, index):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_ipv4_proxy_arp_proxy_arp_by_id(name, index):  # noqa: E501
    """Delete proxy-arp by ID

    Delete operation of resource: proxy-arp # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_ipv4_unnumbered_config_config_by_id(name, index):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_ipv4_unnumbered_interface_ref_config_config_by_id(name, index):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_ipv4_unnumbered_interface_ref_interface_ref_by_id(name, index):  # noqa: E501
    """Delete interface-ref by ID

    Delete operation of resource: interface-ref # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_ipv4_unnumbered_unnumbered_by_id(name, index):  # noqa: E501
    """Delete unnumbered by ID

    Delete operation of resource: unnumbered # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_ipv6_addresses_address_address_by_id(name, index, ip):  # noqa: E501
    """Delete address by ID

    Delete operation of resource: address # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_ipv6_addresses_address_config_config_by_id(name, index, ip):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_ipv6_addresses_address_vrrp_vrrp_by_id(name, index, ip):  # noqa: E501
    """Delete vrrp by ID

    Delete operation of resource: vrrp # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_ipv6_addresses_address_vrrp_vrrp_group_config_config_by_id(name, index, ip, virtualRouterId):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_ipv6_addresses_address_vrrp_vrrp_group_interface_tracking_config_config_by_id(name, index, ip, virtualRouterId):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_ipv6_addresses_address_vrrp_vrrp_group_interface_tracking_interface_tracking_by_id(name, index, ip, virtualRouterId):  # noqa: E501
    """Delete interface-tracking by ID

    Delete operation of resource: interface-tracking # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_ipv6_addresses_address_vrrp_vrrp_group_vrrp_group_by_id(name, index, ip, virtualRouterId):  # noqa: E501
    """Delete vrrp-group by ID

    Delete operation of resource: vrrp-group # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_ipv6_addresses_addresses_by_id(name, index):  # noqa: E501
    """Delete addresses by ID

    Delete operation of resource: addresses # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_ipv6_config_config_by_id(name, index):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_ipv6_ipv6_by_id(name, index):  # noqa: E501
    """Delete ipv6 by ID

    Delete operation of resource: ipv6 # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_ipv6_neighbors_neighbor_config_config_by_id(name, index, ip):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_ipv6_neighbors_neighbor_neighbor_by_id(name, index, ip):  # noqa: E501
    """Delete neighbor by ID

    Delete operation of resource: neighbor # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_ipv6_neighbors_neighbors_by_id(name, index):  # noqa: E501
    """Delete neighbors by ID

    Delete operation of resource: neighbors # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_ipv6_router_advertisement_config_config_by_id(name, index):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_ipv6_router_advertisement_router_advertisement_by_id(name, index):  # noqa: E501
    """Delete router-advertisement by ID

    Delete operation of resource: router-advertisement # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_ipv6_unnumbered_config_config_by_id(name, index):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_ipv6_unnumbered_interface_ref_config_config_by_id(name, index):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_ipv6_unnumbered_interface_ref_interface_ref_by_id(name, index):  # noqa: E501
    """Delete interface-ref by ID

    Delete operation of resource: interface-ref # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_ipv6_unnumbered_unnumbered_by_id(name, index):  # noqa: E501
    """Delete unnumbered by ID

    Delete operation of resource: unnumbered # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_subinterface_by_id(name, index):  # noqa: E501
    """Delete subinterface by ID

    Delete operation of resource: subinterface # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_vlan_config_config_by_id(name, index):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_vlan_egress_mapping_config_config_by_id(name, index):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_vlan_egress_mapping_egress_mapping_by_id(name, index):  # noqa: E501
    """Delete egress-mapping by ID

    Delete operation of resource: egress-mapping # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_vlan_ingress_mapping_config_config_by_id(name, index):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_vlan_ingress_mapping_ingress_mapping_by_id(name, index):  # noqa: E501
    """Delete ingress-mapping by ID

    Delete operation of resource: ingress-mapping # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_config_config_by_id(name, index):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_double_tagged_by_id(name, index):  # noqa: E501
    """Delete double-tagged by ID

    Delete operation of resource: double-tagged # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_inner_list_config_config_by_id(name, index):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_inner_list_double_tagged_inner_list_by_id(name, index):  # noqa: E501
    """Delete double-tagged-inner-list by ID

    Delete operation of resource: double-tagged-inner-list # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_inner_outer_range_config_config_by_id(name, index):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_inner_outer_range_double_tagged_inner_outer_range_by_id(name, index):  # noqa: E501
    """Delete double-tagged-inner-outer-range by ID

    Delete operation of resource: double-tagged-inner-outer-range # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_inner_range_config_config_by_id(name, index):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_inner_range_double_tagged_inner_range_by_id(name, index):  # noqa: E501
    """Delete double-tagged-inner-range by ID

    Delete operation of resource: double-tagged-inner-range # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_outer_list_config_config_by_id(name, index):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_outer_list_double_tagged_outer_list_by_id(name, index):  # noqa: E501
    """Delete double-tagged-outer-list by ID

    Delete operation of resource: double-tagged-outer-list # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_outer_range_config_config_by_id(name, index):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_outer_range_double_tagged_outer_range_by_id(name, index):  # noqa: E501
    """Delete double-tagged-outer-range by ID

    Delete operation of resource: double-tagged-outer-range # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_vlan_match_match_by_id(name, index):  # noqa: E501
    """Delete match by ID

    Delete operation of resource: match # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_vlan_match_single_tagged_config_config_by_id(name, index):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_vlan_match_single_tagged_list_config_config_by_id(name, index):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_vlan_match_single_tagged_list_single_tagged_list_by_id(name, index):  # noqa: E501
    """Delete single-tagged-list by ID

    Delete operation of resource: single-tagged-list # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_vlan_match_single_tagged_range_config_config_by_id(name, index):  # noqa: E501
    """Delete config by ID

    Delete operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_vlan_match_single_tagged_range_single_tagged_range_by_id(name, index):  # noqa: E501
    """Delete single-tagged-range by ID

    Delete operation of resource: single-tagged-range # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_vlan_match_single_tagged_single_tagged_by_id(name, index):  # noqa: E501
    """Delete single-tagged by ID

    Delete operation of resource: single-tagged # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterface_vlan_vlan_by_id(name, index):  # noqa: E501
    """Delete vlan by ID

    Delete operation of resource: vlan # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: None
    """
    return 'do some magic!'


def delete_interfaces_interface_subinterfaces_subinterfaces_by_id(name):  # noqa: E501
    """Delete subinterfaces by ID

    Delete operation of resource: subinterfaces # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def retrieve_interfaces():  # noqa: E501
    """Retrieve interfaces

    Retrieve operation of resource: interfaces # noqa: E501


    :rtype: InterfacesSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_aggregation_aggregation_by_id(name):  # noqa: E501
    """Retrieve aggregation by ID

    Retrieve operation of resource: aggregation # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: AggregationSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_aggregation_config_config_by_id(name):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: AggregationLogicalConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_aggregation_state_state_by_id(name):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: AggregationLogicalState
    """
    return 'do some magic!'


def retrieve_interfaces_interface_aggregation_switched_vlan_config_config_by_id(name):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: VlanSwitchedConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_aggregation_switched_vlan_state_state_by_id(name):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: VlanSwitchedState
    """
    return 'do some magic!'


def retrieve_interfaces_interface_aggregation_switched_vlan_switched_vlan_by_id(name):  # noqa: E501
    """Retrieve switched-vlan by ID

    Retrieve operation of resource: switched-vlan # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: SwitchedVlanSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_config_config_by_id(name):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: InterfacePhysConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_ethernet_config_config_by_id(name):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: EthernetInterfaceConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_ethernet_ethernet_by_id(name):  # noqa: E501
    """Retrieve ethernet by ID

    Retrieve operation of resource: ethernet # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: EthernetSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_ethernet_state_counters_counters_by_id(name):  # noqa: E501
    """Retrieve counters by ID

    Retrieve operation of resource: counters # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: EthernetInterfaceStateCounters
    """
    return 'do some magic!'


def retrieve_interfaces_interface_ethernet_state_state_by_id(name):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: EthernetInterfaceState
    """
    return 'do some magic!'


def retrieve_interfaces_interface_ethernet_switched_vlan_config_config_by_id(name):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: VlanSwitchedConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_ethernet_switched_vlan_state_state_by_id(name):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: VlanSwitchedState
    """
    return 'do some magic!'


def retrieve_interfaces_interface_ethernet_switched_vlan_switched_vlan_by_id(name):  # noqa: E501
    """Retrieve switched-vlan by ID

    Retrieve operation of resource: switched-vlan # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: SwitchedVlanSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_hold_time_config_config_by_id(name):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: InterfacePhysHoldtimeConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_hold_time_hold_time_by_id(name):  # noqa: E501
    """Retrieve hold-time by ID

    Retrieve operation of resource: hold-time # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: HoldTimeSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_hold_time_state_state_by_id(name):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: InterfacePhysHoldtimeState
    """
    return 'do some magic!'


def retrieve_interfaces_interface_interface_by_id(name):  # noqa: E501
    """Retrieve interface by ID

    Retrieve operation of resource: interface # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: SubinterfacesTop
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_config_config_by_id(name):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: VlanRoutedConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv4_addresses_address_address_by_id(name, ip):  # noqa: E501
    """Retrieve address by ID

    Retrieve operation of resource: address # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str

    :rtype: AddressSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv4_addresses_address_config_config_by_id(name, ip):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str

    :rtype: Ipv4AddressConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv4_addresses_address_state_state_by_id(name, ip):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str

    :rtype: Ipv4AddressState
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv4_addresses_address_vrrp_vrrp_by_id(name, ip):  # noqa: E501
    """Retrieve vrrp by ID

    Retrieve operation of resource: vrrp # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str

    :rtype: VrrpSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv4_addresses_address_vrrp_vrrp_group_config_config_by_id(name, ip, virtualRouterId):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: IpVrrpConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv4_addresses_address_vrrp_vrrp_group_interface_tracking_config_config_by_id(name, ip, virtualRouterId):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: IpVrrpTrackingConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv4_addresses_address_vrrp_vrrp_group_interface_tracking_interface_tracking_by_id(name, ip, virtualRouterId):  # noqa: E501
    """Retrieve interface-tracking by ID

    Retrieve operation of resource: interface-tracking # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: InterfaceTrackingSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv4_addresses_address_vrrp_vrrp_group_interface_tracking_state_state_by_id(name, ip, virtualRouterId):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: IpVrrpTrackingState
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv4_addresses_address_vrrp_vrrp_group_state_state_by_id(name, ip, virtualRouterId):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: IpVrrpState
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv4_addresses_address_vrrp_vrrp_group_vrrp_group_by_id(name, ip, virtualRouterId):  # noqa: E501
    """Retrieve vrrp-group by ID

    Retrieve operation of resource: vrrp-group # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: IpVrrpTrackingTop
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv4_addresses_addresses_by_id(name):  # noqa: E501
    """Retrieve addresses by ID

    Retrieve operation of resource: addresses # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: AddressesSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv4_config_config_by_id(name):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: Ipv4GlobalConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv4_ipv4_by_id(name):  # noqa: E501
    """Retrieve ipv4 by ID

    Retrieve operation of resource: ipv4 # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: SubUnnumberedTop
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv4_neighbors_neighbor_config_config_by_id(name, ip):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str

    :rtype: Ipv4NeighborConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv4_neighbors_neighbor_neighbor_by_id(name, ip):  # noqa: E501
    """Retrieve neighbor by ID

    Retrieve operation of resource: neighbor # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str

    :rtype: NeighborSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv4_neighbors_neighbor_state_state_by_id(name, ip):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str

    :rtype: Ipv4NeighborState
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv4_neighbors_neighbors_by_id(name):  # noqa: E501
    """Retrieve neighbors by ID

    Retrieve operation of resource: neighbors # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: NeighborsSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv4_proxy_arp_config_config_by_id(name):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: Ipv4ProxyArpConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv4_proxy_arp_proxy_arp_by_id(name):  # noqa: E501
    """Retrieve proxy-arp by ID

    Retrieve operation of resource: proxy-arp # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: ProxyArpSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv4_proxy_arp_state_state_by_id(name):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: Ipv4ProxyArpConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv4_state_counters_counters_by_id(name):  # noqa: E501
    """Retrieve counters by ID

    Retrieve operation of resource: counters # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: CountersSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv4_state_state_by_id(name):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: IpCommonCountersState
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv4_unnumbered_config_config_by_id(name):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: SubUnnumberedConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv4_unnumbered_interface_ref_config_config_by_id(name):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: InterfaceRefCommon
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv4_unnumbered_interface_ref_interface_ref_by_id(name):  # noqa: E501
    """Retrieve interface-ref by ID

    Retrieve operation of resource: interface-ref # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: InterfaceRefStateContainer
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv4_unnumbered_interface_ref_state_state_by_id(name):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: InterfaceRefCommon
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv4_unnumbered_state_state_by_id(name):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: SubUnnumberedState
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv4_unnumbered_unnumbered_by_id(name):  # noqa: E501
    """Retrieve unnumbered by ID

    Retrieve operation of resource: unnumbered # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: InterfaceRef
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv6_addresses_address_address_by_id(name, ip):  # noqa: E501
    """Retrieve address by ID

    Retrieve operation of resource: address # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str

    :rtype: AddressSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv6_addresses_address_config_config_by_id(name, ip):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str

    :rtype: Ipv6AddressConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv6_addresses_address_state_state_by_id(name, ip):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str

    :rtype: Ipv6AddressState
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv6_addresses_address_vrrp_vrrp_by_id(name, ip):  # noqa: E501
    """Retrieve vrrp by ID

    Retrieve operation of resource: vrrp # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str

    :rtype: VrrpSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv6_addresses_address_vrrp_vrrp_group_config_config_by_id(name, ip, virtualRouterId):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: IpVrrpConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv6_addresses_address_vrrp_vrrp_group_interface_tracking_config_config_by_id(name, ip, virtualRouterId):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: IpVrrpTrackingConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv6_addresses_address_vrrp_vrrp_group_interface_tracking_interface_tracking_by_id(name, ip, virtualRouterId):  # noqa: E501
    """Retrieve interface-tracking by ID

    Retrieve operation of resource: interface-tracking # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: InterfaceTrackingSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv6_addresses_address_vrrp_vrrp_group_interface_tracking_state_state_by_id(name, ip, virtualRouterId):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: IpVrrpTrackingState
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv6_addresses_address_vrrp_vrrp_group_state_state_by_id(name, ip, virtualRouterId):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: IpVrrpState
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv6_addresses_address_vrrp_vrrp_group_vrrp_group_by_id(name, ip, virtualRouterId):  # noqa: E501
    """Retrieve vrrp-group by ID

    Retrieve operation of resource: vrrp-group # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: IpVrrpTrackingTop
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv6_addresses_addresses_by_id(name):  # noqa: E501
    """Retrieve addresses by ID

    Retrieve operation of resource: addresses # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: AddressesSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv6_config_config_by_id(name):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: Ipv6GlobalConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv6_ipv6_by_id(name):  # noqa: E501
    """Retrieve ipv6 by ID

    Retrieve operation of resource: ipv6 # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: SubUnnumberedTop
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv6_neighbors_neighbor_config_config_by_id(name, ip):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str

    :rtype: Ipv6NeighborConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv6_neighbors_neighbor_neighbor_by_id(name, ip):  # noqa: E501
    """Retrieve neighbor by ID

    Retrieve operation of resource: neighbor # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str

    :rtype: NeighborSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv6_neighbors_neighbor_state_state_by_id(name, ip):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str

    :rtype: Ipv6NeighborState
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv6_neighbors_neighbors_by_id(name):  # noqa: E501
    """Retrieve neighbors by ID

    Retrieve operation of resource: neighbors # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: NeighborsSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv6_router_advertisement_config_config_by_id(name):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: Ipv6RaConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv6_router_advertisement_router_advertisement_by_id(name):  # noqa: E501
    """Retrieve router-advertisement by ID

    Retrieve operation of resource: router-advertisement # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: RouterAdvertisementSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv6_router_advertisement_state_state_by_id(name):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: Ipv6RaConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv6_state_counters_counters_by_id(name):  # noqa: E501
    """Retrieve counters by ID

    Retrieve operation of resource: counters # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: CountersSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv6_state_state_by_id(name):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: IpCommonCountersState
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv6_unnumbered_config_config_by_id(name):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: SubUnnumberedConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv6_unnumbered_interface_ref_config_config_by_id(name):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: InterfaceRefCommon
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv6_unnumbered_interface_ref_interface_ref_by_id(name):  # noqa: E501
    """Retrieve interface-ref by ID

    Retrieve operation of resource: interface-ref # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: InterfaceRefStateContainer
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv6_unnumbered_interface_ref_state_state_by_id(name):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: InterfaceRefCommon
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv6_unnumbered_state_state_by_id(name):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: SubUnnumberedState
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_ipv6_unnumbered_unnumbered_by_id(name):  # noqa: E501
    """Retrieve unnumbered by ID

    Retrieve operation of resource: unnumbered # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: InterfaceRef
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_routed_vlan_by_id(name):  # noqa: E501
    """Retrieve routed-vlan by ID

    Retrieve operation of resource: routed-vlan # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: RoutedVlanSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_routed_vlan_state_state_by_id(name):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: VlanRoutedState
    """
    return 'do some magic!'


def retrieve_interfaces_interface_state_counters_counters_by_id(name):  # noqa: E501
    """Retrieve counters by ID

    Retrieve operation of resource: counters # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: CountersSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_state_state_by_id(name):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: InterfaceCountersState
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_config_config_by_id(name, index):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: SubinterfacesConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv4_addresses_address_address_by_id(name, index, ip):  # noqa: E501
    """Retrieve address by ID

    Retrieve operation of resource: address # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str

    :rtype: AddressSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv4_addresses_address_config_config_by_id(name, index, ip):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str

    :rtype: Ipv4AddressConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv4_addresses_address_state_state_by_id(name, index, ip):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str

    :rtype: Ipv4AddressState
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv4_addresses_address_vrrp_vrrp_by_id(name, index, ip):  # noqa: E501
    """Retrieve vrrp by ID

    Retrieve operation of resource: vrrp # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str

    :rtype: VrrpSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv4_addresses_address_vrrp_vrrp_group_config_config_by_id(name, index, ip, virtualRouterId):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: IpVrrpConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv4_addresses_address_vrrp_vrrp_group_interface_tracking_config_config_by_id(name, index, ip, virtualRouterId):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: IpVrrpTrackingConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv4_addresses_address_vrrp_vrrp_group_interface_tracking_interface_tracking_by_id(name, index, ip, virtualRouterId):  # noqa: E501
    """Retrieve interface-tracking by ID

    Retrieve operation of resource: interface-tracking # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: InterfaceTrackingSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv4_addresses_address_vrrp_vrrp_group_interface_tracking_state_state_by_id(name, index, ip, virtualRouterId):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: IpVrrpTrackingState
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv4_addresses_address_vrrp_vrrp_group_state_state_by_id(name, index, ip, virtualRouterId):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: IpVrrpState
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv4_addresses_address_vrrp_vrrp_group_vrrp_group_by_id(name, index, ip, virtualRouterId):  # noqa: E501
    """Retrieve vrrp-group by ID

    Retrieve operation of resource: vrrp-group # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: IpVrrpTrackingTop
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv4_addresses_addresses_by_id(name, index):  # noqa: E501
    """Retrieve addresses by ID

    Retrieve operation of resource: addresses # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: AddressesSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv4_config_config_by_id(name, index):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: Ipv4GlobalConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv4_ipv4_by_id(name, index):  # noqa: E501
    """Retrieve ipv4 by ID

    Retrieve operation of resource: ipv4 # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: SubUnnumberedTop
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv4_neighbors_neighbor_config_config_by_id(name, index, ip):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str

    :rtype: Ipv4NeighborConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv4_neighbors_neighbor_neighbor_by_id(name, index, ip):  # noqa: E501
    """Retrieve neighbor by ID

    Retrieve operation of resource: neighbor # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str

    :rtype: NeighborSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv4_neighbors_neighbor_state_state_by_id(name, index, ip):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str

    :rtype: Ipv4NeighborState
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv4_neighbors_neighbors_by_id(name, index):  # noqa: E501
    """Retrieve neighbors by ID

    Retrieve operation of resource: neighbors # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: NeighborsSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv4_proxy_arp_config_config_by_id(name, index):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: Ipv4ProxyArpConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv4_proxy_arp_proxy_arp_by_id(name, index):  # noqa: E501
    """Retrieve proxy-arp by ID

    Retrieve operation of resource: proxy-arp # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: ProxyArpSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv4_proxy_arp_state_state_by_id(name, index):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: Ipv4ProxyArpConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv4_state_counters_counters_by_id(name, index):  # noqa: E501
    """Retrieve counters by ID

    Retrieve operation of resource: counters # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: CountersSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv4_state_state_by_id(name, index):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: IpCommonCountersState
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv4_unnumbered_config_config_by_id(name, index):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: SubUnnumberedConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv4_unnumbered_interface_ref_config_config_by_id(name, index):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: InterfaceRefCommon
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv4_unnumbered_interface_ref_interface_ref_by_id(name, index):  # noqa: E501
    """Retrieve interface-ref by ID

    Retrieve operation of resource: interface-ref # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: InterfaceRefStateContainer
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv4_unnumbered_interface_ref_state_state_by_id(name, index):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: InterfaceRefCommon
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv4_unnumbered_state_state_by_id(name, index):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: SubUnnumberedState
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv4_unnumbered_unnumbered_by_id(name, index):  # noqa: E501
    """Retrieve unnumbered by ID

    Retrieve operation of resource: unnumbered # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: InterfaceRef
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv6_addresses_address_address_by_id(name, index, ip):  # noqa: E501
    """Retrieve address by ID

    Retrieve operation of resource: address # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str

    :rtype: AddressSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv6_addresses_address_config_config_by_id(name, index, ip):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str

    :rtype: Ipv6AddressConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv6_addresses_address_state_state_by_id(name, index, ip):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str

    :rtype: Ipv6AddressState
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv6_addresses_address_vrrp_vrrp_by_id(name, index, ip):  # noqa: E501
    """Retrieve vrrp by ID

    Retrieve operation of resource: vrrp # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str

    :rtype: VrrpSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv6_addresses_address_vrrp_vrrp_group_config_config_by_id(name, index, ip, virtualRouterId):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: IpVrrpConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv6_addresses_address_vrrp_vrrp_group_interface_tracking_config_config_by_id(name, index, ip, virtualRouterId):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: IpVrrpTrackingConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv6_addresses_address_vrrp_vrrp_group_interface_tracking_interface_tracking_by_id(name, index, ip, virtualRouterId):  # noqa: E501
    """Retrieve interface-tracking by ID

    Retrieve operation of resource: interface-tracking # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: InterfaceTrackingSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv6_addresses_address_vrrp_vrrp_group_interface_tracking_state_state_by_id(name, index, ip, virtualRouterId):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: IpVrrpTrackingState
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv6_addresses_address_vrrp_vrrp_group_state_state_by_id(name, index, ip, virtualRouterId):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: IpVrrpState
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv6_addresses_address_vrrp_vrrp_group_vrrp_group_by_id(name, index, ip, virtualRouterId):  # noqa: E501
    """Retrieve vrrp-group by ID

    Retrieve operation of resource: vrrp-group # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str

    :rtype: IpVrrpTrackingTop
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv6_addresses_addresses_by_id(name, index):  # noqa: E501
    """Retrieve addresses by ID

    Retrieve operation of resource: addresses # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: AddressesSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv6_config_config_by_id(name, index):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: Ipv6GlobalConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv6_ipv6_by_id(name, index):  # noqa: E501
    """Retrieve ipv6 by ID

    Retrieve operation of resource: ipv6 # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: SubUnnumberedTop
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv6_neighbors_neighbor_config_config_by_id(name, index, ip):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str

    :rtype: Ipv6NeighborConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv6_neighbors_neighbor_neighbor_by_id(name, index, ip):  # noqa: E501
    """Retrieve neighbor by ID

    Retrieve operation of resource: neighbor # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str

    :rtype: NeighborSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv6_neighbors_neighbor_state_state_by_id(name, index, ip):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str

    :rtype: Ipv6NeighborState
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv6_neighbors_neighbors_by_id(name, index):  # noqa: E501
    """Retrieve neighbors by ID

    Retrieve operation of resource: neighbors # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: NeighborsSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv6_router_advertisement_config_config_by_id(name, index):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: Ipv6RaConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv6_router_advertisement_router_advertisement_by_id(name, index):  # noqa: E501
    """Retrieve router-advertisement by ID

    Retrieve operation of resource: router-advertisement # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: RouterAdvertisementSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv6_router_advertisement_state_state_by_id(name, index):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: Ipv6RaConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv6_state_counters_counters_by_id(name, index):  # noqa: E501
    """Retrieve counters by ID

    Retrieve operation of resource: counters # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: CountersSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv6_state_state_by_id(name, index):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: IpCommonCountersState
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv6_unnumbered_config_config_by_id(name, index):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: SubUnnumberedConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv6_unnumbered_interface_ref_config_config_by_id(name, index):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: InterfaceRefCommon
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv6_unnumbered_interface_ref_interface_ref_by_id(name, index):  # noqa: E501
    """Retrieve interface-ref by ID

    Retrieve operation of resource: interface-ref # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: InterfaceRefStateContainer
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv6_unnumbered_interface_ref_state_state_by_id(name, index):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: InterfaceRefCommon
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv6_unnumbered_state_state_by_id(name, index):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: SubUnnumberedState
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_ipv6_unnumbered_unnumbered_by_id(name, index):  # noqa: E501
    """Retrieve unnumbered by ID

    Retrieve operation of resource: unnumbered # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: InterfaceRef
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_state_counters_counters_by_id(name, index):  # noqa: E501
    """Retrieve counters by ID

    Retrieve operation of resource: counters # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: CountersSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_state_state_by_id(name, index):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: SubinterfacesState
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_subinterface_by_id(name, index):  # noqa: E501
    """Retrieve subinterface by ID

    Retrieve operation of resource: subinterface # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: SubinterfaceSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_vlan_config_config_by_id(name, index):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: VlanLogicalConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_vlan_egress_mapping_config_config_by_id(name, index):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: VlanLogicalEgressMappingConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_vlan_egress_mapping_egress_mapping_by_id(name, index):  # noqa: E501
    """Retrieve egress-mapping by ID

    Retrieve operation of resource: egress-mapping # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: EgressMappingSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_vlan_egress_mapping_state_state_by_id(name, index):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: VlanLogicalEgressMappingConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_vlan_ingress_mapping_config_config_by_id(name, index):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: VlanLogicalIngressMappingConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_vlan_ingress_mapping_ingress_mapping_by_id(name, index):  # noqa: E501
    """Retrieve ingress-mapping by ID

    Retrieve operation of resource: ingress-mapping # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: IngressMappingSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_vlan_ingress_mapping_state_state_by_id(name, index):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: VlanLogicalIngressMappingConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_config_config_by_id(name, index):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: VlanLogicalDoubleTaggedConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_double_tagged_by_id(name, index):  # noqa: E501
    """Retrieve double-tagged by ID

    Retrieve operation of resource: double-tagged # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: DoubleTaggedSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_inner_list_config_config_by_id(name, index):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: VlanLogicalDoubleTaggedInnerListConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_inner_list_double_tagged_inner_list_by_id(name, index):  # noqa: E501
    """Retrieve double-tagged-inner-list by ID

    Retrieve operation of resource: double-tagged-inner-list # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: DoubleTaggedInnerListSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_inner_list_state_state_by_id(name, index):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: VlanLogicalDoubleTaggedInnerListConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_inner_outer_range_config_config_by_id(name, index):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: VlanLogicalDoubleTaggedInnerOuterRangeConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_inner_outer_range_double_tagged_inner_outer_range_by_id(name, index):  # noqa: E501
    """Retrieve double-tagged-inner-outer-range by ID

    Retrieve operation of resource: double-tagged-inner-outer-range # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: DoubleTaggedInnerOuterRangeSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_inner_outer_range_state_state_by_id(name, index):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: VlanLogicalDoubleTaggedInnerOuterRangeConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_inner_range_config_config_by_id(name, index):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: VlanLogicalDoubleTaggedInnerRangeConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_inner_range_double_tagged_inner_range_by_id(name, index):  # noqa: E501
    """Retrieve double-tagged-inner-range by ID

    Retrieve operation of resource: double-tagged-inner-range # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: DoubleTaggedInnerRangeSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_inner_range_state_state_by_id(name, index):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: VlanLogicalDoubleTaggedInnerRangeConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_outer_list_config_config_by_id(name, index):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: VlanLogicalDoubleTaggedOuterListConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_outer_list_double_tagged_outer_list_by_id(name, index):  # noqa: E501
    """Retrieve double-tagged-outer-list by ID

    Retrieve operation of resource: double-tagged-outer-list # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: DoubleTaggedOuterListSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_outer_list_state_state_by_id(name, index):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: VlanLogicalDoubleTaggedOuterListConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_outer_range_config_config_by_id(name, index):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: VlanLogicalDoubleTaggedOuterRangeConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_outer_range_double_tagged_outer_range_by_id(name, index):  # noqa: E501
    """Retrieve double-tagged-outer-range by ID

    Retrieve operation of resource: double-tagged-outer-range # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: DoubleTaggedOuterRangeSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_outer_range_state_state_by_id(name, index):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: VlanLogicalDoubleTaggedOuterRangeConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_state_state_by_id(name, index):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: VlanLogicalDoubleTaggedConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_vlan_match_match_by_id(name, index):  # noqa: E501
    """Retrieve match by ID

    Retrieve operation of resource: match # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: MatchSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_vlan_match_single_tagged_config_config_by_id(name, index):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: VlanLogicalSingleTaggedConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_vlan_match_single_tagged_list_config_config_by_id(name, index):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: VlanLogicalSingleTaggedListConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_vlan_match_single_tagged_list_single_tagged_list_by_id(name, index):  # noqa: E501
    """Retrieve single-tagged-list by ID

    Retrieve operation of resource: single-tagged-list # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: SingleTaggedListSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_vlan_match_single_tagged_list_state_state_by_id(name, index):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: VlanLogicalSingleTaggedListConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_vlan_match_single_tagged_range_config_config_by_id(name, index):  # noqa: E501
    """Retrieve config by ID

    Retrieve operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: VlanLogicalSingleTaggedRangeConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_vlan_match_single_tagged_range_single_tagged_range_by_id(name, index):  # noqa: E501
    """Retrieve single-tagged-range by ID

    Retrieve operation of resource: single-tagged-range # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: SingleTaggedRangeSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_vlan_match_single_tagged_range_state_state_by_id(name, index):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: VlanLogicalSingleTaggedRangeConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_vlan_match_single_tagged_single_tagged_by_id(name, index):  # noqa: E501
    """Retrieve single-tagged by ID

    Retrieve operation of resource: single-tagged # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: SingleTaggedSchema
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_vlan_match_single_tagged_state_state_by_id(name, index):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: VlanLogicalSingleTaggedConfig
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_vlan_state_state_by_id(name, index):  # noqa: E501
    """Retrieve state by ID

    Retrieve operation of resource: state # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: VlanLogicalState
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterface_vlan_vlan_by_id(name, index):  # noqa: E501
    """Retrieve vlan by ID

    Retrieve operation of resource: vlan # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str

    :rtype: VlanLogicalEgressMappingTop
    """
    return 'do some magic!'


def retrieve_interfaces_interface_subinterfaces_subinterfaces_by_id(name):  # noqa: E501
    """Retrieve subinterfaces by ID

    Retrieve operation of resource: subinterfaces # noqa: E501

    :param name: ID of name
    :type name: str

    :rtype: SubinterfacesSchema
    """
    return 'do some magic!'


def update_interfaces_by_id(interfaces):  # noqa: E501
    """Update interfaces by ID

    Update operation of resource: interfaces # noqa: E501

    :param interfaces: interfacesbody object
    :type interfaces: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        interfaces = InterfacesSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_aggregation_aggregation_by_id(name, aggregation):  # noqa: E501
    """Update aggregation by ID

    Update operation of resource: aggregation # noqa: E501

    :param name: ID of name
    :type name: str
    :param aggregation: aggregationbody object
    :type aggregation: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        aggregation = AggregationSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_aggregation_config_config_by_id(name, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = AggregationLogicalConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_aggregation_switched_vlan_config_config_by_id(name, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = VlanSwitchedConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_aggregation_switched_vlan_switched_vlan_by_id(name, switched_vlan):  # noqa: E501
    """Update switched-vlan by ID

    Update operation of resource: switched-vlan # noqa: E501

    :param name: ID of name
    :type name: str
    :param switched_vlan: switched-vlanbody object
    :type switched_vlan: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        switched_vlan = SwitchedVlanSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_config_config_by_id(name, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = InterfacePhysConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_ethernet_config_config_by_id(name, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = EthernetInterfaceConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_ethernet_ethernet_by_id(name, ethernet):  # noqa: E501
    """Update ethernet by ID

    Update operation of resource: ethernet # noqa: E501

    :param name: ID of name
    :type name: str
    :param ethernet: ethernetbody object
    :type ethernet: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        ethernet = EthernetSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_ethernet_switched_vlan_config_config_by_id(name, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = VlanSwitchedConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_ethernet_switched_vlan_switched_vlan_by_id(name, switched_vlan):  # noqa: E501
    """Update switched-vlan by ID

    Update operation of resource: switched-vlan # noqa: E501

    :param name: ID of name
    :type name: str
    :param switched_vlan: switched-vlanbody object
    :type switched_vlan: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        switched_vlan = SwitchedVlanSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_hold_time_config_config_by_id(name, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = InterfacePhysHoldtimeConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_hold_time_hold_time_by_id(name, hold_time):  # noqa: E501
    """Update hold-time by ID

    Update operation of resource: hold-time # noqa: E501

    :param name: ID of name
    :type name: str
    :param hold_time: hold-timebody object
    :type hold_time: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        hold_time = HoldTimeSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_interface_by_id(name, interface):  # noqa: E501
    """Update interface by ID

    Update operation of resource: interface # noqa: E501

    :param name: ID of name
    :type name: str
    :param interface: interfacebody object
    :type interface: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        interface = SubinterfacesTop.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_config_config_by_id(name, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = VlanRoutedConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_ipv4_addresses_address_address_by_id(name, ip, address):  # noqa: E501
    """Update address by ID

    Update operation of resource: address # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param address: addressbody object
    :type address: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        address = AddressSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_ipv4_addresses_address_config_config_by_id(name, ip, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = Ipv4AddressConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_ipv4_addresses_address_vrrp_vrrp_by_id(name, ip, vrrp):  # noqa: E501
    """Update vrrp by ID

    Update operation of resource: vrrp # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param vrrp: vrrpbody object
    :type vrrp: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        vrrp = VrrpSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_ipv4_addresses_address_vrrp_vrrp_group_config_config_by_id(name, ip, virtualRouterId, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = IpVrrpConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_ipv4_addresses_address_vrrp_vrrp_group_interface_tracking_config_config_by_id(name, ip, virtualRouterId, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = IpVrrpTrackingConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_ipv4_addresses_address_vrrp_vrrp_group_interface_tracking_interface_tracking_by_id(name, ip, virtualRouterId, interface_tracking):  # noqa: E501
    """Update interface-tracking by ID

    Update operation of resource: interface-tracking # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str
    :param interface_tracking: interface-trackingbody object
    :type interface_tracking: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        interface_tracking = InterfaceTrackingSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_ipv4_addresses_address_vrrp_vrrp_group_vrrp_group_by_id(name, ip, virtualRouterId, vrrp_group):  # noqa: E501
    """Update vrrp-group by ID

    Update operation of resource: vrrp-group # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str
    :param vrrp_group: vrrp-groupbody object
    :type vrrp_group: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        vrrp_group = IpVrrpTrackingTop.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_ipv4_addresses_addresses_by_id(name, addresses):  # noqa: E501
    """Update addresses by ID

    Update operation of resource: addresses # noqa: E501

    :param name: ID of name
    :type name: str
    :param addresses: addressesbody object
    :type addresses: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        addresses = AddressesSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_ipv4_config_config_by_id(name, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = Ipv4GlobalConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_ipv4_ipv4_by_id(name, ipv4):  # noqa: E501
    """Update ipv4 by ID

    Update operation of resource: ipv4 # noqa: E501

    :param name: ID of name
    :type name: str
    :param ipv4: ipv4body object
    :type ipv4: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        ipv4 = SubUnnumberedTop.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_ipv4_neighbors_neighbor_config_config_by_id(name, ip, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = Ipv4NeighborConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_ipv4_neighbors_neighbor_neighbor_by_id(name, ip, neighbor):  # noqa: E501
    """Update neighbor by ID

    Update operation of resource: neighbor # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param neighbor: neighborbody object
    :type neighbor: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        neighbor = NeighborSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_ipv4_neighbors_neighbors_by_id(name, neighbors):  # noqa: E501
    """Update neighbors by ID

    Update operation of resource: neighbors # noqa: E501

    :param name: ID of name
    :type name: str
    :param neighbors: neighborsbody object
    :type neighbors: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        neighbors = NeighborsSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_ipv4_proxy_arp_config_config_by_id(name, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = Ipv4ProxyArpConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_ipv4_proxy_arp_proxy_arp_by_id(name, proxy_arp):  # noqa: E501
    """Update proxy-arp by ID

    Update operation of resource: proxy-arp # noqa: E501

    :param name: ID of name
    :type name: str
    :param proxy_arp: proxy-arpbody object
    :type proxy_arp: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        proxy_arp = ProxyArpSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_ipv4_unnumbered_config_config_by_id(name, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = SubUnnumberedConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_ipv4_unnumbered_interface_ref_config_config_by_id(name, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = InterfaceRefCommon.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_ipv4_unnumbered_interface_ref_interface_ref_by_id(name, interface_ref):  # noqa: E501
    """Update interface-ref by ID

    Update operation of resource: interface-ref # noqa: E501

    :param name: ID of name
    :type name: str
    :param interface_ref: interface-refbody object
    :type interface_ref: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        interface_ref = InterfaceRefStateContainer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_ipv4_unnumbered_unnumbered_by_id(name, unnumbered):  # noqa: E501
    """Update unnumbered by ID

    Update operation of resource: unnumbered # noqa: E501

    :param name: ID of name
    :type name: str
    :param unnumbered: unnumberedbody object
    :type unnumbered: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        unnumbered = InterfaceRef.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_ipv6_addresses_address_address_by_id(name, ip, address):  # noqa: E501
    """Update address by ID

    Update operation of resource: address # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param address: addressbody object
    :type address: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        address = AddressSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_ipv6_addresses_address_config_config_by_id(name, ip, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = Ipv6AddressConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_ipv6_addresses_address_vrrp_vrrp_by_id(name, ip, vrrp):  # noqa: E501
    """Update vrrp by ID

    Update operation of resource: vrrp # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param vrrp: vrrpbody object
    :type vrrp: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        vrrp = VrrpSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_ipv6_addresses_address_vrrp_vrrp_group_config_config_by_id(name, ip, virtualRouterId, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = IpVrrpConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_ipv6_addresses_address_vrrp_vrrp_group_interface_tracking_config_config_by_id(name, ip, virtualRouterId, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = IpVrrpTrackingConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_ipv6_addresses_address_vrrp_vrrp_group_interface_tracking_interface_tracking_by_id(name, ip, virtualRouterId, interface_tracking):  # noqa: E501
    """Update interface-tracking by ID

    Update operation of resource: interface-tracking # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str
    :param interface_tracking: interface-trackingbody object
    :type interface_tracking: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        interface_tracking = InterfaceTrackingSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_ipv6_addresses_address_vrrp_vrrp_group_vrrp_group_by_id(name, ip, virtualRouterId, vrrp_group):  # noqa: E501
    """Update vrrp-group by ID

    Update operation of resource: vrrp-group # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str
    :param vrrp_group: vrrp-groupbody object
    :type vrrp_group: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        vrrp_group = IpVrrpTrackingTop.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_ipv6_addresses_addresses_by_id(name, addresses):  # noqa: E501
    """Update addresses by ID

    Update operation of resource: addresses # noqa: E501

    :param name: ID of name
    :type name: str
    :param addresses: addressesbody object
    :type addresses: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        addresses = AddressesSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_ipv6_config_config_by_id(name, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = Ipv6GlobalConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_ipv6_ipv6_by_id(name, ipv6):  # noqa: E501
    """Update ipv6 by ID

    Update operation of resource: ipv6 # noqa: E501

    :param name: ID of name
    :type name: str
    :param ipv6: ipv6body object
    :type ipv6: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        ipv6 = SubUnnumberedTop.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_ipv6_neighbors_neighbor_config_config_by_id(name, ip, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = Ipv6NeighborConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_ipv6_neighbors_neighbor_neighbor_by_id(name, ip, neighbor):  # noqa: E501
    """Update neighbor by ID

    Update operation of resource: neighbor # noqa: E501

    :param name: ID of name
    :type name: str
    :param ip: ID of ip
    :type ip: str
    :param neighbor: neighborbody object
    :type neighbor: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        neighbor = NeighborSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_ipv6_neighbors_neighbors_by_id(name, neighbors):  # noqa: E501
    """Update neighbors by ID

    Update operation of resource: neighbors # noqa: E501

    :param name: ID of name
    :type name: str
    :param neighbors: neighborsbody object
    :type neighbors: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        neighbors = NeighborsSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_ipv6_router_advertisement_config_config_by_id(name, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = Ipv6RaConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_ipv6_router_advertisement_router_advertisement_by_id(name, router_advertisement):  # noqa: E501
    """Update router-advertisement by ID

    Update operation of resource: router-advertisement # noqa: E501

    :param name: ID of name
    :type name: str
    :param router_advertisement: router-advertisementbody object
    :type router_advertisement: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        router_advertisement = RouterAdvertisementSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_ipv6_unnumbered_config_config_by_id(name, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = SubUnnumberedConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_ipv6_unnumbered_interface_ref_config_config_by_id(name, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = InterfaceRefCommon.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_ipv6_unnumbered_interface_ref_interface_ref_by_id(name, interface_ref):  # noqa: E501
    """Update interface-ref by ID

    Update operation of resource: interface-ref # noqa: E501

    :param name: ID of name
    :type name: str
    :param interface_ref: interface-refbody object
    :type interface_ref: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        interface_ref = InterfaceRefStateContainer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_ipv6_unnumbered_unnumbered_by_id(name, unnumbered):  # noqa: E501
    """Update unnumbered by ID

    Update operation of resource: unnumbered # noqa: E501

    :param name: ID of name
    :type name: str
    :param unnumbered: unnumberedbody object
    :type unnumbered: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        unnumbered = InterfaceRef.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_routed_vlan_routed_vlan_by_id(name, routed_vlan):  # noqa: E501
    """Update routed-vlan by ID

    Update operation of resource: routed-vlan # noqa: E501

    :param name: ID of name
    :type name: str
    :param routed_vlan: routed-vlanbody object
    :type routed_vlan: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        routed_vlan = RoutedVlanSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_config_config_by_id(name, index, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = SubinterfacesConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_ipv4_addresses_address_address_by_id(name, index, ip, address):  # noqa: E501
    """Update address by ID

    Update operation of resource: address # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param address: addressbody object
    :type address: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        address = AddressSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_ipv4_addresses_address_config_config_by_id(name, index, ip, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = Ipv4AddressConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_ipv4_addresses_address_vrrp_vrrp_by_id(name, index, ip, vrrp):  # noqa: E501
    """Update vrrp by ID

    Update operation of resource: vrrp # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param vrrp: vrrpbody object
    :type vrrp: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        vrrp = VrrpSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_ipv4_addresses_address_vrrp_vrrp_group_config_config_by_id(name, index, ip, virtualRouterId, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = IpVrrpConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_ipv4_addresses_address_vrrp_vrrp_group_interface_tracking_config_config_by_id(name, index, ip, virtualRouterId, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = IpVrrpTrackingConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_ipv4_addresses_address_vrrp_vrrp_group_interface_tracking_interface_tracking_by_id(name, index, ip, virtualRouterId, interface_tracking):  # noqa: E501
    """Update interface-tracking by ID

    Update operation of resource: interface-tracking # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str
    :param interface_tracking: interface-trackingbody object
    :type interface_tracking: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        interface_tracking = InterfaceTrackingSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_ipv4_addresses_address_vrrp_vrrp_group_vrrp_group_by_id(name, index, ip, virtualRouterId, vrrp_group):  # noqa: E501
    """Update vrrp-group by ID

    Update operation of resource: vrrp-group # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str
    :param vrrp_group: vrrp-groupbody object
    :type vrrp_group: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        vrrp_group = IpVrrpTrackingTop.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_ipv4_addresses_addresses_by_id(name, index, addresses):  # noqa: E501
    """Update addresses by ID

    Update operation of resource: addresses # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param addresses: addressesbody object
    :type addresses: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        addresses = AddressesSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_ipv4_config_config_by_id(name, index, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = Ipv4GlobalConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_ipv4_ipv4_by_id(name, index, ipv4):  # noqa: E501
    """Update ipv4 by ID

    Update operation of resource: ipv4 # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ipv4: ipv4body object
    :type ipv4: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        ipv4 = SubUnnumberedTop.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_ipv4_neighbors_neighbor_config_config_by_id(name, index, ip, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = Ipv4NeighborConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_ipv4_neighbors_neighbor_neighbor_by_id(name, index, ip, neighbor):  # noqa: E501
    """Update neighbor by ID

    Update operation of resource: neighbor # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param neighbor: neighborbody object
    :type neighbor: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        neighbor = NeighborSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_ipv4_neighbors_neighbors_by_id(name, index, neighbors):  # noqa: E501
    """Update neighbors by ID

    Update operation of resource: neighbors # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param neighbors: neighborsbody object
    :type neighbors: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        neighbors = NeighborsSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_ipv4_proxy_arp_config_config_by_id(name, index, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = Ipv4ProxyArpConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_ipv4_proxy_arp_proxy_arp_by_id(name, index, proxy_arp):  # noqa: E501
    """Update proxy-arp by ID

    Update operation of resource: proxy-arp # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param proxy_arp: proxy-arpbody object
    :type proxy_arp: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        proxy_arp = ProxyArpSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_ipv4_unnumbered_config_config_by_id(name, index, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = SubUnnumberedConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_ipv4_unnumbered_interface_ref_config_config_by_id(name, index, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = InterfaceRefCommon.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_ipv4_unnumbered_interface_ref_interface_ref_by_id(name, index, interface_ref):  # noqa: E501
    """Update interface-ref by ID

    Update operation of resource: interface-ref # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param interface_ref: interface-refbody object
    :type interface_ref: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        interface_ref = InterfaceRefStateContainer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_ipv4_unnumbered_unnumbered_by_id(name, index, unnumbered):  # noqa: E501
    """Update unnumbered by ID

    Update operation of resource: unnumbered # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param unnumbered: unnumberedbody object
    :type unnumbered: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        unnumbered = InterfaceRef.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_ipv6_addresses_address_address_by_id(name, index, ip, address):  # noqa: E501
    """Update address by ID

    Update operation of resource: address # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param address: addressbody object
    :type address: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        address = AddressSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_ipv6_addresses_address_config_config_by_id(name, index, ip, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = Ipv6AddressConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_ipv6_addresses_address_vrrp_vrrp_by_id(name, index, ip, vrrp):  # noqa: E501
    """Update vrrp by ID

    Update operation of resource: vrrp # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param vrrp: vrrpbody object
    :type vrrp: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        vrrp = VrrpSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_ipv6_addresses_address_vrrp_vrrp_group_config_config_by_id(name, index, ip, virtualRouterId, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = IpVrrpConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_ipv6_addresses_address_vrrp_vrrp_group_interface_tracking_config_config_by_id(name, index, ip, virtualRouterId, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = IpVrrpTrackingConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_ipv6_addresses_address_vrrp_vrrp_group_interface_tracking_interface_tracking_by_id(name, index, ip, virtualRouterId, interface_tracking):  # noqa: E501
    """Update interface-tracking by ID

    Update operation of resource: interface-tracking # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str
    :param interface_tracking: interface-trackingbody object
    :type interface_tracking: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        interface_tracking = InterfaceTrackingSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_ipv6_addresses_address_vrrp_vrrp_group_vrrp_group_by_id(name, index, ip, virtualRouterId, vrrp_group):  # noqa: E501
    """Update vrrp-group by ID

    Update operation of resource: vrrp-group # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param virtualRouterId: ID of virtualRouterId
    :type virtualRouterId: str
    :param vrrp_group: vrrp-groupbody object
    :type vrrp_group: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        vrrp_group = IpVrrpTrackingTop.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_ipv6_addresses_addresses_by_id(name, index, addresses):  # noqa: E501
    """Update addresses by ID

    Update operation of resource: addresses # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param addresses: addressesbody object
    :type addresses: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        addresses = AddressesSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_ipv6_config_config_by_id(name, index, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = Ipv6GlobalConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_ipv6_ipv6_by_id(name, index, ipv6):  # noqa: E501
    """Update ipv6 by ID

    Update operation of resource: ipv6 # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ipv6: ipv6body object
    :type ipv6: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        ipv6 = SubUnnumberedTop.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_ipv6_neighbors_neighbor_config_config_by_id(name, index, ip, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = Ipv6NeighborConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_ipv6_neighbors_neighbor_neighbor_by_id(name, index, ip, neighbor):  # noqa: E501
    """Update neighbor by ID

    Update operation of resource: neighbor # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ip: ID of ip
    :type ip: str
    :param neighbor: neighborbody object
    :type neighbor: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        neighbor = NeighborSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_ipv6_neighbors_neighbors_by_id(name, index, neighbors):  # noqa: E501
    """Update neighbors by ID

    Update operation of resource: neighbors # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param neighbors: neighborsbody object
    :type neighbors: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        neighbors = NeighborsSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_ipv6_router_advertisement_config_config_by_id(name, index, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = Ipv6RaConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_ipv6_router_advertisement_router_advertisement_by_id(name, index, router_advertisement):  # noqa: E501
    """Update router-advertisement by ID

    Update operation of resource: router-advertisement # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param router_advertisement: router-advertisementbody object
    :type router_advertisement: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        router_advertisement = RouterAdvertisementSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_ipv6_unnumbered_config_config_by_id(name, index, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = SubUnnumberedConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_ipv6_unnumbered_interface_ref_config_config_by_id(name, index, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = InterfaceRefCommon.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_ipv6_unnumbered_interface_ref_interface_ref_by_id(name, index, interface_ref):  # noqa: E501
    """Update interface-ref by ID

    Update operation of resource: interface-ref # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param interface_ref: interface-refbody object
    :type interface_ref: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        interface_ref = InterfaceRefStateContainer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_ipv6_unnumbered_unnumbered_by_id(name, index, unnumbered):  # noqa: E501
    """Update unnumbered by ID

    Update operation of resource: unnumbered # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param unnumbered: unnumberedbody object
    :type unnumbered: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        unnumbered = InterfaceRef.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_subinterface_by_id(name, index, subinterface):  # noqa: E501
    """Update subinterface by ID

    Update operation of resource: subinterface # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param subinterface: subinterfacebody object
    :type subinterface: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        subinterface = SubinterfaceSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_vlan_config_config_by_id(name, index, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = VlanLogicalConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_vlan_egress_mapping_config_config_by_id(name, index, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = VlanLogicalEgressMappingConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_vlan_egress_mapping_egress_mapping_by_id(name, index, egress_mapping):  # noqa: E501
    """Update egress-mapping by ID

    Update operation of resource: egress-mapping # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param egress_mapping: egress-mappingbody object
    :type egress_mapping: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        egress_mapping = EgressMappingSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_vlan_ingress_mapping_config_config_by_id(name, index, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = VlanLogicalIngressMappingConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_vlan_ingress_mapping_ingress_mapping_by_id(name, index, ingress_mapping):  # noqa: E501
    """Update ingress-mapping by ID

    Update operation of resource: ingress-mapping # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param ingress_mapping: ingress-mappingbody object
    :type ingress_mapping: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        ingress_mapping = IngressMappingSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_config_config_by_id(name, index, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = VlanLogicalDoubleTaggedConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_double_tagged_by_id(name, index, double_tagged):  # noqa: E501
    """Update double-tagged by ID

    Update operation of resource: double-tagged # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param double_tagged: double-taggedbody object
    :type double_tagged: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        double_tagged = DoubleTaggedSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_inner_list_config_config_by_id(name, index, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = VlanLogicalDoubleTaggedInnerListConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_inner_list_double_tagged_inner_list_by_id(name, index, double_tagged_inner_list):  # noqa: E501
    """Update double-tagged-inner-list by ID

    Update operation of resource: double-tagged-inner-list # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param double_tagged_inner_list: double-tagged-inner-listbody object
    :type double_tagged_inner_list: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        double_tagged_inner_list = DoubleTaggedInnerListSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_inner_outer_range_config_config_by_id(name, index, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = VlanLogicalDoubleTaggedInnerOuterRangeConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_inner_outer_range_double_tagged_inner_outer_range_by_id(name, index, double_tagged_inner_outer_range):  # noqa: E501
    """Update double-tagged-inner-outer-range by ID

    Update operation of resource: double-tagged-inner-outer-range # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param double_tagged_inner_outer_range: double-tagged-inner-outer-rangebody object
    :type double_tagged_inner_outer_range: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        double_tagged_inner_outer_range = DoubleTaggedInnerOuterRangeSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_inner_range_config_config_by_id(name, index, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = VlanLogicalDoubleTaggedInnerRangeConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_inner_range_double_tagged_inner_range_by_id(name, index, double_tagged_inner_range):  # noqa: E501
    """Update double-tagged-inner-range by ID

    Update operation of resource: double-tagged-inner-range # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param double_tagged_inner_range: double-tagged-inner-rangebody object
    :type double_tagged_inner_range: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        double_tagged_inner_range = DoubleTaggedInnerRangeSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_outer_list_config_config_by_id(name, index, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = VlanLogicalDoubleTaggedOuterListConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_outer_list_double_tagged_outer_list_by_id(name, index, double_tagged_outer_list):  # noqa: E501
    """Update double-tagged-outer-list by ID

    Update operation of resource: double-tagged-outer-list # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param double_tagged_outer_list: double-tagged-outer-listbody object
    :type double_tagged_outer_list: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        double_tagged_outer_list = DoubleTaggedOuterListSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_outer_range_config_config_by_id(name, index, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = VlanLogicalDoubleTaggedOuterRangeConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_vlan_match_double_tagged_outer_range_double_tagged_outer_range_by_id(name, index, double_tagged_outer_range):  # noqa: E501
    """Update double-tagged-outer-range by ID

    Update operation of resource: double-tagged-outer-range # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param double_tagged_outer_range: double-tagged-outer-rangebody object
    :type double_tagged_outer_range: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        double_tagged_outer_range = DoubleTaggedOuterRangeSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_vlan_match_match_by_id(name, index, match):  # noqa: E501
    """Update match by ID

    Update operation of resource: match # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param match: matchbody object
    :type match: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        match = MatchSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_vlan_match_single_tagged_config_config_by_id(name, index, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = VlanLogicalSingleTaggedConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_vlan_match_single_tagged_list_config_config_by_id(name, index, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = VlanLogicalSingleTaggedListConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_vlan_match_single_tagged_list_single_tagged_list_by_id(name, index, single_tagged_list):  # noqa: E501
    """Update single-tagged-list by ID

    Update operation of resource: single-tagged-list # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param single_tagged_list: single-tagged-listbody object
    :type single_tagged_list: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        single_tagged_list = SingleTaggedListSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_vlan_match_single_tagged_range_config_config_by_id(name, index, config):  # noqa: E501
    """Update config by ID

    Update operation of resource: config # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param config: configbody object
    :type config: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        config = VlanLogicalSingleTaggedRangeConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_vlan_match_single_tagged_range_single_tagged_range_by_id(name, index, single_tagged_range):  # noqa: E501
    """Update single-tagged-range by ID

    Update operation of resource: single-tagged-range # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param single_tagged_range: single-tagged-rangebody object
    :type single_tagged_range: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        single_tagged_range = SingleTaggedRangeSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_vlan_match_single_tagged_single_tagged_by_id(name, index, single_tagged):  # noqa: E501
    """Update single-tagged by ID

    Update operation of resource: single-tagged # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param single_tagged: single-taggedbody object
    :type single_tagged: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        single_tagged = SingleTaggedSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterface_vlan_vlan_by_id(name, index, vlan):  # noqa: E501
    """Update vlan by ID

    Update operation of resource: vlan # noqa: E501

    :param name: ID of name
    :type name: str
    :param index: ID of index
    :type index: str
    :param vlan: vlanbody object
    :type vlan: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        vlan = VlanLogicalEgressMappingTop.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_interfaces_interface_subinterfaces_subinterfaces_by_id(name, subinterfaces):  # noqa: E501
    """Update subinterfaces by ID

    Update operation of resource: subinterfaces # noqa: E501

    :param name: ID of name
    :type name: str
    :param subinterfaces: subinterfacesbody object
    :type subinterfaces: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        subinterfaces = SubinterfacesSchema.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
