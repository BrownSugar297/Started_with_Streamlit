import streamlit as st
from streamlit_autorefresh import st_autorefresh
import plotly.graph_objects as go

st.set_page_config(page_title="Mars Lander", layout="wide")

st.markdown("""
    <style>
    div.stButton > button {
        color: white !important;
        border: none !important;
        font-weight: bold !important;
        height: 3em !important;
    }
    button#push_thrust {
        background-color: #ff4b4b !important;
    }
    button#restart {
        background-color: #28a745 !important;
    }
    div.stButton > button:hover {
        opacity: 0.8 !important;
        border: 1px solid white !important;
    }
    </style>
""", unsafe_allow_html=True)

st_autorefresh(interval=300, key="lander_loop")

if 'alt' not in st.session_state:
    st.session_state.update({'alt': 100.0, 'vel': 0.0, 'fuel': 100, 'status': "FLYING"})

def thrust():
    if st.session_state.fuel > 0 and st.session_state.status == "FLYING":
        st.session_state.vel -= 3.5
        st.session_state.fuel -= 2

if st.session_state.status == "FLYING":
    st.session_state.vel += 0.7
    st.session_state.alt -= st.session_state.vel
    if st.session_state.alt <= 0:
        st.session_state.alt = 0
        st.session_state.status = "LANDED ✅" if st.session_state.vel < 6 else "CRASHED 💥"

game_col, dash_col = st.columns([2, 1]) 

with game_col:
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[0, 10], y=[0, 0], fill='toself', line=dict(color='red', width=6)))
    fig.add_trace(go.Scatter(x=[5], y=[st.session_state.alt], mode="markers", 
                             marker=dict(symbol="triangle-up", size=35, color="white", line=dict(color="gray", width=2))))
    fig.update_layout(template="plotly_dark", height=350, margin=dict(l=10, r=10, t=10, b=10),
                      yaxis=dict(range=[-10, 110], showgrid=False, zeroline=False, visible=False), 
                      xaxis=dict(visible=False), showlegend=False)
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

with dash_col:
    st.subheader("Telemetry")
    st.metric("Altitude", f"{st.session_state.alt:.0f} m")
    st.metric("Velocity", f"{st.session_state.vel:.1f} m/s", delta=f"{st.session_state.vel:.1f}", delta_color="inverse")
    st.progress(max(0, st.session_state.fuel) / 100, text=f"Fuel: {st.session_state.fuel}%")
    
    st.divider()
    
    if st.session_state.status == "FLYING":
        st.button("🔥 PUSH THRUST", on_click=thrust, key="push_thrust", use_container_width=True)
    else:
        st.subheader(st.session_state.status)
        if st.button("Restart", key="restart", use_container_width=True):
            st.session_state.update({'alt': 100.0, 'vel': 0.0, 'fuel': 100, 'status': "FLYING"})
            st.experimental_rerun()