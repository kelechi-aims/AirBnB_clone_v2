#!/usr/bin/python3
"""
Fabric script to clean up outdated archives
"""
from fabric.api import env, run, local
from os.path import exists


env.hosts = ['54.234.57.34', '54.89.143.165']


def do_clean(number=0):
    """Deletes out-of-date archives"""
    number = int(number)
    if number < 1:
        number = 1
    else:
        number += 1

    local_archives = local("ls -1t versions", capture=True).splitlines()
    server_archives = run("ls -1t /data/web_static/releases").splitlines()

    for archive in local_archives[number:]:
        local("rm versions/{}".format(archive))

    for archive in server_archives[number:]:
        run("rm -rf /data/web_static/releases/{}".format(archive))
