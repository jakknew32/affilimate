@echo off
setlocal
echo ========================================
echo       W3U to M3U Playlist Converter
echo ========================================
echo.

if "%~1"=="" (
    echo [ERROR] No input file specified.
    echo.
    echo Usage:
    echo   1. Drag and drop a .w3u file onto this .bat file.
    echo   2. Or run from command line: convert.bat filename.w3u
    echo.
    pause
    exit /b 1
)

python "%~dp0w3u_to_m3u.py" "%~1"

echo.
echo Conversion complete!
pause
