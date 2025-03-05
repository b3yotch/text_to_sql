from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-1.5-pro-latest')

    response = model.generate_content([prompt[0], question])
    return response.text.strip()

def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        return rows
    except sqlite3.Error as e:
        return f"Error executing query: {e}"

prompt = [
    """
    You are an expert in converting English questions to SQL queries!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION.
    
    For example: 
    Example 1 - How many entries of records are present?
    The SQL command will be something like this: SELECT COUNT(*) FROM STUDENT;

    Example 2 - Tell me all the students studying in the Data Science class?
    The SQL command will be something like this: SELECT * FROM STUDENT WHERE CLASS = 'Data Science';
    
    Also, the SQL code should not have ''' in the beginning or end and no word 'SQL' in the output.
    """
]

st.set_page_config(page_title="I can retrieve any SQL query")
st.header("Gemini app to retrieve SQL Data")

question = st.text_input("Input", key='input')
submit = st.button("Ask the question")

if submit:
    response = get_gemini_response(question, prompt)
    
    # Check if the response is a valid SQL query before attempting to run it
    if response.lower().startswith("select"):
        result = read_sql_query(response, "student.db")
        st.subheader("Query Result:")
        if isinstance(result, list):
            for row in result:
                st.write(row)
        else:
            st.error(result)
    else:
        st.error("Invalid SQL query generated.")
    
    st.write("Generated SQL Query:", response)

