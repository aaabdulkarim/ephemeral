class Config():
    """
    Config Object which helps communication between user config file and all model classes
    """
    def __init__(self):
        self.absolutePaths = [""]
        self.defaultTimeToLive = 3600

        # Think of Data structure to only use this on a path e.g "home/desktop/"
        self.filetypesToDelete = [""]




    def loadFile(self):
        """
        Attributes will reinitialised with data loaded from the config file
        """
        pass

    def writeFile(self):
        pass
