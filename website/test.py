from pathlib import Path

from website.wsgi import *
BASE_DIR = Path(__file__).resolve().parent.parent

print(os.path.join(BASE_DIR,'templates/'))
