import sys

# S → exp $
# exp → term { addop term }
# term → factor { mulop factor }
# factor → (exp) | number
# number → digit { digit } [.number]
# digit → 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
# addop → + | -
# mulop → * | /

END = '$'
DEBUG = False


def dprint(str):
    if DEBUG:
        print(str)


class Expression:
    def __init__(self, line: str):
        self.linebuf = line
        self.linePos = 0
        self.curChar = self.linebuf[self.linePos]

    def error(self):
        print('ERROR!')
        sys.exit(1)

    def match(self, expectedChar):
        if self.curChar == expectedChar:
            self.linePos += 1
            self.curChar = self.linebuf[self.linePos]
        else:
            self.error()

    # S → exp $
    def start(self) -> int:
        res = self.exp()
        if self.curChar != END:
            self.error()
        print('result = {}'.format(res))
        return res

    # exp → term { addop term }
    # addop → + | -
    def exp(self) -> float:
        val = self.term()
        while self.curChar == '+' or self.curChar == '-':
            if self.curChar == '+':
                self.match('+')
                val += self.term()
                dprint('val = {}'.format(val))
            elif self.curChar == '-':
                self.match('-')
                val -= self.term()
                dprint('val = {}'.format(val))
            else:
                self.error()
        dprint('exp return {}'.format(val))
        return val

    # term → factor { mulop factor }
    # mulop → * | /
    def term(self) -> float:
        lhs = self.factor()
        if self.curChar == '*':
            self.match('*')
            rhs = self.factor()
            dprint('term return {}'.format(lhs*rhs))
            return lhs * rhs
        elif self.curChar == '/':
            self.match('/')
            rhs = self.factor()
            dprint('term return {}'.format(lhs*rhs))
            return lhs / rhs
        # else:
        #     self.error()
        dprint('term return {}'.format(lhs))
        return lhs

    # factor → (exp) | number
    def factor(self) -> float:
        if self.curChar == '(':
            self.match('(')
            val = self.exp()
            self.match(')')
        else:
            val = self.number()
        dprint('factor return {}'.format(val))
        return val

    # number → digit { digit } [.number]
    def number(self) -> float:
        val = ''
        if str.isdigit(self.curChar) is True:
            val += self.curChar
            self.match(self.curChar)
        else:
            self.error()
        while str.isdigit(self.curChar) is True:
            val += self.curChar
            self.match(self.curChar)
        if self.curChar == '.':
            self.match('.')
            val += '.'
            val += str(int(self.number()))
        dprint('number return {}'.format(float(val)))
        return float(val)


if __name__ == '__main__':
    line = input()
    line += '$'
    expression = Expression(line)
    expression.start()
