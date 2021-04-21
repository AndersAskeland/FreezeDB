cd "/Users/andersaskeland/GitHub/FreezeDB"
source ~/.pyenv/versions/FreezeDB/bin/activate 

pyside2-uic resources/user_interface/mainwindow.ui -o resources/user_interface/mainwindow.py
pyside2-uic resources/user_interface/dialog_create_db.ui -o resources/user_interface/dialog_create_db.py

pyside2-rcc resources/graphics/icons.qrc -o icons_rc.py

python FreezeDB.py