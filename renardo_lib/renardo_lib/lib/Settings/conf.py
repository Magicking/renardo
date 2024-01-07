import os.path
from renardo_gatherer import SAMPLES_FOLDER_PATH

# Settings
# ------------------
ADDRESS='localhost'
PORT=57110
PORT2=57120
FONT='Consolas'
SUPERCOLLIDER=""
BOOT_ON_STARTUP=False
CHECK_FOR_UPDATE=True
SC3_PLUGINS=False
MAX_CHANNELS=2
SAMPLES_DIR=SAMPLES_FOLDER_PATH
GET_SC_INFO=True
USE_ALPHA=True
ALPHA_VALUE=0.8
MENU_ON_STARTUP=True
TRANSPARENT_ON_STARTUP=False
RECOVER_WORK=True
LINE_NUMBER_MARKER_OFFSET=0
AUTO_COMPLETE_BRACKETS=True
CPU_USAGE=2 # 0=low, 1=medium, 2=high
CLOCK_LATENCY=0 # 0=low, 1=medium, 2=high
FORWARD_ADDRESS=''
FORWARD_PORT=0

# Text colours
# ------------------

plaintext='#ffffff'
background='#1a1a1a'
functions='#bf4acc'
key_types='#29abe2'
user_defn='#29abe2'
other_kws='#49db8b'
comments='#666666'
numbers='#e89c18'
strings='#eae02a'
dollar='#ec4e20'
arrow='#eae02a'
players='#ec4e20'

# Loading from file
# ------------------

filename = os.path.join(os.path.dirname(__file__), "conf.txt")

try:

    with open(filename) as f:
        contents = f.read()
        code = compile(contents, "FoxDot", "exec")
        exec(code, globals())
except FileNotFoundError:
    pass

# Loading from env
# ------------------

for key, value in os.environ.items():
    if key in globals():
        globals()[key] = value
