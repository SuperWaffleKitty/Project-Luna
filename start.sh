#!/bin/bash
#!/usr/bin/env python3
FILE=Luna.py
ver=$(python -c"import sys; print(sys.version_info.major)")

echo 'attempting to start executable...'

if [ -f "$FILE" ]; then
  echo "File is present..."

  if [ $ver -eq 3 ]; then
      echo "Python is up to date..."
      echo "Starting Executable..."
      python3 Luna.py

  else
      echo "Please upgrade to Python3"
  fi

else
    echo "$FILE does not exist, check to make sure you have the latest version."
fi
