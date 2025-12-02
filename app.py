#!/usr/bin/env python3
# Google Sheets Connect OAuth Integration Example
# This app demonstrates how to use Posit Connect's OAuth integration with Google Sheets
# to list a user's most recent Google Sheets using the Posit SDK

import os
from flask import Flask, render_template, request
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from posit import connect

app = Flask(__name__)

# Initialize the Connect client - runs once at startup
client = connect.Client()

# Connect OAuth Configuration
OAUTH_ID = os.environ.get("CONNECT_OAUTH_ID", "d5af6e61-9b1d-4648-86d4-635f7178ee5d")  # Integration GUID

# Google API Configuration
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

@app.route('/')
def index():
    """Home page with link to sheets list"""
    return render_template('index.html', authenticated=True)

@app.route('/sheets')
def list_sheets():
    """List the user's most recent Google Sheets using Connect OAuth"""
    try:
        # Read the user-session-token header from the request
        user_session_token = request.headers.get("Posit-Connect-User-Session-Token")

        if not user_session_token:
            return "Not running in Posit Connect or user session token not available", 500

        # Fetch the viewer's access token using the Posit SDK
        # Pass the integration GUID using the audience parameter
        oauth_creds = client.oauth.get_credentials(user_session_token, audience=OAUTH_ID)
        access_token = oauth_creds.get("access_token")

        if not access_token:
            return "Could not get access token from Connect OAuth integration. Make sure the OAuth integration is associated with this content.", 500

        # Create credentials from tokens
        credentials = Credentials(
            token=access_token,
            refresh_token=None,  # Connect handles token refresh
            token_uri=None,
            client_id=OAUTH_ID,
            scopes=SCOPES
        )

        # Build the Google Sheets API client
        service = build('sheets', 'v4', credentials=credentials)

        # Call the Sheets API to get file metadata
        drive_service = build('drive', 'v3', credentials=credentials)
        results = drive_service.files().list(
            q="mimeType='application/vnd.google-apps.spreadsheet'",
            orderBy='modifiedTime desc',
            pageSize=5,
            fields="files(id, name, modifiedTime, webViewLink)"
        ).execute()

        sheets = results.get('files', [])

        return render_template('sheets.html', sheets=sheets)

    except Exception as e:
        # If there's an error, show the error message
        error_message = f"Error accessing Google Sheets API: {str(e)}"
        print(error_message)
        return error_message, 500

if __name__ == '__main__':
    # This will only be used when running outside of Connect
    # which isn't the intended use case, but helpful for debugging
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)