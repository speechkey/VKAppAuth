import os
from setuptools import setup, find_packages


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name='VKAppAuth',
    version='0.0.1',
    license='MIT',
    description='Python package for authorize a standalone VK/Vkontakte application and get'
                'access_token for vkontakte api.',
    keywords='vkontakte vk api access_token oauth oauth2',
    long_description=open('README.rst').read() + "\n\n\n" + open('CHANGES.rst').read(),
    url='https://github.com/speechkey/vkappauth',
    download_url='https://github.com/speechkey/VKAppAuth/tarball/0.0.1',
    author='Artem Grebenkin',
    author_email='artem.grebenkin@gmail.com',
    include_package_data=True,
    packages=find_packages(),
    scripts=['bin/vkappauth.py'],
    install_requires=[
        'argparse>=1.2.1'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
