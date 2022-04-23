resource "oci_core_internet_gateway" "internet_gateway" {
    // Required
    compartment_id = var.root_compartment_id
    vcn_id = oci_core_vcn.precog_vcn.id

    // Optional
    display_name = var.internet_gateway_display_name
}
resource "oci_core_route_table" "private_route_table" {
    // Required
    compartment_id = var.root_compartment_id
    vcn_id = oci_core_vcn.precog_vcn.id

    // Optional
    display_name = var.private_route_table_display_name
    route_rules {
        // Required
        network_entity_id = oci_core_internet_gateway.internet_gateway.id

        /* Optional
        cidr_block = var.route_table_route_rules_cidr_block
        description = var.route_table_route_rules_description
        destination = var.route_table_route_rules_destination
        destination_type = var.route_table_route_rules_destination_type */
    }
}
resource "oci_core_route_table" "public_route_table" {
    // Required
    compartment_id = var.root_compartment_id
    vcn_id = oci_core_vcn.precog_vcn.id

    // Optional
    display_name = var.public_route_table_display_name
    route_rules {
        // Required
        network_entity_id = oci_core_internet_gateway.internet_gateway.id

        /* Optional
        cidr_block = var.route_table_route_rules_cidr_block
        description = var.route_table_route_rules_description
        destination = var.route_table_route_rules_destination
        destination_type = var.route_table_route_rules_destination_type */
    }
}
