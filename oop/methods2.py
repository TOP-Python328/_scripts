class Informbureau:
    
    @staticmethod
    def warning() -> None:
        print('Граждане, будьте бдительны.')
    
    @staticmethod
    def emergency() -> None:
        print('ВНИМАНИЕ!')


municipal = Informbureau()


# для статических методов не осуществляется подмены вызова
# >>> Informbureau.warning
# <function Informbureau.warning at 0x000001AA54582CA0>
# >>>
# >>> municipal.warning
# <function Informbureau.warning at 0x000001AA54582CA0>

# >>> Informbureau.warning()
# Граждане, будьте бдительны.
# >>> 
# >>> municipal.warning()
# Граждане, будьте бдительны.
# >>> 
# >>> Informbureau.emergency()
# ВНИМАНИЕ!
# >>> 
# >>> municipal.emergency()
# ВНИМАНИЕ!

