##### Imports ##################################################################

import logging

from sms_sender.SMSSenderExceptions import NotEnoughCurrencyException, AccountIsNotSMSVerifiedException, MissingAccountException
from sms_sender.config import BaseConfig
from sms_sender.utils.NexmoAPI import NexmoAPI
from sms_sender.utils.SMSSenderDAL import SMSSenderDAL
from sms_sender.utils.Utils import Utils

##### Globals ##################################################################

VERIFICATION_MESSAGE_SENDER_NAME = 'sms_sender'
INITIAL_SMS_FREE_AMOUNT = BaseConfig.CONFIG_DATA['INITIAL_SMS_FREE_AMOUNT']
SMS_MESSAGE_COST = BaseConfig.CONFIG_DATA['SMS_MESSAGE_COST']
REFFERER_ACCOUNT_CURRENCY_SUM = BaseConfig.CONFIG_DATA['REFFERER_ACCOUNT_CURRENCY_SUM']

##### Functions ################################################################

##### Classes ##################################################################


class SMSSenderManager(object):

    def create_account(self, first_name, last_name, phone_number, reffering_account_id=None):
        currency_balance = INITIAL_SMS_FREE_AMOUNT * SMS_MESSAGE_COST
        account_id = SMSSenderDAL.create_account(first_name, last_name, phone_number, currency_balance)
        if reffering_account_id:
            reffering_account = SMSSenderDAL.get_account(reffering_account_id)
            new_currency_balance = reffering_account.currency_balance + REFFERER_ACCOUNT_CURRENCY_SUM
            SMSSenderDAL.update_currency_balance(reffering_account_id, new_currency_balance)
        return account_id

    def send_verification_sms(self, account_id):
        verification_code = Utils.generate_verification_code()
        account = SMSSenderDAL.get_account(account_id)
        SMSSenderDAL.update_verification_code(account_id, verification_code)
        verification_message = "Hi, your verification code is {}".format(verification_code)
        NexmoAPI.send_sms_message(VERIFICATION_MESSAGE_SENDER_NAME, account.phone_number, verification_message)

    def verify_sms(self, account_id, verification_code):
        account = SMSSenderDAL.get_account(account_id)
        if account:
            is_verified = account.sms_verification_code == verification_code
            account.is_sms_verified = is_verified

    def send_sms_message(self, account_id, to_number, message):
        account = SMSSenderDAL.get_account(account_id)
        if account:
            if account.is_sms_verified:
                if account.currency_balance >= SMS_MESSAGE_COST:
                    NexmoAPI.send_sms_message(account.first_name + account.last_name, to_number, message)
                    SMSSenderDAL.create_sms_event(message, to_number, account_id)
                    new_currency_balance = account.currency_balance - SMS_MESSAGE_COST
                    SMSSenderDAL.update_currency_balance(account_id, new_currency_balance)
                else:
                    logging.warning("Account ID: {}: Unable to send SMS message: {} to number: {} - not enough currency balance!".format(account_id, message, to_number))
                    raise NotEnoughCurrencyException()
            else:
                logging.warning("Account ID: {}: Unable to send SMS message: {} to number: {} - account is not SMS verified!".format(account_id, message, to_number))
                raise AccountIsNotSMSVerifiedException()
        else:
            logging.warning("Account ID: {}: Unable to send SMS message: {} to number: {} - account not found!".format(account_id, message, to_number))
            raise MissingAccountException()
