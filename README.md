# Text-to-SQL using Gemini API

## Overview
This project is a **Streamlit-based web application** that converts natural language questions into SQL queries using **Google Gemini API**. It then executes the generated SQL queries on a **SQLite database** and displays the results.

## Features
- Converts **English questions** into SQL queries
- Uses **Google Gemini API** for query generation
- Fetches and displays results from a **SQLite database**
- **Streamlit UI** for an interactive experience

## Installation & Setup
### **1. Clone the Repository**
```sh
git clone https://github.com/b3yotch/text_to_sql.git
cd text_to_sql
```

### **2. Create a Virtual Environment & Install Dependencies**
```sh
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
pip install -r requirements.txt
```

### **3. Set Up Environment Variables**
Create a `.env` file and add your Google Gemini API key:
```
GOOGLE_API_KEY=your_api_key_here
```

### **4. Run the Application**
```sh
streamlit run sql.py
```

## Usage
1. Enter your question in plain English.
2. Click **Ask the question**.
3. The app generates an SQL query, executes it on the SQLite database (`student.db`), and displays the result.

## Example Queries

![Screenshot (25)](https://github.com/user-attachments/assets/1b586f9a-819c-4abd-8a2d-631fd8bdb64f)

## Issues & Debugging
- If the **Gemini API** is not responding, check your API key.
- If SQLite returns no results, ensure that `student.db` has the correct data.

## Contributing
Feel free to fork the repository, make improvements, and submit a **pull request**.



