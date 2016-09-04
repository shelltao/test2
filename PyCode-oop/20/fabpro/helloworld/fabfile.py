# coding:utf-8

from fabric.api import run, cd, local


def host_type():
    """ 运行uname在远程"""
    run('luname -s')


def remote_run(command, command2):
    """
    @command,@command2
    """
    run(command)
    run(command2)


def ls_tmp():
    run('cd /var/www')
    run('pwd')
    run('ls')

    with cd('/tmp'):
        run('pwd')
        run('ls')

def local_test():
    local('ls -al')
