import requests
import os

ODDS_API_KEY = os.getenv("ODDS_API_KEY")

def fetch_odds(sport="americanfootball_nfl", region="us", market="h2h"):
    url = f"https://api.the-odds-api.com/v4/sports/{sport}/odds"
    params = {
        "apiKey": ODDS_API_KEY,
        "regions": region,
        "markets": market,
        "oddsFormat": "american"
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        return []
    return response.json()
