# main.py
import streamlit as st
import streamlit_authenticator as stauth
from odds_api import fetch_odds
from ev_utils import calculate_ev, detect_arbitrage
from gpt_summaries import generate_summary
import yaml
from yaml.loader import SafeLoader
import os
from dotenv import load_dotenv

# Load env variables
load_dotenv()

# Load config
def load_auth_config():
    with open("auth_config.yaml") as file:
        return yaml.load(file, Loader=SafeLoader)

config = load_auth_config()

# Authenticator setup
authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"]
)

# This line now just renders the login form
authenticator.login()

# This block checks the session state to see if the user is logged in
if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
    # YOUR APP'S LOGIC GOES HERE

elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')

elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')

if auth_status:
    authenticator.logout("Logout", "sidebar")
    st.sidebar.success(f"Welcome {name} 👋")

    st.title("SharpEdge AI – Real-Time EV + Arbitrage Betting")

    games = fetch_odds()
    if not games:
        st.warning("No live odds available.")
    else:
        for game in games:
            teams = " vs ".join(game["teams"])
            st.subheader(teams)
            for book in game["bookmakers"][:1]:
                outcomes = book["markets"][0]["outcomes"]
                odds_dict = {o["name"]: o["price"] for o in outcomes}

                for team, odds in odds_dict.items():
                    ev = calculate_ev(odds, 0.55)  # TODO: Replace with model/user input
                    st.write(f"**{team}**: {odds} — EV: `{ev:+.2f}`")

                with st.expander("💬 AI Summary"):
                    st.info(generate_summary(teams, odds_dict))

                if len(odds_dict) == 2:
                    a, b = list(odds_dict.values())
                    if detect_arbitrage(a, b):
                        st.success("📈 Arbitrage Opportunity Detected!")

    if username == "premium":
        st.markdown("### 💎 Premium Picks")
        st.success("🏀 Heat ML +130 — 3U Play")
    else:
        st.warning("🔐 Upgrade to premium to unlock exclusive picks.")

elif auth_status is False:
    st.error("Invalid credentials")
elif auth_status is None:
    st.warning("Enter your login details")
