from os import system as sys

print("Starting the Import of Shell Configuration")

sys("tar -xvjf Shell.tar.bz2 -C $HOME")

print("DONE!")