"""
Liskov Substituion Principle — Принцип Подстановки Лисков

Верхний уровень
"""

import solid_lsp_2_low as model


def test_model(shape: model.Rectangle):
    width = shape.width
    shape.height = 10
    expected_area = width * 10
    calculated_area = shape.area
    assert expected_area == calculated_area


rc1 = model.Rectangle(5, 7)

try:
    test_model(rc1)
except AssertionError:
    print('test failed')
else:
    print('test succeeded')

# test succeeded
# >>> 
# >>> rc1.width
# 5
# >>> rc1.height
# 10
# >>> rc1.area
# 50


sq1 = model.Square(5)

try:
    test_model(sq1)
except AssertionError:
    print('test failed')
else:
    print('test succeeded')

# test failed
# >>>
# >>> sq1.width
# 10
# >>> sq1.height
# 10
# >>> sq1.area
# 100

