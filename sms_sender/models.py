##### Imports ##################################################################

from flask_sqlalchemy import SQLAlchemy
import datetime

##### Functions ################################################################

##### Classes ##################################################################

db = SQLAlchemy()

class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True

    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        """Define a base way to print models"""
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
        })

    def json(self):
        """
        Define a base way to jsonify models, dealing with datetime objects
        """
        return {
            column: value if not isinstance(value, datetime.date) else value.strftime('%Y-%m-%d')
            for column, value in self._to_dict().items()
        }


class Account(db.Model):
    """Model for the accounts table"""
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    phone_number = db.Column(db.String)
    currency_balance = db.Column(db.Float)
    is_sms_verified = db.Column(db.Boolean, default=False)
    sms_verification_code = db.Column(db.String)


class SMSEvent(db.Model):
    """Model for the sms events table"""
    __tablename__ = 'sms_events'
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text)
    recipient_phone_number = db.Column(db.String)
    account_id = db.Column(db.Integer, db.ForeignKey("accounts.id"), nullable=False)

##### Main #####################################################################