// Adds preexisting container registry to LiVE stack
resource "oci_artifacts_container_repository" "LiVE_container_repo" {
    compartment_id = var.root_compartment_id
    display_name = var.container_repository_display_name
}

// Add outputs
output "registry_state" {
    value = oci_artifacts_container_repository.LiVE_container_repo.state
}

output "registry_id" {
    value = oci_artifacts_container_repository.LiVE_container_repo.id
}