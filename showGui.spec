# -*- mode: python -*-

block_cipher = None


a = Analysis(['showGui.py'],
             pathex=['/home/yogi/dashboard-gui'],
             binaries=None,
             datas=[('speedometer.png', 'DATA')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas+[('speedometer.png', 'speedometer.png', 'DATA')],
          name='showGui',
          debug=False,
          strip=False,
          upx=True,
          console=True )
