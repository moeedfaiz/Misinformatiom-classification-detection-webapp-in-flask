from google.oauth2 import service_account
from googleapiclient.discovery import build

# Path to your service account key file
SERVICE_ACCOUNT_FILE = 'serious-energy-432707-a3-1c58b80fdb6f.json'

# Define the scopes
SCOPES = ['https://www.googleapis.com/auth/cse']

# Create credentials from the service account file
credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Build the service
service = build('customsearch', 'v1', credentials=credentials)

# Perform a search
def google_search(query, cse_id):
    res = service.cse().list(q=query, cx=cse_id).execute()
    return res

# Example usage
results = google_search('Example search query', '068275577b6e24d6b')
print(results)
print (results.get("items"))

