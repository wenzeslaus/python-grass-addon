import fnmatch

def attributes(obj):
    """Function to return attributes of object
       without magic method
    """
    return sorted(fnmatch.filter(dir(obj), '[!_]*'))
