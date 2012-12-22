#!/usr/bin/env python
# -- coding: utf-8 --
# Commandline tool for VKAppAuth
import getpass
import argparse
from vk_app_auth import VKAppAuth


def main():
    script_args = args()

    password = getpass.getpass("VK Users Password:")
    vk_app_auth = VKAppAuth()
    print vk_app_auth.auth(script_args.VK_EMAIL, password, script_args.VK_APP_ID, script_args.VK_SCOPE)


def args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--vk-email', dest='VK_EMAIL', help='VK users email', required=True)
    parser.add_argument('-a', '--vk-app-id', dest='VK_APP_ID', default=2951857, type=int, help='VK application ID')
    parser.add_argument('-s', '--vk-app-scope', dest='VK_SCOPE', default='audio,offline,wall', help='VK application scope')

    args = parser.parse_args()
    return args

if __name__ == '__main__':
    main()
