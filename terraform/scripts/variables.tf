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

// Container Registry Variables
variable "container_repository_display_name" {
  default = "container_repo"
}
variable "registry_state" {
  default = ""
}
variable "registry_id" {
  default = ""
}

// Container Engine Variables
variable "cluster_kubernetes_version" {
  default = "v1.22.5"
}
variable "cluster_name" {
  default = "Precog"
}

// VCN Variables //

variable "vcn_cidr_blocks" {
  default = ["10.0.0.0/16"]
}
variable "vcn_display_name" {
  default = "oke-vcn-quick-Precog-7dcdc1d33"
}
variable "vcn_dns_label" {
  default = "precog"
}

// Subnet Cidr Blocks

variable "bastion_subnet_cidr_block" {
  default = "10.0.30.0/24"
}
variable "node_subnet_cidr_block" {
  default = "10.0.10.0/24"
}
variable "apiEndpoint_cidr_block" {
  default = "10.0.0.0/28"
}
variable "svclbsubnet_cidr_block" {
  default = "10.0.20.0/24"
}

// Subnet Display Names

variable "bastion_subnet_display_name" {
  default = "oke-bastionSubnet-Precog"
}
variable "node_subnet_display_name" {
  defualt = "oke-nodesubnet-quick-Precog-7dcdc1d33-regional"
}
variable "apiEndpoint_display_name" {
  default = "oke-k8sApiEndpoint-subnet-quick-Precog-7dcdc1d33-regional"
}
variable "svclbsubnet_display_name" {
  default = "oke-svclbsubnet-quick-Precog-7dcdc1d33-regional"
}

// Subnet DNS Labels

variable "bastion_subnet_dns_label" {
  default = "okebastionsubne"
}
variable "node_subnet_dns_label" {
  default = "sub2c881b88d"
}
variable "apiEndpoint_dns_label" {
  default = "sub12209f2a0"
}
variable "svclbsubnet_dns_label" {
  default = "lbsub945739bd8"
}

// Subnet Security List IDs

variable "bastion_subnet_security_list_ids" {
  default = "ocid1.securitylist.oc1.iad.aaaaaaaaxge3zxys7ztgoococjk4kwszvj7fscnpx3ejxbcfke7k5trpwm4q"
}
variable "node_subnet_security_lists_ids" {
  default = "ocid1.securitylist.oc1.iad.aaaaaaaa5d4wzajhnohrrgpit4t6gd72ixjbaljvrizra6sneoux3zxo42qq"
}
variable "apiEndpoint_subnet_security_list_ids" {
  default = "ocid1.securitylist.oc1.iad.aaaaaaaazzt4okeeippelfyuddbnkihxgkktkm2fwqxsconlta6ybcnwcmva"
}
variable "svclbsubnet_subnet_security_list_ids" {
  default = "ocid1.securitylist.oc1.iad.aaaaaaaaxge3zxys7ztgoococjk4kwszvj7fscnpx3ejxbcfke7k5trpwm4q"
}

// Route Table Display Names
variable "private_route_table_display_name" {
  default = "oke-private-routetable-Precog-7dcdc1d33"
}
variable "public_route_table_display_name" {
  default = "oke-public-routetable-Precog-7dcdc1d33"
}
variable "internet_gateway_display_name" {
  default = "oke-igw-quick-Precog-7dcdc1d33"
}