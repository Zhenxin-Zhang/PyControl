"""
Self-control is not easy. Let Py-Control help you and achieve your goal!
Run it with: sudo python py_control.py
"""

sites_to_block = ['zhihu.com', 'bilibili.com', 'sephora.com', 'ulta.com',
                  '1point3acres.com', 'tieba.baidu.com', 'lemmelive.com',
                  'patmcgrath.com', 'petsmart.com', 'discord.com',
                  'wechat.com', 'wx.qq.com', 'wx2.qq.com','etsy.com', 'youtube.com/results?search_query=qin+ai+de+gong+zhu+bing']

hosts_path = "/etc/hosts"
redirect = "127.0.0.1"


def block_sites():
    with open(hosts_path, 'r+') as hostsfile:
        hosts_content = hostsfile.read()
        for site in sites_to_block:
            if site not in hosts_content:
                hostsfile.write(redirect + " " + site + "\n")
                hostsfile.write(redirect + " " + "www." + site + "\n")

if __name__ == "__main__":
    print("Self-control is not easy. Py-Control can help!")
    print("")
    print("Block webisites here, e.g. 'abc.com'\n")
    print("type 'no' to stop\n")
    x = ""
    arr = []
    while x != "no":
        x = input()
        if x != "no":
            arr.append(x)

    sites_to_block.extend(arr)
    print("")
    print("Here's your block list! Never have to see those web again~")
    print(sites_to_block)
    print("")
    block_sites()
    print("")
    print("All Done! Cheer up :)")
