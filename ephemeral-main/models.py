import os
import threading

class EphemeralFileManager:
    
    def __init__(self, base_path, term="ephemeral"):
        self.base_path = base_path
        self.term = term.lower()
        self.registered_paths = []


    def add_ephemeral_path(self, root, d, hours, minutes):
        """
        Register an ephemeral path with its lifetime in hours and minutes.
        """
        path = os.path.join(root, d)
        file_dict = {
            "pathname": path,
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


    def check_files(self):
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

class TimeManager:
    def __init__(self, configObject):
        self.configs = configObject


# Example usage
manager = EphemeralFileManager("/home/amadeus")
manager.check_files()
print(manager.registered_paths)
