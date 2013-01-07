#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# pysfeMovie - Python binding for sfeMovie
# Copyright 2013, Jonathan De Wachter <dewachter.jonathan@gmail.com>
#
# This software is released under the LGPLv3 license.
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import sys, os, platform
from distutils.core import setup, Command
from distutils.extension import Extension

# check if cython is needed (if c++ files are generated or not)
NEED_CYTHON = not all(map(os.path.exists, ['src/sfemovie.cpp']))
	
try:
	USE_CYTHON = NEED_CYTHON or bool(int(os.environ.get('USE_CYTHON', 0)))
except ValueError:
	USE_CYTHON = NEED_CYTHON or bool(os.environ.get('USE_CYTHON'))

# define the include directory
if platform.system() == 'Windows':
	include_dir = sys.prefix + "\\include\\pySFML"
else:
	major, minor, _, _ , _ = sys.version_info
	include_dir = sys.prefix + "/include/python{0}.{1}/sfml/".format(major, minor)

# define libraries to link with
if platform.system() == 'Windows':
	libraries=['sfml-system', 'sfml-window', 'sfml-graphics', 'sfeMovie', 'swscale', 'swresample', 'avutil', 'avformat', 'avfilter', 'avfilter', 'avcodec']
else:
	libraries=['sfml-system', 'sfml-window', 'sfml-graphics', 'sfeMovie', 'swscale']

if USE_CYTHON:
	try:
		from Cython.Distutils import build_ext
	except ImportError:
		from subprocess import call
		try:
			call(["cython", "--cplus", "src/sfemovie.pyx", "-Iinclude", -"I"+include_dir])
			USE_CYTHON = False
		except OSError:
			print("Please install the correct version of cython and run again.")
			sys.exit(1)
			
if USE_CYTHON:
	src = 'src/sfemovie.pyx'
else:
	src = 'src/sfemovie.cpp'

sfemovie = Extension('sfemovie', 
	sources = [src], 
	include_dirs = ['include', include_dir], 
	language='c++', 
	libraries=libraries)

with open('README', 'r') as f:
	long_description = f.read()

major, minor, micro, releaselevel, serial = sys.version_info

kwargs = dict(name='pysfeMovie',
			ext_modules=[sfemovie],
			package_dir={'': 'src'},
			version='1.0',
			description='Python binding for sfeMovie',
			long_description=long_description,
			author="Jonathan De Wachter",
			author_email='dewachter.jonathan@gmail.com',
			url='http://sfemovie.python-sfml.org',
			license='LGPLv3',
			classifiers=['Development Status :: 5 - Production/Stable',
						'Intended Audience :: Developers',
						'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
						'Operating System :: OS Independent',
						'Programming Language :: Cython',
						'Topic :: Games/Entertainment',
						'Topic :: Multimedia',
						'Topic :: Software Development :: Libraries :: Python Modules'],
			cmdclass=dict())

if USE_CYTHON:
	kwargs['cmdclass'].update({'build_ext': build_ext})

setup(**kwargs)
