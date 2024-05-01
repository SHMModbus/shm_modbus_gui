.PHONY : all

all: ../src/py_ui/mainwindow.py \
		../src/py_ui/mbxxxoutput.py \
		../src/py_ui/randomize_shm.py \
		../src/py_ui/shm_hexdump.py \
	 	../src/py_ui/inspect_shm.py \
	 	../src/py_ui/inspect_shm_add_int.py \
	 	../src/py_ui/inspect_shm_add_float.py \
	 	../src/py_ui/inspect_shm_add_bool.py \
	 	../src/py_ui/inspect_shm_add_string.py

../src/py_ui/mainwindow.py: mainwindow.ui
	pyside6-uic -o $@ $?

../src/py_ui/mbxxxoutput.py: mbxxxoutput.ui
	pyside6-uic -o $@ $?

../src/py_ui/randomize_shm.py: randomize_shm.ui
	pyside6-uic -o $@ $?

../src/py_ui/shm_hexdump.py: shm_hexdump.ui
	pyside6-uic -o $@ $?

../src/py_ui/inspect_shm.py: inspect_shm.ui
	pyside6-uic -o $@ $?

../src/py_ui/inspect_shm_add_int.py: inspect_shm_add_int.ui
	pyside6-uic -o $@ $?

../src/py_ui/inspect_shm_add_float.py: inspect_shm_add_float.ui
	pyside6-uic -o $@ $?

../src/py_ui/inspect_shm_add_bool.py: inspect_shm_add_bool.ui
	pyside6-uic -o $@ $?

../src/py_ui/inspect_shm_add_string.py: inspect_shm_add_string.ui
	pyside6-uic -o $@ $?
