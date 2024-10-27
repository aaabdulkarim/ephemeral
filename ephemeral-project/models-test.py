import threading
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
        self.assertIn(expectedString, foundPathNames)

    def test_task_manager_adds_timer(self):
        """
        Prerequisits: file with ephemeral naming convention on the system
        """
        self.taskManager.start_tasks()
        self.assertGreaterEqual(len(self.taskManager.timers), 1)  


    def test_task_manager_adds_expected_timer(self):
        """
        Prerequisits: file with ephemeral naming convention on the system
        """
        self.taskManager.start_tasks()
        
        foundTimers = [timer for timer in self.taskManager.timers]

        expectedString = "/home/amadeus/Documents/eigene-projekte/ephemeral/sample-files/testing-purpose-ephemeral-0-:-20"
        expectedTimer = threading.Timer(60 * 20, self.ephemeralFileManager.delete_path, args=(expectedString))
        self.assertIn(expectedTimer, foundTimers)



    def test_task_manager_triggers_delete_fun(self):
        """
        Prerequisits: file with ephemeral naming convention on the system
        """
        self.taskManager.start_tasks()
        print(self.taskManager.timers[0].interval)



unittest.main()