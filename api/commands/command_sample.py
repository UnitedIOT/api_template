# coding=utf-8

from flask_script import Command

import logging
logging.basicConfig(format='%(levelname)5s %(asctime)-15s #%(filename)-20s@%(funcName)-20s: %(message)s',
                    level=logging.INFO)


class SampleCommand(Command):
    """
    Sample Command
    """

    def run(self):
        logging.info("This is sample command")

