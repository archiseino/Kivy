## Kivy is Not Platform Agnostic (Just Develop on Windows for Now)

Note to self, I think it's should better to stick on the Windows and Develop that with the Installer.

Notes:

python 3.10, 3.11 are stuck on trace loop when building, potential solution to downgrade to Pyinstaller 5.6.2, also for this 3 version, one needs to include the ipaddress like this issue suggest

https://github.com/pyinstaller/pyinstaller/issues/7692

Also python 3.12 are not supported for building.

Potential solution is using python 3.9, 3.10, 3.11 and install the ipaddress package and update the `compat.py` on pyinstaller library and you'll be fine
