from os import system as sys
from environments import config

def install_python_310():
    print("Add the python3.10 repository")
    sys("sudo add-apt-repository ppa:deadsnakes/ppa")

    print("Update repository")
    sys("sudo apt-get update")

    print("Install python3.10")
    sys("sudo apt-get install python3.10")

    print("Setting python3.10 as the default python interpreter")
    sys("sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1 && "
        "sudo update-alternatives --config python3")


class DfConfigs:
    export_dir = "/tmp/OS_export"
    # default_editor = "vim"
    default_editor = f"{config[DefaultEditor]}"
    default_shell = "zsh"
    package_list = ["neovim", "anydesk", "python3.10"]


def main(export_dir=DfConfigs.export_dir, def_editor=DfConfigs.default_editor, def_shell=DfConfigs.default_shell,
        ):

    # print("Starting the default process and configurations...")
    # sys(f"mkdir {export_dir}")
    
    # Header
    print("""
 _   _ _____ _     _     ___    _____ _   _ _____ ____  _____ _  
| | | | ____| |   | |   / _ \  |_   _| | | | ____|  _ \| ____| | 
| |_| |  _| | |   | |  | | | |   | | | |_| |  _| | |_) |  _| | | 
|  _  | |___| |___| |__| |_| |   | | |  _  | |___|  _ <| |___|_| 
|_| |_|_____|_____|_____\___/    |_| |_| |_|_____|_| \_\_____(_) 
                                                                
""")

    define_configs = input(f"""
    The default directory to put exports in: {export_dir}
    The default editor for git config: {def_editor}
    The default shell that you use: {def_shell}
    
    Do you need to change them Y/n?
    """)
    if define_configs == "n" or "N":
        export_dir = input("What is the desired directory to put exports? ")
        def_editor = input("WHat is the desired editor? ")
        def_shell = input("What is the desired shell? ")
    else:
        pass

    print(f"This is the package list that is going to be used and installed based on the Operating System: ",
          f"{DfConfigs.package_list}")
    package_list = input("Do you need to change them y/n? ")
    if package_list == "y" or "Y" or "":
        pkglist = []
        
        #TODO: read packages from a file!
        # get_pkg = input
