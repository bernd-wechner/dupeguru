# -*- mode: python -*-
a = Analysis([os.path.join(HOMEPATH,'support\\_mountzlib.py'), os.path.join(HOMEPATH,'support\\useUnicode.py'), 'start.py'],
             pathex=['C:\\src\\dupeguru\\se'])
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build\\pyi.win32\\dupeGuru', 'dupeGuru.exe'),
          debug=False,
          strip=False,
          upx=True,
          console=False,
          icon='base\\images\\dgse_logo.ico',
          version='verinfo_tmp')
coll = COLLECT( exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name=os.path.join('dist'))