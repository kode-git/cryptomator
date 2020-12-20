#!/bin/bash

dir=$1
mode=$2
_pwd=${pwd}
# going to the source file
# cd ../src

cd ../src

if [ -d "$dir" ]; then
  if [ "$mode" = "--list" ];then
    python3 core.py "$dir" -l
  true
  elif [ "$mode" = "--enc" ]; then
    python3 core.py "$dir" -e
  else
      echo "ERROR: mode need to be -e to encrypt or -l to list the directory"
  fi
fi


cd "${pwd}"

