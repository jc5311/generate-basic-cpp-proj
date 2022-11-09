#!/usr/bin/env python3

"""
This program was designed to automatically generate a starting cpp project directory
complete with a starting .cpp, .h, and Makefile.
"""

import os     #needed for calls like os.path.exists()
import sys    #needed for things like sys.argv to get cli args
import shutil #needed for shutil.rmtree()

# "#defines"
DEFAULT_PROJECT_NAME    = "main"
FILES_TO_CPY_PATH       = "/opt/genProjCpp/filesToCopy/"
PROJECT_SRC_CPP         = "projectSource.cpp"
PROJECT_HEADER_H        = "projectHeader.h"
MAKEFILE                = "Makefile"
MAKEFILE_STR_TO_REPLACE = "_PROJECT_NAME_"

# Functions ----------------------------------------------------------------------------------------
def replaceInFile(filename, strToReplace, strToUse):

    # Read in the file
    with open(filename, "r") as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace(strToReplace, strToUse)

    # Write the file out again
    with open(filename, "w") as file:
        file.write(filedata)

def writeHeaderGuardToFile(filename, projectName):
    # Open and write to the file
    with open(filename, "w") as file:
        file.write("#ifndef __%s_H__\n" %(projectName.upper()))
        file.write("#define __%s_H__\n\n" %(projectName.upper()))
        file.write("#endif //__%s_H__\n" %(projectName.upper()))

# Main ---------------------------------------------------------------------------------------------
# print(os.getcwd()) #print cwd; debug only

if (len(sys.argv) > 1):
    projectName = sys.argv[1]
else:
    projectName = DEFAULT_PROJECT_NAME

#check if the directory exists, if so, ask the user if they really wish to
#generate new project files there
if (os.path.exists(projectName)):
    print("Directory \"%s\" already exists. Remove and create new project in its place?" %(projectName))
    response = input("Enter (y/n): ").lower()

    if (response == 'y'):
        print("Replacing \"%s\" with fresh new directory" %(projectName))
        shutil.rmtree(projectName)
    else:
        print("Exiting...")
        quit()

"""
Steps:
1. Create <projectName> directory
2. Copy over projectSource.cpp to <projectName>/<projectName>.cpp
3. Copy over projectHeader.h to <projectName>/<projectName>.h
4. Write header guards into <projectName>/<projectName>.h
5. Copy over Makefile to <projectName>/Makefile
6. Replace all usages of "projectName" in target Makefile to <projectName>
"""

#step 1
os.mkdir(projectName)
os.chdir(projectName)
#step 2
shutil.copy(FILES_TO_CPY_PATH + PROJECT_SRC_CPP, projectName + ".cpp")
#step 3
shutil.copy(FILES_TO_CPY_PATH + PROJECT_HEADER_H, projectName + ".h")
#step 4
writeHeaderGuardToFile(projectName + ".h", projectName)
#step 5
shutil.copy(FILES_TO_CPY_PATH + MAKEFILE, MAKEFILE)
#step 6
replaceInFile(MAKEFILE, MAKEFILE_STR_TO_REPLACE, projectName)

print ("Done!")