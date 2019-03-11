##### Imports ##################################################################

import nexmo

from sms_sender.SMSSenderExceptions import NexmoAPIException
from sms_sender.config import BaseConfig

##### Constants ################################################################

NEXMO_API_KEY = BaseConfig.CONFIG_DATA['NEXMO_API_KEY']
NEXMO_API_SECRET = BaseConfig.CONFIG_DATA['NEXMO_API_SECRET']

##### Functions ################################################################

##### Classes ##################################################################


class NexmoAPI(object):

    @classmethod
    def send_sms_message(cls, from_name, to_number, message):
        """
        Senda an sms message via nexmo api
        :param from_name: The name of the sender
        :param to_number: The number of the recipient
        :param message: The message to send
        """
        try:
            client = nexmo.Client(key=NEXMO_API_KEY, secret=NEXMO_API_SECRET)
            client.send_message({
                'from': from_name,
                'to': to_number,
                'text': message
            })
        except Exception as e:
            raise NexmoAPIException(e.message)
