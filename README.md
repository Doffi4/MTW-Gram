# MTW-Gram

An unofficial Windows client for the Telegram messaging service, built on Telegram Desktop with an interface inspired by Telegram for macOS.

[Русский](README.ru.md) · [Download for Windows](https://github.com/Doffi4/MTW-Gram/releases) · [Changelog](CHANGELOG.md)

- A floating chat list, folder tabs, and a composer with replies and edits inside the input capsule.
- In-window settings with a section sidebar, grouped controls, and animated navigation.
- Restyled search, attachment and reaction menus, and emoji, sticker, and GIF panels.

## Install

Download the Windows x64 ZIP from Releases, extract it to its own writable folder, and run `Telegram.exe`. The beta is unsigned. Each installation keeps its profile in `tdata` next to the executable. Keep that folder when updating MTW-Gram. Download newer betas from GitHub Releases.

## Build from source

MTW-Gram uses C++ and Qt. Its changes live in two Git patches over pinned Telegram Desktop sources. Run these commands from the repository root in a Windows x64 Visual Studio Developer Command Prompt with MSVC 14.44, ATL, a Windows SDK, Git, and Python. Prepare the dependencies using the [upstream Windows build guide](https://github.com/telegramdesktop/tdesktop/blob/5ff615713d2178b8458e201778d23d7abe78db9b/docs/building-win.md).

```bat
git clone https://github.com/telegramdesktop/tdesktop.git refs/tdesktop
git -C refs/tdesktop checkout --detach 5ff615713d2178b8458e201778d23d7abe78db9b
git -C refs/tdesktop submodule update --init --recursive
git -C refs/tdesktop apply --binary ../../patches/tdesktop.patch
git -C refs/tdesktop/Telegram/lib_ui apply --binary ../../../../patches/lib_ui.patch
call refs\tdesktop\Telegram\build\prepare\win.bat
```

For a local Debug build, run `tools\build-win.bat Debug`. For Release, configure with your own [Telegram API credentials](https://core.telegram.org/api/obtaining_api_id/). Keep the credentials and CMake cache local.

```bat
pushd refs\tdesktop\Telegram
call configure.bat x64 -D TDESKTOP_API_ID=YOUR_API_ID -D TDESKTOP_API_HASH=YOUR_API_HASH -D TDESKTOP_API_TEST=OFF -D DESKTOP_APP_DISABLE_AUTOUPDATE=ON -D DESKTOP_APP_DISABLE_CRASH_REPORTS=ON
popd
call tools\build-win.bat Release
python -m unittest discover -s tools -p "test_*.py"
```

The executable is under `refs\tdesktop\out\Release`. Both upstream revisions are recorded in [patches/BASE](patches/BASE). The build documentation and patches in this repository are covered by [GPL-3.0-or-later](LICENSE). See the [upstream notice](LEGAL.upstream) for the OpenSSL exception and upstream copyright.
