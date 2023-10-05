#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
"""
import os
from datetime import datetime
from fabric.api import local, runs_once


@runs_once
def do_pack():
    """Archives the static files."""
    output_dir = "versions"
    os.makedirs(output_dir, exist_ok=True)
    d_time = datetime.now()
    output = f"{output_dir}/web_static_{d_time:%Y%m%d%H%M%S}.tgz"

    try:
        print(f"Packing web_static to {output}")
        local(f"tar -cvzf {output} web_static")
        size = os.stat(output).st_size
        print(f"web_static packed: {output} -> {size} Bytes")
    except Exception as e:
        output = None

    return output
