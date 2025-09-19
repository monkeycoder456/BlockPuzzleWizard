"""
    This file was made by MonkeyCoder456 on Github
    
    A bunch of useful descrete structures for use. these are mainly just classes made for the hell of it.
    Updates will basically always be pending.

"""

class Matrix:
    """A class that represents the typical grid, bunch of rows and columns
        each point is initiated upon creation, so no holes.
        functionally graph paper.
        this ain't swiss cheese! all grids is either a square or a rectangle.

        NOTE: 
        THE SLOTS WOULD BE THE X!! FOR THEY ARE THE COLUMNS
        THE ROWS WOULD BE THE Y!! FOR THEY ARE THE ROWS

        NOTE: DO NOT, I REPEAT, DO NOT MISTAKE COLUMNS FOR ROWS AND ROWS FOR COLUMNS. MATRIX NUMBER OF ROWS (Y), MATRIX[0] NUMBER OF COLUMNS (X)

        Attributes:
            matrix (list[list]): the matrix itself
            rows (int): rows in grid
            columns (int): columns in grid
    
    """
    def __init__(self, rows : int, slots : int, defualtFiller = '#'):
        """Makes your grid. if you don't bother with defualt filler
            it will be just '#'.

            Args:
                rows (int): rows of grid.
                slots (int): columns of grid.
                defualtFiller (any): what the grid should be filled with to begin with.
        
        """
        self.matrix = []
        self.rows = rows
        self.columns = slots
        for row in range(1,rows+1):
            self.matrix.append([])
            for slot in range(1,slots+1):
                self.matrix[row-1].append(defualtFiller)

    def __str__(self) -> str:
        """Prints the grid in a pretty manner. for a more "classic" (left aligned) print
            use fancyprint()

            Returns:
             str: centered grid into terminal
        """
        stringy = ''
        for row in enumerate(self.matrix):
            rowwy = ''
            if row[0] != 0: 
                stringy += '\n'
            for slot in enumerate(self.matrix[row[0]]):
                rowwy += str(slot[1]) + '  '
            rowwy = f"{rowwy : ^100}"
            stringy += rowwy
        stringy += '\n'
        return stringy
    
    def replace(self, target, new) -> None:
        """locates all target data, and replaces them with new data
        
            TODO: make a proper description of this diddy-blud"""
        
        government_officals = self.scanGridSeveralSR(target)

        for head in government_officals:
            self.writeToPointSR(new,head)

    def getStats(self) -> list:
        """Gives you the rows and columns of the grid. you can access
            these directly from the object's atributes
        
            Returns 
            list: [rows, columns]
        """
        return len(self.matrix), len(self.matrix[0])

    def archaicPrint(self) -> None:
        """Prints the matrix in a crude manner, this means you see the 
            ugly list braces and commas. this is mainly here for 
            legacy purposes as my first printing method for matrix.
        """
        for row in self.matrix:
            print(row)
        print()
    
    def fancyPrint(self) -> None:
        """Prints in a more refined manner, best used for user view.
            This print method is now redundant with __str__ being a thing.
            This method was written before I could figure out a good way to
            write a __str__. also here for legacy purposes.

        
        """
        for row in enumerate(self.matrix):
            if row[0] != 0: 
                print()
            for slot in enumerate(self.matrix[row[0]]):
                print(slot[1], end = '  ')
        print('\n')

    def writeToPoint(self, obj : any, coord : tuple) -> None:
        """Writes "obj" to the specifed coordinate. the coordinates
            begin at the top left. the origin is at the TOPLEFT.
            keep in mind indices begin at 0! 
            coordinates are written as (row,column).

            Args:
                obj (str) : str you want to write.
                coord (tuple) : coordinates you want to write to (ROW, COLUMN).
        """
        self.matrix[coord[0]][coord[1]] = obj

    def writeToPoints(self, obj : any, coord_bunch : list) -> None:
        """Writes "obj" to the specifed coordinates. the coordinates
            begin at the top left. the origin is at the TOPLEFT.
            keep in mind indices begin at 0! 
            coordinates are written as (column,row).

            Args:
                obj (any) : data you want to write.
                coord_bunch (list) : coordinates you want to write to (COLUMN, ROW).
        """
        for point in coord_bunch:
            self.writeToPointSR(obj, point)

    def writeToPointSR(self, obj : any, coord : tuple) -> None:
        """Writes "obj" to the specifed coordinates. the coordinates
            begin at the top left. the origin is at the TOPLEFT.
            keep in mind indices begin at 0! 
            coordinates are written as (column,row).
            this is primarly here if you want to use the (x,y) system instead.
            use this now on for newer code/programs

            Args:
                obj (str) : str you want to write.
                coord (tuple) : coordinates you want to write to (COLUMN, ROW).
        """
        self.matrix[coord[1]][coord[0]] = obj

    def fillToRow(self, obj : any, row : int) -> None:
        """Fills a whole row with one string only, basically drawing a line.
            Indexes begin at 0.
        
            Args:
                obj (str): str you want to write.
                row(int): the row you want to fill.
        """
        for slot in enumerate(self.matrix[row]):
            self.matrix[row][slot[0]] = obj
    
    def fillToColumn(self, obj : any, column : int) -> None:
        """Fills a whole column with one string only, basically drawing a line.
            Indexes begin at 0.
        
            Args:
                obj (str): str you want to write.
                column(int): the column you want to fill.
        """
        for row in enumerate(self.matrix):
            self.matrix[row[0]][column] = obj
    
    def brushFill(self, brush_strokes : tuple) -> None:
        """ allows for a more creative approach to filling arrays
            a "brush stroke" is defined as follows:
                * symbol you want (any)
                * is it a horozontal or vertical stroke? (0 H or 1 V)
                * which row/colum (int)
            
            all of which is bundled together via TUPLES
            
            for some instances it is more tact then using "write to points!!
            
            Args:
                brush_strokes(list): a list of tuples defining strokes"""
        for stroke in brush_strokes:
            if stroke[1] == False:
                self.fillToRow(stroke[0], stroke[2])
            else:
                self.fillToColumn(stroke[0], stroke[2])

    def feedToRow(self, lister : list, row : int) -> None:
        """Feeds specific data in the form of a list into a row. replacing the target row.
            The only catch is that the feeded list MUST be of same length to the target list, as to prevent size issues.
            indices start at 0.
            
            Args:
                Lister (list): List you want to insert into the matrix
                row (int): the row you are inserting too.
        """
        if len(lister) == len(self.matrix[row]):
            #self.matrix[row] = lister.copy
            for slot in enumerate(self.matrix[row]):
                self.matrix[row][slot[0]] = lister[slot[0]]
        else:
            print('the row and the inserting row are not equal length!! no change made...\n')

    def feedToAll(self, arrayArray : list[list]) -> None:
        """Feeds specific data in the form of an array of arrays to the grid, overwritting it entirely.
            there is a catch : if the inputted array of arrays does not match the size of the matrix
            exactly, than nothing will happen.

            Args:
                arrayArray (list[list]) : an array of arrays you want to overwrite the current matrix with.
        """
        if (len(arrayArray) == len(self.matrix))and(len(arrayArray[0]) == len(self.matrix[0])):
            for lane in enumerate(arrayArray):
                self.matrix[lane[0]].clear()
                for obj in lane[1]:
                    self.matrix[lane[0]].append(obj)
        else:
            print('the matrix you are trying to feed doesn\'t match the size of the matrix. no changes made...')

    def feedtoColumn(self, lister : list, column : int) -> None:
        """Feeds specific data in the form of a list into a column. replacing the target column.
            The only catch is that the feeded list MUST be of same length to the target list, as to prevent size issues.
            indices start at 0.
            
            Args:
                Lister (list): List you want to insert into the matrix
                column (int): the column you are inserting too.
        """
        if len(lister) == len(self.matrix):
            for row in enumerate(self.matrix):
                self.matrix[row[0]][column] = lister[row[0]]
        else:
            print('the column and the inserting column are not equal length!! no change made...\n')

    def duple(self) -> list[list]:
        """Creates a  deep copy of the original matrix, this copy is also a matrix.
            because of this methods age it uses the writetoPoint() method.

            Returns:
                Matrix: a deep copy of your matrix
        """
        height = len(self.matrix)
        length = len(self.matrix[0])
        mimic = Matrix(height, length)

        for row in enumerate(self.matrix):
            for slot in enumerate(row[1]):
                mimic.writeToPoint(slot[1],(row[0],slot[0]))
        return mimic
    
    def iterable(self) -> list[list]:
        """Creates an iterable version of the matrix, creating a literal list of lists. this method
            was made because I struggled to realize you can access the matrix directly, so I used this method
            for iterating over the matrix. if you do not want to access matrix directly and only want a copy
            to iterate through this is your best bet.

            Returns
                list[list]: a list of lists where each list in the list is a row.
        """
        mimic = []
        for row in self.matrix:
            mimic.append(row)
        return mimic

    def scanGridSingleJR(self, target : any) -> tuple:
        """Scans the grid for the first instance of your target. the scan goes ROW BY ROW, one after another.
            once the target is found it returns a tuple. returned coordinates are in (ROW,COLUMN) <-- !!
            if it cannot find the target it returns an empty tuple.

            Args:
                target (str): thing you are looking for
            Returns:
                tuple: coordinates of target in (row,column)
        """

        for row in enumerate(self.matrix):
            for slot in enumerate(row[1]):
                if slot[1] == target:
                    return (row[0],slot[0])
        else:
            return ()

    def scanGridSingleSR(self, target : any) -> tuple:
        """Scans the grid for the first instance of your target. the scan goes ROW BY ROW, one after another.
            once the target is found it returns a tuple. returned coordinates are in (column,row)/(x,y)
            if it cannot find the target it returns an empty tuple.

            Args:
                target (str): thing you are looking for
            Returns:
                tuple: coordinates of target in (x,y)
        """

        for row in enumerate(self.matrix):
            for slot in enumerate(row[1]):
                if slot[1] == target:
                    return (slot[0],row[1])
        else:
            return ()

    def scanGridSeveralJR(self, target : any) -> list:
        """Scans the grid for multiple instances of your target. the scan goes ROW BY ROW, one after another.
            once a target is found it is stored in a set. when finished scanning it returns a set of tuples in (ROW,COLUMN) <-- !!
            if it cannot find the target it returns an empty set.

            Args:
                target (str): thing you are looking for
            Returns:
                set : a set of tuples that are the locations of all targets written in (row,column)/(y,x)
        """
        hits = set()
        for row in enumerate(self.matrix):
            for slot in enumerate(row[1]):
                if slot[1] == target:
                    hits.add((row[0],slot[0]))
        else:
            return list(hits)

    def scanGridSeveralSR(self, target : any) -> list:
        """Scans the grid for multiple instances of your target. the scan goes ROW BY ROW, one after another.
            when an instance is found it is added to a set, when finished scanning it returns a set of tuples in (column,row)/(x,y)
            if it cannot find the target it returns an empty set.

            Args:
                target (str): thing you are looking for
            Returns:
                set : a set of tuples that are the locations of all targets written in (x,y)/(column,row)
        """
        hits = set()
        for row in enumerate(self.matrix):
            for slot in enumerate(row[1]):
                if slot[1] == target:
                    hits.add((slot[0],row[0]))
        else:
            return list(hits)

    def readRow(self, Row : int) -> list:
        """Returns a row as a list

            Args:
                Row (int) : the row you want data from
            
            Returns:
                list : your data
            
        """
        return self.matrix[Row]

    def readColumn(self, Column : int) -> list:
        """Returns a column as a list

            Args:
                Column (int) : the column you want data from
            
            Returns:
                list : your data
        """
        thing_to_return = []
        for row in enumerate(self.matrix):
                thing_to_return.append(self.matrix[row[0]][Column])

        return thing_to_return

    def readPoint(self, coords : tuple) -> any:
        """Returns data at point, coords are expected in (column,row)/(x,y) form

            Args:
                coords (tuple) : the point you want data from
            
            Returns:
                any : your data
        """
        return self.matrix[coords[1]][coords[0]]
            
    def examinePoint(self, obj : any, coord : tuple) -> bool:
        """Checks a point for specified data, mainly used by classes who want
            to peek into the matrix through a method. expects use of the (x,y) system.

            Args:
                obj (str): the string you want to check is there.
                coord(tuple): the spot you want to check.
            
            Returns
                bool: if the data matches

        """
        # print("inside S using coord {0}".format(coord))
        if obj == self.matrix[coord[1]][coord[0]]:
            return True
        else:
            return False

    def reverseRow(self, row: int) -> None:
        """reverses the desire row to have an opposite order
        
            Args:
                row (int): which row you want reversed"""
        self.matrix[row] = list(reversed(self.matrix[row]))
    
    def mirror(self) -> None:
        """reverses every row of the matrix"""
        for row in range(self.getStats()[0]):
            self.matrix[row] = list(reversed(self.matrix[row]))
    
    def flip(self) -> None:
        """flips the image top to bottom to bottom to top"""
        self.matrix = list(reversed(self.matrix))

    def subMatrix(self, topLeft : tuple, bottomRight : tuple) -> list[list]:
        """creates a submatrix from the current matrix. this sub matrix is a
        DEEP copy, so any writes to it, DO NOT write to the parent/super of this submatrix
        ALL MUST BE DONE IN (X,Y), (COLUMNS, ROWS)
        
        Args:
            topleft (tuple):  the top left bound of the submatrix
            bottomright (tuple): the bottom left of the submatrix
        Returns:
            submatrix (list[list]): enjoy"""
        
        new_columns = bottomRight[0] - topLeft[0] + 1
        new_rows = bottomRight[1] - topLeft[1] + 1

        # print(new_columns, new_rows)

        new_matrix = Matrix(new_rows,new_columns)

        #insert old data into new matrix.
        #to get the bounds, use list slicing to cut away at the old array
        #start with rows
        stamp = self.matrix[topLeft[1]:bottomRight[1]+1]
        # print(stamp)
        #then do columns
        for row in enumerate(stamp):
            stamp[row[0]] = row[1][topLeft[0]:bottomRight[0]+1]
        
        # print(stamp)
        # print(stamp)

        for row in enumerate(new_matrix.matrix):
            new_matrix.feedToRow(stamp[row[0]],row[0])
        return new_matrix
    
    @staticmethod
    def numberFlood(land : list[list], minvalue : int, maxvalue : int) -> list[list]:
        """Takes an array of arrays and creates a new one of same dimensions but filled with random numbers from 0 to 25.
            If you want to input a matrix, you must make it iterable compliant (use iterable method or pass matrix directly).

            Args:
                land (list[list]) : the matrix you want to have a copy of that is filled with random numbers
                minvalue : lowest number 
                maxvalue : highest number
            
            Returns:
                matrix: a matrix filled with random numbers
        """
        import random as r
        flooded = []
        for row in enumerate(land):
            flooded.append([])
            for slot in row[1]:
                flooded[row[0]].append(r.randint(minvalue,maxvalue))

        newWorld = Matrix(len(land), len(land[0]))
        newWorld.feedToAll(flooded)
        del r
        return newWorld
    
    @staticmethod
    def matrixToCSV(FileTOFIND = str, filenameNEW = 'newfile.txt', Iterableof2D = list[list], writeToAlreadyExistingFile = False) -> None:
        """takes the inputeed Array of Arrays and turns it into CSV file. if the
            second param is set to True it will write to the text file requested, appending
            to the end of it. make sure the file you want to edit is in the working directory!!
            SPECIFICALLY FOR THE CREATION OF A NEW FILE : at the first line of the file it will have the size of the grid declared, this is mainly so you can convert back with the
            CSVToMatrix() method.

            Args:
                filenameNEW (str): if writing to new file, the name you want.
                FileTOFIND (Str): if writing to an existing file, the file you want.
                Iterableof2D (list[list]) : your array of arrays to be converted.
                writeToAlreadyExistingFile (bool) :  a bool to dictate if you want to write to file that already exists, if left blank a new
                file will be made.
        """
        import csv
        import pathlib as p

        if writeToAlreadyExistingFile != True:
            with open(filenameNEW, 'w') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow([len(Iterableof2D), len(Iterableof2D[0])])
                csvwriter.writerows(Iterableof2D)
                csvfile.close()

            with open(filenameNEW, 'r') as newthing:
                stuff = newthing.readline().split(',')
                stuff[1] = stuff[1][0:-1]

                restof = newthing.readlines()

                index = 0
                for thing in restof:
                    if not(index % 2 == 0):
                        stuff.append(thing)
                    index += 1
                newthing.close()

            with open(filenameNEW, 'w') as evenNewerthing:
                evenNewerthing.write(stuff[0]+","+stuff[1]+"\n")
                for bobber in stuff[2:]:
                    evenNewerthing.write(bobber)
                evenNewerthing.close()

        else:
            pathnerd = p.Path(__file__).parent / FileTOFIND
            with open(pathnerd,"a") as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow([len(Iterableof2D), len(Iterableof2D[0])])
                csvwriter.writerows(Iterableof2D)
                csvfile.close()
        
        del p
        del csv

    @staticmethod
    def CSVToMatrix(File = str) -> list[list]:
        """takes a CVS or TXT file and converts the data into a matrix object. format the file in a way this function can properly interpret.
            line one of the file should contain only 2 numbers (ints) that serve as the declaration of the file size. an example would look like:

            1 | 20,15\\n

            here the matrix is being declared as having a size of 20 rows by 15 columns. and such the CSV below should be arranged in a 20 by 15
            fashion.

            Args:
                File (str) : the file you want read.

            Returns:
                matrix = your new matrix.
        """
        import pathlib
        pathnerd = pathlib.Path(__file__).parent / File
        lot = open(pathnerd, 'r')

        size = lot.readline().split(',')
        size[1] = size[1][0:-1]
        size = [int(i) for i in size]

        matrix = Matrix(size[0],size[1])

        for row in range(0, size[0]):
            line = lot.readline().split(',')
            if line == ['']:
                break
            #remove the newline char at the end
            if line[-1][-1] == "\n":
                line[-1] = line[-1][0:-1]
            #inserting each point one at a time
            for char in enumerate(line):
                matrix.writeToPoint(char[1],(row,char[0]))
        return matrix

    @staticmethod
    def rotate(grid: list[list], clock: bool) -> list[list]:
        """Creates a new Grid that is a version of the old one rotated once 90 degrees.
            This doesn't write to the old grid.
            Args:
                grid(list[list]): the grid you want rotated
                clock (bool): 0 = COUNTERCLOCKWISE , 1 = CLOCKWISE
            Returns:
                Matrix: the old matrix rotated clockwise once 90 degrees.
        """
        # newGrid = Matrix(len(self.matrix),len(self.matrix[0]))

        # rottoid = 0
        # for row in enumerate(self.matrix):
        #     newGrid.feedtoColumn(row[1],rottoid-1)
        #     rottoid -= 1 
        
        # return newGrid
        copy_grid = grid.duple()

        if clock == 0:
        #MIRROR = COUNTER CLOCKWISE ROTATION
            copy_grid.mirror()
        #FLIP = CLOCKWISE ROTATION
        else:
            copy_grid.flip() 



        newGrid = Matrix(grid.getStats()[1], grid.getStats()[0])

        for row in enumerate(copy_grid.matrix):
            newGrid.feedtoColumn(row[1],row[0])

        return newGrid

