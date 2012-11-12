#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# pySFML2 - Cython SFML Wrapper for Python
# Copyright 2012, Jonathan De Wachter <dewachter.jonathan@gmail.com>
#
# This software is released under the GPLv3 license.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from dsystem cimport Time, Vector2i, IntRect
from dgraphics cimport Texture

cdef extern from "sfeMovie/Movie.hpp" namespace "sfe":

	cdef enum Status:
		Stopped
		Paused
		Playing
		
	cdef cppclass Movie:
		Movie()
		bint openFromFile(char*&)
		void play()
		void pause()
		void stop()
		bint hasVideoTrack()
		bint hasAudioTrack()
		void setVolume(float)
		float getVolume()
		Time getDuration()
		Vector2i getSize()
		void resizeToFrame(IntRect)
		void resizeToFrame(IntRect, bint)
		float getFramerate()
		unsigned int getSampleRate()
		unsigned int getChannelCount()
		Status getStatus()
		Time getPlayingOffset()
		Texture& getCurrentFrame()
