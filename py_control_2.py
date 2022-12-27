"""
Updated: Py_Control 2.0.0
Self-control is not easy. Let Py-Control help you and achieve your goal!
Run it with: sudo python py_control.py

+ updated description for more motivation + smiles
+ hand-curated list only for more productive, future you
"""

import random as random

# recommended_sites

sites_to_block = ['ulta.com', 'twitter.com', 'sephora.com', 'discord.com',
'bilibili.com', 'mercari.com', 'zhihu.com', 'facebook.com', 'etsy.com', 'instagram.com',
'ebay.com', 'tumblr.com', 'youtube.com', 'tiktok.com', 'poshmark.com',
'sydneygraceco.com', 'amazon.com', 'baidu.com', 'reddit.com', 'xvideos.com', 'temptalia.com',
'chewy.com', 'pornhub.com', 'pinterest.com']

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
    random_num = random.random()
    if random_num < 0.5:
        print("You'll never be alone, Py-Control'll be with you from dusk till dusk \U0001F609 \n")
    else:
        print("Darling I'd block anything for you \U0001F970 \n")

    print("Put webisites to block here, e.g. 'abc.com'\n")
    print("type 'no' to stop\n")
    x = ""
    arr = []
    while x != "no":
        x = input()
        if x != "no":
            arr.append(x)

    sites_to_block.extend(arr)
    print("")
    print("Here's your block list! Au revoir \U0001F920")
    print(sites_to_block)
    print("")
    block_sites()
    print("")
    print("All done! You took the courage to become your better self \U0001F973")
