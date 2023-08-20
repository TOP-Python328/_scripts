def process_track_info(
        *,
        # параметры после * — строго ключевые 
        song_title: str,
        artist: str,
        album: str,
        year: int,
        channels: int,
        bit_depth: int,
        sample_rate: float
):
    ...


# приведёт к TypeError
# process_track_info(
#     'Boom',
#     'Boomers',
#     'BOOM!',
#     2010,
#     6,
#     16,
#     48.0,
# )

process_track_info(
    song_title='Boom',
    artist='Boomers',
    album='BOOM!',
    year=2010,
    channels=6,
    bit_depth=16,
    sample_rate=48.0,
)


def calculator(
        # параметры до * — позиционно-ключевые
        num1: int, 
        num2: int, 
        *, 
        # параметр после * — строго ключевой
        operation: str
) -> int | float:
    ...


# >>> calculator(1, 2, operation='+')
# 3
# >>> calculator(num2=2, operation='-', num1=1)
# -1

