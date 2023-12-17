from pytest import mark

from calculator.app import model


models = (
    (model.Add, '+'),
    (model.Sub, '-'),
    (model.Mul, '*'),
    (model.Div, '/'),
)


@mark.parametrize('expr_cls,oper', models)
class TestExpressionInstantiate:
    
    correct_operands_numbers = (
        (0, 0),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
        (0.5, -10.1),
        (1j, -1j),
    )
    incorrect_operands_numbers = (
        ('1', '1'),
        ('a', 'b'),
    )
    
    @mark.parametrize('left,right', correct_operands_numbers)
    def test_correct_operands(self, expr_cls, left, right, oper):
        assert expr_cls(left, right)
    
    @mark.parametrize('left,right', incorrect_operands_numbers)
    def test_incorrect_operands(self, expr_cls, left, right, oper):
        try:
            expr_cls(left, right)
        except ValueError as exc:
            assert exc
        else:
            assert False
    
    def test_correct_operation(self, expr_cls, oper):
        assert expr_cls.operation == oper
    
    def test_incorrect_operation(self, expr_cls, oper):
        ...

