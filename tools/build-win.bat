@echo off
setlocal
rem x64 build of refs\tdesktop: build-win.bat [Debug|Release], Debug by default. Needs VS 2022 Build Tools (MSVC 14.44, ATL, en-US language pack).
set VSLANG=1033
set "ROOT=%~dp0..\refs\tdesktop"
set "CACHE=%ROOT%\out\CMakeCache.txt"
set "CONFIG=%~1"
if not defined CONFIG set "CONFIG=Debug"
if /i "%CONFIG%"=="Release" (
    findstr /x /c:"TDESKTOP_API_TEST:BOOL=OFF" "%CACHE%" >nul 2>nul ^
        && findstr /x /c:"DESKTOP_APP_DISABLE_AUTOUPDATE:BOOL=ON" "%CACHE%" >nul 2>nul ^
        && findstr /x /c:"DESKTOP_APP_DISABLE_CRASH_REPORTS:BOOL=ON" "%CACHE%" >nul 2>nul
    if errorlevel 1 (
        echo Configure Release with your Telegram API credentials and disable upstream update and crash reporting. See README.md.
        exit /b 1
    )
)
if /i not "%VSCMD_ARG_TGT_ARCH%"=="x64" (
    call "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvars64.bat" -vcvars_ver=14.44 || exit /b 1
)
cd /d "%ROOT%\Telegram" || exit /b 1
if not exist "%CACHE%" (
    call configure.bat x64 -D TDESKTOP_API_TEST=ON -D DESKTOP_APP_DISABLE_AUTOUPDATE=ON -D DESKTOP_APP_DISABLE_CRASH_REPORTS=ON || exit /b 1
)
rem 5 compilers x 2 projects fits in 32 GB; more runs cl out of heap.
cmake --build "%ROOT%\out" --config %CONFIG% --target Telegram -- /m:2 /p:CL_MPCount=5 /nologo /v:m
