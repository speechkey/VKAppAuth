VKAppAuth
=========

There is a wondeful `vk.com (aka vkontakte.ru) API wrapper <https://github.com/shazow/urllib3/blob/master/test/benchmark.py>`_. But
if you would like to use it, you neet that your vk.com user authorize your
application and gives it all required rights, bevor you obtain an access
token and can make this wonderfull vk.com API wrapper usefull. VKAppAuth
module gives you functionality to very easy get this access token.

Install
=======

Checkout this repository or download an archive and run::

  python setup.py install

Install with pip::

  pip install vkappauth

Usage
=====

>>> from vkappauth import VKAppAuth
>>> vkaa = VKAppAuth()
>>> email = 'example@example.com'
>>> password = 'password'
>>> app_id = 123456
>>> scope = 'audio'
>>> scope = ['audio', 'offline']
>>> access_data = vkaa.auth(email, password, app_id, scope)
>>> print access_data
{'access_token': '41c5105ae83edc2a07896d62ed11f0b31f79f70ec1e657da65d32e497557665a33ab063b97d456530fe65', 'expires_in': '86400', 'user_id': '104184112'}

License
=======

The MIT License (MIT)
Copyright (c) 2012 Artem Grebenkin

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Source
======

Based on post `dzhloev <https://github.com/shazow/urllib3/blob/master/test/benchmark.py>`_.