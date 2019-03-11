##### Imports ##################################################################

import unittest

from sms_sender.SMSSenderManager import SMSSenderManager
from sms_sender.app import app
from sms_sender.models import db
from sms_sender.utils.SMSSenderDAL import SMSSenderDAL

##### Globals ##################################################################

##### Functions ################################################################

##### Classes ##################################################################


class TestSMSSenderManager(unittest.TestCase):

    def setUp(self):
        with app.app_context():
            db.drop_all()
            db.create_all()
        self._mgr_class = SMSSenderManager()

    def tearDown(self):
        with app.app_context():
            db.drop_all()
            db.create_all()

    def test_create_account(self):
        account_id = self._mgr_class.create_account('Yehuda', 'Zargarov', '972503473119')
        account = SMSSenderDAL.get_account(account_id)
        self.assertIsNotNone(account)
