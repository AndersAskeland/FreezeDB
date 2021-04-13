##################################################################################
##                                                                              ##
## Title: CSS                                                                   ##
##                                                                              ##
## What: CSS elements specifically used                                         ##
##                                                                              ##
##################################################################################

# When button is not active
css_btn_idle = (u"QPushButton {\n"
"	color: rgb(201, 202, 204);\n"
"	font-size: 20px;\n"
"	padding-left: 20px;\n"
"	text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"")

# When button is pressed
css_btn_pressed = (u"QPushButton {\n"
"	color: rgb(201, 202, 204);\n"
"	font-size: 20px;\n"
"	padding-left: 20px;\n"
"   background-color: rgb(85, 170, 255);\n"
"	text-align: left;\n"
"}\n"
"")