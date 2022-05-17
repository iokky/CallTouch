import os
import datetime
from datetime import datetime as dt
from datetime import timedelta

from dotenv import load_dotenv
import requests
import pyodbc
from db.db import SessionLocal
from db.models import CallTouch

from logger.telegram import send_message

load_dotenv()


class CallTouchCon:
    @staticmethod
    def set_date() -> datetime.date:
        date = (dt.today() - timedelta(1)).strftime('%d/%m/%Y')
        send_message(f'ct_agent_set_date: {date}')
        return date

    def get_data(self, date=None) -> requests.Request:
        if date is None:
            date = self.set_date()
        url = f'http://api.calltouch.ru/calls-service/RestAPI/{os.getenv("CT_CLIENT")}/calls-diary/calls?clientApiId={os.getenv("CT_TOKEN")}&dateFrom={date}&dateTo={date}'
        response = requests.get(url)
        return response.json()

    @staticmethod
    def create_item(db: SessionLocal, row: dict) -> None:
        item = CallTouch(
            call_id=row.get('callId'),
            date=str(row.get('date')[0:10]),
            time=str(row.get('date')[12:20]),
            host=row.get('hostname'),
            client_number=str(row.get('callerNumber')),
            phone_number=str(row.get('phoneNumber')),
            status=str(row.get('successful')),
            uniq_target_call=str(row.get('uniqTargetCall')),
            city=row.get('city'),
            source=row.get('source'),
            medium=row.get('medium'),
            campaign=row.get('utmCampaign'),
            keyword=row.get('keyword'),
            ga_client_id=str(row.get('clientId')),
            device=row.get('device'),
            os=row.get('os')
        )
        try:
            db.add(item)
            db.commit()
            db.refresh(item)
        except pyodbc.Error:
            print('double')
            pass

    def run(self, date=None) -> requests.Request:
        data = self.get_data(date)
        if data:
            send_message('ct_agent_run witch data')
        db = SessionLocal()
        for row in data:
            self.create_item(db=db, row=row)
        return
