#!/usr/bin/python

import sys, os, re

def success_message(message):
    # http://en.wikipedia.org/wiki/Tick_(check_mark)
    tick = u"\u2714"
    print '[%s] %s' % (tick, message)

def error_message(message):
    # http://en.wikipedia.org/wiki/X_mark
    cross = u"\u2718"
    print '[%s] %s' % (cross, message)

def info():
    print 'usage: python rewriterunner.py <test_url>'

class htaccess:
    filename = '.htaccess'
    contents = []

    def __init__(self, filename=None):
        if filename:
            self.filename = filename

        if os.path.isfile(self.filename):
            success_message(self.filename + ' found')
        else:
            error_message(self.filename + ' not found in current directory')
            sys.exit(1)

        self.parseData()

    def parseData(self):
        # Hot damn. So much logic in one line
        contents = [line.strip() for line in open(self.filename)]

        # Remove empty lines and comments
        contents = filter(None, contents)

        # Errrrr as I understand the function in filter should eval to False to remove a line.. which makes the above
        # None filter incorrect as None would return true and filter out not None lines? @todo Understand this
        self.contents = filter(lambda value: not value.startswith('#'), contents)

        success_message('Extracted %d lines of data' % len(self.contents))

    def isRewriteEngineOn(self):
        regex = re.compile('RewriteEndgine\s*[o|O]n')
        return [match.group(0) for line in self.contents for match in [regex.search(line)] if match]


def main(argv):
    if not argv:
        info()
        sys.exit(1)

    if argv[1:]:
        info()
        sys.exit(1)

    if argv[0]:
        url = argv[0]

        htaccessObj = htaccess()
        if htaccessObj.isRewriteEngineOn():
            success_message('RewriteEngine On')
        else:
            error_message('RewriteEngine Off (or not found)')


if __name__ == '__main__':
    print '# RewriteRunner'
    # Pass everything after the 1st argument to main()
    main(sys.argv[1:])