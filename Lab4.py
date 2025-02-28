import streamlit as st
from PIL import Image
import requests
from io import BytesIO

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
    st.image(comparisons[selection][0], caption="Hubble Telescope", use_column_width=True)
with col2:
    st.image(comparisons[selection][1], caption="Webb Telescope", use_column_width=True)

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

# Interactive Markdown for Observations
st.markdown("### Key Differences & Observations")
st.text_area("Write your observations here...", placeholder="What differences do you notice between the images?")

# Additional details
st.markdown("""
### Why Webb is Different?
- **Webb Telescope** captures infrared light, revealing previously unseen cosmic details.
- **Hubble Telescope** primarily captures visible and ultraviolet light.
- Webb’s images show more structure, depth, and clarity compared to Hubble’s observations.
""")

st.sidebar.markdown("---")
st.sidebar.subheader("Rate this App")
feedback = st.sidebar.radio("How do you like this comparison app?", ["Excellent", "Good", "Average", "Needs Improvement"])
st.sidebar.write(f"You selected: {feedback}")

st.sidebar.success("Explore the wonders of space with these interactive comparisons!")
