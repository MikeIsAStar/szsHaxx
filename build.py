"""Constructs the loader for all regions and embeds it within the file 'wc24scr.vff'.
"""

__author__ = 'MikeIsAStar'
__date__ = '20 May 2024'

import os
import shutil
import subprocess
import sys

if sys.version_info < (3, 6):
    sys.exit('This program requires Python 3.6 or above !')


# Constants
REGIONS = ['RMCP', 'RMCE', 'RMCJ', 'RMCK']
VFF_FILE_HEADER_SIZE = 0x20
VFF_FILE_PATH = './data/save/vff/clean/wc24scr.vff'


def main():
    completed_process = subprocess.run(["make", "clean", "all"], cwd="./loader")
    if completed_process.returncode != 0:
        sys.exit('Failed to make the loader !')

    for region in REGIONS:
        loader_filepath = f'./loader/out/{region}/loader.bin'
        output_filepath = f'./data/save/vff/modified/{region}/wc24scr.vff'

        try:
            output_directory = os.path.dirname(output_filepath)
            os.makedirs(output_directory, exist_ok=True)
        except OSError:
            sys.exit(
                f'Failed to create the directory \'{output_directory}\' !')

        try:
            shutil.copy(VFF_FILE_PATH, output_filepath)
        except:
            sys.exit(
                f'Failed to copy the file \'{VFF_FILE_PATH}\' to \'{output_filepath}\' !')

        try:
            with open(loader_filepath, 'rb') as loader_file:
                loader_file_contents = loader_file.read()
        except:
            sys.exit(
                f'Failed to read in the contents of the file \'{loader_filepath}\' !')

        try:
            with open(output_filepath, 'r+b') as vff_file:
                vff_file.seek(VFF_FILE_HEADER_SIZE + 0x10)
                vff_file.write(loader_file_contents)
        except:
            sys.exit(
                f'Failed to write the loader to the file \'{output_filepath}\' !')

        print(
            f'Successfully wrote the loader to the file \'{output_filepath}\' ')


if __name__ == '__main__':
    main()
