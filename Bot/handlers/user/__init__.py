# Start должен быть всегда самым первым импортом т.к в нем проверка зареган ли юзер
from .start import dp 
from .help import dp
from .game import dp


__all__ = ['dp']