"""
See https://developers.google.com/drive/api/v3/about-sdk



Upload a file in this folder: IdéSYS/Pôle Suivi d'Etudes/Projets/Projets 2017-2018/Le Garrec

folder_id = gdrive.get_folder(creds, "IdéSYS/Pôle Suivi d'Etudes/Projets/Projets 2017-2018/Le Garrec")
link = gdrive.upload(creds, file_path, 'text/plain', 'text/plain', folder_id)

"""

from os import path, mkdir
import io


from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload


OUTPUT_PATH = 'external_apis/gsuite_api/downloaded'

if not path.exists(OUTPUT_PATH):
    mkdir(OUTPUT_PATH)


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
            q="mimeType = 'application/vnd.google-apps.folder' and '{}' in parents and trashed=false"
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
    media = MediaFileUpload(output_path,
                            mimetype=media_mimetype,
                            resumable=True)
    file = drive_service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id, webViewLink').execute()
    return file


def download(creds, file_id, filename):
    """Download a file from Google Drive.

    Example:

        # Download a Google Document as a pdf,
        # can be done with Google Doc, google Sheet and Google Slide (maybe more)
        # To do that, just add `.pdf` suffix at the `filename` argument.
        gdrive.download(creds, '1UhmhiOYCD4oTxWfHtka4xxyDW9yB_1WbrlDrse-9Rzw', 'myfile.pdf')

        # Download a file, as it is stored in Google Drive
        gdrive.download(creds, '1WMV9O2xlfgpaUjpDo9RuVNE34KPSzNAA', 'myfile')

    """
    drive_service = build('drive', 'v3', credentials=creds)

    output_path = path.join(OUTPUT_PATH, filename)

    if filename.endswith('pdf'):
        request = drive_service.files().export_media(fileId=file_id,
            mimeType='application/pdf')

    else:
        request = drive_service.files().get_media(fileId=file_id)

    fh = io.BytesIO()

    # Download in memory
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        _, done = downloader.next_chunk() # the variable _ is status

    # Write on a file
    fh.seek(0)
    with open(output_path, 'wb') as my_file:
        my_file.write(fh.read())
