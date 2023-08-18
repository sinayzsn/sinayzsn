from os import system as sys


def export_ssh(export_dir):
    print("Creating an export from SSH directory...")
    sys(f"tar -cjf {export_dir}/ssh_export.tar.bz2  -C $HOME .ssh")

    print(f"Export Complete putting the file in {export_dir}")
