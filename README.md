# GoogleDriveUploader

# Overview
To upload a file to Google Drive using Python, you can use the Google Drive API along with the google-api-python-client library. Here are the steps you can follow:

# Prerequisites
Make sure you have the following prerequisites before using this project:
  - Python installed
  - Pip installed

# Installation
Use the following commands to install the required Python libraries:
  - pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

# Getting Started
  # Step 1: Set up Google Drive API
  1. Go to the Google API Console:
      - Open your web browser and navigate to the Google API Console.
  2. Create a new project:
      - Click on the project dropdown menu at the top of the page.
      - Click on the "New Project" button.
      - Enter a name for your project in the "Project Name" field.
      - Click the "Create" button.
  3. Enable the "Google Drive API" for your project:
      - In the API Console, navigate to the "Library" using the left-hand menu.
      - In the search bar, type "Google Drive API" and select it from the results.
      - Click the "Enable" button.
  4. Create credentials for a service account with the "Editor" role:
      - In the API Console, navigate to "Credentials" using the left-hand menu.
      - Click on the "Create Credentials" button and select "Service account key."
      - If prompted, select or create a service account.
      - Choose the "Project" role and the "Editor" role from the "Role" dropdown.
      - Click the "Continue" button.
      - Click the "Done" button.
  5. Download the JSON file containing the credentials:
      - After creating the service account key, your browser will prompt you to download a JSON file containing the credentials.
      - Save this JSON file in a secure location on your machine. This file contains sensitive information and should be kept confidential.
      or
        - if your browser didn't prompt you to download a JSON file
          - In the Google Cloud Console, navigate to the "Credentials" page for your project.
          - n the "Credentials" page, find the service account key you created. It should be listed under "Service account keys."
          - In the "Actions" column for your service account key, click on the pencil/edit icon to edit the settings.
          - In the service account key details, navigate to the "KEYS" tab in your project.
          - click on ADD KEY and create new key and select key-type as a JSON and click on CREATE.
          - Save the downloaded JSON file in a secure location on your machine. This file contains sensitive information and should be kept confidential.

  # Step 2: Usage
  1. Replace Credentials File:
      - Replace the google_drive_api_settings.json file with your own downloaded Credentials.JSON file.
  2. Modify Script Parameters:
      - Open upload_files.py and update the following variables according to your use case:
        - credentials_path: Path to the downloaded credentials file (google_drive_api_settings.json).
        - file_to_upload: Absolute file path of the file you want to upload to Google Drive.
        - target_folder_id: URL of the Google Drive folder, extract the folder ID from the link (e.g., https://drive.google.com/drive/folders/FOLDER_ID).
          Example: target_folder_id = 'FOLDER_ID'
          
  # Step 3: Run the script:
       - Run the Python script: python upload_to_drive.py












## Acknowledgments
I would like to express my gratitude to the following resources that have contributed to the development of this project:
- **Google API Python Client:** A powerful library that made it easy to interact with the Google Drive API.
