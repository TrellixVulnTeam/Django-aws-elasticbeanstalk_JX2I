#!C:\users\user\desktop\python-server\server_code\eb-virt\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'numpy==1.15.0','console_scripts','conv-template'
__requires__ = 'numpy==1.15.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('numpy==1.15.0', 'console_scripts', 'conv-template')()
    )