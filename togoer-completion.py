#!/usr/bin/python
import sys
from togoer import ToGoer

def main():
    goer = ToGoer()

    def completion_hook(cmd, curr_word, prev_word):
        if not goer.exists_toscriptdir():
            print('\nNo directory \'{0}\'\n'.format(goer.toscriptdir))
            return []
        elif not goer.has_scripts_toscriptdir():
            print('\nNo scripts found in \'{0}\'\n'.format(goer.toscriptdir))
            return []
        elif prev_word == 'to' or prev_word == '--test':
            potential_matches = goer.toscripts_basenames
        else:
            potential_matches = []
        matches = [k for k in potential_matches if k.startswith(curr_word)]
        return matches

    results = completion_hook(*sys.argv[1:])
    if len(results):
          print('\n'.join(results))

if __name__ == "__main__":
    main()