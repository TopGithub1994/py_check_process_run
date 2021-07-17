import psutil

for top in psutil.process_iter(attrs=['pid', 'name']):
    if top.info['name'] == "chrome.exe":
        print("yes", (top.info['name']))
    # else:
        # print("no")
print("==================")