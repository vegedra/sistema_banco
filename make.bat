@echo off
cls
echo 1) sem TUI
echo 2) com TUI
choice /c 12 /n

if %errorlevel% EQU 1 python main_semTUI.py
if %errorlevel% EQU 2 python main_comTUI.py

pause