# generate-basic-cpp-proj
A python script for creating a basic c++ project including a .cpp, .h, and makefile.

## Install directions:
* On a Linux machine copy the genProjCpp directory to /opt
* In /usr/bin create a symbolic link pointing to /opt/genProjCpp/genProjCpp.py

## How to run:
`$ genProjCpp <project_name>`

## Description:
I wrote this script to facilitate creating starter files for c++ projects. When
studying c++ textbooks or Udemy courses I like following and storing exercises
locally on my PC. With time it got tiring making fresh directories, .cpp, .h,
and Makefiles for each small exercise, hence the birth of this repo ;)

The python script genProjCpp.py will create a new <project_name> directory wherever
it is run and add the following files to it:
* <project_name>.cpp
* <project_name>.h
* Makefile

Each file will already have some starter content to work with including header
guards for the .h file and rules for the Makefile.
