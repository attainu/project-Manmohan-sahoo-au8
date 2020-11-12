# junk file organiser

# importinf modules from python library

import os
import math
import datetime
import shutil
# for command line
import sys
import argparse

CURRENT_DIRECTORY=r"E:\folder"

#organize by extension:

def organizeByExtension(path):
  files=os.listdir(path)
  all_files=[]

#split file extension
  for i in files:
    _, split = os.path.splitext(i)
    if split not in all_files:
      all_files.append(split)

# creating the separate folders 
  for extension in all_files:
    if extension:
      os.mkdir(os.path.join(path,extension))

#moving all the files to their specific folder
  for i in files:
    _, extension = os.path.splitext(i)
    old_path=os.path.join(path,i)
    new_path=os.path.join(path,extension,i)
    os.rename(old_path, new_path)



#define the function for command line parsing
def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--path",default=".",help="Which folder to organize ?")
  parser.add_argument("--o",default="extension",help="organize by?",choices=["extension"])

  args=parser.parse_args()
  path=args.path
  organize_by=args.o

  if organize_by == "extension":
    organizeByExtension(path)
  else:
    print("wrong input")

if __name__ == "__main__":
    main()





