from os import system as sys


# Configure git editor
def git_config(editor, shell):
    sys(f"git config --global core.editor '{editor}'")
    sys("""echo 'alias git-log = "git log --graph --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) "
        "%C(white)%an%C(reset)%C(bold yellow)%d%C(reset) %C(dim white)- %s%C(reset)' --all"' > ~/.bashrc """
        )

# Configure the pip usage in Iran
# The shell could be one the following:
# 1. bashrc
# 2. zshrc
def pip_config(shell):
    piplist = '''
alias pip_china1="pip install --trusted-host https://pypi.tuna.tsinghua.edu.cn -i https://pypi.tuna.tsinghua.edu.cn/simple/ "
alias pip_china2="pip install --trusted-host https://mirrors.aliyun.com -i https://mirrors.aliyun.com/pypi/simple/ "
alias pip_china3="pip install --trusted-host https://pypi.mirrors.ustc.edu.cn -i https://pypi.mirrors.ustc.edu.cn/simple/ "
alias pip_china4="pip install --trusted-host https://repo.huaweicloud.com -i https://repo.huaweicloud.com/repository/pypi/simple/ "
alias pip_china5="pip install --trusted-host http://pypi.douban.com -i http://pypi.douban.com/simple/ "
alias pip_china6="pip install --trusted-host http://pypi.sdutlinux.org -i http://pypi.sdutlinux.org/ "
alias pip_china7="pip install --trusted-host http://pypi.hustunique.com -i http://pypi.hustunique.com/ "
'''
    sys(f"echo {piplist} >> {shell}")

