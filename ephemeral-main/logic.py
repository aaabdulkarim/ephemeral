import os


def checkFiles(searchTermList):
    """
    Algorithim which will check all files 
    """
    timer = 0

    # Os walk really just walks through every directory. 
    # Every Directory has a root (like the path), 
    # dirs (directories in the current one) and files
    #
    # The task of this method is to check if the Terms are in the file or directory names
    # 
    for root, dirs, files in os.walk("/"):
        for d in dirs:
            for term in searchTermList:
                if term in d.split("-"):
                    print(root, d) 

checkFiles(["temp"])