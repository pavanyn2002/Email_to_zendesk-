import streamlit as st
import requests
import os


API_URL = os.getenv("API_URL", "http://localhost:8080/create-ticket")

st.title("IntelliTicket: AI-Powered Support Ticket Creation")

email_content = st.text_area("Paste your support email here:", height=200)

if st.button("Analyze & Create Ticket"):
    if email_content.strip():
        with st.spinner("Analyzing..."):
            response = requests.post(
                API_URL,
                json={"email_content": email_content}
            )
            if response.status_code == 200:
                result = response.json()
                st.success("Ticket Created!")
                st.write(f"**Summary:** {result['summary']}")
                st.write(f"**Priority:** {result['priority']}")
                st.write(f"**Category:** {result['category']}")
                st.write(f"**Original Email:**\n{result['original_email']}")
            else:
                st.error(f"Error: {response.json().get('detail', 'Unknown error')}")
    else:
        st.warning("Please enter email content.")