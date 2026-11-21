import base64
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


SOURCE = (
    Path(__file__).resolve().parents[1]
    / "refs/tdesktop/Telegram/SourceFiles/core/update_github.cpp"
)


def powershell_string(value):
    encoded = base64.b64encode(str(value).encode()).decode()
    return f"[Text.Encoding]::UTF8.GetString([Convert]::FromBase64String('{encoded}'))"


@unittest.skipUnless(os.name == "nt", "Windows installer")
class GitHubUpdateTest(unittest.TestCase):
    def test_replaces_executable_after_exit_and_keeps_profile(self):
        script = SOURCE.read_text(encoding="utf-8").split('R"ps(', 1)[1].split(')ps"', 1)[0]
        script = script.replace("Start-Process -FilePath", "Start-Process -Wait -FilePath")
        system = Path(os.environ["SystemRoot"]) / "System32"
        powershell = system / "WindowsPowerShell/v1.0/powershell.exe"
        with tempfile.TemporaryDirectory(prefix="MTW-Gram ' update ") as folder:
            directory = Path(folder)
            target = directory / "Telegram.exe"
            staged = directory / "Telegram.exe.staged"
            backup = directory / "Telegram.exe.mtw-previous"
            original = system / "ping.exe"
            replacement = system / "where.exe"
            shutil.copyfile(original, target)
            shutil.copyfile(replacement, staged)
            backup.write_bytes(b"backup from a previous update")
            tdata = directory / "tdata"
            tdata.mkdir()
            profile = tdata / "profile"
            profile.write_bytes(b"keep me")
            with subprocess.Popen(
                [str(target), "-n", "4", "127.0.0.1"],
                stdout=subprocess.DEVNULL,
                creationflags=subprocess.CREATE_NO_WINDOW,
            ) as parent:
                parameters = {
                    "staged": staged,
                    "target": target,
                    "workdir": directory,
                    "argsLine": "/q where.exe",
                }
                prefix = f"$parentId = {parent.pid}\n" + "".join(
                    f"${key} = {powershell_string(value)}\n"
                    for key, value in parameters.items()
                )
                encoded = base64.b64encode((prefix + script).encode("utf-16le"))
                subprocess.run(
                    [str(powershell), "-NoProfile", "-NonInteractive",
                     "-EncodedCommand", encoded.decode()],
                    creationflags=subprocess.CREATE_NO_WINDOW,
                    capture_output=True,
                    timeout=15,
                    check=True,
                )
                self.assertEqual(parent.poll(), 0)
            self.assertEqual(target.read_bytes(), replacement.read_bytes())
            self.assertEqual(backup.read_bytes(), original.read_bytes())
            self.assertEqual(profile.read_bytes(), b"keep me")
            self.assertFalse(staged.exists())


if __name__ == "__main__":
    unittest.main()
