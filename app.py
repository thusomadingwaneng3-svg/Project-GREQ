import streamlit as st
import pandas as pd
import hashlib

# --- APP CONFIG ---
st.set_page_config(page_title="Project GREQ", page_icon="🌍")

# --- INITIALIZE "DATABASE" (Simulated in Session Memory) ---
if 'mesh' not in st.session_state:
    st.session_state.mesh = []
if 'trust' not in st.session_state:
    st.session_state.trust = {"Founder": 1.0}

# --- HEADER ---
st.title("🌍 Project GREQ")
st.subheader("The Global Resource Equalizer")
st.write("Bridging needs and surplus without money.")

# --- SIDEBAR: TRUST & PROFILE ---
with st.sidebar:
    st.header("Your Profile")
    user_id = st.text_input("Enter Username", "Citizen_01")
    if user_id not in st.session_state.trust:
        st.session_state.trust[user_id] = 0.5
    st.metric("Trust Score", f"{st.session_state.trust[user_id] * 100}%")
    st.info("Help others to increase your score.")

# --- TABBED INTERFACE ---
tab1, tab2, tab3 = st.tabs(["📢 Broadcast", "🔍 Find Resources", "📚 Knowledge"])

with tab1:
    st.header("Report a Surplus or Need")
    action_type = st.radio("What are you doing?", ["Offering Surplus", "Reporting a Need"])
    category = st.selectbox("Category", ["Food", "Tools", "Skills", "Medicine", "Education"])
    details = st.text_area("Details", placeholder="Describe what you have or what is missing...")
    
    if st.button("Broadcast to Mesh"):
        new_entry = {
            "User": user_id,
            "Type": action_type,
            "Category": category,
            "Details": details,
            "Trust": st.session_state.trust[user_id]
        }
        st.session_state.mesh.append(new_entry)
        st.success("Broadcast sent to local network!")

with tab2:
    st.header("Local Mesh Activity")
    if not st.session_state.mesh:
        st.write("No active broadcasts in your area.")
    else:
        df = pd.DataFrame(st.session_state.mesh)
        st.table(df)
        
        selected_index = st.number_input("Enter row number to help/interact", min_value=0, max_value=len(st.session_state.mesh)-1, step=1)
        if st.button("Resolve This Imbalance"):
            # Update trust for the person who helped
            st.session_state.trust[user_id] += 0.05
            st.session_state.mesh.pop(selected_index)
            st.balloons()
            st.success("Imbalance resolved! Your Trust Score has increased.")

with tab3:
    st.header("Offline Knowledge Seeds")
    seeds = {
        "Water Purification": "Filter through sand -> Boil 1 min.",
        "First Aid": "Pressure on wounds -> Elevate limb.",
        "Solar Oven": "Lined box + Glass + Black paint."
    }
    topic = st.selectbox("Select Topic", list(seeds.keys()))
    st.info(seeds[topic])
    if st.button("Download Offline Seed"):
        st.write(f"Seed for {topic} saved to local storage.")
