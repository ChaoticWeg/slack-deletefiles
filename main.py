from dotenv import load_dotenv
from slack import get_files, delete_files

def run():
    get_files()
    delete_files([])

if __name__ == "__main__":
    load_dotenv()
    run()
