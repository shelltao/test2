# coding:utf-8

from fabric.api import (
    run, env, roles, hosts, cd,
    local, put
)


env.roledefs = {
    'name': 'the5fire@localhost',
    'webserver_1': 'huyang@localhost',
    'webserver': [
        'huyang@localhost',
        'huyang@localhost'
    ],
    'dbserver': [
        'the5fire@localhost',
        'the5fire@localhost'
    ],
    'nginx': [
        'the5fire@localhost',
        'the5fire@localhost'
    ]
}


#@roles('webserver')
def host_type():
    run('uname -s')


@hosts('huyang@localhost', 'huyang@localhost')
def remote_run(command):
    run(command)
