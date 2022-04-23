resource "oci_containerengine_cluster" "container_engine" {
    // Required
    compartment_id = var.root_compartment_id
    
    // Optional
    kubernetes_version = var.cluster_kubernetes_version
    name = var.cluster_name
    vcn_id = oci_core_vcn.precog_vcn.id
    endpoint_config {
        is_public_ip_enabled = "false"
        subnet_id = oci_core_subnet.precog_node_subnet.id
    }
}