##### Imports ##################################################################

import logging

from sms_sender.SMSSenderManager import SMSSenderManager

##### Globals ##################################################################

##### Functions ################################################################

##### Classes ##################################################################


class SMSSenderService(object):

    def create_account(self, first_name, last_name, phone_number, reffering_account_id=None):
        """
        Creats an account for sending sms messages.
        :param first_name: The first name of the user
        :param last_name: The last name of the user
        :param phone_number: The phone number of the user
        :param reffering_account_id: The account id the refferd this user
        """
        logging.info("SMSSenderService.create_account called with {}, {}, {}, {}".format(first_name, last_name, phone_number, reffering_account_id))
        sms_sender_manager = SMSSenderManager()
        return sms_sender_manager.create_account(first_name, last_name, phone_number, reffering_account_id)

    def send_verification_sms(self, account_id):
        """
        Sends verification message to user.
        :param account_id: The account id to send verification sms to
        """
        logging.info("SMSSenderService.send_verification_sms called with {}".format(account_id))
        sms_sender_manager = SMSSenderManager()
        return sms_sender_manager.send_verification_sms(account_id)

    def verify_sms(self, account_id, verification_code):
        """
        Verifies a given verification code for a given account id
        :param account_id: The account id to verify
        :param verification_code: the verification code to check
        """
        logging.info("SMSSenderService.verify_sms called with {}, {}".format(account_id, verification_code))
        sms_sender_manager = SMSSenderManager()
        return sms_sender_manager.verify_sms(account_id, verification_code)

    def send_sms_message(self, account_id, to_number, message):
        """
        Sends a given message as sms message to a given number.
        :param account_id: The id of the account to send from
        :param to_number: The number to send sms to
        :param message: The message to send
        """
        logging.info("SMSSenderService.send_sms_message called with {}, {}, {}".format(account_id, to_number, message))
        sms_sender_manager = SMSSenderManager()
        return sms_sender_manager.send_sms_message(account_id, to_number, message)
