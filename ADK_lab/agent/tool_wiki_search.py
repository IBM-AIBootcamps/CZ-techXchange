from ibm_watsonx_orchestrate.agent_builder.tools import *
import requests
from urllib.parse import quote

@tool
def wiki_search(query : str) -> str:
    """
    Pokud má uživatel konkrétní dotaz, vyhledává informace na internetu pomocí Wikpedia API.

    :param query: Dotaz uživatele, například "Co je to inflace?"
    
    :returns: Vrátí summarizaci informace dohledané pomocí Wikpedia API vztažené k dotazu.
    """
    url = "https://cs.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json"
    }
    r = requests.get(url, params=params)
    results = r.json().get("query", {}).get("search", [])[:3]
    title = results[0]["title"]
    encoded_title = quote(title.replace(" ", "_"))
    url = f"https://cs.wikipedia.org/api/rest_v1/page/summary/{encoded_title}"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        return data.get("extract")
    return None