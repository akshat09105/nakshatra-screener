import streamlit as st
import psycopg2
import pandas as pd

def get_connection():
    return psycopg2.connect(
        host=st.secrets["DB_HOST"],
        port=int(st.secrets["DB_PORT"]),
        database=st.secrets["DB_NAME"],
        user=st.secrets["DB_USER"],
        password=st.secrets["KLRahul@1234"],
        sslmode="require"
    )

def get_companies():
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM companies", conn)
    conn.close()
    return df