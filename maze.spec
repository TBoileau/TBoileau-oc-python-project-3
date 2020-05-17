# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

added_files = [
         ( 'assets/img/*.png', 'assets/img' ),
         ( 'assets/fonts/*.ttf', 'assets/fonts' )
         ]

a = Analysis(['maze.py'],
             pathex=['D:\\Openclassrooms\\Parcours\\DA Python\\oc-python-project-3'],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='maze',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
