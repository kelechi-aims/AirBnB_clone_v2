#!/usr/bin/python3
"""
Fabric script that delete out-of-date archives using do_clean
"""
import os
from fabric.api import *

env.hosts = ["3.90.70.201", "54.146.67.238"]


def do_clean(number=0):
    '''
    This delete out-of-date archives.
    '''
    number = max(1, int(number))  # Ensure number is at least 1

    # Local cleanup
    with lcd("versions"):
        local_archives = sorted(os.listdir("."))
        for archive in local_archives[:-number]:
            local("rm -f {}".format(archive))

    # Remote cleanup
    with cd("/data/web_static/releases"):
        remote_archives = run("ls -tr | grep 'web_static_'", warn_only=True)
        remote_archives = remote_archives.split()
        for archive in remote_archives[:-number]:
            run("rm -rf {}".format(archive))
