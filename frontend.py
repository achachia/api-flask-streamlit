import streamlit as st 
import requests

def main():
    st.title('Streamlit Frontend for Flask API')
    response = requests.get('http://127.0.0.1:8080/api/data')
    data = response.json()
    st.write(f"Data from Flask API: {data['data']}")

if __name__ == '__main__':
    main()
