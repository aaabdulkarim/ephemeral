# ephemeral
This Package will delete files a while after creation. It is used for downloaded files, which are meant to be used temporarily. 

# Usage

By default, after installation of the package any file which ends with a "-temp" will be deleted after the default time configuration. Also directories, which are named temp, will be cleared. Using the config files you can specify which directories should be treated as "temporary files".

The Program checks every 5 minutes for files, which are recognized by the naming convention. It will then be added to the pool and be deleted based on the file name with correct naming convention. If the file name doesn't match the naming convention and was only recognised because it has a term (or absolute path is given in the configs) it will instead be deleted after the default time to live.

# Default Config File

...


