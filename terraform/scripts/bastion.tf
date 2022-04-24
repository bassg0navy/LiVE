## This configuration was generated by terraform-provider-oci

resource oci_bastion_bastion export_Hodor {
  bastion_type = "STANDARD"
  client_cidr_block_allow_list = [
    "0.0.0.0/0",
  ]
  compartment_id = var.compartment_ocid
  defined_tags = {
    "Oracle-Tags.CreatedBy" = "oracleidentitycloudservice/bassgonavy@gmail.com"
    "Oracle-Tags.CreatedOn" = "2022-04-17T20:49:13.639Z"
  }
  freeform_tags = {
  }
  max_session_ttl_in_seconds = "10800"
  name                       = "Hodor"
  #phone_book_entry = <<Optional value not found in discovery>>
  static_jump_host_ip_addresses = [
  ]
  target_subnet_id = "ocid1.subnet.oc1.iad.aaaaaaaa3lg2wgbembx2bjnwquoj4spshxc7gw7z2dehm632hhdluwufhoyq"
}

