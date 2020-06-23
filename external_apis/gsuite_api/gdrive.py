"""
See https://developers.google.com/drive/api/v3/about-sdk



Upload a file in this folder: IdéSYS/Pôle Suivi d'Etudes/Projets/Projets 2017-2018/Le Garrec

folder_id = gdrive.get_folder(creds, "IdéSYS/Pôle Suivi d'Etudes/Projets/Projets 2017-2018/Le Garrec")
link = gdrive.upload(creds, file_path, 'text/plain', 'text/plain', parent_id)

"""

from os import path


from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload



def get_folder(creds, path):
    folders = path.split('/')
    parent_id = 'root'
    for folder in folders:
        result = _get_folders_in_parent(
            creds,
            parent_id,
            folder
        )
        parent_id = result.get('id')
    return parent_id

def _get_folders_in_parent(creds, parent, name):
    drive_service = build('drive', 'v3', credentials=creds)
    page_token = None
    while True:
        response = drive_service.files().list(
            q="'{}' in parents"
            .format(parent),
            spaces='drive',
            fields='nextPageToken, files(id, name, parents)',
            pageToken=page_token).execute()
        for file in response.get('files', []):
            if file.get('name') == name:
                return file
        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break


def upload(creds, output_path, metadata_mime_type, media_mimetype, parent=None):
    """Upload a file to Google Drive

    output_path: the local path of the file to upload
    parents: a list with the ids of the parent folders in Drive
        Use this argument to put a file in a specific folder in GDrive.
    """
    drive_service = build('drive', 'v3', credentials=creds)
    if parent is None:
        file_metadata = {
            'name': path.basename(output_path),
            'mimeType':metadata_mime_type,
        }
    else:
        file_metadata = {
            'name': path.basename(output_path),
            'mimeType':metadata_mime_type,
            'parents': [parent]
        }
    print(file_metadata)
    media = MediaFileUpload(output_path,
                            mimetype=media_mimetype,
                            resumable=True)
    file = drive_service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='webViewLink').execute()
    return file.get('webViewLink')
