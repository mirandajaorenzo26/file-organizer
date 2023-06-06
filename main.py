import os
import shutil
import time


def organize_files(directory_path):
    files = os.listdir(directory_path)

    # Dictionary mapping file extensions to directory names
    file_extensions = {
        'pdf': 'PDFs',
        'png': 'Images',
        'jpg': 'Images',
        'jpeg': 'Images',
        'gif': "Images",
        'doc': 'Documents',
        'docx': 'Documents',
        'xlsx': 'Spreadsheets',
        'ppt': 'Presentations',
        'txt': 'Texts',
        'csv': 'CSVs',
        'zip': 'Archives',
        'rar': 'Archives',
        'exe': 'Executables',
        'mp4': 'Videos',
        'mov': 'Videos',
        'avi': 'Videos',
        'mp3': 'Music',
        'wav': 'Music',
        'flac': 'Music'
    }

    for file_extension, directory_name in file_extensions.items():
        directory = os.path.join(directory_path, directory_name)
        os.makedirs(directory, exist_ok=True)

    # Move files to respective directories based on file extension
    for file in files:
        # Split filename and extension
        filename, extension = os.path.splitext(file)
        extension = extension[1:]

        # Get the destination directory based on the file extension
        destination_directory = os.path.join(directory_path, file_extensions.get(extension, 'Other'))

        # Move the file to the destination directory
        if os.path.exists(destination_directory):
            shutil.move(os.path.join(directory_path, file), os.path.join(destination_directory, file))

    # Check for empty directories and delete them
    for root, dirs, files in os.walk(directory_path, topdown=False):
        for directory in dirs:
            folder_path = os.path.join(root, directory)
            if not os.listdir(folder_path):
                os.rmdir(folder_path)


while True:
    print("--FILE ORGANIZER--")
    directory_path = input('Enter Path: ')
    choice = input(f'Are you sure you want to organize the files located in {directory_path} [y/N]: ')

    if choice.lower() == "y":
        print("Organizing...")
        time.sleep(3)
        organize_files(directory_path)
        print("Done")
        time.sleep(3)
        os.system('cls')
    else:
        print("Cancelled")
        print("Closing...")
        time.sleep(3)

        break
