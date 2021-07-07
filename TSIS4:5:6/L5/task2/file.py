import os, os.path
from pathlib import Path

path = os.getcwd()

def work_with_dir():
    print("""Choose option:
            1) Rename
            2) How many files in dir
            3) How many directories in dir
            4) Content
            5) Add file
            6) Add new directory 
    """)
    x = int(input())
    if x == 1:
        rename_dir()
    elif x == 2:
        files_dir()
    elif x == 3:
        directs_dir()
    elif x == 4:
        content_dir()
    elif x == 5:
        add_file_dir()
    elif x == 6:
        add_direct_dir()
    else:
        print("Invalid input")

def rename_dir():
    print("Write name of directory: ")
    try: 
        old_dir = str(input())
        new_dir = str(input("Write new name of directory: "))
        os.rename(old_dir, new_dir)
        print("Successfully changed!")
    except FileNotFoundError:
        print("File doesn't exist")

def files_dir():
    cnt = 0
    with os.scandir(path) as f:
        for i in f:
            if i.is_file():
                cnt += 1
    print(cnt, "files in directory {}".format(path))
        
def directs_dir():
    cnt = 0
    with os.scandir(path) as f:
        for i in f:
            if i.is_dir():
                cnt += 1
    print(cnt, "directories in directory {}".format(path))

def content_dir():
    cont = os.listdir(path)
    for i in cont:
        print(i)

def add_file_dir():
    print("Write name of new file: ")
    s = str(input())
    with open(s, "w") as f:
        print("File successfully created")
        f.close()

def add_direct_dir():
    print("Write name of new directory: ")
    s = str(input())
    os.mkdir(s)
    print("Directory is successfully created")

def work_with_file():
    print("""Choose option:
            1) Delete file
            2) Rename file
            3) Add content 
            4) Rewrite content 
            5) Return to the parent directory
    """)
    x = int(input())
    if x == 1:
        delete_file()
    elif x == 2:
        rename_file()
    elif x == 3:
        add_file()
    elif x == 4:
        edit_file()
    elif x == 5:
        return_file()
    else:
        print("Invalid input")

def delete_file():
    print("Write name of file: ")
    try:
        s = str(input())
        os.remove(s)
        print("File deleted")
    except FileNotFoundError:
        print("File doesn't exist")

def rename_file():
    print("Write name of file:")
    try:
        old_name = str(input())
        new_name = str(input("Write new name of file: "))
        os.rename(old_name, new_name)
        print("Successfully changed!")
    except FileNotFoundError:
        print("File doesn't exist")

def add_file():
    print("Write name of file: ")
    try:
        s = str(input())
        with open(s, "a") as f:
            f.write(str(input("Write data: ")))
        print("Successfully added!")
    except FileNotFoundError:
        print("File doesn't exist")

def edit_file():
    print("Write name of file: ")
    try: 
        s = str(input())
        with open(s, "w") as f:
            f.write(str(input("Write new data: ")))
        print("Successfully rewrited!")
    except FileNotFoundError:
        print("File doesn't exist")

def return_file():
    print("Enter path")
    try:
        s = str(input())
        path = Path(s).parent
        print(path)
    except FileNotFoundError:
        print("File doesn't exist")

def start():
    cur_dir = os.getcwd()
    print("You are on {}".format(cur_dir))
    print("""Choose option:
            1) Work with directory
            2) Work with file
            3) Exit
    """)
    x = int(input())
    if x == 1:
        work_with_dir()
    elif x == 2:
        work_with_file()
    elif x == 3:
        exit()
    else:
        print("Invalid input")
while(True):
    start()
