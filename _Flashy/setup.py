from setuptools import setup

APP = ['Flashy.py']
DATA_FILES = [('', ['data']),
              ('', ['images'])]
OPTIONS = {
    'iconfile': '/private/var/code/personal/python_learning/31_flash_card_app/Flashy.icns',
    'argv_emulation': True,
    'packages': ['setuptools', 'pandas', 'tkinter', 'random', 'textwrap']
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
