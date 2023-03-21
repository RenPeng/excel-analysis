#! /bin/bash

current_dir=$(pwd)
dirname=$(dirname ${current_dir}/$1)

pyuic5 ${current_dir}/$1 -o ${dirname}/window.py
pyrcc5 -o ${current_dir}/resources/icon_rc.py /Users/renpeng/code/qt-resources/icon/resource.icon.qrc

# ImportError: libgthread-2.0.so.0: cannot open shared object file: No such file or directory
# apt update
# apt install libglib2.0-dev


# ImportError: libGL.so.1: cannot open shared object file: No such file or directory
# apt install libgl1-mesa-glx -y