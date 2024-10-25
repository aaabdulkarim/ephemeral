import os

# Saves Directory Pahts and File Paths
registeredPaths = []


def isEphemeral(dirs, term, root):
    """
    If File or Directory is Ephimeral it will be added to the registeredPaths list
    """
    condition = False
    for idx, d in enumerate(dirs):
        str_list = d.split()
        # if Term is triggered
        if idx < len(str_list) - 3:
            conditionTerm = term.lower() in str_list
            conditionMinutes = str_list[idx + 1].isnumeric()
            condtionColon = str_list[idx + 2] == ":" 
            conditionSeconds = str_list[idx + 3].isnumeric()
            

            condition = conditionTerm  and  conditionMinutes and conditionSeconds  

            if condition:
                print(root, d)
                registeredPaths.append(root + d)

    

def checkFiles(term):
    """
    Algorithim which will check all files 
    """

    # Os walk really just walks through every directory. 
    # Every Directory has a root (like the path), 
    # dirs (directories in the current one) and files
    #
    # The task of this method is to checregisteredPaths.append(d)k if the Terms are in the file or directory names
    # 
    for root, dirs, files in os.walk("/home/amadeus"):
        isEphemeral(dirs, term, root)

        isEphemeral(files, term, root)            


    


checkFiles("temp")

