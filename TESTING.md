# Testing the Google Sheets Connect OAuth Application

This document provides instructions for testing the Google Sheets OAuth application on Posit Connect.

## Prerequisites

1. A Posit Connect server with Google OAuth integration configured
   - Our Connect server is at: `https://connect-helm.local.cofer.me/`
   - The Google OAuth integration GUID is: `d5af6e61-9b1d-4648-86d4-635f7178ee5d`

2. Google Sheets API enabled in your Google Cloud project

## Deployment and Testing on Posit Connect

1. **Deploy the application to Posit Connect**:
   - Use the "Publish" button in RStudio or Posit Workbench
   - Or deploy via the Connect dashboard by creating a new content item

2. **Associate the OAuth integration**:
   - After deployment, navigate to your application's settings in Connect
   - Go to the "OAuth" tab
   - Select the Google OAuth integration
   - Save the settings

3. **Access and test the application**:
   - Open the application through Connect's URL
   - Click "List My Recent Google Sheets"
   - The application will display your 5 most recent Google Sheets with links to open them

## Troubleshooting

1. **OAuth Integration Issues**:
   - Verify that the Google OAuth integration is correctly configured in Connect
   - Check that the integration GUID in the application (`d5af6e61-9b1d-4648-86d4-635f7178ee5d`) matches your Connect integration
   - Ensure the OAuth integration is associated with your application content

2. **Environment Variable Access**:
   - Check Connect logs for OAuth-related errors
   - Verify that the Connect server URL is correct (`https://connect-helm.local.cofer.me/`)
   - Make sure Connect is properly injecting the OAuth token into the application's environment

3. **Google API Errors**:
   - Ensure the OAuth integration includes the necessary scopes (`https://www.googleapis.com/auth/spreadsheets.readonly`)
   - Check that the Google Sheets API is enabled in your Google Cloud project
   - Verify the user has access to Google Sheets

## How the Application Works

The application uses Connect's environment variables to securely access Google Sheets:

1. When a user accesses the application, Connect automatically injects OAuth tokens into the environment
2. The application reads these tokens from environment variables with names like `CONNECT_OAUTH_{GUID}`
3. The application creates Google API credentials using this token
4. These credentials are used to query the Drive API for the user's most recent sheets
5. The results are displayed in a simple web interface

All authentication is handled automatically by Connect, with no need for browser-based OAuth flows or token storage.