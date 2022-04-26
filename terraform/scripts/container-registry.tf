resource "oci_artifacts_container_repository" "proxy-webserver_repository" {
    #Required
    compartment_id = var.root_compartment_id
    display_name = "proxy-webserver"

    /* Optional
    is_immutable = var.container_repository_is_immutable
    is_public = var.container_repository_is_public */
    readme {
        #Required
        content = "proxy-webserver container repository"
        format = "text/plain"
    }
}
data "oci_artifacts_container_image" "proxy-webserver_image" {
    image_id = var.proxy-webserver-latest_container_image_ocid
}

// Add outputs
output "registry_state" {
    value = oci_artifacts_container_repository.proxy-webserver_repository.state
}

output "registry_id" {
    value = oci_artifacts_container_repository.proxy-webserver_repository.id
}