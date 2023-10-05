#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
"""
from fabric.operations import local
import os
from datetime import datetime


def do_pack():
