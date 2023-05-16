# Start должен быть всегда самым первым импортом т.к в нем проверка зареган ли юзер
from .start import dp 
from .help import dp
from .game import dp
from .menu import dp
from .minefield import dp
from .report import dp
from .coin import dp
from .plug import dp

from .MiniGames import dp

from .Callback import dp


__all__ = ['dp']