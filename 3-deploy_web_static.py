#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to the web servers
"""

from fabric.api import env, local, put, run, task
from datetime import datetime
from os.path import exists

env.hosts = ['3.90.70.201', '54.146.67.238']
env.user = 'ubuntu'


@task
def do_pack():
    '''
    This generates a tgz archive
    '''
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = f'versions/web_static_{date}.tgz'

        if not exists('versions'):
            local('mkdir -p versions')

        local(f'tar -cvzf {file_name} web_static')
        return file_name
    except Exception as e:
        return None


@task
def do_deploy(archive_path):
    '''
    This distributes an archive to the web servers
    '''
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        path = '/data/web_static/releases/'

        put(archive_path, '/tmp/')
        run(f'mkdir -p {path}{no_ext}')
        run(f'tar -xzf /tmp/{file_name} -C {path}{no_ext}')
        run(f'rm /tmp/{file_name}')
        run(f'mv {path}{no_ext}/web_static/* {path}{no_ext}/')
        run(f'rm -rf {path}{no_ext}/web_static')
        run('rm -rf /data/web_static/current')
        run(f'ln -s {path}{no_ext}/ /data/web_static/current')
        return True
    except Exception as e:
        return False


@task
def deploy():
    '''
    This creates and distributes an archive to the web servers
    '''
    archive_path = do_pack()
    if archive_path is None:
        return False

    return do_deploy(archive_path)
