# generator.py - change this to code generator or something similar, keep it separate from descriptions

def generate_example(resource_name):

    templates = {

        "Object Storage Bucket": """
resource "oci_objectstorage_bucket" "this" {
  
  # Required
  compartment_id = var.compartment_id
  namespace = data.oci_objectstorage_namespace.ns.namespace
  name = var.name

  # Optional
  access_type = var.access_type
  auto_tiering = var.auto_tiering

}
""",

        "Block Volume": """
resource "oci_core_volume" "example" {

  # Required
  compartment_id = var.compartment_id 
  availability_domain = var.availability_domain

  # Optional
  display_name = var.display_name
  size_in_gbs = var.size_in_gbs

}
""",

        "File Storage File System": """
resource "oci_file_storage_file_system" "example" {

  # Required
  availability_domain = var.availability_domain
  compartment_id      = var.compartment_id

  # Optional
  display_name = var.display_name

}
"""

    }

    return templates.get(
        resource_name,
        "Template not found."
    )
