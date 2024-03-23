.PHONY : all

all: ../src/py_ui/mainwindow.py ../src/py_ui/mbxxxoutput.py ../src/py_ui/randomize_shm.py ../src/py_ui/shm_hexdump.py

../src/py_ui/mainwindow.py: mainwindow.ui
	pyside6-uic -o $@ $?

../src/py_ui/mbxxxoutput.py: mbxxxoutput.ui
	pyside6-uic -o $@ $?

../src/py_ui/randomize_shm.py: randomize_shm.ui
	pyside6-uic -o $@ $?

../src/py_ui/shm_hexdump.py: shm_hexdump.ui
	pyside6-uic -o $@ $?