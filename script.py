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
    orgo_create(main_path,"Text_Files",".txt")
    orgo_create(main_path,"Documents",".doc",".docx",".pptx",".rtf",".ppt")
    orgo_create(main_path,"CSV_Files",".xlsx",".csv")
    orgo_create(main_path,"Media",".mp3",".mp4",".mkv",".webm")
    orgo_create(main_path,"PDF_Files",".pdf")
    orgo_create(main_path,"Images",".jfif",".jpeg",".jpg",".png",".svg",".psd",".webp")
    orgo_create(main_path,"Applications",".lnk",".exe")
    orgo_create(main_path,"Torrents",".torrent")
    orgo_create(main_path,"HTML_AND_CSS",".html",".css",".ejs")
    orgo_create(main_path,"PythonCodes",".py",".pkl",".ipynb",".yml")
    orgo_create(main_path,"Zipped",".zip",".rar")
    orgo_create(main_path,"APK",".apk")
    orgo_create(main_path,"Subtitles",".srt")
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
        