resource "oci_core_subnet" "precog_bastion_subnet" {
    // Required
    cidr_block = var.bastion_subnet_cidr_block
    compartment_id = var.root_compartment_id
    vcn_id = oci_core_vcn.precog_vcn.id

    // Optional
    display_name = var.bastion_subnet_display_name
    dns_label = var.bastion_subnet_dns_label
    prohibit_internet_ingress = "false"
    prohibit_public_ip_on_vnic = "false"
    route_table_id = oci_core_route_table.public_route_table.id
    security_list_ids = var.bastion_subnet_security_list_ids
}
resource "oci_core_subnet" "precog_node_subnet" {
    // Required
    cidr_block = var.node_subnet_cidr_block
    compartment_id = var.root_compartment_id
    vcn_id = oci_core_vcn.precog_vcn.id

    // Optional
    display_name = var.node_subnet_display_name
    dns_label = var.node_subnet_dns_label
    prohibit_internet_ingress = "false"
    prohibit_public_ip_on_vnic = "false"
    route_table_id = oci_core_route_table.private_route_table.id
    security_list_ids = var.node_subnet_security_list_ids
}
resource "oci_core_subnet" "precog_apiEndpoint_subnet" {
    // Required
    cidr_block = var.apiEndpoint_cidr_block
    compartment_id = var.root_compartment_id
    vcn_id = oci_core_vcn.precog_vcn.id

    // Optional
    display_name = var.apiEndpoint_display_name
    dns_label = var.apiEndpoint_dns_label
    prohibit_internet_ingress = "false"
    prohibit_public_ip_on_vnic = "false"
    route_table_id = oci_core_route_table.private_route_table.id
    security_list_ids = var.apiEndpoint_subnet_security_list_ids
}
resource "oci_core_subnet" "precog_svclbsubnet_subnet" {
    // Required
    cidr_block = var.svclbsubnet_cidr_block
    compartment_id = var.root_compartment_id
    vcn_id = oci_core_vcn.precog_vcn.id

    // Optional
    display_name = var.svclbsubnet_display_name
    dns_label = var.svclbsubnet_dns_label
    prohibit_internet_ingress = "false"
    prohibit_public_ip_on_vnic = "false"
    route_table_id = oci_core_route_table.public_route_table.id
    security_list_ids = var.svclbsubnet_subnet_security_list_ids
}