#!/usr/bin/env python3
import sys, os
from cmd import Cmd
from colorama import Fore, Back, Style
import datetime

import types
import functionallity as funct

from expr import *


asciiflex="""
 _____ _____      __ _                           _____ 
/  ___|_   _|    / _| |                         |  _  |
\ `--.  | | ___ | |_| |___      ____ _ _ __ ___ | |/' |
 `--. \ | |/ _ \|  _| __\ \ /\ / / _` | '__/ _ \|  /| |
/\__/ / | | (_) | | | |_ \ V  V / (_| | | |  __/\ |_/ /
\____/  \_/\___/|_|  \__| \_/\_/ \__,_|_|  \___| \___/ 
Willkommen bei SToftware0 by bschwering & ftuente
Besuche doch mal die Website benedikt-schwering.de/SToftware0
"""


class ST0Prompt(Cmd):
    prompt = "ST0: "

    def default(self, inp):#binomial
        pass

    def completedefault(self, text, line, begidx, endidx):
        return list()

    def completenames(self, text, *ignored):
        dotext = 'do_'+text
        docmds = [a[3:] for a in self.get_names() if a.startswith(dotext)]
        funcHooks=[getattr(funct, module).hook() for module in funct.__all__]
        #print(funcHooks)
        funcHooks = [item for sublist in funcHooks for item in sublist]
        #print(funcHooks)
        funcHooks=list(filter(None,funcHooks))
        return docmds+funcHooks
        
    def do_exit(self, inp):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S.%f")
        logmsg("exited: "+timestamp)
        return True

    def do_test(self,inp):
        print(funct.__all__)
        for module in funct.__all__:
            print(getattr(funct, module).hook())
        #print(dir(functions))
        #print([getattr(functions, a) for a in dir(functions) if isinstance(getattr(functions, a), types.ModuleType)])

    do_EOF = do_exit

def logmsg(msg):
    print(Fore.CYAN+msg+Style.RESET_ALL)

def warnmsg(msg):
    print(Fore.YELLOW+msg+Style.RESET_ALL)

if __name__ == '__main__':
    ST0Prompt().cmdloop(intro=asciiflex)