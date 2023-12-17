from pytest import mark


def upper(text: str) -> str:
    if len(text) < 15:
        return text.upper()
    else:
        raise ValueError


@mark.parametrize(
    'data',
    [
        'длинная строка',
        'очень длинная строка',
        ''
    ]
)
def test_upper(data: str):
    assert type(upper(data)) is str

