.PHONY : all

all: ../py_ui/mainwindow.py ../py_ui/mbxxxoutput.py ../py_ui/randomize_shm.py ../py_ui/shm_hexdump.py

../py_ui/mainwindow.py: mainwindow.ui
	pyside6-uic -o $@ $?

../py_ui/mbxxxoutput.py: mbxxxoutput.ui
	pyside6-uic -o $@ $?

../py_ui/randomize_shm.py: randomize_shm.ui
	pyside6-uic -o $@ $?

../py_ui/shm_hexdump.py: shm_hexdump.ui
	pyside6-uic -o $@ $?