#!/usr/bin/env python
#coding:utf-8
# Author        : tuxpy
# Email         : q8886888@qq.com.com
# Last modified : 2015-11-05 13:53:48
# Filename      : auth.py
# Description   : 
from __future__ import print_function, unicode_literals
from wiz.api import api_request
from wiz import e

class AuthManager(object):
    def __new__(cls, *args, **kwargs):
        if hasattr(cls, '_instance'):
            return cls._instance

        _instance = object.__new__(cls, *args, **kwargs)
        AuthManager._instance = _instance

        return _instance

    @property
    def access_token(self):
        return {
                'token'         :       getattr(self, '_token', None),
        #        'user_guid'     :       getattr(self, '_user_guid', None),
                'kb_guid'       :       getattr(self, '_kb_guid', None),
                'cert_no'       :       getattr(self, '_CertNo', None),
                'user_id'       :       getattr(self, '_user_id', None),
                }

    def __init__(self, username = None, password = None):
        self.__username, self.__password = username, password

    def login(self, username = None, password = None):
        username = username or self.__username
        password = password or self.__password

        result, error = api_request('/api/login', method = 'POST',
                data = {'user_id': username, 'password': password,
                    'token': ''})

        if error:
            raise e.WizLoginFailed(error)

        self.__login_success_after(result)

    def __login_success_after(self, login_response):
        self._token = login_response['token']
        self._user_id = login_response['user']['user_id']
        self._user_guid = login_response['user']['user_guid']
        self._kb_guid = login_response['kb_guid']
        self._CertNo = login_response['cookie_str']

