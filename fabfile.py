# -*- coding: utf-8 -*-

import os
from fabric.api import *
from fabric.operations import *
from fabric.colors import red, green, yellow

env.hosts = ['root@192.168.0.31:22', 'root@192.168.0.32:22',
             'root@192.168.0.33:22', 'root@192.168.0.34:22']
env.passwords = {
    'root@192.168.0.31:22': '12345678',
    'root@192.168.0.32:22': '12345678',
    'root@192.168.0.33:22': '12345678',
    'root@192.168.0.34:22': '12345678'}

local_file = raw_input("Enter the file's name you wanna update:\n")
remote_path = raw_input("Enter the path you wanna update:\n")

# test for connection
def host_type():
    run('uname -s')

# test for local path's filename list
def get_file_name_list():
    local_path = os.getcwd()
    file_name_list = os.listdir(local_path)
    file_name_list = filter(lambda x:x != 'fabfile.py' and x != 'fabfile.pyc', file_name_list)
    return file_name_list

def update_file():
    global remote_path
    global local_file

    file_name_list = local_file.split()
    local_path = os.getcwd()
    # file_name_list = get_file_name_list()
    # remote_path = '/test'
    print (yellow("The file you wanna update:%s" % file_name_list))
    print (yellow("The path you wanna update:%s" % remote_path))
    # remote_path = raw_input('Please enter the remote path you want update:\n')
    # /test
    with cd("%s" % remote_path):
        remote_file_list = run('ls')
    remote_old_path = '/'.join([remote_path, 'backup'])

    if 'backup' not in remote_file_list:
        print (green("Check Remote Backup Folder: No Backup Folder!"))
        print (green("Create A Backup Folder Named 'backup'."))
        with cd(remote_path):
            sudo("mkdir backup")
    else:
        print (green("Check Remote Backup Folder:Backup Folder Exists!"))

    old_file_list = run("ls %s" % remote_old_path)

    for f in file_name_list:
        if f in remote_file_list:
            if f in old_file_list:
                print (green("%s Have An Old Version In Backup Folder." % f))
                print (green("Delete The Old Version %s In Backup Folder." % f))
                old_file_path = '/'.join([remote_old_path, f])
                sudo("rm %s" % old_file_path)
            print (green("Backup The Last Version of %s To Backup Folder." % f))
            remote_file = '/'.join([remote_path, f])
            run("mv -v %s %s" % (remote_file, remote_old_path))
        file_path = '/'.join([local_path, f])
        print (red("Update %s to %s." % (f, remote_path)))
        put("%s" % file_path, "%s" % remote_path)