# exercise: write a DSL in Python such that you can write expressions like ((1 + 2) * 3).eval() == 9 and ((1 + 2) * 3).print() == '((1 + 2) * 3)'

from typing import Any


class Expr:
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass

class Const(Expr):
    def __init__(self, left) -> None:
        self.left = left

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self.left
    
    def __str__(self) -> str:
        return str(self.left)

class Add(Expr):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self.left() + self.right()

class Multiply(Expr):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self.left() * self.right()
    
class Divide(Expr):
    def __init__(self, left, right):
        super().__init__(left, right)

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self.left / self.right

class Exponent(Expr):
    def __init__(self, left, right):
        super().__init__(left, right)

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self.left() ** self.right()
    

expr1 = Add(Const(1), Const(2))

print(expr1() == 3)


# expr1 = Add(Const(1), Const(2)) == 1 + 2