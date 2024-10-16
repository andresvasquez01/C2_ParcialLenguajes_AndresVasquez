# Generated from Fourier.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,7,52,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,
        3,1,4,1,4,1,5,4,5,34,8,5,11,5,12,5,35,1,5,1,5,4,5,40,8,5,11,5,12,
        5,41,3,5,44,8,5,1,6,4,6,47,8,6,11,6,12,6,48,1,6,1,6,0,0,7,1,1,3,
        2,5,3,7,4,9,5,11,6,13,7,1,0,2,1,0,48,57,3,0,9,10,13,13,32,32,55,
        0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,
        1,0,0,0,0,13,1,0,0,0,1,15,1,0,0,0,3,24,1,0,0,0,5,26,1,0,0,0,7,28,
        1,0,0,0,9,30,1,0,0,0,11,33,1,0,0,0,13,46,1,0,0,0,15,16,5,102,0,0,
        16,17,5,111,0,0,17,18,5,117,0,0,18,19,5,114,0,0,19,20,5,105,0,0,
        20,21,5,101,0,0,21,22,5,114,0,0,22,23,5,40,0,0,23,2,1,0,0,0,24,25,
        5,44,0,0,25,4,1,0,0,0,26,27,5,41,0,0,27,6,1,0,0,0,28,29,5,91,0,0,
        29,8,1,0,0,0,30,31,5,93,0,0,31,10,1,0,0,0,32,34,7,0,0,0,33,32,1,
        0,0,0,34,35,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,43,1,0,0,0,37,
        39,5,46,0,0,38,40,7,0,0,0,39,38,1,0,0,0,40,41,1,0,0,0,41,39,1,0,
        0,0,41,42,1,0,0,0,42,44,1,0,0,0,43,37,1,0,0,0,43,44,1,0,0,0,44,12,
        1,0,0,0,45,47,7,1,0,0,46,45,1,0,0,0,47,48,1,0,0,0,48,46,1,0,0,0,
        48,49,1,0,0,0,49,50,1,0,0,0,50,51,6,6,0,0,51,14,1,0,0,0,5,0,35,41,
        43,48,1,6,0,0
    ]

class FourierLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    NUMBER = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'fourier('", "','", "')'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "NUMBER", "WS" ]

    grammarFileName = "Fourier.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


