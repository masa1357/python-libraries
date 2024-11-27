import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.service_account import Credentials

# 認証情報の設定
SCOPES = ['https://www.googleapis.com/auth/drive.file']
CREDENTIALS_FILE = '/home/masa1357/Dockerdata/python-libraries/Auth/oval-abode-443007-d0-55bd55ec47e4.json'  # 認証情報ファイルのパス
creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
drive_service = build('drive', 'v3', credentials=creds)

# Google Driveのアップロード先フォルダID
UPLOAD_FOLDER_ID = '18bpUCiBVEIJ80HJ3A5BqiP_PL9B4ekYt'  # アップロード先フォルダIDを指定

# ローカルディレクトリ内の画像をGoogle Driveにアップロードする関数
def upload_images_to_drive(local_dir: str = "../fig/", drive_folder_id: str = UPLOAD_FOLDER_ID):
    """
    指定したローカルディレクトリ内のすべての画像をGoogle Driveの指定フォルダにアップロードする関数。

    Args:
        local_dir (str): ローカルディレクトリのパス（例: './fig/'）
        drive_folder_id (str): Google DriveのフォルダID
    """
    # 指定ディレクトリ内のすべてのファイルをチェック
    for file_name in os.listdir(local_dir):
        # ファイルが画像かどうかを判定（拡張子で判定）
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', 'svg', 'eps')):
            file_path = os.path.join(local_dir, file_name)  # ファイルパスを作成
            print(f"Uploading: {file_name}")
            
            # Google Driveにアップロード
            file_metadata = {'name': file_name, 'parents': [drive_folder_id]}
            media = MediaFileUpload(file_path, mimetype='image/jpeg')  # 画像のMIMEタイプを指定
            drive_service.files().create(
                body=file_metadata,
                media_body=media,
                fields='id'
            ).execute()
            print(f"Uploaded: {file_name}")

# 使用例
# local_directory = './fig/'  # ローカルディレクトリ（アップロードする画像が保存されている場所）
# upload_images_to_drive(local_directory, UPLOAD_FOLDER_ID)
