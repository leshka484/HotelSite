from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import update_reservations

def start():
    scheduler = BackgroundScheduler(replace_existing=True)
    update_reservations()
    scheduler.add_job(update_reservations, 'interval', days = 1)
    scheduler.start()