from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 112, 149, 225 ]
edges = []
transform = new_matrix()

parse_file( 'script', edges, transform, screen, color )
