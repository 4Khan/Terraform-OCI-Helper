# descriptions.py - store descriptions for resources here

def generate_description(resource_name):

    templates = {

        "Object Storage Bucket" : """
A bucket is a container for storing objects in a compartment within a namespace.
    A bucket is associated with a single compartment. 
    The compartment has policies that indicate what actions a user can perform on a bucket and all the objects in the bucket.
""",

        "Block Volume" : """
A detachable block volume device that allows you to dynamically expand the storage capacity of an instance.
""",

"File Storage File System": """
A Network File System (NFS). 
To allow access to a file system, add it to an export set and associate the export set with a mount target. 
The same file system can be in multiple export sets and associated with multiple mount targets.
"""

    }

    return templates.get(resource_name, 
                         "Description not found.")