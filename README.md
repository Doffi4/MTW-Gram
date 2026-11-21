# MTW-Gram

An unofficial Windows client for the Telegram messaging service, built on Telegram Desktop with an interface inspired by Telegram for macOS.

[Русский](README.ru.md) · [Download for Windows](https://github.com/Doffi4/MTW-Gram/releases) · [Changelog](CHANGELOG.md)

- A floating chat list, folder tabs, and a composer with replies and edits inside the input capsule.
- In-window settings with a section sidebar, grouped controls, and animated navigation.
- Restyled search, attachment and reaction menus, and emoji, sticker, and GIF panels.

## Install

Download the Windows x64 ZIP from Releases, extract it to its own writable folder, and run `Telegram.exe`. The beta is unsigned. Each installation keeps its profile in `tdata` next to the executable. Builds with the GitHub updater can check for a release under **Settings → General → Check for updates**, download it, and install it on restart. For manual updates, keep the `tdata` folder.

## Build from source

MTW-Gram uses C++ and Qt. Its changes live in two Git patches over Telegram Desktop 7.4.4. Run these commands from the repository root in a Windows x64 Visual Studio Developer Command Prompt with MSVC 14.44, ATL, a Windows SDK, Git, and Python. Prepare the dependencies using the [upstream Windows build guide](https://github.com/telegramdesktop/tdesktop/blob/bf4f714036f21c750d535dab199c811b3f9bfdd4/docs/building-win.md).

```bat
git clone https://github.com/telegramdesktop/tdesktop.git refs/tdesktop
git -C refs/tdesktop checkout --detach bf4f714036f21c750d535dab199c811b3f9bfdd4
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
