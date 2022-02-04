#!/usr/bin/env python3

import os
import sys

cmd = os.getcwd()
if len(sys.argv)>=2:
    cmd = sys.argv[1]
bash_command = ["cd "+cmd, "git status 2>&1"]
result_os = os.popen(' && '.join(bash_command)).read()
for result in result_os.split('\n'):
    if result.find('fatal') != -1:
        print(cmd+" git не найден")
    if result.find('изменен') != -1:
        prepare_result = result.replace('\изменен:   ', '')
        print(prepare_result)