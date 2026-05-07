import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "backend"))

from app.main import app
from mangum import Mangum

_mangum = Mangum(app, lifespan="off")

def handler(request, context):
    return _mangum(request, context)
