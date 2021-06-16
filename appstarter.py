import eel
import pandas as pd
import numpy as np
import sys
from parsers.CLR1 import generateclr1
from parsers.LALR1 import generatelalr1
from parsers.LL0 import generatell0
from parsers.LL1 import generatell1
from parsers.LR0 import generatelr0
from parsers.LR1 import generatelr1
from parsers.SLR1 import generateslr1

eel.init('D:/HTML/codes/CDParsers4/web')

@eel.expose
def ll0parser(q,qq):
    return generatell0(q,qq)

@eel.expose
def ll1parser(q,qq):
    return generatell1(q,qq)

@eel.expose
def lr0parser(q,qq):
    return generatelr0(q,qq)

@eel.expose
def lr1parser(q,qq):
    return generatelr1(q,qq)

@eel.expose
def slr1parser(q,qq):
    return generateslr1(q,qq)

@eel.expose
def clr1parser(q,qq):
    return generateclr1(q,qq)

@eel.expose
def lalr1parser(q,qq):
    return generatelalr1(q,qq)


eel.start('html1.html')