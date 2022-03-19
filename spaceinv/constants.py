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
FONT_FILE = "spaceinv/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
Movement1_SOUND = "spaceinv/asset/sounds/sounds_0.wav"
Movement2_SOUND = "spaceinv/asset/sounds/sounds_1.wav"
Movement3_SOUND = "spaceinv/asset/sounds/sounds_2.wav"
Movement4_SOUND = "spaceinv/asset/sounds/sounds_4.wav"
Invaderkilled_SOUND = "spaceinv/asset/sounds/sounds_invaderkilled.wav"
Mysteryentered_SOUND = "spaceinv/asset/sounds/sounds_mysteryentered.wav"
Mysterykilled_SOUND = "spaceinv/asset/sounds/sounds_mysterykilled.wav"
Shipexplotion_SOUND = "spaceinv/asset/sounds/sounds_shipexplotion.wav"
Shoot_SOUND = "spaceinv/asset/sounds/sounds_shoot.wav"
Shoot2_SOUND = "spaceinv/asset/sounds/sounds_shoot2.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
RED = Color(237, 28, 36)
GREEN = Color(78, 255, 87)
YELLOW = Color(241, 255, 0)
BLUE = Color(80, 255, 239)
PURPLE = Color(203, 0, 255)
WHITE = Color(255, 255, 255)

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

