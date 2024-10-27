import os
import threading




class EphemeralFileManager:
    
    def __init__(self, base_path, term="ephemeral"):
        self.base_path = base_path
        self.term = term.lower()
        self.registered_paths = []

    
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
        self.registered_paths.append(file_dict)
        print(f"Registered ephemeral path: {path}")


    def is_ephemeral(self, dirs, root):
        """
        Check if a directory or file is ephemeral based on the naming convention.
        """
        for d in dirs:
            # Split 
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


    def delete_path(self, path_index):
        """
        Delete a file or directory at a given index in registered paths.
        """
        try:
            path_info = self.registered_paths.pop(path_index)
            path = path_info["pathname"]

            if os.path.isfile(path):
                os.remove(path)
            elif os.path.isdir(path):
                os.rmdir(path)
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
    

    def start_tasks(self):
        for path in self.fileManager.registered_paths: 
            method_delay = self.configs.defaultTimeToLive

            # Needs to check if hourLeft and minutesLeft isn't empty
            if "minutesLeft" in path and "hoursLeft" in path:
                method_delay = path["hourseLeft"] * 3600 + path["minutesLeft"] * 60
            
            timer = threading.Timer(method_delay, self.fileManager.delete_path, args=(path["pathName"]))
            timers.append(timer)


    def continous_loop(self):
        SECONDS_TO_WAIT = 60 * 5
        while True:
            self.fileManager.makro_file_check()
            time.sleep(SECONDS_TO_WAIT)
