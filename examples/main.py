#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# pysfeMovie - a Python binding for sfeMovie
# Copyright 2012, Jonathan De Wachter <dewachter.jonathan@gmail.com>
#
# This software is released under the GPLv3 license.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import sfml as sf
import sfemovie as sfe

# some settings
fullscreen = False

# create window and enable VSync
window = sf.RenderWindow(sf.VideoMode(640, 480), "sfeMovie for Python")
window.vertical_synchronization = True

# open a movie
try:
	movie = sfe.Movie.from_file("some_movie.ogv")
except IOError: exit(1)

# scale the movie to the window drawing area
movie.resize_to_frame((0, 0, 640, 480), True)

# start movie playback
movie.play()

while window.is_open:
	for event in window.events:
		
		# window closure
		if type(event) is sf.CloseEvent:
			window.close()
			
		if type(event) is sf.KeyEvent and event.pressed:
		
			# play/stop
			if event.code == sf.Keyboard.SPACE:
				movie.play()
			else:
				movie.pause()
				
			if event.code == sf.Keyboard.S:
				movie.stop()
				
			# restart the playback
			if event.code == sf.Keyboard.R:
				movie.stop()
				movie.play()
				
			# toggle fullscreen mode
			if event.code == sf.Keyboard.F:
				fullscreen = not fullscreen
				
				# we want to switch to the full screen mode
				if fullscreen:
					size, _ = sf.VideoMode.get_desktop_mode()
					w, h = size
					window.recreate(sf.VideoMode(w, h), "sfeMovie for Python", sf.Style.FULLSCREEN)
					movie.resize_to_frame((0, 0, w, h))
				else:
					window.recreate(sf.VideoMode(640, 480), "sfeMovie for Python")
					movie.resize_to_frame((0, 0, 640, 480))
					
	window.clear()
	window.draw(movie)
	window.display()
	
