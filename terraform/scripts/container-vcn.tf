resource "oci_core_vcn" "precog_vcn" {
    // Required
    compartment_id = var.root_compartment_id

    // Optional
    cidr_blocks = var.vcn_cidr_blocks
    display_name = var.vcn_display_name
    dns_label = var.vcn_dns_label
}