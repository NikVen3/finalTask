import os
import logging
from collections import namedtuple

# Configure logging
logging.basicConfig(filename='file_info.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Define namedtuple for file information
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])


def collect_file_info(directory_path):

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_name, file_extension = os.path.splitext(file)
            file_info = FileInfo(
                name=file_name,
                extension=file_extension[1:],  # Remove the dot from the extension
                is_directory=False,
                parent_directory=os.path.basename(root)
            )
            logging.info(file_info)

        for directory in dirs:
            directory_info = FileInfo(
                name=directory,
                extension=None,
                is_directory=True,
                parent_directory=os.path.basename(root)
            )
            logging.info(directory_info)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    if not os.path.isdir(directory_path):
        print(f"Error: {directory_path} is not a valid directory.")
        sys.exit(1)

    collect_file_info(directory_path)
