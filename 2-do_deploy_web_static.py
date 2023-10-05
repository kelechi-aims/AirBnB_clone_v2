#!/usr/bin/python3
"""
Fabric script that use do_deploy to distributes an archive to your web servers
"""

from datetime import datetime
from fabric.api import *
import os

env.hosts = ["3.90.70.201", "54.146.67.238"]
env.user = "ubuntu"


def do_pack():
    """
    Create a compressed archive of the web_static folder.
    """
    local("mkdir -p versions")
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(current_time)
    result = local("tar -cvzf {} web_static".format(archive_path))

    if result.succeeded:
        return archive_path
    else:
        return None


def do_deploy(archive_path):
    """
    Deploy the compressed archive to the web servers.
    """
    if os.path.exists(archive_path):
        archive_filename = os.path.basename(archive_path)
        target_dir = "/data/web_static/releases/{}/".format(
            archive_filename.split('.')[0])
        tmp_archive_path = "/tmp/{}".format(archive_filename)

        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(target_dir))
        run("sudo tar -xzf {} -C {}".format(tmp_archive_path, target_dir))
        run("sudo rm {}".format(tmp_archive_path))
        run("sudo mv {}web_static/* {}".format(target_dir, target_dir))
        run("sudo rm -rf {}web_static".format(target_dir))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(target_dir))

        print("New version deployed!")
        return True

    return False
