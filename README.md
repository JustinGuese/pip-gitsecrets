an easy way to encrypt and decrypt files in a github repository. 

i am using it for kubernetes secrets for example.

## usage

### 1. init

the init command creates a folder "gitsecrets", with subfolders "encrypted" and "raw", and a .gitignore that features the raw folder.

also the init command outputs a password that you need to store somewhere in order to decrypt the secrets.

### 2. encrypt

save some files in the **gitsecrets/raw/** folder, and run
`gitsecrets.py -e YOURPASSWORD`

this creates an encrypted copy of that file in the **gitsecrets/encrypted/** folder.

### 3. decrypt

using your password you can then decrypt all files into the **raw** folder again

`gitsecrets.py -d YOURPASSWORD`