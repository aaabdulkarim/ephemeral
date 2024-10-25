class Config():
    """
    How do we design the config file to allow "filters" which are related
    """
    def __init__(self):
        self.absolutePaths = [""]
        self.timeToDelete = 300

        # Think of Data structure to only use this on a path e.g "home/desktop/"
        self.filetypesToDelete = [""]




    def loadFile(self):
        """
        Attributes will reinitialised with data loaded from the config file
        """
        pass

    def writeFile(self):
        pass
