##### Imports ##################################################################

from sms_sender.app import app
from sms_sender.models import db, Account, SMSEvent

##### Constants ################################################################

##### Functions ################################################################

##### Classes ##################################################################


class SMSSenderDAL(object):

    @classmethod
    def create_account(cls, first_name, last_name, phone_number, currency_balance):
        with app.app_context():
            account = Account(first_name=first_name, last_name=last_name, phone_number=phone_number, currency_balance=currency_balance)
            db.session.add(account)
            db.session.commit()
            return account.id

    @classmethod
    def create_sms_event(cls, message, recipient_phone_number, account_id):
        with app.app_context():
            event = SMSEvent(message=message, recipient_phone_number=recipient_phone_number, account_id=account_id)
            db.session.add(event)
            db.session.commit()
            return event.id

    @classmethod
    def update_verification_code(cls, account_id, verification_code):
        account = cls.get_account(account_id)
        if account:
            with app.app_context():
                account.sms_verification_code = verification_code
                db.session.commit()

    @classmethod
    def update_currency_balance(cls, account_id, currency_balance):
        account = cls.get_account(account_id)
        if account:
            with app.app_context():
                account.currency_balance = currency_balance
                db.session.commit()
                return account.id

    @classmethod
    def get_account(cls, account_id):
        with app.app_context():
            return Account.query.filter_by(id=account_id).first()
