@echo off
echo Attempting to start using Python EXE on PATH.
python Luna.py || goto NotExePath
goto CommonExit

:NotExePath
echo The python executable hasn't been installed on your PATH. Attempting to use Python Launcher.
py Luna.py || goto PyLaunchNotWork
goto CommonExit

:PyLaunchNotWork
echo Python launcher hasn't worked. Presumably python isn't installed.
goto CommonExit

:CommonExit
echo CommonExit
