from dotenv import load_dotenv
from slack import get_files, delete_files

def run():
    while True:
        try:
            ids = get_files()
            delete_files(ids)
            if len(ids) < 1:
                break

if __name__ == "__main__":
    load_dotenv()
    run()
