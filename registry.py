# registry.py

import requests

def get_resource_page(resource_name):

    urls = {
        "Object Storage Bucket": "https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/objectstorage_bucket",

        "Block Volume": "https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/core_volume",

        "File Storage File System": "https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/file_storage_file_system"
    }

    return urls.get(resource_name, "URL not found.")

