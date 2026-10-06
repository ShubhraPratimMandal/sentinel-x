variable "compartment_ocid" {
  description = "OCI compartment OCID."
  type        = string
}

variable "region" {
  description = "OCI region."
  type        = string
  default     = "ap-hyderabad-1"
}

variable "project_name" {
  description = "Project resource prefix."
  type        = string
  default     = "sentinel-x"
}