#begin work on this after alcazar becuase this one is a doozy
class graphicalmatrix(Matrix):
    """A class that represents the typical grid, bunch of rows and columns
        each point is initiated upon creation, so no holes.
        functionally graph paper.
        this ain't swiss cheese! all grids is either a square or a rectangle.
        this class allows for easier use of the turtle library with it's exclusive drawGrid() method.

        Attributes:
            matrix (list[list]): the matrix itself
            rows (int): rows in grid
            columns (int): columns in grid  
    """

    def __init__(self, rows : int, slots : int, defualtFiller = '#'):
        """Makes your grid. if you don't bother with defualt filler
            it will be just '#'.

            Args:
                rows (int): rows of grid.
                slots (int): columns of grid.
                defualtFiller (str): what the grid should be filled with to begin with.
        
        """

        self.matrix = []
        self.rows = rows
        self.columns = slots
        self.updateNeeded = False
        for row in range(1,rows+1):
            self.matrix.append([])
            for slot in range(1,slots+1):
                self.matrix[row-1].append(defualtFiller)

    def __str__(self) -> str:
        """Prints the grid in a pretty manner. for a more "classic" (left aligned) print
            use fancyprint()

            Returns:
             str: centered grid into terminal
        """
        stringy = ''
        for row in enumerate(self.matrix):
            rowwy = ''
            if row[0] != 0: 
                stringy += '\n'
            for slot in enumerate(self.matrix[row[0]]):
                rowwy += str(slot[1]) + '  '
            rowwy = f"{rowwy : ^100}"
            stringy += rowwy
        stringy += '\n'
        return stringy

    @staticmethod
    def numberFlood(land : list[list], minvalue : int, maxvalue : int) -> list[list]:
        """Takes an array of arrays and creates a new one of same dimensions but filled with random numbers from 0 to 25.
            If you want to input a matrix, you must make it iterable compliant (use iterable method or pass matrix directly).

            Args:
                land (list[list]) : the matrix you want to have a copy of that is filled with random numbers
                minvalue : lowest number 
                maxvalue : highest number
            
            Returns:
                graphicalmatrix: a graphical matrix filled with random numbers
        """
        import random as r
        flooded = []
        for row in enumerate(land):
            flooded.append([])
            for slot in row[1]:
                flooded[row[0]].append(r.randint(minvalue,maxvalue))

        newWorld = graphicalmatrix(len(land), len(land[0]))
        newWorld.feedToAll(flooded)
        del r
        return newWorld
    
    ##ALL THE BELOW STATICS FUNCTIONS ARE ASSISTANT FUNCTIONS AND SHOULD NOT BE TOUCHED
    @staticmethod
    def drawSquare(pen, color) -> list:
        """draws a square from the top left corner and ends at the top right. 
        intended to be used back to back in order to form grids. color is just the filler color.
        returns the corners of the squares as a list. ENDS WITH THE PEN UP"""
        pen.down()
        pen.fillcolor(color)
        pen.begin_fill()
        corners = []
        for i in range(4):
            pen.forward(50)
            pen.right(90)
            corners.append(pen.pos())
        pen.forward(50)
        pen.right(90)
        pen.left(90)
        pen.end_fill()
        pen.up()
        return corners

    @staticmethod
    def drawCross(crosser, corners) -> None:
        """draws a cross using the color of the pen currently, requires a list of four points."""
        crosser.up()
        crosser.goto(corners[0])
        crosser.down()
        crosser.goto(corners[2])
        crosser.up()
        crosser.goto(corners[1])
        crosser.down()
        crosser.goto(corners[3])
        crosser.forward(50)

    @staticmethod
    def rollback(drawer, origin: tuple) -> None:
        """Takes the turtle and shoves it back to the origin's X position. It is as if pressing new line.

            Args:
                drawer(turtle): what you want to orient.
                origin(tuple): the point you want to orient to.
        """
        drawer.up()
        drawer.setx(origin[0])
        drawer.right(90)
        drawer.forward(50)
        drawer.left(90)
        drawer.pencolor('black')
        drawer.fillcolor('black')
        drawer.width(6)
        drawer.down()

    @staticmethod
    def drawNA(crosser) -> None:
        """draws a defualt pattern (redbox with a big red X) for when there is no pallete color to represent the string. requires 2 turtles to work.

            Args:
            pen(turtle): the turtle responsible for drawing the box
            crosser(turtle): the turtle responsible for drawing the cross
        """
        crosser.color('red')
        graphicalmatrix.drawCross(crosser,graphicalmatrix.drawSquare(crosser, 'white'))
        crosser.color('black')

    @staticmethod
    def setUpTurt(background, gridwdith, gridheight) -> tuple:
        """sets up turtle for use. has the pen placed in the center
            using the default color and fillcolor. pen is UP"""
        import turtle as t

        windowWidth = gridwdith * 50
        windowLength = gridheight * 50
        
        t.bgcolor(background)
        t.setup(windowWidth * 2, windowLength * 2,0,0)
        t.tracer(0)
        t.resetscreen()
        
        #setting up the main drawing turtle "feather"
        
        feather = t.Turtle()
        feather.up()
        feather.speed(1)
        feather.width(6)
        feather.goto((-1*(windowWidth/2),windowLength/2))
        feather.color('black')
        origin = feather.pos()
        
        #we need this data for later
        return (origin, feather, t)

    def drawGrid(self, drawkey = {}, background = 'black', setupturtpackage = ()) -> None:
        """using python turtle it will draw the grid, centered in the window, in accordance to the supplied drawkey.
            a 'drawkey' is a dict that has keys as the grid's expected symbols, and the values are the names of valid
            turtle colors. an example is shown below:
            
            * DrawkeyTruth = { 1 : white, 0 : black } 
            
            if there are symbols in the grid that do not have a listed color in the drawkey, the spot will be filled in with a red box and a cross.
            drawkeys are best kept in a seperate file. turtle is imported at the calling of this method (as t).

            also the turtle.mainloop function is called so get all conditonals and other stuff setup before hand.
            
           Args:
                drawkey (dict) : the drawkey to define the colors you want to use.
                background (str) : the background color you want to use.
        """
        origin = setupturtpackage[0]
        feather = setupturtpackage[1]
        turr = setupturtpackage[2]
        
        for row in self.matrix:
            for slot in row:
                possiblecolor = drawkey.get(slot, 'NA')
                if possiblecolor != 'NA':
                    graphicalmatrix.drawSquare(feather, possiblecolor)
                else:
                    graphicalmatrix.drawNA(feather)
            graphicalmatrix.rollback(feather, origin)
        turr.mainloop()
    
    def drawagain(self, drawkey = {}, setTurtpackage = ()):
        setTurtpackage[1].reset()
        setTurtpackage[1].clear()
        setTurtpackage[2].tracer(0)
        for row in self.matrix:
            for slot in row:
                possiblecolor = drawkey.get(slot, 'NA')
                if possiblecolor != 'NA':
                    graphicalmatrix.drawSquare(setTurtpackage[1], possiblecolor)
                else:
                    graphicalmatrix.drawNA(setTurtpackage[1])
            graphicalmatrix.rollback(setTurtpackage[1], setTurtpackage[0])

