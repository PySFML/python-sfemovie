#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# pySFML2 - Cython SFML Wrapper for Python
# Copyright 2012, Jonathan De Wachter <dewachter.jonathan@gmail.com>
#
# This software is released under the GPLv3 license.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys, os
from distutils.core import setup, Command
from distutils.extension import Extension

USE_CYTHON = os.environ.get('USE_CYTHON', False)


if USE_CYTHON:
	import Cython.Distutils

	src = 'src/sfemovie.pyx'

else:
	src = 'src/sfemovie.cpp'

# TODO: improve /usr/local/include/
sfemovie = Extension('sfemovie', [src], ['include', '/usr/local/include/python-sfml2'], language='c++', libraries=['sfml-system', 'sfml-window', 'sfml-graphics', 'sfml-audio', 'sfml-network', 'sfeMovie'])


with open('README.md', 'r') as f:
	long_description = f.read()

major, minor, micro, releaselevel, serial = sys.version_info

kwargs = dict(name='pysfeMovie',
			ext_modules=[sfemovie],
			package_dir={'': 'src'},
			version='1.0',
			description='A Python binding for sfeMovie',
			long_description=long_description,
			author_email='dewachter.jonathan@gmail.com',
			url='http://openhelbreath.be/python-sfml2',
			license='GPLv3',
			classifiers=['Development Status :: 5 - Production/Stable',
						'Intended Audience :: Developers',
						'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
						'Operating System :: OS Independent',
						'Programming Language :: Cython',
						'Topic :: Games/Entertainment',
						'Topic :: Multimedia',
						'Topic :: Software Development :: Libraries :: Python Modules'])

if major == 2:
	kwargs.update(author='Jonathan De Wachter'.decode())
else:
	kwargs.update(author='Jonathan De Wachter')

if USE_CYTHON:
	kwargs.update(cmdclass={'build_ext': Cython.Distutils.build_ext})

setup(**kwargs)
