terraform {
  required_version = ">= 1.8.0"
  required_providers {
    oci = {
      source  = "oracle/oci"
      version = "~> 7.0"
    }
  }
}

provider "oci" {
  region = var.region
}

resource "oci_core_vcn" "sentinel" {
  compartment_id = var.compartment_ocid
  cidr_block     = "10.42.0.0/16"
  display_name   = "${var.project_name}-vcn"
  dns_label      = "sentinelx"
}

resource "oci_core_subnet" "public" {
  compartment_id = var.compartment_ocid
  vcn_id         = oci_core_vcn.sentinel.id
  cidr_block     = "10.42.1.0/24"
  display_name   = "${var.project_name}-public"
  dns_label      = "public"
  prohibit_public_ip_on_vnic = false
}

resource "oci_core_subnet" "private" {
  compartment_id = var.compartment_ocid
  vcn_id         = oci_core_vcn.sentinel.id
  cidr_block     = "10.42.10.0/24"
  display_name   = "${var.project_name}-private"
  dns_label      = "private"
  prohibit_public_ip_on_vnic = true
}

output "vcn_id" {
  value = oci_core_vcn.sentinel.id
}

output "public_subnet_id" {
  value = oci_core_subnet.public.id
}

output "private_subnet_id" {
  value = oci_core_subnet.private.id
}
