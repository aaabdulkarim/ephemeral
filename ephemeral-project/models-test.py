import app.models
import unittest
from app.models import EphemeralFileManager, TaskManager
from app.configmodel import Config



class ModelTest(unittest.TestCase):


    def setUp(self):
        self.config = Config()
        self.config.loadFile()
        self.ephemeralFileManager = EphemeralFileManager("/")
        self.taskManager = TaskManager(self.config, self.ephemeralFileManager)


        
    def test_makro_file_check(self):
        expectedString = "/home/amadeus/Documents/eigene-projekte/ephemeral/sample-files/testing-purpose-ephemeral-0-:-20"
        self.ephemeralFileManager.makro_file_check()
        
        # List Comprehension - returns a list of the pathnames from all dicts saved in the listS
        foundPathNames = [pathName["pathName"] for pathName in self.ephemeralFileManager.registered_paths]
        self.assertTrue(expectedString in foundPathNames)



unittest.main()