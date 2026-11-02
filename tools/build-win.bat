@echo off
rem x64 build of refs\tdesktop: build-win.bat [Debug|Release], Debug by default. Needs VS 2022 Build Tools (MSVC 14.44, ATL, en-US language pack).
set VSLANG=1033
set "ROOT=%~dp0..\refs\tdesktop"
call "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvars64.bat" -vcvars_ver=14.44 || exit /b 1
cd /d "%ROOT%\Telegram" || exit /b 1
if exist "%ROOT%\out\CMakeCache.txt" goto build
call configure.bat x64 -D TDESKTOP_API_TEST=ON || exit /b 1
:build
set CONFIG=%1
if "%CONFIG%"=="" set CONFIG=Debug
rem 5 compilers x 2 projects fits in 32 GB; more runs cl out of heap.
cmake --build "%ROOT%\out" --config %CONFIG% --target Telegram -- /m:2 /p:CL_MPCount=5 /nologo /v:m
