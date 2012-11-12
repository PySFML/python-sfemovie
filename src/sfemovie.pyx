#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# pysfeMovie - a Python binding for sfeMovie
# Copyright 2012, Jonathan De Wachter <dewachter.jonathan@gmail.com>
#
# This software is released under the GPLv3 license.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

cimport dsystem, dgraphics, dsfemovie


cdef extern from "system.h":
	cdef class sfml.system.Vector2 [object PyVector2Object]:
		cdef public object x
		cdef public object y
		
	cdef class sfml.system.Time [object PyTimeObject]:
		cdef dsystem.Time *p_this
        
cdef extern from "graphics.h":
	cdef class sfml.graphics.Drawable [object PyDrawableObject]:
		pass
		
	cdef class sfml.graphics.RenderTarget [object PyRenderTargetObject]:
		cdef dgraphics.RenderTarget *p_rendertarget
		
	cdef class sfml.graphics.Texture [object PyTextureObject]:
		cdef dgraphics.Texture *p_this
		cdef bint               delete_this
		
cdef dsystem.IntRect rectangle_to_intrect(rectangle):
	l, t, w, h = rectangle
	return dsystem.IntRect(l, t, w, h)
		
cdef Time wrap_time(dsystem.Time* p):
	cdef Time r = Time.__new__(Time)
	r.p_this = p
	return r
	
cdef Texture wrap_texture(dgraphics.Texture *p, bint d=True):
	cdef Texture r = Texture.__new__(Texture)
	r.p_this = p
	r.delete_this = d
	return r


cdef class Movie(Drawable):
	cdef dsfemovie.Movie *p_this

	def __init__(self):
		raise UserWarning("Use a specific constructor")

	def __dealloc__(self):
		del self.p_this
		
	@classmethod
	def from_file(cls, filename):
		cdef dsfemovie.Movie *p = new dsfemovie.Movie()
		cdef char* encoded_filename	

		encoded_filename_temporary = filename.encode('UTF-8')	
		encoded_filename = encoded_filename_temporary
		
		if p.openFromFile(encoded_filename):
			return wrap_movie(p)
			
		del p
		# TODO: raise error and print message
		
	def draw(self, RenderTarget target, states):
		target.p_rendertarget.draw((<dgraphics.Drawable*>self.p_this)[0])

	def play(self):
		self.p_this.play()

	def pause(self):
		self.p_this.pause()
		
	def stop(self):
		self.p_this.stop()
		
	property has_video_track:
		def __get__(self):
			return self.p_this.hasVideoTrack()
			
	property has_audio_track:
		def __get__(self):
			return self.p_this.hasAudioTrack()
			
	property volume:
		def __get__(self):
			return self.p_this.getVolume()
			
		def __set__(self, float volume):
			self.p_this.setVolume(float)
			
	property duration:
		def __get__(self):
			cdef dsystem.Time* p = new dsystem.Time()
			p[0] = self.p_this.getDuration()
			return wrap_time(p)

	property size:
		def __get__(self):
			return Vector2(self.p_this.getSize().x, self.p_this.getSize().y)

	def resize_to_frame(self, frame, bint preserve_ratio=True):
		self.p_this.resizeToFrame(rectangle_to_intrect(frame), preserve_ratio)

	property framerate:
		def __get__(self):
			return self.p_this.getFramerate()
			
	property sample_rate:
		def __get__(self):
			return self.p_this.getSampleRate()
			
	property channel_count:
		def __get__(self):
			return self.p_this.getChannelCount()
			
	property status:
		def __get__(self):
			return self.p_this.getStatus()

	property playing_offset:
		def __get__(self):
			cdef dsystem.Time* p = new dsystem.Time()
			p[0] = self.p_this.getPlayingOffset()
			return wrap_time(p)

	property current_frame:
		def __get__(self):
			cdef dgraphics.Texture* p
			p = <dgraphics.Texture*>&self.p_this.getCurrentFrame()
			return wrap_texture(p, False)

cdef Movie wrap_movie(dsfemovie.Movie *p):
	cdef Movie r = Movie.__new__(Movie)
	r.p_this = p
	return r
