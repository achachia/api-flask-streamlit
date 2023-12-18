
/******************************** Exemple code ************************************/
import streamlit as st

st.session_state['answer'] = ''!

st.write(st.session_state)

realans = ['', 'abc', 'edf']

if  st.session_state['answer'] in realans:
    answerStat = "correct"
elif st.session_state['answer'] not in realans:
    answerStat = "incorrect"

st.write(st.session_state)
st.write(answerStat)
/**********************************************************/

from flask import Flask, render_template
import streamlit as st

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/streamlit')
def streamlit():
    st.set_page_config(page_title="My Streamlit App")
    st.write("Hello, world!")
if __name__ == '__main__':
    app.run()

index.html
<!DOCTYPE html>
<html>
  <head>
    <title>My Flask App</title>
  </head>
  <body>
    <h1>Welcome to my Flask app</h1>
    <iframe src="/streamlit" width="100%" height="800"></iframe>
  </body>
</html>

/*********************************************************/   

import streamlit as st 
import requests

def main():
    st.title('Streamlit Frontend for Flask API')
    response = requests.get('http://localhost:5000/api/data')
    data = response.json()
    st.write(f"Data from Flask API: {data['data']}")

if __name__ == '__main__':
    main()
