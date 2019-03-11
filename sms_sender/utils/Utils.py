##### Imports ##################################################################

import string
import random

##### Globals ##################################################################

##### Functions ################################################################

##### Classes ##################################################################


class Utils(object):

    @classmethod
    def generate_verification_code(cls, size=6):
        chars = string.ascii_uppercase + string.digits
        return ''.join(random.choice(chars) for _ in range(size))
