import streamlit as st
import json

st.set_page_config(page_title="API Documentation", layout="wide")

st.title("📌 API Documentation - User Verification")

st.header("🔹 API Endpoint")
st.code("https://verification-system-production-75de.up.railway.app/verify_user/", language="plaintext")
st.subheader("Authorization: Basic Auth")
# st.code("POST /auth", language="plaintext")
example_request = {
    "Username": "testuser",
    "Password": "affixcon1234"
}
st.code(json.dumps(example_request, indent=2), language="json")

col1,col2 = st.columns(2)
with col1:
    st.subheader(':orange[**POST**] Indonesia Residential')
    st.markdown("🔹 **No. of Records 167 million**")
    st.subheader("📤 Example Request")
    example_request = {
    "country_prefix": "indonisia",
    "id_number": "1171015704980001",
    "first_name":"Arfian",
    "middle_name" : "Putra",
    "sur_name":"Marhennata",
    "dob":"1998-04-17",
    "addressElement1": "Baiturrahman",
    "addressElement2": " Kota Banda",
    "addressElement3": "Aceh Aceh",
    "addressElement4": "23244",
    "mobile" : "08228992992",
    "email" : ""
    }
    st.code(json.dumps(example_request, indent=2), language="json")

    # Example Response
    st.subheader("📥 Example Response")
    example_response = {
    "OverallResults": {
        "NIK Verified": True,
        "IDV Record Verified": True,
        "IDV Verified Level": "M1",
        "IDV Contact Verified Level": "P2",
        "IDV Multi Level Verification": False
    },
    "ReturnItems": {
        "FULL_ADDRESS": "Baiturrahman Kota Banda Aceh Aceh, 23244"
    },
    "Scoring": {
        "SourceStatus": "Successful",
        "ErrorMessage": "",
        "Name Match Level": "Exact Match",
        "Full Name Score": 100,
        "First Name Score": 100,
        "Middle Name Score": 100,
        "Surname Score": 100,
        "Address Match Level": "Full Match",
        "Full Address Score": 100,
        "AddressElement1 Score": 100,
        "AddressElement2 Score": 100,
        "AddressElement3 Score": 100,
        "AddressElement4 Score": 100,
        "DOB Match": True,
        "MobileMatch": True,
        "EmailMatch": True
    }
}
    st.code(json.dumps(example_response, indent=2), language="json")


with col2:
    st.subheader(':orange[**POST**] Mexico Residential')
    st.markdown("🔹 **No. of Records 49.5 million**")
    st.subheader("📤 Example Request")
    example_request = {
    "country_prefix": "mx",
    "id_number": "CAVM970222HMNBLR04",
    "first_name":"MARTHA",
    "middle_name" : "ALEJANDRA CABALLERO",
    "sur_name":"VILLANUEVA",
    "dob":"1997-02-22",
    "addressElement1": "Morelia",
    "addressElement2": "Michoacán",
    "addressElement3": "de Ocampo",
    "addressElement4": "58116.0",
    "mobile" : "4432339523",
    "email" : ""
    }
    st.code(json.dumps(example_request, indent=2), language="json")

    # Example Response
    st.subheader("📥 Example Response")
    example_response = {
    "OverallResults": {
        "NIK Verified": True,
        "IDV Record Verified": True,
        "IDV Verified Level": "M1",
        "IDV Contact Verified Level": "P2",
        "IDV Multi Level Verification": False
    },
    "ReturnItems": {
        "FULL_ADDRESS": "  Morelia Michoacán de Ocampo 58116.0"
    },
    "Scoring": {
        "SourceStatus": "Successful",
        "ErrorMessage": "",
        "Name Match Level": "Exact Match",
        "Full Name Score": 100,
        "First Name Score": 100,
        "Middle Name Score": 100,
        "Surname Score": 100,
        "Address Match Level": "Full Match",
        "Full Address Score": 100,
        "AddressElement1 Score": 100,
        "AddressElement2 Score": 100,
        "AddressElement3 Score": 100,
        "AddressElement4 Score": 100,
        "DOB Match": True,
        "MobileMatch": True,
        "EmailMatch": True
    }
}
    st.code(json.dumps(example_response, indent=2), language="json")
# Show API Test Button
if st.button("Run in Postman"):
    postman_url = "https://web.postman.co/"
    st.markdown(f"[Open in Postman]({postman_url})", unsafe_allow_html=True)
