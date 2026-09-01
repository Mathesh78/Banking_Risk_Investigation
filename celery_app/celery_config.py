from celery import Celery
import os

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = os.getenv("REDIS_PORT", "6379")

REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"


celery = Celery(
    "banking_worker",

    broker=REDIS_URL,  # Route tasks via local Redis database

    backend=REDIS_URL,  #Store task statuses & returns in database

    include=[     # Automatically import these modules
        "celery_app.tasks"  
    ]
) 