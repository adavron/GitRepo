#!/usr/bin/env python

from fabric.api import *

env.gateway = 'username@IPofgatewayHost'
env.hosts = ['IP can be listed here']

@task
def openssl():
    sudo('openssl dhparam 1024 >> /etc/pki/tls/certs/localhost.crt')

@task
def httpdi_restart():
    sudo('/etc/init.d/httpd restart')

@task
def hostname():
    run('hostname')


"""
@task
def hos():
    with settings(hide('stderr', 'stdout'), warn_only=True):
        run('psfd;sleep 5; pwd')
"""


@task
def cmdrun(arg):
    """Usage: fab -H server1, server2 cmdrun:"uptime" """
    run(arg)


@task
def sudorun(arg):
    """Usage: fab -H server1, server2 sudorun:"df -hT" """
    sudo(arg)

@task
def download(arg):
    """Usage: fab -H server1, server2 download:"/path/to/file" """
    get(remote_path=arg, local_path="/tmp/", use_sudo=True)

@task
def upload(arg1, arg2):
    """Usage: fab -H server1, server2 upload:"/localfile","/remote/path/" """
    put(local_path=arg1, remote_path=arg2, use_sudo=True)

