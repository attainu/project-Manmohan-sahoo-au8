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

#organize by size

def organizeBySize(path):
  dirs=os.listdir(path)
  dir_size1={}

  for j in dirs:
    dir_size1[j]=os.stat(os.path.join(path,j)).st_size

  sorted_dir=sorted(dir_size1.items(),key=lambda c:c[1])
  dir_size0 = []
  size_types = []

  for j in sorted_dir:
    a1 = (os.stat(os.path.join(path,j[0])).st_size)
    a2 = convert_size(a1)
    a3 = str(a2).split("_")

    if a3 == [] or a3 == ["0B"]:
      pass
    else:
      dir_size0.append(a3)
  types=[]
  sub = "."
  for j in sorted_dir:
    if sub in j[0]:
      b1=j[0][::-1].find(".")
      b2=j[0][-b1:]
      if b2 not in types:
        types.append(b2)

#creating folder
  for j in dir_size0:
    if j[1] not in size_types:
      size_types.append(j[1])
  for j in size_types:
    for k in dir_size0:
      if k[1] == j and int(k[0]) < 50 :
        if not os.path.exists(os.path.join(path,"lessThan50" + k[1])):
          os.mkdir(os.path.join(path,"lessThan50"+k[1]))
      elif k[1] == j and int(k[0]) > 50:
        if not os.path.exists(os.path.join(path,"graterThan100" + k[1])):
          os.mkdir(os.path.join(path,"graterThan100" + k[1]))

#moving files to folder
  newFiles = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path,file))]
  x = [x for x in newFiles if checkFIle(x) == False]
  for j in x:
    new_size = convert_size(os.stat(os.path.join(path,j)).st_size)
    new_size = new_size.split("_")
    if int(new_size[0]) < 50 :
      shutil.move(os.path.join(path,j),os.path.join(path,"lessThan50" + new_size[1]))
    else:
      shutil.move(os.path.join(path,j),os.path.join(path,"graterThan100" + new_size[1]))

# converting bytes to readable size
def convert_size(size_bytes):
  if size_bytes == 0:
    return "0B"

  size_name=("B","KB","MB","GB","TB","PB","EB","ZB","YB")
  i=int(math.floor(math.log(size_bytes,1024)))
  p=math.pow(1024,i)
  s=round(size_bytes/p,2)
  return "%s_%s" % (round(s),size_name[i])

def checkFIle(fileName):
  d = os.path.basename(__file__)
  if fileName == d:
    return True
  return False


#define the function for command line parsing
def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--path",default=".",help="Which folder to organize ?")
  parser.add_argument("--o",default="extension",help="organize by?",choices=["extension","size"])

  args=parser.parse_args()
  path=args.path
  organize_by=args.o

  if organize_by == "extension":
    organizeByExtension(path)
  elif organize_by == "size":
    organizeBySize(path)
  else:
    print("wrong input")


if __name__ == "__main__":
    main()





