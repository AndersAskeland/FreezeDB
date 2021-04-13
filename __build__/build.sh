cd "/Users/andersaskeland/GitHub/FreezeDB/### REWRITE ###"
source ~/.pyenv/versions/FreezeDB/bin/activate 

pyside2-uic resources/user_interface/mainwindow.ui -o resources/user_interface/mainwindow.py
pyside2-uic resources/user_interface/dialog_create_db.ui -o resources/user_interface/dialog_create_db.py

pyside2-rcc resources/graphics/icons.qrc -o icons_rc.py

python __build__/pyqss/pyQSS.py resources/stylesheets/stylesheet_main_dark.pyqss resources/stylesheets/stylesheet_main_dark.qss
python __build__/pyqss/pyQSS.py resources/stylesheets/stylesheet_main_light.pyqss resources/stylesheets/stylesheet_main_light.qss


python main.py