import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')

# TODO: Use the glob.glob() function to obtain the list of filenames

# TODO: use os.path.getsize to find each file's size

# TODO: Add a test to only display files that are not zero length

# TODO: Remove the leading directory name(s) from each filename before you print it - 
# using os.path.basename()




def size(path):
    return os.path.getsize(path)


def greaterThanZero(num):
    return len(num) > 30


def fileBaseName(finalpath):
    return os.path.basename(finalpath)


filesList = glob.glob(pattern)
noEmptyFiles = list(filter(greaterThanZero, filesList))
fileSizeList = map(size, noEmptyFiles)
final = list(fileSizeList)
fileBase = list(map(fileBaseName, noEmptyFiles))






print(final)
print(fileBase)







