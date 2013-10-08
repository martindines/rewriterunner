#!/usr/bin/python

import sys, os

def success_message(message):
    # http://en.wikipedia.org/wiki/Tick_(check_mark)
    tick = unichr(2714)
    print '[' + tick + '] ' + message

def error_message(message):
    # http://en.wikipedia.org/wiki/X_mark
    cross = unichr(2718)
    print '[' + cross + '] ' + message

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

        htaccessFilename = '.htaccess'
        if os.path.isfile(htaccessFilename):
            success_message(htaccessFilename + ' found')
        else:
            error_message(htaccessFilename + ' not found in current directory')
            sys.exit(1)

        htaccessFileHandler = open(htaccessFilename)
        for line in htaccessFileHandler:
            exit()
            #print line

if __name__ == '__main__':
    print '# RewriteRunner'
    # Pass everything after the 1st argument to main()
    main(sys.argv[1:])