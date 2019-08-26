import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


APP_SETTINGS = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
}

LOGLEVEL = "DEBUG"
LOGFORMAT = "%(asctime)s %(module)s %(lineno)s %(levelname)s: %(message)s"
LOGFILE = "/tmp/feedback.log"
LOG_ROTATION = {
        "when": "H",
        "interval": 1,
        "backupCount": 5
}

DB = {
    "USER": os.getenv("MYSQL_USER"),
    "PASSWORD": os.getenv("MYSQL_PASSWORD"),
    "HOST": os.getenv("MYSQL_HOST"),
    "DATABASE": os.getenv("MYSQL_DATABASE")
}

MINIO = {
        "ACCESS_KEY": os.getenv("MINIO_ACCESS_KEY"),
        "SECRET_KEY": os.getenv("MINIO_SECRET_KEY"),
        "HOST": os.getenv("MINIO_HOST"),
        "PORT": 9000,
        "BUCKET": {
            "FILE_STORE": "files",
            "RECORD_STORE": "records"
        }
}


engine = create_engine(f"mysql+mysqldb://{DB['USER']}:{DB['PASSWORD']}@{DB['HOST']}/{DB['DATABASE']}")
session = sessionmaker(bind=engine)()
