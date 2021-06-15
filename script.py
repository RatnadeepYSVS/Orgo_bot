from os import *
from os.path import isfile
from subprocess import *
from shutil import *
from glob import *
def orgo_create(main_path,folder,*extensions):
    cr_path=main_path+"\\"+folder
    for extension in extensions:
        ext_req_files=glob(main_path+"\\*"+extension)
        if len(ext_req_files)!=0:
            try:
                makedirs(cr_path)
            except FileExistsError:
                print("Folder Exists.Adding Files in here")
            for file in ext_req_files:
                move(file,cr_path)
command=["ls"]
result=run(command,stdout=PIPE,stderr=PIPE,universal_newlines=True)
print(f"Hi I Am Orgo Your Directories Organizer Bot")
print("I can move your files and folders, organize them and if you want i can delete them")
print("Please Select Any One Option Below")
print("1.Move Your Files And Folders In Your Current Directory To Your Required Folder")
print("2.Organize Your Files And Folders In The Directory")
print("3.Delete The Files and Folders U Specify")
main_path=input("Please Enter Path To The Directory U Want ")
print("The Files And Folders In this path are")
dirs=listdir(main_path)
print(dirs)
option=int(input("Please Select Any One Option "))
if option==1:
    files_folders=input("Enter The Files or Folders name which you want to move ").split()
    for k in files_folders:
        try:
            move_path=input("Please Enter the path to folder you want to move this file or folder ")
            move(main_path+"\\"+k,move_path)
        except FileNotFoundError:
            print("Please Provide A Valid File Or Folder")
elif option==2:
    if any(".txt" or ".docx" or ".doc" or ".pptx" in i for i in dirs):
        orgo_create(main_path,"Text_Files",".txt")
    if any(".docx" or ".doc" or ".pptx" in i for i in dirs):
        orgo_create(main_path,"Documents",".doc",".docx",".pptx")
    if any(".xlsx" or ".csv" in i for i in dirs):
        orgo_create(main_path,"CSV_Files",".xlsx",".csv")
    if any(".mp3" or ".mp4" or ".mkv" in i for i in dirs):
        orgo_create(main_path,"Media",".mp3",".mp4",".mkv")
    if any(".pdf" in i for i in dirs):
        orgo_create(main_path,"PDF_Files",".pdf")
    if any(".jfif" or ".jpeg" or ".jpg" or ".png" in i for i in dirs):
        orgo_create(main_path,"Images",".jfif",".jpeg",".jpg",".png")
    if any(".lnk" or ".exe" in i for i in dirs):
        orgo_create(main_path,"Applications",".lnk",".exe")
elif option==3:
    files_to_remove=input("Enter Files and folders u want to remove ").split()
    for i in files_to_remove:
        p=main_path+"\\"+i
        if isfile(p):
            remove(p)
        else:
            try:
                rmdir(p)
            except:
                print("You are trying to remove a directory of files")
                print("Are you sure u want to delete the directory this action is irreversible")
                k=input("Yes : No")
                if k=="Yes":
                    rmtree(p)
                else:
                    pass
        