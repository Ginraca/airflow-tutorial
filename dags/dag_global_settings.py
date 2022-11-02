from datetime import timedelta
from email.policy import default

def init():
    global default_args
    default_args = {
        'owner': 'admin',
        'retries': 5,
        'retry_delay': timedelta(minutes=1),
    }