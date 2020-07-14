# Create a script that let the user type in a search term and opens and search on the browser for that term on google. 
import requests
import webbrowser

google_search_url = 'https://www.google.com/search?q='

input_search_string = input('Enter a query to search in Google: ')
webbrowser.open(google_search_url+input_search_string)    # O/P: Opens a new default browser - tab

#google_api_url = 'https://www.googleapis.com/webmasters/v3'

#search_query = requests.put(google_api_url)

'''

- Step 1: Go to -- https://console.developers.google.com/flows/enableapi?apiid=webmasters&credential=client_key
and create a new project, 

### OPTIONAL  #####

- The API is enabled
The project has been created and Undefined parameter - API_NAMES has been enabled.

- Go to credentials: 

- Create credentials --> OAuth Client ID 

#### END - OPTIONAL #####

- Step 2: pip3 install beautifulsoup4
- pip install google

'''

