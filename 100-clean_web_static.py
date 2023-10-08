#!/usr/bin/python3
"""
Fabric script to clean up outdated archives
"""
from fabric.api import *


env.hosts = ['54.234.57.34', '54.89.143.165']


def do_clean(number=0):
    """Deletes out-of-date archives"""
    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
