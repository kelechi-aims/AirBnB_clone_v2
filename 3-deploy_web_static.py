#!/usr/bin/python3
"""
Fabric script to create and distribute an archive to web servers
"""
from fabric.api import local run, put, env
from datetime import datetime
import os

env.hosts = ['54.234.57.34', '54.89.143.165']


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    try:
        if not os.path.exists("versions"):
            local("mkdir -p versions")
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_{}.tgz".format(current_time)
        local("tar -cvzf versions/{} web_static".format(archive_name))
        return "versions/{}".format(archive_name)
    except Exception:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')
        archive_filename = os.path.basename(archive_path)
        archive_folder = '/data/web_static/releases/' + \
            archive_filename.split('.')[0]
        run('mkdir -p {}'.format(archive_folder))
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, archive_folder))
        run('rm /tmp/{}'.format(archive_filename))
        run('mv {}/web_static/* {}'.format(archive_folder, archive_folder))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(archive_folder))
        print("New version deployed!")
        return True
    except Exception:
        return False


def deploy():
    """Deploy function to create and distribute the archive"""
    archive_path = do_pack()
    if archive_path:
        return do_deploy(archive_path)
    return False
