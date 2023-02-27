# PasswordManager

## A password manager, generator and cipher made in python 🐍

This project is an password manager in python. It encrypt your key and after cipher your password with the unencrypt key.
This is firstely a personnal project but I've finely put it in github if someone want to use it.
All your data is stored in a local file.

## Setup 🖥️

For the setup of the Manager, you just have to launch `setup.py`. After, just launch pw-manager and enter "TEST" on the shell.
If you want to change the master key, you have to change `setup.py` and put your own key.

## PasswordEncrypter 🔑

To encrypt the key, I put all the ascii code of the letters of the key in a matrix and I multiply it by itself. After, I translate the matrix in a new string and it's the first line of `password.txt`.
For all of the passwords, I multiply the ascii code of all of the letters by the coresponding code of the unencrypted key. 

## PasswordGenerator 🔁

For the generator, I use random.SystemRandom which use the real random of your OS and it's better for crypography like I want to do. 
