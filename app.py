# app.py
import streamlit as st
from datetime import date

st.set_page_config(page_title="Days Since We Met 💕", page_icon="💖", layout="centered")

# --- EDIT THIS to your start date ---
START_DATE = date(2025, 9, 15)   # <-- change to your date
# -------------------------------------

today = date.today()
days_since = (today - START_DATE).days
months_since = round(days_since / 30.44, 2)
years_since = round(days_since / 365.25, 3)

st.title("💕 Days Since We Met 💕")
st.markdown("---")
st.subheader(f"🗓️ We started talking on: {START_DATE.strftime('%B %d, %Y')}")
st.metric("Days Together", f"{days_since:,} days")
st.metric("Months Together", f"{months_since} months")
st.metric("Years Together", f"{years_since} years")

# special milestone UI
if days_since % 100 == 0 and days_since != 0:
    st.balloons()
    st.success(f"🎉 Today is your {days_since}th day together! 💕")
elif (days_since + 1) % 100 == 0:
    st.info(f"✨ Tomorrow is your {days_since + 1}th day together!")