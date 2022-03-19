from game.casting.color import Color

# GAME
GAME_NAME = "Batter"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "batter/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = "batter/assets/sounds/boing.wav"
WELCOME_SOUND = "batter/assets/sounds/start.wav"
OVER_SOUND = "batter/assets/sounds/over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
WHITE = Color(255, 255, 255)
GREEN = Color(78, 255, 87)
YELLOW = Color(241, 255, 0)
BLUE = Color(80, 255, 239)
RED = Color(237, 28, 36)

# KEYS
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# LEVELS
LEVEL_FILE = "batter/assets/data/level-{:03}.txt"
BASE_LEVELS = 5

