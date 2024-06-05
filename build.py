"""Generates the files 'rksys.dat' and 'wc24scr.vff' for all regions of Mario Kart Wii.
"""

__author__ = 'MikeIsAStar'
__date__ = '04 Jun 2024'

from dataclasses import dataclass
import os
import struct
import subprocess
import sys
import zlib

if sys.version_info < (3, 7):
    sys.exit('This program requires Python 3.7 or above !')


def read_from_file(filepath, bytes_to_read=-1):
    try:
        with open(filepath, 'rb') as file:
            return file.read(bytes_to_read)
    except BaseException:
        sys.exit(f'Failed to read the contents of the file \'{filepath}\' !')


def write_to_file(filepath, bytes_to_write):
    destination_directory = os.path.dirname(filepath) or os.curdir

    try:
        os.makedirs(destination_directory, exist_ok=True)
    except BaseException:
        sys.exit(f'Failed to create the directory \'{destination_directory}\' !')

    try:
        with open(filepath, 'wb') as file:
            file.write(bytes_to_write)
    except BaseException:
        sys.exit(f'Failed to write the contents to the file \'{filepath}\' !')


def compile_loader():
    try:
        completed_process = subprocess.run(['make', 'clean', 'all'], cwd='./loader')
    except BaseException:
        sys.exit('Failed to execute the \'make\' command !')

    if completed_process.returncode != 0:
        sys.exit('Failed to compile the loader for all regions of Mario Kart Wii !')


def create_rksys_dat_files():
    @dataclass(frozen=True)
    class RKSysDatFileInfo:
        modified_filepath: str
        region_id: bytes

    clean_rksys_dat_filepath = './data/save/rksys/clean/rksys.dat'
    rksys_dat_checksum_offset = 0x27FFC
    rksys_dat_file_info_array = [
        RKSysDatFileInfo('./data/save/rksys/modified/RMCJ/JPN/rksys.dat', b'\x00'),
        RKSysDatFileInfo('./data/save/rksys/modified/RMCE/rksys.dat'    , b'\x10'),
        RKSysDatFileInfo('./data/save/rksys/modified/RMCP/EUR/rksys.dat', b'\x20'),
        RKSysDatFileInfo('./data/save/rksys/modified/RMCP/AUS/rksys.dat', b'\x30'),
        RKSysDatFileInfo('./data/save/rksys/modified/RMCJ/TWN/rksys.dat', b'\x40'),
        RKSysDatFileInfo('./data/save/rksys/modified/RMCK/rksys.dat'    , b'\x50'),
    ]
    rksys_dat_region_id_offset = 0x26B0A

    modified_rksys_dat_file_contents = bytearray(read_from_file(clean_rksys_dat_filepath))

    for rksys_dat_file_info in rksys_dat_file_info_array:
        modified_rksys_dat_file_contents[rksys_dat_region_id_offset:rksys_dat_region_id_offset + len(
            rksys_dat_file_info.region_id)] = rksys_dat_file_info.region_id
        crc32_checksum = struct.pack('>I', zlib.crc32(
            modified_rksys_dat_file_contents[:rksys_dat_checksum_offset]))
        modified_rksys_dat_file_contents[rksys_dat_checksum_offset:
                                         rksys_dat_checksum_offset + len(crc32_checksum)] = crc32_checksum
        write_to_file(rksys_dat_file_info.modified_filepath, modified_rksys_dat_file_contents)


def create_wc24scr_vff_files():
    clean_wc24scr_vff_filepath = './data/save/vff/clean/wc24scr.vff'
    regions = ['RMCP', 'RMCE', 'RMCJ', 'RMCK']
    vff_file_header_size = 0x20

    modified_wc24scr_vff_file_contents = bytearray(read_from_file(clean_wc24scr_vff_filepath))

    for region in regions:
        loader_bin_filepath = f'./loader/out/{region}/loader.bin'
        modified_wc24scr_vff_filepath = f'./data/save/vff/modified/{region}/wc24scr.vff'

        loader_bin_file_contents = read_from_file(loader_bin_filepath)
        modified_wc24scr_vff_file_contents[vff_file_header_size +
                                           0x10: vff_file_header_size +
                                           0x10 +
                                           len(loader_bin_file_contents)] = loader_bin_file_contents
        write_to_file(modified_wc24scr_vff_filepath, modified_wc24scr_vff_file_contents)


def main():
    compile_loader()
    print('Successfully compiled the loader for all regions of Mario Kart Wii !')
    create_rksys_dat_files()
    print('Successfully created the file \'rksys.dat\' for all regions of Mario Kart Wii !')
    create_wc24scr_vff_files()
    print('Successfully created the file \'wc24scr.vff\' for all regions of Mario Kart Wii !')


if __name__ == '__main__':
    main()
