import requests
from bs4 import BeautifulSoup

def get_steampulse_data():
    """Fetches Top 10 Sellers and enriches them with Live Player counts."""
    store_url = "https://store.steampowered.com/search/?filter=topsellers"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    
    try:
        response = requests.get(store_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        rows = soup.find_all('a', class_='search_result_row', limit=10)
        
        dashboard_data = []
        for row in rows:
            app_id = row.get('data-ds-appid')
            name = row.find('span', class_='title').text
            
            # Call Steam API for live player count
            api_url = f"https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid={app_id}"
            api_res = requests.get(api_url).json()
            player_count = api_res.get('response', {}).get('player_count', 0)

            dashboard_data.append({
                "id": app_id,
                "name": name,
                "players": f"{player_count:,}", # Format with commas
                "image": f"https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/{app_id}/header.jpg",
                "link": f"https://store.steampowered.com/app/{app_id}/"
            })
        return dashboard_data
    except Exception as e:
        print(f"Error scraping Steam: {e}")
        return []