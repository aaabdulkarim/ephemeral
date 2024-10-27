from models import EphemeralFileManager, TaskManager
from configmodel import Config


def main():
    config = Config()
    config.loadFile()
    ephemeralFileManager = EphemeralFileManager("/")
    taskManager = TaskManager(config, ephemeralFileManager)
    taskManager.start_tasks()
    print(ephemeralFileManager.registered_paths)
if __name__ == "__main__":
    main()