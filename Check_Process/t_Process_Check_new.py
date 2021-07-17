# import psutil

# for top in psutil.process_iter(attrs=['pid', 'name']):
#     if top.info['name'] == "chrome.exe":
#         print("yes", (top.info['name']))
#     # else:
#         # print("no")
# print("==================")

# import psutil

# for process in psutil.process_iter():
#     cmdline = process.cmdline
#     if "top_test.py" in cmdline:
#         # do something
#         print("yes")

# import os
# import psutil

# def find_procs_by_name(name):
#     # "Return a list of processes matching 'name'."
#     assert name, name
#     ls = []
#     for p in psutil.process_iter():
#         name_, exe, cmdline = "", "", []
#         try:
#             name_ = p.name()
#             cmdline = p.cmdline()
#             exe = p.exe()
#         except (psutil.AccessDenied, psutil.ZombieProcess):
#             pass
#         except psutil.NoSuchProcess:
#             continue
#         if name == name_ or cmdline[0] == name or os.path.basename(exe) == name:
#             ls.append(p)
#     return ls
# find_procs_by_name("cmd.exe")

import psutil

PROCNAME = "cmd.exe"

for proc in psutil.process_iter():
    cmdline = proc.cmdline
    if proc.name() == PROCNAME:
        print(cmdline)