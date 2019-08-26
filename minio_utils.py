import io
import json
import socket

from minio import Minio
from settings import MINIO

mc = Minio(f"{MINIO['HOST']}:{MINIO['PORT']}", access_key=MINIO["ACCESS_KEY"], secret_key=MINIO["SECRET_KEY"], secure=False)


def get_or_create_bucket(bucket_name):
    """Create the bucket if not already present"""
    if not mc.bucket_exists(bucket_name):
        mc.make_bucket(bucket_name)
    return bucket_name


def backup_log_file(_file):
    """Backup the log file to minio bucket"""
    try:
        get_or_create_bucket(MINIO["BUCKET"]["FILE_STORE"])
        object_name = f"Server {socket.gethostname()} - {_file.split('/')[-1]}"
        mc.fput_object(MINIO["BUCKET"]["FILE_STORE"], object_name, _file, content_type="application/text")
    except Exception as e:
        print("Unable to backup log file to minio", e)


async def update_record_store(data):
    """Update the metadata bucket on minio with log data"""
    get_or_create_bucket(MINIO["BUCKET"]["RECORD_STORE"])
    object_name = f"{data['timestamp']}/{data['clientip']}"
    mc.put_object(MINIO["BUCKET"]["RECORD_STORE"], object_name, io.BytesIO(json.dumps(data).encode()), len(json.dumps(data)), content_type="application/json")

