@ECHO off

set pymt_portable_root=%~dp0
ECHO botstrapping PyMT @ %pymt_portable_root%


if %pymt_paths_initialized == "yes" goto runpymt;

ECHO Setting Environment Variables: 
ECHO #################################

set GST_PLUGIN_PATH=%pymt_portable_root%gstreamer\lib\gstreamer-0.10
ECHO GST_PLUGIN_PATH: 
ECHO %GST_PLUGIN_PATH%
ECHO ---------------

set PATH=%pymt_portable_root%;%pymt_portable_root%Python;%pymt_portable_root%gstreamer\bin;%pymt_portable_root%MinGW\bin;%PATH%
ECHO PATH: 
ECHO %PATH%
ECHO ----------------------------------

set PYTHONPATH=%pymt_portable_root%pymt;%PYTHONPATH%
ECHO PYTHONPATH: 
ECHO %PYTHONPATH% 
ECHO ----------------------------------

set pymt_paths_initialized = "yes"

:runpymt
ECHO ##################################
ECHO done bootstraping pymt...have fun!
ECHO running "python.exe %*"
python.exe  %*