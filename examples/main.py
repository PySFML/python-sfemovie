import sfml as sf
import sfemovie as sfe

window = sf.RenderWindow(sf.VideoMode(640, 480), "sfeMovie for Python")

movie = sfe.Movie.from_file("some_movie.ogv")
movie.resize_to_frame((0, 0, 640, 480), True)

movie.play()

while window.opened:
	for event in window.events:
		# close window: exit
		if type(event) is sf.CloseEvent:
			window.close()
			
	window.clear()
	window.draw(movie)
	window.display()
	
