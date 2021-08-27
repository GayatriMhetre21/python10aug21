def filesize(fname):
    import os
    statinfo=os.stat(fname)
    return statinfo.st_size
print("File size :: "+str(filesize("text.txt"))+"bytes")