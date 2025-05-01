import streamlit as st
from datetime import datetime

def get_ordinal(n):
    if 10 <= n % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return str(n) + suffix

def smart_date_formatter(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        day = get_ordinal(date_obj.day)
        return date_obj.strftime(f'%A, %B {day}, %Y')
    except ValueError:
        return "❌ Invalid date format. Please use YYYY-MM-DD."

# Streamlit App
st.title("📅 Smart Date Formatter")
st.write("Convert a date like `2025-05-01` into a smart readable format.")

date_input = st.text_input("Enter a date (YYYY-MM-DD)")

if date_input:
    formatted = smart_date_formatter(date_input)
    st.success(f"Formatted Date: {formatted}")


