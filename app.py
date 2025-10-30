import streamlit as st
from datetime import date
import base64

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="Days Since We Met 💕",
    page_icon="💖",
    layout="centered"
)

# -------------------------
# BACKGROUND IMAGE FUNCTION
# -------------------------
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image:
        encoded_string = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            background-repeat: no-repeat;
        }}
        /* Add subtle overlay for text readability */
        .stApp::before {{
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: rgba(255, 255, 255, 0.5);
            z-index: 0;
        }}
        /* Make content visible above overlay */
        [data-testid="stMarkdownContainer"], [data-testid="stMetric"], .st-bf {{
            z-index: 1;
            position: relative;
        }}
        /* Center the metrics nicely */
        .css-1lcbmhc, .css-12oz5g7 {{
            text-align: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# -------------------------
# SET BACKGROUND IMAGE
# -------------------------
# Option 1: Use a local image in the same folder
add_bg_from_local("background.jpeg")

# Option 2: If you prefer to use an online URL, comment the above line and use below:
# st.markdown("""
# <style>
# .stApp {
#     background-image: url("https://images.unsplash.com/photo-1526778548025-fa2f459cd5c1");
#     background-size: cover;
#     background-position: center;
#     background-attachment: fixed;
# }
# </style>
# """, unsafe_allow_html=True)

# -------------------------
# MAIN APP CONTENT
# -------------------------

# Change this to your special start date ❤️
START_DATE = date(2025, 9, 15)

# Calculate time differences
today = date.today()
days_since = (today - START_DATE).days
months_since = round(days_since / 30.44, 2)
years_since = round(days_since / 365.25, 3)

# Header
st.title("💕 Days Since We Met 💕")
st.markdown("---")

# Info
st.subheader(f"🗓️ We started talking on: {START_DATE.strftime('%B %d, %Y')}")

# Metrics (Days / Months / Years)
col1, col2, col3 = st.columns(3)
col1.metric("Days Together", f"{days_since:,} 💞")
col2.metric("Months Together", f"{months_since}")
col3.metric("Years Together", f"{years_since}")

# -------------------------
# MILESTONE CELEBRATION
# -------------------------
if days_since % 100 == 0 and days_since != 0:
    st.balloons()
    st.success(f"🎉 Today is your {days_since}th day together! 💕")
elif (days_since + 1) % 100 == 0:
    st.info(f"✨ Tomorrow is your {days_since + 1}th day together!")

# -------------------------
# FOOTER
# -------------------------
st.markdown("---")
st.caption("Made with ❤️ by You")