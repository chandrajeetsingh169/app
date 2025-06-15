import streamlit as st
import webbrowser

st.title("Tab Manager")
st.subheader("Manage your tabs here")
st.markdown("""<hr style='border: 5px solid black;'>""",unsafe_allow_html=True)
st.header("primary tab")


# Initialize session state for inputs
if "input_count" not in st.session_state:
    st.session_state.input_count = 1

# Button to add more inputs
if st.button("Add another link"):
    st.session_state.input_count += 1

# Display inputs based on count
links = []
for i in range(st.session_state.input_count):
    link = st.text_input(f"Link {i+1}", key=f"link_{i}", placeholder="https://example.com")
    links.append(link)

# Use the first link as the primary tab
a = links[0] if links and links[0] else ""

if a and st.button("Open Link", key="primary_tab_open"):
    st.write("Opening the link...")
    webbrowser.open(a)
    st.divider()
    st.write("Link opened successfully!")
    st.divider()

if not a:
    st.write("No link provided. Please enter a link to open.")

for i in range(st.session_state.input_count):
    def save_link():
        link = st.session_state.get(f"link_{i}", "")
        if link:
            st.session_state[f"link_{i}"] = link
            st.success(f"Link {i+1} saved successfully!")
    link = st.session_state.get(f"link_{i}", "")
    if link:
        st.markdown(f"<a href='{link}' target='_blank'>{link}</a>", unsafe_allow_html=True)
        st.button("Save Link", key=f"save_link_{i}", on_click=save_link)
st.markdown(
    "<hr style='border: 1px solid black;'>",
    unsafe_allow_html=True
)


# Inject custom CSS with st.markdown
st.markdown(
    """
    <style>
    .stApp {
        background-color: lightblue; /* background */
        color: brown; /* text */
        ; /* text */
    }
    .stButton>button {
        text-transform: lowercase;
        background-color: #D1A074; /* skin */
        color:blue ; /* text */}
        stButton>button:hover {
            background-color: #D1A074; /* skin */
            color: black; /* text */
        }
        stTextInput>input {
            background-color: ##FF0000; /* skin */
            color: black; /* text */
        }
        stTextInput>input:focus {
            background-color: #FF0000; /* skin */
            color: black; /* text */
        }
        stTextInput>input::placeholder {
            color: red; /* placeholder text */
        }
        stTextInput>input:focus::placeholder {
            color: red; /* placeholder text */
        }
        stTextInput>input:focus {
            border-color: #D1A074; /* skin */
            box-shadow: 0 0 5px #D1A074; /* skin */
        }
        stlistContainer {
            color: brown; /* text */
        }
    </style>
    """,
    unsafe_allow_html=True
)

 
st.divider()
