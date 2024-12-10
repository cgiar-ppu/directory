import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Technical Solutions Directory",
    page_icon="🗃️",
    layout="wide"
)

# Page Title
st.title("Technical Solutions Directory")
st.write("Welcome to our internal directory of technical solutions and dashboards. \
Explore the options below, view details, and find direct links to the resources you need.")

# Some styling options
st.markdown("""
<style>
    .tool-container {
        border: 1px solid #ddd;
        border-radius: 5px;
        padding: 10px;
        margin-bottom: 20px;
        background-color: #f9f9f9;
    }
    .tool-title {
        font-size: 1.2rem;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .tool-description {
        font-size: 0.9rem;
        margin-bottom: 10px;
        color: #555;
    }
    .tool-thumbnail {
        max-width: 100%;
        border-radius: 5px;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Helper function to display a tool or dashboard item
def display_item(title, description, details, link="#", image_url=None):
    with st.container():
        st.markdown('<div class="tool-container">', unsafe_allow_html=True)
        # Image (placeholder)
        if image_url:
            st.image(image_url, use_column_width=True)
        else:
            # Display a placeholder image if none provided
            st.image("https://via.placeholder.com/300x150.png?text=Thumbnail", use_column_width=True)
        
        st.markdown(f'<div class="tool-title">{title}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="tool-description">{description}</div>', unsafe_allow_html=True)
        
        with st.expander("More details"):
            st.write(details)
            st.markdown(f"[Access here]({link})")
        st.markdown('</div>', unsafe_allow_html=True)

# Layout: We'll create two columns: Left for Tools, Right for Dashboards
col1, col2 = st.columns(2)

with col1:
    st.subheader("Tools")
    # Display 6 tools
    display_item(
        title="Tool 1",
        description="Short description of Tool 1.",
        details="Detailed explanation about how Tool 1 works, including examples and instructions.",
        link="https://example.com/tool1"
    )
    display_item(
        title="Tool 2",
        description="Short description of Tool 2.",
        details="Detailed explanation about how Tool 2 works, including examples and instructions.",
        link="https://example.com/tool2"
    )
    display_item(
        title="Tool 3",
        description="Short description of Tool 3.",
        details="Detailed explanation about how Tool 3 works, including examples and instructions.",
        link="https://example.com/tool3"
    )
    display_item(
        title="Tool 4",
        description="Short description of Tool 4.",
        details="Detailed explanation about how Tool 4 works, including examples and instructions.",
        link="https://example.com/tool4"
    )
    display_item(
        title="Tool 5",
        description="Short description of Tool 5.",
        details="Detailed explanation about how Tool 5 works, including examples and instructions.",
        link="https://example.com/tool5"
    )
    display_item(
        title="Tool 6",
        description="Short description of Tool 6.",
        details="Detailed explanation about how Tool 6 works, including examples and instructions.",
        link="https://example.com/tool6"
    )

with col2:
    st.subheader("Dashboards")
    # Display 6 dashboards
    display_item(
        title="Dashboard 1",
        description="Short description of Dashboard 1.",
        details="Detailed explanation about the data sources, filters, and KPIs shown in Dashboard 1.",
        link="https://example.com/dashboard1"
    )
    display_item(
        title="Dashboard 2",
        description="Short description of Dashboard 2.",
        details="Detailed explanation about the data sources, filters, and KPIs shown in Dashboard 2.",
        link="https://example.com/dashboard2"
    )
    display_item(
        title="Dashboard 3",
        description="Short description of Dashboard 3.",
        details="Detailed explanation about the data sources, filters, and KPIs shown in Dashboard 3.",
        link="https://example.com/dashboard3"
    )
    display_item(
        title="Dashboard 4",
        description="Short description of Dashboard 4.",
        details="Detailed explanation about the data sources, filters, and KPIs shown in Dashboard 4.",
        link="https://example.com/dashboard4"
    )
    display_item(
        title="Dashboard 5",
        description="Short description of Dashboard 5.",
        details="Detailed explanation about the data sources, filters, and KPIs shown in Dashboard 5.",
        link="https://example.com/dashboard5"
    )
    display_item(
        title="Dashboard 6",
        description="Short description of Dashboard 6.",
        details="Detailed explanation about the data sources, filters, and KPIs shown in Dashboard 6.",
        link="https://example.com/dashboard6"
    )

# Footer or additional info
st.write("---")
st.write("For questions or support, please reach out to the DevOps team or IT support desk.")
