from decimal import Decimal as dec

# >>> 0.1 + 0.1 + 0.1 == 0.3
# False
# >>>
# >>> dec(0.1)
# Decimal('0.1000000000000000055511151231257827021181583404541015625')
# >>>
# >>> dec(0.3)
# Decimal('0.299999999999999988897769753748434595763683319091796875')
# >>>
# >>> dec('0.1') + dec('0.1') + dec('0.1') == dec('0.3')
# True

# >>> dec(str(1.5))
# Decimal('1.5')

# >>> dec('0.1') + 1
# Decimal('1.1')
# >>>
# >>> 1 + dec('0.1')
# Decimal('1.1')
# >>>
# >>> dec('2.2') + 3.3
# ...
# TypeError: unsupported operand type(s) for +: 'decimal.Decimal' and 'float'

