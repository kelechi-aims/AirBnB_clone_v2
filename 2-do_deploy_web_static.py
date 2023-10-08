#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy
"""
from fabric.api import run, put, env
import os


env.hosts = ['54.234.57.34', '54.89.143.165']


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory on the server
        put(archive_path, '/tmp/')
        # Extract archive to the folder /data/web_static/releases/
        archive_filename = os.path.basename(archive_path)
        archive_folder = '/data/web_static/releases/' + \
            archive_filename.split('.')[0]
        run('mkdir -p {}'.format(archive_folder))
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, archive_folder))

        # Delete the uploaded archive from the web server
        run('rm /tmp/{}'.format(archive_filename))

        # Move the extracted content to the correct location
        run('mv {}/web_static/* {}'.format(archive_folder, archive_folder))

        # Remove the symbolic link /data/web_static/current
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link
        run('ln -s {} /data/web_static/current'.format(archive_folder))

        print("New version deployed!")
        return True

    except Exception:
        return False
