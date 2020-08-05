import os
import sys
import subprocess
projects = r"C:\Users\pin-d\OneDrive\Bureaublad\projects\InProgress Projects\Important"
tutorials = r"C:\Users\pin-d\OneDrive\Bureaublad\projects\Tutorials"
vs_code =  r"C:\Users\pin-d\AppData\Local\Programs\Microsoft VS Code\Code.exe"

def openMark(string):
    return '-o' in string

def main():
    choices = ('t', 'p')

    if len(sys.argv) != 2:
        print(f"Provide type of work choices are: {' or '.join(choices)}")
        return
    typeOfWork = sys.argv[1]
    if typeOfWork not in choices:
        print(f"{typeOfWork} is not in available")
        return
    if typeOfWork == 't':
        os.chdir(os.path.abspath(tutorials))
    else:
        os.chdir(os.path.abspath(projects))
    print('--------Current directory is:----------')
    print(os.getcwd())
    print()
    print('--------Files in this directory--------')
    for item in os.listdir():
        print(item)
    print()
    keyword = input('Select your keyword: ')
    without_mark =  keyword.replace('-o', '') if openMark(keyword) else keyword
    filter_by_keyword = [x for x in os.listdir() if without_mark.lower() in x.lower()]
    if len(filter_by_keyword) == 0:
        print('Didnt fount anything with that keyword')
    elif len(filter_by_keyword) == 1:
        pathOfFolder = os.path.join(os.getcwd(), filter_by_keyword[0])
        if openMark(keyword) or len(folders_in(pathOfFolder)) == 0:
            os.chdir(pathOfFolder)
            subprocess.Popen([vs_code, os.getcwd()])
        else:
            for count, item in enumerate(folders_in(pathOfFolder)):
                print(folders_in(pathOfFolder))
            # openPath = os.path.join(os.getcwd(), filter_by_keyword[0])
            # os.chdir(openPath)
            # subprocess.Popen([vs_code, os.getcwd()])
    else:
        print('huh')
        print(choices_items(filter_by_keyword))
        # items={}
        # for count, item in enumerate(filter_by_keyword):
        #     print(str(count)+': ' + item)
        #     items[count] = item
        # choice = input('Which one do you mean?:')
        # if choice in str(items.keys()):
        #     print()
    # print(os.listdir())
    # subprocess.Popen('explorer /select,{projects}')

def folders_in(path_to_parent):
    folders = []
    exceptions = ['.git']
    for fname in os.listdir(path_to_parent):
        if os.path.isdir(os.path.join(path_to_parent,fname)):
            if fname in exceptions:
                continue
            else:
                folders.append(fname)
    return folders


def choices_items(list_with_dir):
    items={}
    print(items)
    for count, item in enumerate(list_with_dir):
        print(str(count)+': ' + item)
        items[count] = item
    choice=False
    while not choice:
        user_input = input('Which one do you mean?:')
        if choice in str(items.keys()):
            choice = user_input
    print(items[choice])
    return items[choice]
main()