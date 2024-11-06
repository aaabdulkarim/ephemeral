import os
import time
import threading
import unittest

from app.configmodel import Config


class ConfigModelTest(unittest.TestCase):


    def setUp(self):
        testPath = "./sample-files/deleteme"
        testPath2 = "./sample-files/testing-purpose-ephemeral-0-:-20"

        with open(testPath, 'w') as f:
            f.write("Temporary test content")


        with open(testPath2, 'w') as f:
            f.write("Temporary test content")


        self.config = Config()
        self.config.loadFile()
        self.ephemeralFileManager = EphemeralFileManager("/")
        self.taskManager = TaskManager(self.config, self.ephemeralFileManager)

    