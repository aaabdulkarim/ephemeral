import os

# Saves Directory Pahts and File Paths
registeredPaths = []


def isEphemeral(dirs, term, root):
    """
    If File or Directory is Ephemeral it will be added to the registeredPaths list
    """
    condition = False
    for d in dirs:
        str_list = d.split("-")
        # if Term is triggered
        for idx, str in enumerate(str_list):
            
            conditionTerm = term.lower() == str
            if conditionTerm:
                try:   
                    minutes = str_list[idx + 1]
                    conditionMinutes = minutes.isnumeric()

                    colon = str_list[idx + 2]
                    condtionColon = colon == ":"

                    seconds = str_list[idx + 3]
                    conditionSeconds = seconds.isnumeric()
                    

                    condition = conditionTerm  and  conditionMinutes and conditionSeconds  

                    if condition:
                        print(root, d)
                        registeredPaths.append(root + d)
                except IndexError:
                    continue
    

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
        isEphemeral(files, term, root)            

        isEphemeral(dirs, term, root)



    


checkFiles("ephemeral")

