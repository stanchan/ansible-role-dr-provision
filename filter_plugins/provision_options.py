#!/usr/bin/python

from six import iteritems

def provision_options(options):
    option_string = ""
    for (key, value) in iteritems(options):
        if isinstance(value, bool) and value:
            option_string += " --{0}".format(key)
        elif value:
            option_string += " --{0}={1}".format(key, value)
            
    return option_string

class FilterModule(object):
    def filters(self):
        return {
            'provision_options': provision_options
        }
