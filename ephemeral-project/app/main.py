from models import EphemeralFileManager, TaskManager
from configmodel import Config


def main():
    config = Config()
    config.loadFile()
    ephemeralFileManager = EphemeralFileManager("/")
    taskManager = TaskManager(config, ephemeralFileManager)

    ephemeralFileManager.makro_file_check()
    taskManager.start_tasks()

if __name__ == "__main__":
    main()