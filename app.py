# app.py

import streamlit as st

from registry import get_resource_page
from generator import generate_example
from descriptions import generate_description

st.title("OCI Terraform Resource Helper")

# Provide a list of options
options = ["Object Storage Bucket", "Block Volume", "File Storage File System"]

# Use segmented control widget for user to select one of the options - note, selection mode is single so only one option can be selected at a time
selected_resource = st.segmented_control(
    "Storage Resources (select one):", options, selection_mode="single"
)

# Show user what they have selected - might be redundant
st.markdown(f"Your selected option: {selected_resource}.")



# We can probably get rid of some of the code below for now, as instead I want the selection to show info on the resources instead.
# resource_name = st.text_input(
#     "Enter OCI Terraform Resource",
#     "oci_core_vcn"
# )

if st.button("Generate Info"):

    registry_url = get_resource_page(selected_resource)

    st.subheader("Description")

    # I need to put the below into a function that generates this text. As currently it will show the same text for all resources.
    description = generate_description(
        selected_resource
    )

    st.markdown(
        f"{description}"
    )

    st.subheader("Registry Documentation")

    st.markdown(
        f"{registry_url}"
    )

    example_code = generate_example(
        selected_resource
    )

    st.subheader(
        "Example Usage"
    )

    st.code(
        example_code,
        language="terraform"
    )