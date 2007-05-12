# -*- coding: <%= FILE_ENCODING %> -*-
<%= make_docstring(MODULE, '''\
This package just provides one function that resolves the view functions
from the modules in this package. This is a django like way to find callback
functions.''') %>

def get_view(name):
    module, callback = name.split('/', 1)
    m = __import__('<%= PACKAGE %>.views.%s' % module, None, None, [callback])
    return getattr(m, callback)