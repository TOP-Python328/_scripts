class NonTextCharsError(Exception):
    def __init__(self, class_):
        super().__init__(f"{class_.__name__!r} can contain only letter characters")


class Username(str):
    def __new__(cls, value: str):
        instance = super().__new__(cls, value)
        if not instance.isalpha():
            raise NonTextCharsError(cls)
        return instance


# >>> Username('gennadiy')
# 'gennadiy'
# >>>
# >>> Username('igor1980')
# ...
# NonTextCharsError: 'Username' can contain only letters' characters

