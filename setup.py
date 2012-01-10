import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'SQLAlchemy',
    'transaction',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'zope.sqlalchemy',
    'Babel',
    'lingua',
    ]

if sys.version_info[:3] < (2,5,0):
    requires.append('pysqlite')

setup(name='c3sPortal',
      version='0.0',
      description='c3sPortal',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      message_extractors={'.': [
            ('**.py', 'lingua_python', None),
            ('**.pt', 'lingua_xml', None),
            ]},
      test_suite='c3sportal',
      install_requires = requires,
      entry_points = """\
      [paste.app_factory]
      main = c3sportal:main
      [console_scripts]
      populate_c3sPortal = c3sportal.scripts.populate:main
      """,
      )

