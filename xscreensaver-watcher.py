#! /usr/bin/python
#
# Module: xscreensaver-watcher.py
#
# Reads stdin, and executes commands to when screensaver lock/unlock are detected.
#
# Usage:
#   xscreensaver-command -watch | python xscreensaver-watcher.py
#
# Author: Gabriel Knoy (gknoy)
#

import os
import six
import sys
import subprocess


# Note that keys are just substrings. No regex support yet.
COMMANDS_D = {
    # TODO: Allow options for using stop vs pause
    'BLANK': 'clementine --pause',
    'LOCK': 'clementine --pause',

    'UNBLANK': 'clementine --play',
}


class XScreensaverWatcher(object):

    def __init__(self, stream):
        '''
        :param stream: An input stream (e.g. sys.stdin) from which to look for xscreensaver events
        '''
        self.stream = stream

    def run_if_line_matches(self, line, status, cmd, verbose=False):
        '''
        Run cmd if line starts with status
        '''
        if line.startswith(status):
            if verbose:
                print("    exec: `{}`".format(status, cmd))
            subprocess.call(cmd, shell=True)

    def watch(self, commands_d, verbose=False):
        '''
        Watch for commands in stdin, execute things when we see them.

            UNBLANK Thu Jul 10 13:06:53 2014  <-- 'lock' invoked
            LOCK Thu Jul 10 13:16:45 2014
            UNBLANK Thu Jul 10 13:16:51 2014  <-- unlocked

        :param commands_d: A dict of line prefixes and resulting commands to run when we match them
        :param verbose: Print info when we respond to things
        '''

        # Use this construct rather than 'for line in self.stream'
        # see http://stackoverflow.com/questions/3670323/setting-smaller-buffer-size-for-sys-stdin
        while True:
            line = self.stream.readline()
            if not line: break  # EOF

            if verbose:
                print("IN: {}".format(line.strip()))
            for status, cmd in six.iteritems(commands_d):
                self.run_if_line_matches(line, status, cmd, verbose=verbose)


if __name__ == "__main__":

    new_stdin = os.fdopen(sys.stdin.fileno(), 'r', 0)  # unbuffered stdin

    XScreensaverWatcher(new_stdin).watch(COMMANDS_D, verbose=True)
