import os

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5811564674:AAEtIRgiN6jCHwt3b5b4ZrqZljOWG6rK3M0")
    
    API_ID = int(os.environ.get("API_ID", 7753414))
    
    API_HASH = os.environ.get("API_HASH","a7bdb544de65a8d693e4388fdd7687fb")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 50000000

    TG_MAX_FILE_SIZE = 2097152000

    FREE_USER_MAX_FILE_SIZE = 50000000
    
    CHUNK_SIZE = int(128)

    HTTP_PROXY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 3600
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "1983881496"))

    SESSION_NAME = "UploadLinkToFileBot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://priyankjivani92:EEMGR5fq3dgeQZnx@cluster0.ava4c3o.mongodb.net/?retryWrites=true&w=majority")

    MAX_RESULTS = "50"
