#!/usr/bin/env python3
import datetime
import os
import sys
import types
from cmd import Cmd

import regex
from colorama import Back, Fore, Style

import functionallity as funct
from functionallity import * # loads everything from __all__
from expr import isTerm, clean


asciiflex = """
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

    def default(self, inp):
        inp = clean(inp)
        inp = inp.strip()
        inp = regex.split(r"\s+", inp, flags=regex.UNICODE)
        modu = "simple"
        if len(inp) == 0:
            pass
        elif len(inp) == 1:
            if isTerm(inp[0]):
                funct.simple.getComponents(inp[0], list())
        else:
            for module in funct.__allcli__:
                if inp[0] in getattr(funct, module).hook():
                    modu = module
                    break
            if getattr(funct, modu).needsterm():
                term = None  # find term
                termi = None
                for i in range(1, len(inp)):
                    if isTerm(inp[i]):
                        if not term:
                            term = inp[i]
                            termi = i
                        # maybe first parseble argument is term always
                        elif "x" in inp[i] and "x" not in term:
                            term = inp[i]
                            termi = i
                if not term:
                    warnmsg("No Term found")
                else:
                    parts = list()
                    for i in range(1, len(inp)):
                        if i != termi:
                            parts.append(inp[i])
                    getattr(funct, modu).getComponents(term, parts)

            else:
                parts = inp[1::]
                getattr(funct, modu).getComponents(parts)

        inp = " ".join(inp)
        funct.eastereggs.getComponents(inp)

    def completedefault(self, text, line, begidx, endidx):
        return list()

    def completenames(self, text, *ignored):
        dotext = 'do_'+text
        docmds = [a[3:] for a in self.get_names() if a.startswith(dotext)]
        funcHooks = [getattr(funct, module).hook() for module in funct.__allcli__]
        funcHooks = [item for sublist in funcHooks for item in sublist]
        funcHooks = list(filter(None, funcHooks))
        funcHooks = list(filter(lambda x: x.startswith(text), funcHooks))
        return docmds+funcHooks

    def do_exit(self, inp):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S.%f")
        logmsg("exited: "+timestamp)
        return True

    def do_test(self, inp):
        print(funct.__allcli__)
        print(dir(funct))
        for module in funct.__allcli__:
            print(getattr(funct, module).hook())

    do_EOF = do_exit


def logmsg(msg):
    print(Fore.CYAN+msg+Style.RESET_ALL)


def warnmsg(msg):
    print(Fore.YELLOW+msg+Style.RESET_ALL)


if __name__ == '__main__':
    ST0Prompt().cmdloop(intro=asciiflex)
