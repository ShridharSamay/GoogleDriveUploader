import os

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload


class UploadFile:

    def __init__(self):
        self.credentials_path = 'path/to/credentials.json' # Replace 'path/to/credentials.json' with the path to your downloaded JSON credentials file
        self.file_to_upload = 'path/to/upload/file.txt' # Replace 'path/to/upload/file.txt' with the path to the file you want to upload
        self.target_folder_id = 'folder_id' # Replace 'folder_id' with the ID of the target folder in your Google Drive
        self.drive_service = None
        
        self.drive_service = self.authenticate_drive()
        
    def authenticate_drive(self):
        try:
            credentials = service_account.Credentials.from_service_account_file(
                self.credentials_path,
                scopes=['https://www.googleapis.com/auth/drive']
            )
            self.drive_service = build('drive', 'v3', credentials=credentials)

            self.upload_file()
        except Exception as error:
            print("Exception occured in authenticate_drive. error: ", error)

    def upload_file(self):
        file_name = os.path.basename(self.file_to_upload)

        # Check if the file already exists in the folder
        try:
            existing_file = self.drive_service.files().list(
                q=f"name = '{file_name}' and '{self.target_folder_id}' in parents").execute()

            if existing_file.get('files', []):
                file_id = existing_file['files'][0]['id']
                media = MediaFileUpload(self.file_to_upload, resumable=True)
                request = self.drive_service.files().update(
                    fileId=file_id,
                    media_body=media
                )
                request.execute()
                print(f"File '{file_name}' updated successfully.")
            else:
                # If the file does not exist, create a new one
                media = MediaFileUpload(self.file_to_upload, resumable=True)
                file_metadata = {
                    'name': file_name,
                    'parents': [self.target_folder_id],
                }
                self.drive_service.files().create(
                    body=file_metadata,
                    media_body=media,
                    fields='id'
                ).execute()
                print(f"File '{file_name}' uploaded successfully.")
        except Exception as error:
            print("Exception occured in uploadfile. error: ", error)

if __name__ == "__main__":
    uploader = UploadFile()