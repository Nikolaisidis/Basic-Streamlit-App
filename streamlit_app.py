import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

st.set_page_config(page_title="Autobiography & Portfolio", layout="wide")

st.markdown(
    """
    <style>
    .main {
        background-color: #F2E8C6;
    }

    p, div, span, button, select, input, textarea, footer {
        font-family: Arial, sans-serif;
    }

    .stDataFrame, .stTable {
        border: 1px solid black;
        color: #161D6F;
    }

    footer {
        text-align: center;
        background-color: #DAD4B5;
        color: black;
        padding: 10px;
        margin-top: 20px;
        font-size: 14px;
    }
    
    .stTabs [role="tab"] {
        padding: 10px 100px;
    }
    
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.title("Select Visualization")
show_map = st.sidebar.checkbox("Show the map", value=True)
chart_type = st.sidebar.selectbox(
    "Choose a Chart Type", ["Line Chart", "Bar Chart"])

st.title("Autobiography & Portfolio")
st.write("Hello! I am Alestair Cyril Coyoca, a college student pursuing a Bachelor of Science in Information Technology. Welcome to my autobiography and portfolio, where you can learn more about my journey, experiences, and interests.")

tabs = st.tabs(["Home", "Autobiography", "Portfolio", "Contact"])

with tabs[0]:
    st.header("My Personal Space")
    st.image("profile.jpg",
             caption="I don't take pictures, this was from my SHS photo", width=300)

    st.subheader("My Hobbies")
    interests = st.multiselect(
        "List of hobbies and interests:",
        ["🎶 Listening to Old Songs", "🐱 Cats",
            "🎥 Watching Movies", "🎮 Playing Online Games", "🛌 Sleeping"]
    )
    st.write(f"Selected hobbies and interests: {', '.join(interests)}")

with tabs[1]:
    st.header("Autobiography")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Early Life")
        st.markdown(
            """
            <div style="text-align: justify;">
                I was born in Cebu City, Philippines. I only have one sibling, which is my sister. I remember that when I was a child, I tended to worry a lot to the point where my heart would beat so fast because I would create fake scenarios in my mind. One example I remember is when my marble fell into the basin of our neighbor while she was washing clothes. I worried that it might get picked up by her child and swallowed. When I reached the age of 6-7 years old, while playing hide and seek with my friends, I suddenly looked up at the sky and asked if someone superior really exists. This moment was a turning point for me and had a significant impact on how I think today.
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.subheader("Education")
        education_data = {
            'Degree': ['Elementary', 'Junior High School', 'Senior High School', 'College'],
            'School': ['Basak Community School', 'Cebu City Don Carlos A. Gothong MNHS', 'University of Cebu SHS Department', 'Cebu Institute of Technology University (CIT-U)'],
            'Year': ['2009-2015', '2015-2019', '2019-2021', '2021-Present']
        }
        education_df = pd.DataFrame(education_data)
        st.table(education_df)

    st.subheader("Achievements")
    st.write("""
    - Special Science Class Program (Elementary and High School)
    - Best in ICT (2018 - 2019)
    - Consistent Honor Student since High School
    - Top 8 overall BSIT 2nd year level
    - Parangal Awardee, CIT - U (2021-2022)
    - Dean's Lister 3rd year level
    """)

    st.subheader("Skills")
    st.write("**Technical Skills:** Python, SQL, Data Analysis, Web Development")
    st.write(
        "**Soft Skills:** Leadership, Communication, Teamwork, Proper Time Management")
    st.write("**Languages:** Bisaya, Tagalog, English")

with tabs[2]:
    st.header("Portfolio")

    st.write("""
    As a student, I wanted to build an application that could help the community. During our appdev in 3rd year, my co-members created an app called Palit where it can help local vendors sell their goods to nearby customers. It is kind of inspired by Angkas and Grabfood but we wanted it for more convenience so we used geo-location to detect nearby customers and deliver the goods immediately.
    """)

    st.subheader("Skills Progression Over Time")
    skills_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['SQL', 'Next.js', 'Web Development']
    )
    if chart_type == "Line Chart":
        st.line_chart(skills_data)
    else:
        st.bar_chart(skills_data)

    st.subheader("Commits in Github")
    hours = st.slider(
        "Select the number of commits done per week on projects", 0, 60, 40)

    if show_map:
        st.subheader("One of these dots is the place where I live 😂")
        df_map = pd.DataFrame(
            np.random.randn(1000, 2) / [50, 50] +
            [10.31, 123.89],  # Cebu City coordinates
            columns=['lat', 'lon']
        )
        st.map(df_map)

with tabs[3]:
    st.header("Contact Me")

    contact_info = {
        "Phone": "231-2832",
        "Mobile Number": "09823712394",
        "Email": "alestaircyril12@gmail.com",
        "Address": "Cebu City, Philippines"
    }

    for key, value in contact_info.items():
        st.write(f"**{key}:** {value}")

    contact_form = """
    <style>
        form {
            display: flex;
            flex-direction: column;
            width: 300px;
            margin: 0;
        }
        input, textarea, button {
            margin-bottom: 10px;
            padding: 10px;
            font-size: 16px;
        }
        textarea {
            resize: vertical;
            height: 100px;
        }
    </style>
    <form action="https://formsubmit.co/alestaircyril12@gmail.com" method="POST">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your Message" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

st.write("---")
st.markdown('<footer>© 2024 by Alestair Cyril Coyoca</footer>',
            unsafe_allow_html=True)
