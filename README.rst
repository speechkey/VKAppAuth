VKAppAuth
=====

Python package for authorize a VK application and get access_token for `vk api <http://vk.com/developers.php>`_.
Based on `dzhloev <http://habrahabr.ru/post/143972/>`_ 

Installation
------------

You can install from PyPI::

    $ pip install VKAppAuth==0.0.1


Example Of Usage
----------------

Add a `standalone VK application <http://vk.com/editapp?act=create>`_. Also keep in mind `VK development guide <https://vk.com/developers.php?id=-1_37230422&s=1>`_.

Now you can use VKAppAuth::

    >>> from VKAppAuth import VKAppAuth
    >>> login = 'email@example.com'
    >>> pwd = 'password'
    >>> app_id = 123456789
    >>> scopes = ['wall', 'friends']
    >>> scopes = 'wall'
    >>> vk_app_auth = VKAppAuth()
    >>> token = vk_app_auth.auth(login, pwd, app_id, scopes)
    >>> access_token = token.access_token
    >>> user_id = token.user_id
    >>> expires_in = token.expires_in

or a vkappauth script.

After receiving access_token you can be using `vkontakte package <https://crate.io/packages/vkontakte/>`_
