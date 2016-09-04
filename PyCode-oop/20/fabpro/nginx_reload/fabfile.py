# coding:utf-8

from fabric.api import (
    run, env, roles, cd,
    local, put, files
)

env.roledefs = {
    'webserver': [
        'huyang@localhost',
        'huyang@localhost'
    ],
    'dbserver': [
        'the5fire@localhost'
    ]
}

PROJECT_NAME = 'nginx_conf'
NGINX_BIN = '/tmp/etc/nginx/sbin/nginx'
NGINX_CONF = '/tmp/etc/nginx/conf/nginx.conf'
NGINX_CONF_PATH = '/tmp/etc/nginx/conf'


@roles('webserver')
def deploy():
    tar_file = pre_deploy(PROJECT_NAME)
    replace_conf(tar_file, NGINX_CONF_PATH)
    nginx_install(NGINX_BIN, NGINX_CONF)
    nginx_reload(NGINX_BIN, NGINX_CONF)


def nginx_install():
    # if 'not found' not in run('which nginx'):
    # run('yum install nginx -y')
    # or run('wget ...')
    # else:
    return True


def pre_deploy(project_name):
    """
    对本地项目进行打包
    """
    tar_name = project_name + '.tar.gz'
    local('tar -cvf %s %s' % (tar_name, project_name))
    put(tar_name, '/tmp')
    return tar_name


def replace_conf(tar_file, dest_path):
    with cd('/tmp'):
        run('tar -xvf %s' % tar_file)
        if files.exists(dest_path):
            run('mv -f %s %s' % (PROJECT_NAME, dest_path))


def nginx_reload(nginx_bin, nginx_conf):
    result = run('%s -c %s -s test' % (nginx_bin, nginx_conf))
    if 'success' in result:
        run('%s -c %s -s reload' % (nginx_bin, nginx_conf))
    else:
        print result
