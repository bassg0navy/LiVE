// Variables File
variable "app_name" {
    default = "LiVE"
}
variable "region" {
  default = "us-ashburn-1"
}
variable "private_key_path" {
    default = "/app/storage-webserver/.oci/abstract-rsa-private-key.pem"
}
variable "tenancy_ocid" {
    default = "ocid1.tenancy.oc1..aaaaaaaadkxkk76ljinkchc3gmtgohryrbegiiaakcyrnhgyuy6a7iutlmtq"
}
variable "root_compartment_id" {
    default = "ocid1.tenancy.oc1..aaaaaaaadkxkk76ljinkchc3gmtgohryrbegiiaakcyrnhgyuy6a7iutlmtq"
}
variable "ManagedCompartmentForPaaS_id" {
  default = "ocid1.compartment.oc1..aaaaaaaahn7ibzcqsf4ywp4qr34hw6n4lrawqxiooy7oq6h7nxygxurmflrq"
  description = "child compartment under root compartment (bassg0navy)"
}
variable "fingerprint" {
  default = "a6:f6:08:bc:b8:bd:18:21:ce:37:23:0e:68:45:e8:ee"
}
variable "user_ocid" {
  default = "ocid1.user.oc1..aaaaaaaa6y2u73mpdyoxy23syxzlmivcum3wdq3uqaod65eqdlkrnylyadzq"
}
variable "container_repository_display_name" {
  default = "LiVE-Containers"
}
variable "registry_state" {
  default = ""
}
variable "registry_id" {
  default = ""
}
