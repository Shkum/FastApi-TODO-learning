import os

import uvicorn
from todo.app import app

if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=os.getenv("PORT", default=5000), log_level="info")
