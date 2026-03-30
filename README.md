# SteamPulse: Live Market & Engagement Dashboard


**SteamPulse** is a full-stack Flask application that bridges the gap between commercial success and real-time player engagement. By aggregating data from the **Steam Store** and the **Official Steam Web API**, it provides a unified view of the current "Top 10 Sellers" alongside their live concurrent player counts.


---


## The Problem Solved
Steam's "Top Sellers" list is ranked by revenue, which can be misleading. A game might be a top seller due to a price spike or a pre-order campaign but have very few active players. **SteamPulse** allows analysts and gamers to validate "market hype" with "live heat" (actual player activity) in a single, scannable dashboard.


## Tech Stack
* **Backend:** Python 3.10+, Flask
* **Scraping:** BeautifulSoup4 (for unstructured HTML parsing)
* **API Integration:** RESTful requests to the SteamWorks Web API (JSON)
* **Frontend:** Jinja2 Templates, HTML5, Modern CSS3
* **Data Handling:** Regex (Regular Expressions) for AppID extraction


## How It Works
1. **Extraction:** The app scrapes the `topsellers` page of the Steam Store to identify the current top 10 trending apps.
2. **Normalization:** It uses Regex to isolate the unique `AppID` from each store URL.
3. **Enrichment:** It calls the official `GetNumberOfCurrentPlayers` Steam API for each AppID to fetch live engagement stats.
4. **Transformation:** Data is combined into a clean Python dictionary and passed to a dynamic frontend.


## Installation & Setup
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/steampulse.git](https://github.com/yourusername/steampulse.git)
   cd steampulse