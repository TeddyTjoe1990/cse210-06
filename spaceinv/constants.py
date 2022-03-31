from game.casting.color import Color

# GAME
GAME_NAME = "space invaders"
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

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5

# HUD
HUD_MARGIN = 15
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
LEVEL_FORMAT = "LEVEL: {}"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"

# SHIP
SHIP_GROUP = "ships"
SHIP_IMAGE = "spaceinv/assets/images/ship.png"
SHIP_WIDTH = 28
SHIP_HEIGHT = 28
SHIP_RATE = 6
SHIP_VELOCITY = 6

# SHOOT 
SHOOT_GROUP = "shoots"
SHOOT_IMAGES = "spaceinv/assets/images/laser.png" 
SHOOT_WIDTH = 28
SHOOT_HEIGHT = 14
SHOOT_RATE = 6
SHOOT_VELOCITY = 7

# ENEMY
ENEMY_GROUP = "enemies"
ENEMY_IMAGES = {
    "b": [f"spaceinv/assets/images/{i:03}.png" for i in range(4, 6)],
    "g": [f"spaceinv/assets/images/{i:03}.png" for i in range(7, 9)],
    "p": [f"spaceinv/assets/images/{i:03}.png" for i in range(1, 3)]
}
ENEMY_WIDTH = 28
ENEMY_HEIGHT = 28
ENEMY_RATE = 4
ENEMY_VELOCITY = 7
ENEMY_POINTS = 50

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"
