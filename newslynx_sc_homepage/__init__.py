
import os
from newslynx.sc import SousChef

class SayMyName(SousChef):

    def run(self):
        msg = 'Hello {my_name}!'.format(**self.options)
        os.system("say '{}'".format(msg))
        self.log.info(msg)
        return self.options

