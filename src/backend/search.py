from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

load_dotenv() # take environment variables from .env
google_key = os.getenv("G_KEY")
google_cx = os.getenv("G_CX")

# func takes list of extracted terms and returns dict of resultant page titles and links
def google_search(phrases):
    service = build("customsearch", "v1", developerKey=google_key)

    results = [] # contains all results

    for term in phrases:
        resources = {} # contains individual json responses
        
        # make search through search engine api
        data = service.cse().list(
                                q=term,
                                cx=google_cx,
                                num=1,
                                siteSearch="wikipedia.org",
                                siteSearchFilter="i"
                                ).execute()

        # add resultant page title, link and icon to dict
        resources['title'], resources['url'] = data['items'][0]['title'], data['items'][0]['link']
        resources['icon'] = "/".join( (data['items'][0]['link']).split("/")[:5] ) + "/favicon.ico"
        if resources not in results:
            results.append(resources) # add unique resources

    return results[:3] # top 3 unique results