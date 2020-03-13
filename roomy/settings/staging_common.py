from .common import BASE_DIR
from google.oauth2 import service_account
import os
DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_BUCKET_NAME = 'roomy-bucket'

GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
     os.path.join(BASE_DIR, '../bucket-key.json')
)
