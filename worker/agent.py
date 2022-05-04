from apscheduler.schedulers.background import BackgroundScheduler

from connectors.call_touch.client import CallTouchCon

from logger.telegram import send_message


call_touch_agent = CallTouchCon()



def ct_run():
    call_touch_agent.run()
    send_message('ct_agent done ')


scheduler = BackgroundScheduler({'apscheduler.timezone': 'Europe/Moscow'})
scheduler.start()
scheduler.add_job(ct_run, 'cron', hour='01', minute='1')
# scheduler.add_job(ct_run, 'cron', hour='11', minute='10')
# scheduler.add_job(ct_run, 'cron', minute='*')

# date -s "03 MAY 2022 02:10:00"
