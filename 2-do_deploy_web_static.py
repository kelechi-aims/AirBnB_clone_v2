#!/usr/bin/python3
"""
Fabric script to distribute an archive to your web servers
"""
from fabric.api import run, put, env
from os.path import exists


env.hosts = ['54.234.57.34', '54.89.143.165']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers
    """
    if not exists(archive_path):
        return False

    try:
        filename = archive_path.split('/')[-1]
        folder_name = '/data/web_static/releases/{}'.format(
            filename.strip('.tgz')
        )

        # Upload the archive to /tmp/ directory on the server
        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(folder_name))
        run('tar -xzf /tmp/{} -C {}'.format(filename, folder_name))

        # Remove the archive from the server
        run('rm /tmp/{}'.format(filename))

        # Move files to correct location
        run('mv {}/web_static/* {}'.format(folder_name, folder_name))

        # Remove unnecessary directory
        run('rm -rf {}/web_static'.format(folder_name))

        # Remove the old symbolic link
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link
        run('ln -s {} /data/web_static/current'.format(folder_name))

        print("New version deployed!")
        return True
    except Exception:
        return False
