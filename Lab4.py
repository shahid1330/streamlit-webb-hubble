import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import random

st.set_page_config(page_title="Webb vs Hubble - Space Telescope Comparison", page_icon="🔭", layout="wide")

# Sidebar
st.sidebar.header("🔭 Webb vs Hubble Telescope")
st.sidebar.markdown("Compare images captured by the **Hubble Space Telescope** and the **James Webb Space Telescope**.")
st.sidebar.info("Use the dropdown to choose an image comparison!")
st.sidebar.markdown("[Original Project by John Christensen](https://github.com/JohnEdChristensen/WebbCompare)")
st.sidebar.markdown("---")
st.sidebar.subheader("Select an image to compare")

# Main Header
st.title("🔭 Webb Space Telescope vs Hubble Telescope")

st.markdown("""
### Overview
The **James Webb Space Telescope (JWST)** provides images with higher resolution and greater detail compared to the **Hubble Space Telescope**. Use the sections below to explore their differences.
""")

# Image comparison dictionary
comparisons = {
    "Southern Ring Nebula": [
        "https://www.webbcompare.com/img/hubble/southern_nebula_700.jpg",
        "https://www.webbcompare.com/img/webb/southern_nebula_700.jpg"
    ],
    "Galaxy Cluster SMACS 0723": [
        "https://www.webbcompare.com/img/hubble/deep_field_700.jpg",
        "https://www.webbcompare.com/img/webb/deep_field_700.jpg"
    ],
    "Carina Nebula": [
        "https://www.webbcompare.com/img/hubble/carina_2800.png",
        "https://www.webbcompare.com/img/webb/carina_2800.jpg"
    ],
    "Stephan's Quintet": [
        "https://www.webbcompare.com/img/hubble/stephans_quintet_2800.jpg",
        "https://www.webbcompare.com/img/webb/stephans_quintet_2800.jpg"
    ]
}

# Dropdown for selection
selection = st.sidebar.selectbox("Choose an image to compare:", list(comparisons.keys()))

# Display the selected comparison
st.markdown(f"### {selection}")
col1, col2 = st.columns(2)

with col1:
    st.image(comparisons[selection][0], caption="Hubble Telescope", use_container_width=True)
with col2:
    st.image(comparisons[selection][1], caption="Webb Telescope", use_container_width=True)

# Download option for images
st.sidebar.markdown("---")
st.sidebar.subheader("Download Images")

def download_image(url, filename):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.save(filename)
    return filename

if st.sidebar.button("Download Hubble Image"):
    hubble_img = download_image(comparisons[selection][0], "hubble_image.jpg")
    st.sidebar.download_button("Click to Download", hubble_img)

if st.sidebar.button("Download Webb Image"):
    webb_img = download_image(comparisons[selection][1], "webb_image.jpg")
    st.sidebar.download_button("Click to Download", webb_img)

# Key Observations
st.markdown("### Key Differences & Observations")
st.text_area("Write your observations here...", placeholder="What differences do you notice between the images?")

# Why Webb is Different
st.markdown("""
### Why Webb is Different?
- **Webb Telescope** captures infrared light, revealing previously unseen cosmic details.
- **Hubble Telescope** primarily captures visible and ultraviolet light.
- Webb’s images show more structure, depth, and clarity compared to Hubble’s observations.
""")

# Self-Learning Section
st.markdown("## 📚 Self-Learning Section")

# 💡 Random Fact Generator
facts = [
    "The James Webb Space Telescope orbits the Sun, not Earth.",
    "Webb's mirror is over 6 times larger in area than Hubble's.",
    "Infrared light can pass through cosmic dust, which helps Webb reveal hidden stars.",
    "Hubble was launched in 1990; Webb in 2021.",
    "Webb can see galaxies formed just a few hundred million years after the Big Bang."
]

if st.button("💡 Show a Random Space Fact"):
    st.info(random.choice(facts))

# 🧠 Random Quiz Generator
st.markdown("### 🧠 Random Quiz")
quiz_data = [
    {
        "question": "Which telescope captures infrared light?",
        "options": ["Hubble", "Webb", "Both"],
        "answer": "Webb"
    },
    {
        "question": "Which telescope was launched first?",
        "options": ["Hubble", "Webb", "Both launched together"],
        "answer": "Hubble"
    },
    {
        "question": "Which telescope orbits the Sun at Lagrange Point 2?",
        "options": ["Hubble", "Webb", "None"],
        "answer": "Webb"
    },
    {
        "question": "Which telescope primarily captures **visible and ultraviolet** light?",
        "options": ["Webb", "Hubble", "Both"],
        "answer": "Hubble"
    },
    {
        "question": "Which telescope was launched in 2021?",
        "options": ["Hubble", "Webb", "Neither"],
        "answer": "Webb"
    }
]

if "quiz_index" not in st.session_state:
    st.session_state.quiz_index = random.randint(0, len(quiz_data) - 1)

if st.button("🎲 Generate Random Quiz Question"):
    st.session_state.quiz_index = random.randint(0, len(quiz_data) - 1)

q = quiz_data[st.session_state.quiz_index]
user_answer = st.radio(q["question"], q["options"], key=q["question"])

if user_answer:
    if user_answer == q["answer"]:
        st.success("✅ Correct!")
    else:
        st.error(f"❌ Incorrect. The correct answer is: {q['answer']}")

# 📘 Learn More Links
st.markdown("### 📘 Learn More About Space Telescopes")
st.markdown("""
- [🔗 NASA Webb Official Site](https://webb.nasa.gov/)
- [🔗 Hubble Space Telescope Site](https://hubblesite.org/)
- [🔗 How Infrared Astronomy Works (NASA)](https://science.nasa.gov/astrophysics/focus-areas/how-does-infrared-astronomy-work/)
- [🔗 Webb vs Hubble Comparison Video](https://www.youtube.com/results?search_query=webb+vs+hubble)
""")

# Feedback Section
st.sidebar.markdown("---")
st.sidebar.subheader("Rate this App")
feedback = st.sidebar.radio("How do you like this comparison app?", ["Excellent", "Good", "Average", "Needs Improvement"])
st.sidebar.write(f"You selected: {feedback}")
st.sidebar.success("Explore the wonders of space with these interactive comparisons!")
