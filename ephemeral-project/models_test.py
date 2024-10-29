import os
import time
import threading
import unittest

from app.models import EphemeralFileManager, TaskManager
from app.configmodel import Config


class ModelTest(unittest.TestCase):


    def setUp(self):
        testPath = "/home/amadeus/Documents/eigene-projekte/ephemeral/sample-files/deleteme"

        with open(testPath, 'w') as f:
            f.write("Temporary test content")

        self.config = Config()
        self.config.loadFile()
        self.ephemeralFileManager = EphemeralFileManager("/")
        self.taskManager = TaskManager(self.config, self.ephemeralFileManager)

    def test_delete_path(self):
        """
        This tests the EphemeralFileManager.delete_path method if it can delete any files
        """
        testPath = "/home/amadeus/Documents/eigene-projekte/ephemeral/sample-files/deleteme"
        
        # Ensure the file exists before trying to delete it
        if not os.path.exists(testPath):
            # Create the file for testing purposes
            with open(testPath, 'w') as f:
                f.write("Temporary test content")

        else:
            print("False")
        # Attempt to delete the file
        self.ephemeralFileManager.delete_path(testPath)
            
        
        fileExists = os.path.exists(testPath)
        self.assertFalse(fileExists)

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
        self.ephemeralFileManager.makro_file_check()
        self.taskManager.eval_timers()
        self.assertGreaterEqual(len(self.taskManager.timers), 1)  


    def test_task_manager_adds_expected_timer(self):
        """
        Prerequisits: file named testing-purpose-ephemeral-0-:-20 convention on the system
        """
        self.ephemeralFileManager.makro_file_check()
        self.taskManager.eval_timers()

        expectedFun = self.ephemeralFileManager.delete_path


        foundExpectedTimer = False
        for timer in self.taskManager.timers:
            conditions = [
                timer.interval == 60*20,
                timer.function == expectedFun
            ]    
            if all(conditions):
                foundExpectedTimer = True
                break
        
        
        self.assertTrue(foundExpectedTimer)



    def test_task_manager_triggers_delete_fun(self):
        """
        Prerequisits: file with ephemeral naming convention on the system
        """
        self.ephemeralFileManager.makro_file_check()
        self.taskManager.eval_timers()

        firstTimer = self.taskManager.timers[0]

        copiedFunction = firstTimer.function
        copiedArgs = firstTimer.args
        
        # Fast Forward effect by replacing time
        firstTimer = threading.Timer(5, copiedFunction, args=(copiedArgs))
        firstTimer.start()
        time.sleep(11)

    
        print("Finished")
        print(firstTimer.finished._flag)
        print("Args: " + firstTimer.args)
        print(firstTimer.function)

        fileDeleted = os.path.exists(firstTimer.args)
            
        self.assertFalse(fileDeleted)

