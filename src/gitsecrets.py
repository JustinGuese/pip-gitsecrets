import argparse
from pathlib import Path
from glob import glob
from cryptography.fernet import Fernet
from sys import exit

parser = argparse.ArgumentParser("gitsecrets")
parser.add_argument("-e", "--encrypt", help="Encrypt all secrets in this folder with the given password")
parser.add_argument("-d", "--decrypt", help="Decrypt all secrets in this folder with the given password")#
parser.add_argument("-i", "--init", help="Initialize gitsecrets", action="store_true")

args = parser.parse_args()
# only one can be set
if args.encrypt and args.decrypt:
    parser.error("Only one of -e or -d can be set")
# check if setup folders already exist
if not Path("gitsecrets").exists():
    # tell them to run init if they sayd not init
    if not args.init:
        print("Please run `gitsecrets -i` to initialize gitsecrets")
        exit(1)
    else:
        # they ran git init
        Path("gitsecrets").mkdir()
        Path("gitsecrets/raw").mkdir()
        Path("gitsecrets/encrpyted").mkdir()
        
        with open(".gitignore", "a") as f:
            f.write("\ngitsecrets/raw/*\n")
            
        # then generate a password for the user
        key = Fernet.generate_key()
        print("!! your password is " + key.decode("utf-8"))
        print("save this to a secure location as i will not repeat it again")
        del key
else:
    # if folder already set up
    if args.init:
        print("gitsecrets already initialized. continue with -e or -d")
        exit(1)
    # else check if they want to encrypt or decrypt
    if args.encrypt is not None:
        try:
            key = Fernet(args.encrypt)
        except Exception as e:
            raise ValueError("problem with password! are you sure you used the one the init gave you? looks like: dd4e1pk3UlYgx47ZadAX9GU_dbHYfche62zMTkOsleI=")
        # encrypt all files in gitsecrets/raw folder
        for file in glob("gitsecrets/raw/*"):
            with open(file, "rb") as f:
                data = f.read()
            encrypted_data = key.encrypt(data)
            purefilename = Path(file).name
            with open("gitsecrets/encrpyted/" + purefilename, "wb") as f:
                f.write(encrypted_data)
            del encrypted_data, data
    # decrypt
    if args.decrypt is not None:
        try:
            key = Fernet(args.decrypt)
        except Exception as e:
            raise ValueError("problem with password! are you sure you used the one the init gave you? looks like: dd4e1pk3UlYgx47ZadAX9GU_dbHYfche62zMTkOsleI=")
        # decrypt all files in gitsecrets/encrpyted folder
        for file in glob("gitsecrets/encrpyted/*"):
            with open(file, "rb") as f:
                data = f.read()
            decrypted_data = key.decrypt(data)
            purefilename = Path(file).name
            with open("gitsecrets/raw/" + purefilename, "wb") as f:
                f.write(decrypted_data)
            del decrypted_data, data