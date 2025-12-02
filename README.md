# Posit Connect Google Sheets OAuth Integration Example

WARNING: This code is AI generated to serve as an Example, not as a production-ready implementation. There are likely a number of security issues in this repository, and for it's purpose, there isn't a reason to resolve them.

This is a simple Flask web application that demonstrates how to use Posit Connect's OAuth integration with Google to access the Google Sheets API and list the user's most recent sheets. This application uses the Posit Connect SDK to securely obtain OAuth tokens.

## Requirements

- Posit Connect with Google OAuth Integration configured
- Python 3.9 or higher
- Posit Connect SDK (`posit-sdk` package)

## Setup Instructions

1. **Configure Google OAuth in Posit Connect:**
   - Follow the instructions at https://docs.posit.co/connect/admin/integrations/oauth-integrations/google/
   - Make sure to enable the Google Sheets API in your Google Cloud project
   - Add the necessary scopes: `https://www.googleapis.com/auth/spreadsheets.readonly`

2. **Deploy the application to Posit Connect:**
   - Use the Posit Publisher extension in Posit Workbench or the Connect UI
   - The application is pre-configured to use the Google OAuth integration with GUID: `d5af6e61-9b1d-4648-86d4-635f7178ee5d`, replace this with your Google Sheet integration guid
   - If needed, you can override this by setting the `CONNECT_OAUTH_ID` environment variable in Connect

3. **Associate the OAuth Integration with the Content:**
   - After deployment, go to your application's settings in Connect
   - Navigate to the "OAuth" tab
   - Select the Google OAuth integration
   - Save the settings

## How it Works

1. The application initializes the Posit Connect Client at startup
2. When a user accesses the application, it reads the Posit Connect user session token from the request headers
3. The application uses the Connect SDK to fetch the OAuth credentials for the user
4. These credentials are used to authenticate requests to the Google Sheets API
5. The application retrieves and displays the user's most recent Google Sheets

## Application Structure

- `app.py` - Main Flask application that uses the Posit Connect SDK for OAuth
- `templates/` - HTML templates for the user interface
- `requirements.txt` - Python package dependencies including the Posit Connect SDK
- `manifest.json` - Posit Connect deployment manifest

## Using the Posit Connect SDK

This application demonstrates how to use the Posit Connect SDK to obtain OAuth tokens:

```python
from posit import connect

# Initialize the Connect client
client = connect.Client()

# Get the user session token from the request headers
user_session_token = request.headers.get("Posit-Connect-User-Session-Token")

# Fetch OAuth credentials for the user
oauth_creds = client.oauth.get_credentials(user_session_token, audience=OAUTH_ID)
access_token = oauth_creds.get("access_token")
```

## Important Notes

- This application is designed to run ONLY on Posit Connect
- Users must have a valid Google account with access to Google Sheets
- The Posit Connect SDK must be installed via pip: `pip install posit-sdk`
- This approach provides a more secure and reliable method for obtaining OAuth tokens