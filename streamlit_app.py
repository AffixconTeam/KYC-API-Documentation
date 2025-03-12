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
    "Summary": {
        "NIKVerified": True,
        "IDVRecordVerified": True,
        "IDVVerifiedLevel": "M1",
        "IDVContactVerifiedLevel": "P2",
        "IDVMultiLevelVerification": False
    },
    "ReturnItems": {
        "ADDRESS": "Baiturrahman Kota Banda Aceh Aceh, 23244"
    },
    "Scoring": {
        "SourceStatus": "Successful",
        "ErrorMessage": "",
        "NameMatchLevel": "Exact Match",
        "FullNameScore": 100,
        "FirstNameScore": 100,
        "MiddleNameScore": 100,
        "SurnameScore": 100,
        "AddressMatchLevel": "Full Match",
        "FullAddressScore": 100,
        "AddressElement1Score": 100,
        "AddressElement2Score": 100,
        "AddressElement3Score": 100,
        "AddressElement4Score": 100,
        "DOBMatch": True,
        "MobileMatch": True,
        "EmailMatch": True
    },
    "Description": {
        "IDVVerifiedLevel": {
            "M1": "Full Name Full Address DOBMatch",
            "N1": "Full Name Full Address Match",
            "M2": "Full Name DOBMatch",
            "P1": "Full Name, Mobile, and Email",
            "P2": "Full Name and Mobile",
            "P3": "Full Name and Email"
        },
        "MultiSourceLevel": {
            "true": "M1>=2 or (M1>=1 and M2>=1) or (M1>=1 and N1>=1) or (M2>=1 and N1>=1)",
            "false": "otherwise"
        },
        "NameMatchLevels": {
            "Exact Match": "Full Name Match",
            "Hyphenated Match": "Hyphenated Match",
            "Transposed Match": "Transposed Match",
            "Middle Name Mismatch": "Middle Name Mismatch",
            "Initial Match": "Initial Match",
            "SurName only Match": "SurName only Match"
        }
    }
}
    st.code(json.dumps(example_response, indent=2), language="json")


with col2:
    st.subheader(':orange[**POST**] Mexico Residential')
    st.markdown("🔹 **No. of Records 49.5 million**")
    st.subheader("📤 Example Request")
    example_request =    {
        "country_prefix": "mx",
        "id_number": "SITM970206HSRQRR01",
        "first_name":"MARTHA",
        "middle_name" : "CECILIA SIQUEIROS",
        "sur_name":"TARAZON",
        "dob":"1997-02-06",
        "addressElement1": "Hermosillo",
        "addressElement2": "Hermosillo",
        "addressElement3": "Sonora",
        "addressElement4": "83000.0",
        "mobile" : "6622145317",
        "email" : ""
        }
     
    st.code(json.dumps(example_request, indent=2), language="json")

    # Example Response
    st.subheader("📥 Example Response")
    example_response = {
    "Summary": {
        "NIKVerified": True,
        "IDVRecordVerified": True,
        "IDVVerifiedLevel": "M1",
        "IDVContactVerifiedLevel": "P2",
        "IDVMultiLevelVerification": False
    },
    "ReturnItems": {
        "ADDRESS": "Hermosillo Hermosillo Sonora 83000.0"
    },
    "Scoring": {
        "SourceStatus": "Successful",
        "ErrorMessage": "",
        "NameMatchLevel": "Exact Match",
        "FullNameScore": 100,
        "FirstNameScore": 100,
        "MiddleNameScore": 70,
        "SurnameScore": 100,
        "AddressMatchLevel": "Full Match",
        "FullAddressScore": 100,
        "AddressElement1Score": 100,
        "AddressElement2Score": 100,
        "AddressElement3Score": 100,
        "AddressElement4Score": 100,
        "DOBMatch": True,
        "MobileMatch": True,
        "EmailMatch": True
    },
    "Description": {
        "IDVVerifiedLevel": {
            "M1": "Full Name Full Address DOBMatch",
            "N1": "Full Name Full Address Match",
            "M2": "Full Name DOBMatch",
            "P1": "Full Name, Mobile, and Email",
            "P2": "Full Name and Mobile",
            "P3": "Full Name and Email"
        },
        "MultiSourceLevel": {
            "true": "M1>=2 or (M1>=1 and M2>=1) or (M1>=1 and N1>=1) or (M2>=1 and N1>=1)",
            "false": "otherwise"
        },
        "NameMatchLevels": {
            "Exact Match": "Full Name Match",
            "Hyphenated Match": "Hyphenated Match",
            "Transposed Match": "Transposed Match",
            "Middle Name Mismatch": "Middle Name Mismatch",
            "Initial Match": "Initial Match",
            "SurName only Match": "SurName only Match"
        }
    }
}
    st.code(json.dumps(example_response, indent=2), language="json")
# Show API Test Button
if st.button("Run in Postman"):
    postman_url = "https://web.postman.co/"
    st.markdown(f"[Open in Postman]({postman_url})", unsafe_allow_html=True)
