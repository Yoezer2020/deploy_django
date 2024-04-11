# -*- mode: python ; coding: utf-8 -*-
import io
import sys

class CatchOutErr:
    def __init__(self):
        self.val = ""

    def write(self, text):
        self.val += text

    def flush(self):
        pass

stdout = sys.stdout
stderr = sys.stderr
sys.stdout = CatchOutErr()
sys.stderr = CatchOutErr()

a = Analysis(
    ['manage.py'],
    pathex=[],
    binaries=[],
    datas=[('dzongkha_nextword', 'dzongkha_nextword'), ('dzo_nextword\\static', 'static'), ('dzo_nextword\\templates', 'templates')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

# Write out sys.stdout and sys.stderr to be able to see error messages
sys.stdout = sys.stderr = open(os.path.join(DISTPATH, 'output.log'), 'w')

# Optionally remove --noupx if you installed pyup
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='manage',
    debug=False,
    strip=False,
    upx=True,
    console=True,
    runtime_tmpdir=None,
    icon=None,
)