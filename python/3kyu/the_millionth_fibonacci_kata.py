# https://www.codewars.com/kata/the-millionth-fibonacci-kata/train/python

class Matrix():
    def __init__(self, rows):
        self.rows = rows

    def __mul__(self, other):
        return Matrix([[sum([rc[0]*rc[1] for rc in zip(row, col)])  for col in zip(*other.rows)] for row in self.rows])

    def __pow__(self, power):
        if power == 0: return Matrix([[1,0],[0,1]])
        if power == 1: return self
        if power == 2: return self*self
        if power % 2:
            return self*((self**(power//2))**2)
        else:
            return (self**(power//2))**2

    def __repr__(self):
        return "Matrix(%s)" % self.rows

    def __getitem__(self, position):
        return self.rows[position]

def fib(n):
    """Calculates the nth Fibonacci number"""
    matrix = Matrix([[1,1],[1,0]])
    init_vector = Matrix([[1], [0]])
    if n == 0: return 0
    if n < 0: return fib(-n) if n % 2 else -fib(-n)
    f = (matrix ** (n-1)) * init_vector
    return f[0][0]
