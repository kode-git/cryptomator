# this file include functions of encrypting for files in sha256 format
# made by kode with love

import hashlib
import os


# Buff size for encrypt at 64 KB
BUF_SIZE = 65536

def encrypt(filename, dump):
    """
    Given a filename (str) and a dump (string), it encrypts the files and append the hash into dump
    """

    # sha256 encryption
    sha256 = hashlib.sha256()
    with open(filename, "rb") as file:

        while True:
            data = file.read(BUF_SIZE)
            if not data:
                break
            sha256.update(data)
    with open(dump, "a") as file:
        # writing in the dump the format <name> -> <hash>
        file.write(f'{filename.path} -> {sha256.hexdigest()}\n')


def wrapper_encrypt_r(path, dump):
    """
    Wrapping func for dump file controls
    """
    try:
        # control on file for no overwriting content
        os.remove(dump)
        file = open(dump, 'w')
        file.close()
        encrypt_r(path, dump)
    except FileNotFoundError:
        encrypt_r(path, dump)


def encrypt_r(path, dump):
    """
    Visit directories of path and save the hash of files in dump
    """
    for file in os.scandir(path):
        if file.is_file():
            print('Hash for: ' + file.path)
            encrypt(file, dump)
        elif file.is_dir():
            print('Going inside: ' + file.path)
            encrypt_r(file.path, dump)


def wrapper_list_file(path):
    print("=========================")
    print(f"Total files: {list_file(path, 0)}")


def list_file(path, i):
    """
    Recursive func to list files form a root path
    """
    for file in os.scandir(path):
        if file.is_file():
            print('File check: ' + file.path)
            i = i + 1
        elif file.is_dir():
            print('Going inside: ' + file.path)
            i = list_file(file.path, i)
    return i


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="File encrypt/decrypt")

    # essential arguments
    parser.add_argument("direct", help="Directory to encrypt/decrypt")


    # not essential if -l is specified
    parser.add_argument("-e", "--encrypt", action="store_true",
                        help="Whether to encrypt the file, only -e or -d can be specified.")
    # not essential if -d is specified
    parser.add_argument("-l", "--list", action="store_true",
                        help="Whether to encrypt the file, only -e or -l can be specified.")

    # get arguments from input with parse_args
    args = parser.parse_args()
    direct = args.direct
    encrypt_ = args.encrypt
    list_ = args.list


    # check encrypt or list files
    if encrypt_ and list_:
        raise TypeError("Please specify -e to encrypt files or -l to list files")
    elif encrypt_:
        dump_name = input("Digit the name of the dump file where store hash.\nWARNING: Do not write extension (e.g. if write file.txt will be file.txt.txt)\nDigit the name of the dump file: ")
        dump_name = f"{dump_name}.txt"
        wrapper_encrypt_r(direct, dump_name)
    elif list_:
        wrapper_list_file(direct)
    else:
        raise TypeError("Please specify whether you want to encrypt the file or decrypt it.")
