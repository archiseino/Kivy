# -*- mode: python ; coding: utf-8 -*-


from kivy_deps import sdl2, glew
import os 
import site

def get_jaraco_path():
    return os.path.join(site.getsitepackages()[1], "setuptools", "_vendor", "jaraco")

block_cipher = None


a = Analysis(
    ['D:\\Stuff That I Need to Do\\Kivy\\Hrv-Plus-Ultra\\main.py'],
    pathex=[],
    # binaries=[("C:\\Users\\ACER\\miniconda3\\envs\\env_dsp\\Lib\\site-packages\\setuptools\\_vendor\\jaraco", "jaraco")],
    binaries=[(get_jaraco_path(), "jaraco")],
    datas=[],
    hiddenimports = [
        "kivy_matplotlib_widget.uix",
        "kivy_matplotlib_widget.uix.graph_widget",
        "widgets.containers.ShadowBox",
        "widgets.inputs.Text",
        "widgets.buttons.IconButton",
        "widgets.containers.OverlayContainer",
        "widgets.containers.StatusBox"
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz, Tree("D:\\Stuff That I Need to Do\\Kivy\\Hrv-Plus-Ultra"),
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
    [],
    name='HRV',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
