.. py:module:: sfemovie

sfeMovie binding
================
This binding is made of only one class :class:`Movie`. You can play 
movie with it.




.. class:: Movie

   :class:`Movie` allows you to play movies in sfml applications.

   Usage example::

      # load the video
      try:
          movie = sf.Movie.from_file("some_movie.ovg")
          
      except IOError: exit(1)
      
      # start the movie
      movie.play()
      
      # display the current frame
      window.draw(movie)
      window.display()
      
   .. classmethod:: from_file(filename)
   
      Attemps to open a media file (movie or audio)
   
      Opening can fails either because of a wrong filename, or because you tried to open a movie file that has unsupported video and audio format.
      
      :raise: :exc:`IOError` - If loading failed.
      :param str filename: Path of the music file to open
      :rtype: :class:`Movie`
      
   .. method:: play()
   
      Play the movie.
      
   .. method:: pause()

      Pauses the movie playback. If the movie playback is already 
      paused, this does nothing, otherwise the playback is paused.
   
   .. method:: stop()
   
      Stop the movie.
      
   .. attribute:: has_video_track
   
      Returns whether the opened movie contains a video track (images) 

      :return: **True** if the opened movie contains a video track, **False** otherwise
      :rtype: boolean
      
   .. attribute:: has_audio_track
   
      Returns whether the opened movie contains a audio track (images) 

      :return: **True** if the opened movie contains a audio track, **False** otherwise
      :rtype: boolean
      
   .. attribute:: volume
   
      The sound's volume (default is 100) 
      
      :rtype: integer
      
   .. attribute:: duration
   
      The duration of the movie.
      
      :rtype: :class:`sfml.system.Time`
      
   .. attribute:: size
   
      The size (width, height) of the movie. 
      
      :rtype: :class:`sfml.system.Vector2`
   
   .. method:: resize_to_frame(frame[, preserve_ratio=True])
   
      Scales the movie to fit the requested frame.

      If the ratio is preserved, the movie may be centered in the given 
      frame. Thus the movie position may be different from the one you 
      specified. 
      
      :param sfml.graphics.Rectangle frame: The target frame in which you want to display the movie
      :param boolean preserve_ratio: **True** to keep the original movie ratio, **False** otherwise
      
   .. attribute:: framerate
   
      The amount of video frames per second.
      
      :rtype: float
      
   .. attribute:: sample_rate
   
      The amount of audio samples per second.
      
      :rtype: integer
      
   .. attribute:: channel_count
   
      The count of audio channels. 
      
      :rtype: integer
      
   .. attribute:: status

      The current status of the movie.
      
      :rtype: integer
   
   .. attribute:: playing_offset
   
      The current playing position in the movie. 
      
      :rtype: :class:`sfml.system.Time`
      
   .. attribute:: current_frame

      Returns the movie texture currently being displayed. The returned texture is a texture in VRAM

      .. note::

         Although the returned texture reference remains the same, :attr:`current_frame` must be called for each new frame until you also use **draw()** ; otherwise the texture won't be updated.

      If the movie has no video track, this returns an empty texture. 

      :return: The current image of the movie 
      :rtype: :class:`sfml.graphics.Texture`
