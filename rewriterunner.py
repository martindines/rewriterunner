#!/usr/bin/python

import sys, os

def error_message(message):
    print '[X] ' + message

def info():
    print 'usage: python rewriterunner.py <test_url>'

def main(argv):
    if not argv:
        info()
        sys.exit(1)

    if argv[1:]:
        info()
        sys.exit(1)

    if argv[0]:
        url = argv[0]

        htaccess = os.path.isfile('.htaccess')
        if htaccess:
            print 'We have .htaccess'
        else:
            error_message('.htaccess not found in current directory')
            sys.exit(1)

if __name__ == '__main__':
    print '# RewriteRunner'
    # Pass everything after the 1st argument to main()
    main(sys.argv[1:])