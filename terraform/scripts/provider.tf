provider "oci" {
  //version = "4.72.0"
  region = var.region
  tenancy_ocid = var.tenancy_ocid
  user_ocid = var.user_ocid
  fingerprint = var.fingerprint
  private_key_path = var.private_key_path
  //config_file_profile= "LiVE"
}