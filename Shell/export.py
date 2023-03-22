from os import system as sys


def export_shell(export_dir):
    print("Exporting shell configurations...")

    # Creating the main directory for archives
    # sys("mkdir -p /tmp/shell-archives")

    files_dir = [".bashrc .oh-my-zsh .p10k.zsh .zhistory .zim .zimrc .zsh_history .zshrc"]

    for i in files_dir:
        sys(f"tar -cjf {export_dir}Shell.tar.bz2 -C $HOME { i }")

    # print("Exporting is done please refer to this directory. () ")
    print("DONE!")


def import_shell(export_dir):
    print("Starting the Import of Shell Configuration")

    sys(f"tar -xvjf {export_dir}Shell.tar.bz2 -C $HOME")

    print("DONE!")
