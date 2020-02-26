#!/usr/bin/python

from __future__ import print_function
import os
import glob
import sys

class ToGoer(object):
    """docstring for ToGoer"""
    def __init__(self):
        super(ToGoer, self).__init__()
        self.toscriptdir = self.get_toscriptdir()
        self.toscripts = self.get_toscripts()
        self.toscripts_basenames = [ os.path.basename(s).replace('.sh', '') for s in self.toscripts ]
        self.test_mode = False

    def get_toscriptdir(self):
        return os.environ.get(
            'TOSCRIPTDIR',
            os.path.join(os.environ['HOME'], 'toscripts')
            )

    def get_toscripts(self):
        if not self.exists_toscriptdir():
            return []
        return glob.glob(
            os.path.join(self.toscriptdir, '*.sh')
            )

    def exists_toscriptdir(self):
        return os.path.isdir(self.toscriptdir)

    def has_scripts_toscriptdir(self):
        return len(self.toscripts) > 0

    def get_script(self, basename):
        if not self.exists_toscriptdir():
            print('No directory \'{0}\''.format(self.toscriptdir))
            sys.exit(1)
        elif not basename in self.toscripts_basenames:
            print('No script corresponds with \'{0}\''.format(basename))
            print('Registered scripts: {0}'.format(
                ', '.join(self.toscripts_basenames)
                ))
            sys.exit(1)
        else:
            script = self.toscripts[self.toscripts_basenames.index(basename)]
            script = os.path.abspath(script)
            return script

    def print_contents(self, script):
        with open(script, 'r') as fp:
            print(fp.read())
        sys.exit(0)



if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('script_basename', type=str, help='basename of the script to execute' )
    parser.add_argument('--test', action='store_true', help='does not execute the script, prints info instead')
    args = parser.parse_args()

    goer = ToGoer()
    script = goer.get_script(args.script_basename)

    # Return the path to the script
    print(script)

    if args.test:
        sys.exit(1)
    else:
        sys.exit(0)
