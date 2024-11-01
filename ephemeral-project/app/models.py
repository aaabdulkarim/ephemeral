import os
import threading
import time


class EphemeralFileManager:

    def __init__(self, base_path, term="ephemeral"):
        self.base_path = base_path
        self.term = term.lower()

        # instead of making 2 lists we can make another attribute in the path Object Dict
        # Adding pathObjects to different lists based on conditions
        # is a hard way of giving these objects another boolean attribute
        # OR We keep it that way and don't cause any bugs
        self.registered_paths = []
        self.already_handled_paths = []


    def add_ephemeral_path(self, list):
        """
        This Methods adds external lists to the registered path
        """
        self.registered_paths = self.registered_paths + list


    def add_ephemeral_path(self, root, d, hours, minutes):
        """
        Register an ephemeral path with its lifetime in hours and minutes.
        """
        path = os.path.join(root, d)
        file_dict = {
            "pathName": path,
            "hoursLeft": int(hours),
            "minutesLeft": int(minutes)
        }

        # Stops the Program from allowing duplicates
        if file_dict not in self.registered_paths:
            self.registered_paths.append(file_dict)

    def is_ephemeral(self, dirs, root):
        """
        Check if a directory or file is ephemeral based on the naming convention.
        """
        for d in dirs:
            str_list = d.split("-")
            for idx, part in enumerate(str_list):
                if part.lower() == self.term:
                    try:
                        hours = str_list[idx + 1]
                        colon = str_list[idx + 2]
                        minutes = str_list[idx + 3]

                        if hours.isnumeric() and colon == ":" and minutes.isnumeric():
                            self.add_ephemeral_path(root, d, hours, minutes)


                    except IndexError:
                        continue


    def makro_file_check(self):
        """
        Walk through directories and files to find ephemeral ones based on the term.
        """
        for root, dirs, files in os.walk(self.base_path):
            self.is_ephemeral(files, root)
            self.is_ephemeral(dirs, root)


    def delete_path(self, path):
        """
        Delete a file or directory at a given path.
        """
        try:

            if os.path.isfile(path):
                os.remove(path)
            elif os.path.isdir(path):
                os.rmdir(path)
            # Removes from already_handled_
            self.already_handled_paths.remove(path)
            print(f"Deleted {path}")

        except IndexError:
            print("Invalid index for registered path.")
        except Exception as e:
            print(f"Error deleting {path}: {e}")


class TaskManager:
    def __init__(self, configObject, ephemeralFileManager):
        self.configs = configObject
        self.fileManager = ephemeralFileManager
        self.timers = []
    

    def eval_timers(self):
        for path in self.fileManager.registered_paths: 
            method_delay = self.configs.defaultTimeToLive
            self.fileManager.registered_paths.remove(path)

            if path not in self.fileManager.already_handled_paths:
                # Needs to check if hourLeft and minutesLeft isn't empty
                if "minutesLeft" in path and "hoursLeft" in path:
                    method_delay = path["hoursLeft"] * 3600 + path["minutesLeft"] * 60
                
                timer = threading.Timer(method_delay, self.fileManager.delete_path, args=(path["pathName"]))
                
                # So the system of the file manager doesnt allow duplicates
                self.fileManager.already_handled_paths.append(path)
                self.timers.append(timer)

    def start_tasks(self):
        for timer in self.timers:                
            timer = timers.remove(timer)
            if timer.is_alive() == False:
                timer.start()
        
    def continous_loop(self):
        """
        The task of this method is to act as a continous loop
        which will do a makro system check for ephemeral files every 5 minutes        
        """
        SECONDS_TO_WAIT = 60 * 5
        while True:
            # The problem is that after the second iteration it will add the timers of previous
            # Ephemeral Files again.
            self.fileManager.makro_file_check()
            self.fileManager.start_tasks()
            """
            Need to create new ephemeral file manager and check for every Config File Path as base parameter
            Add the regsitered_paths to the main ephemeral File manager registered_paths 
            """

            time.sleep(SECONDS_TO_WAIT)
