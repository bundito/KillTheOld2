
import os
from os import stat
import time
import arrow

BASEDIR = r'C:\Users\bundi\Downloads\\'

isoFiles = []
isoDirs = []
archFiles = []
imgFormats = {".iso", ".bin"}
arcFormats = {".rar", ".zip", ".7z", ".gz", ".nzb", ".exe"}
returnItems = []

def dateCheck(item, suns=7):
    itemTime = os.path.getatime(item)

    # itemTime =  * 1000

    # make moments
    itemSafe = False

    itemArrow = arrow.get(itemTime)
    nowArrow = arrow.now()

    agedSeven = itemArrow.shift(days=+suns)

    if agedSeven <= nowArrow:
        itemSafe = True
    return itemSafe

'''
    print("item: ", item)
    print("atime: ", itemArrow)
    print("aged: ", agedSeven)
    print("+7: ", itemSafe)
    print("-----------------")

'''

# Clean out old disc image files left over from decompression

# Start at top level of directory
def checkFiles():
    filesOnly = os.scandir(BASEDIR)
    for thisFile in filesOnly:
        if os.path.isfile(thisFile):
            if os.path.splitext(thisFile)[1] in imgFormats:
                if dateCheck(thisFile,3):
                    isoFiles.append(thisFile)
                break
    return isoFiles


# Recurse into subdirectories; flag parent for deletion
def checkDirs():
    dirsOnly = os.listdir(BASEDIR)
    for searchDir in os.scandir(BASEDIR):
        if os.path.isdir(searchDir):
            for seekFile in os.listdir(searchDir):
                if os.path.splitext(seekFile)[1] in imgFormats:
                    if dateCheck(searchDir, 3):
                        isoDirs.append(searchDir)
                    break
    return isoDirs

# Scour archive files the same way, but we only have to worry about top level
def checkArchives():
    filesOnly = os.scandir(BASEDIR)
    for thisFile in filesOnly:
        if os.path.isfile(thisFile):
            if os.path.splitext(thisFile)[1] in arcFormats:
                if dateCheck(thisFile):
                    archFiles.append(thisFile)
    return archFiles

