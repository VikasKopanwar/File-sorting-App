import os, shutil

folders = {
    'videos': ['.mp4'],
    'audios': ['.wav','.mp3'],
    'images':['.jpg','.png'],
    'documents':['.docx','.xlsx','.xls','.pdf','.zip','.rar'],
}

#print(folders)

# for folder_name in folders:
#     print(folder_name,folders[folder_name])

#Rename folder to lower case
def rename_folder():
    #loop through each file in the dir
    for folder in os.listdir(directory):
        #check if it is directory or not
        if os.path.isdir(os.path.join(directory,folder))==True:
            #rename the folder to lower case
            #first parameter to specify the path
            #second parameter to lower the folder name
            os.rename(os.path.join(directory,folder),os.path.join(directory,folder.lower()))



def create_move(ext,file_name):
    '''
    Move files to folders
    '''
    find = False
    for folder_name in folders:
        #check if file extension there in folders dict 
        #comparing extension passed with data elements of the dict
        if '.'+ext in folders[folder_name]:
            #if folder_name i.e. 'videos', 'audio' etc not in the directory make a new folder using os.mkdir(os.path.join())
            if folder_name not in os.listdir(directory):
                os.mkdir(os.path.join(directory,folder_name))
            else:
                '''move the files using shutil.move()
                first parameter current directory
                second parameter is to which the files will be moved
                '''
                shutil.move(os.path.join(directory,file_name),os.path.join(directory,folder_name))
            find = True
            break
    if find!= True:
        '''
        #if file extension not matched in the listed dict(folders)
        '''
        #if othername folder already in directory
        if other_name not in os.listdir(directory):
            #make new dir/folder in the dir in the name of other_name
            os.mkdir(os.path.join(directory,other_name))
            shutil.move(os.path.join(directory,file_name),os.path.join(directory,other_name))


#takes file path as input from user
directory = "C:\\Users\\Priyen\\OneDrive\\Desktop\\MCA Study Material"

#for other extension files; other than mentioned in folders dict
other_name =input("Enter folder name for unknown: ")

#returns all the files in the user specified path as list
all_files = os.listdir(directory)

#length of all files
length = len(all_files)
count = 1

#Call function
rename_folder()

#loop over the files in the directory
for i in all_files:
    #check whether there are files in the path mentioned
    if os.path.isfile(os.path.join(directory,i))==True:
        #calling the function
        #splitting the file in with "." extension and also getting the file name
        create_move(i.split('.')[-1],i)
    print(f"Total files: {length} | Done: {count} | Left: {length-count} ")
    count = count + 1
    