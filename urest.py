# -*- coding: UTF-8 -*-

""" μREST is a small and simple module to send HTTP requests. """

import urllib2
import urllib


class uREST:

    """ Main μREST class. """

    def __getattr__(self, method):
        def rest_handler(*args, **kwargs):
            # only following request methods allowed
            if method in ['post', 'get', 'put', 'delete']:
                # compiling request
                request = urllib2.Request(args[0])
                # adding data to POST request
                if 'data' in kwargs:
                    # no data can be passed to non POST request
                    if method != 'post':
                        raise Exception('Data only allowed for POST requests.')
                    request.add_data(urllib.urlencode(kwargs['data']))
                # adding headers to request
                if 'headers' in kwargs:
                    for header, value in kwargs['headers'].items():
                        request.add_header(header, value)
                # setting method (dirty hack! monkey patch! shame on me!)
                request.get_method = lambda: method.upper()
                # getting response
                response = urllib2.urlopen(request)
                # parsing response
                response = {
                    'url': response.url,
                    'headers': dict(response.headers.items()),
                    'status': response.getcode(),
                    'body': response.read()
                }
                # returning response
                return response
            raise Exception('Unsupported request type.')
        return rest_handler