class graph:
    """More custom made for graph theory and its troop of shinanigans. graphs are stored as adjecency list entries.

        Attributes:
            railway (dict) = the adjecency list saved as set.
            railwaySize (int) = the number of vertices the graph has.
    
    """
    def __init__(self):
        """Creates the graph, all graphs start empty."""
        self.railway = {}
        self.railwaySize = 0
    
    def __str__(self) -> str:
        """Makes a clear visual representation of the graph printing it in adjecency list form. the number at the bottom is the size of the graph

            Returns:
                str : your string of the graph.
        """

        stringy = ''
        stringy += f"{self.railwaySize : ^ 20}"
        stringy += '\n'
        for entry in self.railway:
            stringy += f"{entry : ^10}" + str(self.railway[entry])
            stringy += '\n'


        return stringy
    
    def addVert(self, nodeName : any, nodeConnections: list = [] ) -> None:
        """Adds a new vertex to your graph. has the optional argument of adding it with connections if you wish. THE CONNECTIONS MUST BE TO
            VERTICES THAT DO EXIST IN THE GRAPH ALREADY.

            Args:
                nodeName (any) : the name you want the new vertex to have
                nodeConnections (list) : the list of edges you want it to have upon creation.
        """
        self.railway[nodeName] = set()
        self.railwaySize += 1
        if nodeConnections != None:
            for node in nodeConnections:
                self.railway[nodeName].add(node)
                self.railway[node].add(nodeName)
    
    def addConnection(self, Node1 : any, Node2 : any) -> None:
        """Creates a new edge between the two requested vertices.

            Args:
                Node1 (any) : vertex you want to connect
                Node2 (any) : vertex you want to connect
        """
        self.railway[Node1].add(Node2)
        self.railway[Node2].add(Node1)
    
    def addArbitraryConnection(self, Node1 : any, Node2 : any) -> None:
        """ For directed graph functionality, this will add a connection reguardless of the
            existance of Node2. if Node2 does exist, then it still will not point back at
            Node1.

            Args:
                Node1 : the first vertice
                Node2 : the vertice you want the first one to point at
        """
        self.railway[Node1].add(Node2)
        
    def deleteVert(self, node : any) -> None:
        """Deletes a vertex and gets rid of the connects it had, if it had any.

            Atribbutes:
                node (any) : name of vertex you want to remove

        """
        self.railway.pop(node)
        self.railwaySize -= 1
        for rail in self.railway:
            self.railway[rail].discard(node)

    def deleteConnection(self, node1 : any, node2 : any) -> None:
        """Deletes a connection (edge) between two vertices. this will go
            Both ways for both vertices.

            Args:
                node1 : vertex to remove edge from.
                node2 : vertex to remove edge from.
        """
        self.railway[node1].discard(node2)
        self.railway[node2].discard(node1)

    def deleteArbitraryConnection(self, Node1 : any, Node2 : any) -> None:
        """ For directed graph functionality, this will delete a connection one way.
            more specifically Node1 will have it's edge with Node2 forgotten, while
            Node2 (if it exists) will keep its edge with Node1.

            Args:
                Node1 : the first vertice
                Node2 : the vertice you want the first one to forget
        """
        self.railway[Node1].discard(Node2)

    def getConnections(self, node : any) -> list:
        """Returns a list of neighbors the vertex has.

            Args:
                node (any) : Thing you want to check.
            Returns:
                list : A list of neighbors.
        """
        neighboors = self.railway[node]
        if len(neighboors) == 0:
            return None
        else:
            return list(neighboors)

    @staticmethod
    def matrixToGraph(matrix : list[list]) -> set:
        """Takes the inputted adjecency matrix and converts it into a Graph.
            This is a static utility method. an adjecency matrix is a truth table of 1s and 0s.

            Args:
                matrix : the adjecency matrix you want interpreted, expected as an array of arrays
            Returns:
                set : a brand new graph.
        """
        newGraph = graph()
        for row in enumerate(matrix):
            newGraph.addVert(row[0])
            for connection in enumerate(row[1]):
                if connection[1] == 1:
                    newGraph.addArbitraryConnection(row[0],connection[0])

        return newGraph

