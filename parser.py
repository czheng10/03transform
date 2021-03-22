from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguments (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    script  = open(fname, 'r')
    content = script.read()
    conlist = content.splitlines()
    script.close()
    i = 0

    while i < len(conlist):
        c = conlist[i]   #current command

        #line
        if c == "line":
            coordlist = conlist[i+1].split(" ")
            add_edge(points, int(coordlist[0]),int(coordlist[1]),int(coordlist[2]),int(coordlist[3]),int(coordlist[4]),int(coordlist[5]))
            i+=2

        #ident
        elif c == "ident":
            ident(transform)
            i+=1

        #scale
        elif c == "scale":
            slist = conlist[i+1].split(" ")
            smatrix = make_scale(int(slist[0]), int(slist[1]), int(slist[2]))
            matrix_mult(smatrix, transform)
            i+= 2

        #translate
        elif c == "move":
            tlist = conlist[i+1].split(" ")
            tmatrix = make_translate(int(tlist[0]), int(tlist[1]), int(tlist[2]))
            matrix_mult(tmatrix, transform)
            i+= 2

        #rotate
        elif c == "rotate":
            rlist = conlist[i+1].split(" ")
            if rlist[0] == "x":
                rmatrix = make_rotX(float(rlist[1]))
            elif rlist[0] == "y":
                rmatrix = make_rotY(float(rlist[1]))
            elif rlist[0] == "z":
                rmatrix = make_rotZ(float(rlist[1]))
            matrix_mult(rmatrix, transform)
            i+= 2

        #apply
        elif c == "apply":
            matrix_mult(transform, points)
            i+= 1

        #display
        elif c == "display":
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
            i+= 1

        #save
        elif c == "save":
            clear_screen(screen)
            draw_lines(points, screen, color)
            savelist = conlist[i+1].split(" ")
            fileName = savelist[0]
            save_extension(screen, fileName)
            i+=2
        #quit
        elif c == "quit":
            break
