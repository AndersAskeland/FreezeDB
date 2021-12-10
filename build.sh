# Go to direct location
cd "/Users/andersaskeland/GitHub/FreezeDB"

# Remove previous settings
rm "/Users/andersaskeland/GitHub/FreezeDB/resources/settings/config.ini"

# Activate virtual enviorment
source ~/.pyenv/versions/FreezeDB/bin/activate 

# Build UI file using uic
pyside2-uic resources/user_interface/mainwindow.ui -o resources/user_interface/mainwindow.py
pyside2-uic resources/user_interface/dialog_create_db.ui -o resources/user_interface/dialog_create_db.py

# Create icons
pyside2-rcc resources/graphics/icons.qrc -o icons_rc.py

# Build file
pyinstaller --specpath "pyinstaller" \
    --workpath "pyinstaller/build" \
    --distpath "pyinstaller/dist" \
    --log-level=WARN \
    --windowed \
    --noconfirm \
    --add-data="../resources/data:resources/data" \
    --add-data="../resources/settings:resources/settings" \
    --add-data="../resources/user_interface:resources/user_interface" \
    --add-data="../resources/stylesheets:resources/stylesheets" \
    FreezeDB.py