class alcazar:
    """
        A 3D graph represented as a tower with floors. 
        along with rows and columns, there are now pillars. which serve as a way to 
        see/effect one spot on several floors.

        Quirks:
            * for user sake, there is no 0'th floor on there end. if they want
            to get the data from the first floor, they must ask for floor 1.
            so basically everything is shifted 1 up from standard indexing.

            * some of alcazars functionality is reliant on the methods found
            in matrix. that means if there is a change in matrix, specifically
            to method names, refactoring must be done.


        Attribs:
        name (str) : A string of what the alcazar is named.
        alcazar (dict) : all floors are stored in corisponding dict entries.
        rows (int) : number of rows
        columns (int) : number of columns
        floors (int) : number of floors
    """

    def __init__(self, floors : int, rows : int, slots : int, name : str, defualtchar = '#'):
        self.name = name
        self.alcazar = {}
        self.rows = rows
        self.columns = slots
        self.floors = floors
        for floor in range(floors):
            self.alcazar.update({ floor : Matrix(rows, slots, defualtchar)})

    def __str__(self) -> str:
        """when the string of the tower is givin, it is givin in a very \"bombastic\" way."""
        stringy = ''
        stringy += f"{'ALCAZAR OF:' : ^100}\n"
        stringy += f"{self.name.upper() : ^100}\n"
        stringy += '\n'
        for floor in reversed(self.alcazar):
            stringy += f"{'floor' : >50} {floor + 1 : <50}\n"
            stringy += str(self.alcazar[floor])
            stringy += '\n'
        
        return stringy

    def getstats(self) -> tuple:
        """returns a bunch of stats on the tower as a tuple.
            written as (name, height, rows columns).

        Returns:
        stats (tuple) : your tuples highness.
        """
        return self.name,self.floors,self.rows,self.columns

    def archaicTower(self) -> None:
        """prints the tower in a more \"classic\" way."""
        for floor in reversed(self.alcazar):
            print(f'floor {floor}')
            self.alcazar.get(floor).archaicPrint()
    
    def fancyPrintTower(self) -> None:
        """prints the tower in a very \"bombastic\" way. redundant but here if needed."""
        print(f'alcazar of {self.name}')
        for floor in reversed(self.alcazar):
            print(f'floor {floor + 1}')
            self.alcazar.get(floor).fancyPrint()
    
    def archaicFloor(self, floor : int) -> None:
        """Prints a single requested floor. it prints a floor using the archaicPrint() method.

            Args:
            floor(int) : the floor you want to print
        """
        print(f'floor {floor}')
        self.alcazar.get(floor - 1, 'Called invalid Floor!!').archaicPrint()

    def fancyPrintFloor(self, floor : int) -> None:
        """Prints a single floor using the fancyPrint() method.

            Args:
            floor(int) : the floor you want to print.
        """
        print(f'floor {floor}')
        self.alcazar.get(floor - 1, 'Called invalid Floor!!').fancyPrint()

    def writeToPointFloor(self, floor : int, obj : any, coord : tuple) -> None:
        """For a specific floor, write to a specific point on said floor.
            BE WARNED WHEN INPUTTING COORDS THEY MUST BE IN (ROW, COLUMN).

            Args:
            floor (int) : the floor you want to write too
            obj (any) : the data you want to write
            coord (tuple) : coordinates you want to write to (ROW, COLUMN).
        """
        self.alcazar.get(floor - 1, 'Called invalid Floor!!').writeToPoint(obj, coord)

    def fillToRowFloor(self, floor : int, obj : any, row : int) -> None:
        """writes to a row, on a single floor, fills it with entirely one thing and one thing only

            Args:
            floor (int) : floor you want.
            obj (any) : data you want to write.
            row (int) : row you want to write too.
        """
        self.alcazar.get(floor - 1, 'Called invalid Floor!!').fillToRow(obj, row)

    def fillToColumnFloor(self, floor : int, obj : any, column : int) -> None:
        """writes to a column, on a single floor, fills it with entirely one thing and one thing only

            Args:
            floor (int) : floor you want.
            obj (any) : data you want to write.
            column (int) : column you want to write too.
        """
        self.alcazar.get(floor - 1, 'Called invalid Floor!!').fillToColumn(obj, column)

    def fillToPillar(self, obj : any, coord : tuple) -> None:
        """writes to a point, on every floor, writes only obj and thats it.

            Args:
            obj (any) : data you want to write.
            cords (tuple): "pillar" point you want to write too on every floor
        """
        for floor in self.alcazar:
            self.alcazar.get(floor).writeToPoint(obj, coord)

    def feedtoRowFloor(self, floor : int, lister : list, row : int) -> None:
        """Writes a list to a row, outright replaces it's contents, this method allows for more than just one any
            has the same catch as grid, the insterting list must be of equal length of existing row 

            Args:
            floor (int) : the floor you want to feed
            lister (list) : the data
            row (int) : the row you want to feed

        """
        if len(lister) == len(self.alcazar.get(floor-1, 'Called invalid Floor!!').iterable()[row]):
            self.alcazar.get(floor-1).feedToRow(lister,row)
        else:
            print('insering list not equal to existing list')
 
    def feedToColumnFloor(self,floor : int, lister : list, column : int) -> None:
        """Writes a list to a column, outright replaces it's contents, this method allows for more than just one any
            has the same catch as grid, the insterting list must be of equal length of existing column.
            the first index of the list will be at the top most index when inserted into the columns. 

            Args:
            floor (int) : the floor you want to feed
            lister (list) : the data
            column (int) : the column you want to feed

        """
        if len(lister) == len(self.alcazar.get(floor-1, 'Called invalid Floor!!').iterable()):
            self.alcazar.get(floor-1).feedtoColumn(lister, column)

    def feedtoPillarTower(self, lister : list, coord : tuple) -> None:
        """
            Writes a list to a pillar, outright replaces its contente, this method allows for more than just one any.
            because it is a pillar function we check hieght of tower for validity.
            inserting pillar is also fed in from BOTTOM UP, floor 1 gets index 0, so on!!
            COORDS ARE HANDLED IN (ROW, COLUMN)!!

            Args:
            lister (list) : "pillar" points you want to insert
            coord (tuple) : the coords you want to write to, (row, column) handling.
        """
        if len(lister) == len(self.alcazar):
            for floor in self.alcazar:
                self.alcazar.get(floor).writeToPoint(lister[floor], coord)
        else:
            print('inserting pillar is not the same size as existing pillar')
    
    def duple(self, name : str) -> dict[list[list]]:
        """creates a mew alcazar object identical to this one. this is a DEEP copy,
            so the return value is a new alcazar.

            Args:
            name (str) : the name for your new alcazar.

            Returns:
            mimic : your new alcazar.
        """

        height = len(self.alcazar)
        rows = len(self.alcazar.get(0, 'Called invalid Floor!!').iterable()[0])
        slots = len(self.alcazar.get(0, 'Called invalid Floor!!').iterable())

        mimic = alcazar(height, rows, slots, name)

        #copy over the floor data using the feedToRowFloor method, filling in row by row
        #for floor in mimic
        #for row in floor
        #also throw in an enumerate in there we will probably need it
        #gotta use plus 1 for feedToRowFloor because of how it is coded
        #must have copy() as to not have the two towers be linked in any way
        for floor in self.alcazar:
            for row in enumerate(self.alcazar[floor].iterable()):
                mimic.feedtoRowFloor(floor+1, row[1].copy(),row[0])
            
        return mimic

    def iterable(self) -> list[list[list]]:
        """
            Creates an iterable version of the alcazar, allowing for outsider methods/functions to view the alcazar, this method
            should be entirely reserved for viewing and not keeping tabs on the alcazar, that is what the duple method is for
            returns a list of lists of lists. when printing for yourself the bottom most floor is index 0, so it will be printed FIRST
            so everything will appear flipped but for methods/functions that will look through the alcazar they will see it right side up.

            Returns:
            mimic : your list of floors that have a list of rows that have a list of columns.
        """
        mimic = []
        for floor in self.alcazar:
            mimic.append(self.alcazar[floor].iterable())

        return mimic
