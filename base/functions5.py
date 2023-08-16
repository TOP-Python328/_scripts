def test_function():
    return 'abc'
    # никогда не будет выполнено
    print('после возврата')


test_function()
test_function()
test_function()



def str_to_num(number: str) -> int | float | None:
    if not isinstance(number, str):
        return None
    
    dots = number.count('.')
    if dots == 1:
        digits_dot = set('0123456789') | {'.'}
        if (
                set(number) <= digits_dot 
             or number[0] == '-' 
            and set(number[1:]) <= digits_dot
        ):
            return float(number)
        else:
            return None
    
    elif dots == 0:
        digits = set('0123456789')
        if (
                set(number) <= digits 
             or number[0] == '-' 
            and set(number[1:]) <= digits
        ):
            return int(number)
        else:
            return None
    
    else:
        return None
