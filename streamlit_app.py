import streamlit as st
import json
import pandas as pd

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
    example_request =  {
        "CountryPrefix": "indonisia",
        "IDNumber": "1171015704980001",
        "FirstName":"Arfian",
        "MiddleName" : "Putra",
        "Surname":"Marhennata",
        "Dob":"1998-04-17",
        "AddressElement1": "Baiturrahman",
        "AddressElement2": " Kota Banda",
        "AddressElement3": "Aceh Aceh",
        "AddressElement4": "23244",
        "Mobile" : "08228992992",
        "Email" : ""
        }
    st.code(json.dumps(example_request, indent=2), language="json")

    # Example Response
    st.subheader("📥 Example Response")
    example_response = {
    "Summary": {
        "NIKVerified": True,
        "IDVRecordVerified": True,
        "IDVVerifiedLevel": "N1",
        "IDVContactVerifiedLevel": "P2",
        "IDVMultiLevelVerification": False
    },
    "ReturnItems": {
        "Address": "Baiturrahman Kota Banda Aceh Aceh, 23244"
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
    }
}
    st.code(json.dumps(example_response, indent=2), language="json")


with col2:
    st.subheader(':orange[**POST**] Mexico Residential')
    st.markdown("🔹 **No. of Records 49.5 million**")
    st.subheader("📤 Example Request")
    example_request =    {
            "CountryPrefix": "mx",
            "IDNumber": "SITM970206HSRQRR01",
            "FirstName":"MARTHA",
            "MiddleName" : "CECILIA SIQUEIROS",
            "Surname":"TARAZON",
            "Dob":"1997-02-06",
            "AddressElement1": "Hermosillo",
            "AddressElement2": "Hermosillo",
            "AddressElement3": "Sonora",
            "AddressElement4": "83000.0",
            "Mobile" : "6622145317",
            "Email" : ""
            }
     
    st.code(json.dumps(example_request, indent=2), language="json")

    # Example Response
    st.subheader("📥 Example Response")
    example_response = {
    "Summary": {
        "NIKVerified": True,
        "IDVRecordVerified": True,
        "IDVVerifiedLevel": "N1",
        "IDVContactVerifiedLevel": "P2",
        "IDVMultiLevelVerification": False
    },
    "ReturnItems": {
        "Address": "Hermosillo Hermosillo Sonora 83000.0"
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
    }
}
    st.code(json.dumps(example_response, indent=2), language="json")


def display_match_explanation_new():
    """
    Displays an expander in the Streamlit app with bullet points explaining key concepts of the matching process.
    """
    with st.expander(":red[**Detailed Description**]"):
        st.markdown("""
        :green[**1) IDV Verified Level**] : A multi-attribute determination of verification status.
        - Consolidates matches across **Name**, **Address**, and **Date of Birth (DOB)** into a single outcome.
        """)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("- **M1**: Full Name, Full Address, and DOB Match")
            st.markdown("- **N1**: Full Name and Full Address Match")
        with col2:
            st.markdown("- **M2**: Full Name and DOB Match")

        st.markdown("""
        Verification Level Hierarchy: The verification levels are prioritized as : **M1 > N1 > M2**
        """)


        st.markdown("""
         :green[**2) IDV Contact Verified Level**] : This process determines contact verification by evaluating multiple attributes.  
        - Matches across **Name**, **Mobile**, and **Email** are combined into a unified verification outcome.
        """)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("- **P1**: Match on Full Name, Mobile, and Email")
            st.markdown("- **P2**: Match on Full Name and Mobile")
        with col2:
            st.markdown("- **P3**: Match on Full Name and Email")

        st.markdown("""
         Verification Level Priority: The verification levels are ranked by reliability as follows: **P1**  > **P2** > **P3**
        """)

        st.markdown("""
         :green[**3) IDV Record Verified**] : A validation indicator determined by Single source.
        - **True**: The record is verified and meets the required validation criteria.  
        - **False**: The record is not verified and fails to meet the validation standards.  
        """)

        st.markdown("""
         :green[**4) IDV Multi Level Verification**] : An advanced validation indicator determined by multiple sources.
        - **True**: The record is validated by meeting one or more multi-condition criteria, ensuring higher reliability.  
        - **False**: The record does not satisfy the multi-condition criteria, indicating insufficient validation from multiple sources.  

        A record is marked as **True** if any of the following conditions are met:  """)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("- **M1** >= 2")
            st.markdown("- **M1** >= 1 **and** **M2** >= 1")
        with col2:
            st.markdown("- **M1** >= 1 **and** **N1** >= 1")
            st.markdown("- **M2** >= 1 **and** **N1** >=1 ")
        
         
          
         

        st.markdown("""
         :green[**5) Profile**] : This section provides the database records that align with the input data.  
        - Returns data entries from the database that match the provided input criteria.  
        """)

        

        st.markdown("""
        :green[**6) Scoring**] : A score quantifying how closely each input matches the expected values.""")
        col1, col2 = st.columns(2)
        st.markdown("- (60-99) indicates a fuzzy match.")
        with col1:
            st.markdown("- 100 indicates an exact match.")
        with col2:
            st.markdown("- 0 indicates no match. ")

        st.markdown(""":green[**6) Full Name Similarity**] : Measures how well the full input name matches the target name.""")


        st.markdown(""":green[**7) Name Match Level**] : Categorizes overall name matching.""")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("- Exact Match")
            st.markdown("- Middle Name Mismatch")
            st.markdown("- SurName Only Match")
        with col2:
            st.markdown("- Initial Match")
            st.markdown("- Hyphenated Match")
            st.markdown("- Transposed Match")

display_match_explanation_new()

# Show API Test Button
if st.button("Run in Postman"):
    postman_url = "https://web.postman.co/"
    st.markdown(f"[Open in Postman]({postman_url})", unsafe_allow_html=True)
