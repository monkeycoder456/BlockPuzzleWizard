import Structures as S

class Shape(S.Matrix):
    """A shape is a small grid which has "holes" in it, of course holes cannot exist in a matrix so
        the holes are simply marked by the filler. the shaping makes the bones of the shape giving it form
        these are meant for use in grid insertion in game."""
    def __init__(self, row : int, slots : int, defined_or_drawn = 0, shaping = "#", filler = ".", array_of_my_shape = [], predefined_shape = "small_square"):
        """list of predefined shapes:
            * back_L
            * forw_L
            * horse
            * comma
            * big_T
            * small_T
            * big_M
            * apple (full right)
            * bad_apple (full left)
            * 5_tall
            * 3_tall
            * small_L
            * small_back_L
            * small_square
            * small_S
            * small_Z"""
        self.SHAPING = shaping
        self.FILLER = filler
        #defined uses a special word, drawn uses the tuples
        #defined = 0, drawn = 1

        if defined_or_drawn == True:
            # print("drawn")
            super().__init__(row,slots,filler)
            #array of my shape is filled with TUPLES of coords
            self.writeToPoints(shaping,array_of_my_shape)   
        else:
            # print("predetermined")
            match predefined_shape:
                case "back_L":
                    super().__init__(3,3,filler)
                    self.brushFill([(shaping,1,2),(shaping,0,2)])
                case "forw_L":
                    super().__init__(3,3,filler)
                    self.brushFill([(shaping,1,0),(shaping,0,2)])
                case "horse":
                    super().__init__(2,3,filler)
                    self.brushFill([(shaping,0,0),(shaping,1,0),(shaping,1,2)])
                case "big_T":
                    super().__init__(3,3,filler)
                    self.brushFill([(shaping,1,1),(shaping,0,0)])
                case "small_T":
                    super().__init__(2,3,filler)
                    self.brushFill([(shaping,1,1),(shaping,0,0)])
                case "comma":
                    super().__init__(2,2,filler)
                    self.writeToPoints(shaping,[(0,0),(1,0),(0,1)])
                case "big_M":
                    super().__init__(3,3,filler)
                    self.writeToPoints(shaping,[(0,0),(1,0),(1,1),(2,1),(2,2)])
                    pass
                case "apple":
                    super().__init__(3,2,filler)
                    self.brushFill(([shaping,0,1],[shaping,0,2],[shaping,1,1]))
                case "bad_apple":
                    super().__init__(3,2,filler)
                    self.brushFill(([shaping,0,1],[shaping,0,2],[shaping,1,0]))
                case "5_tall":
                    super().__init__(5,1,filler)
                    self.fillToColumn(shaping,0)
                case "3_tall":
                    super().__init__(3,1,filler)
                    self.fillToColumn(shaping,0)
                case "small_L":
                    super().__init__(3,2,filler)
                    self.brushFill(([shaping,1,0],[shaping,0,2]))
                case "small_back_L":
                    super().__init__(3,2,filler)
                    self.brushFill(([shaping,1,1],[shaping,0,2]))
                case "small_square":
                    super().__init__(2,2,shaping)
                case "small_S":
                    super().__init__(2,3,filler)
                    self.writeToPoints(shaping,((1,0),(1,1),(0,1),(2,0)))
                case "small_Z":
                    super().__init__(2,3,filler)
                    self.writeToPoints(shaping,((0,0),(1,1),(1,0),(2,1)))
                case "smiley":
                    super().__init__(1,1,shaping)

    def getHoles(self) -> list:
        """returns a tuple of where all the holes are
            
            Returns:
                * list of points where the gaps are"""
        new = self.scanGridSeveralSR(self.FILLER)
        return new
    
    def getShape(self) -> list:
        """returns a tuple of where all the shape is
            
            Returns:
                * list of points where the shape is"""
        new = self.scanGridSeveralSR(self.SHAPING)
        return new
    
    def getShaping(self) -> str:
        return self.SHAPING
    
    @staticmethod
    def matrix_to_shape(matrix : S.Matrix, shaping : str, filler: str):
        """turn a matrix into a shape, assuming the matrix is an appropriate shape
            WARNING: this BRUTEFORCES a shape into existance"""
        problem = Shape(matrix.getStats()[0],matrix.getStats()[0],1,shaping,filler,[])
        problem.matrix = matrix.matrix
        return problem

class GameGrid(S.Matrix):
    """predetermined game grid sizes
        * 5x5 : small
        * 5x7 : medium
        * 7x7 : large

        for now the game grid will only be filled with blanks
        blanks are "."
        """
    def __init__(self, size : str, empty = "."):
        match size:
            case "small":
                super().__init__(5,5,".")
            case "medium":
                super().__init__(5,7,".")
            case "large":
                super().__init__(7,7,".")
        self.empty = empty


    def is_it_clear(self, shape:Shape, where:tuple) -> bool:
        """a checking function for if a shape can be placed at the desired location. where is the desired spot
            for the top left of the shape.

            NOTE:
                DOESN'T HAVE A FAILSAFE IF THE INSERTING SHAPE IS OUT OF THE BOUNDS!!!

            Args:
                * shape (Shape) : the shape you want to put into the matrix, should desireably have "." as it's blanks
                * where (tuple) : the coordinates of where you want to put the TOPLEFT OF THE MATRIX you want to place down, on the greater matrix.
                what this means is that the (0,0) of the placing shape, is going there, and the rest go reletivly onto it.
            Return:
                * 0 for success
                * 1 for failure"""
        
        #use a looping function which begins AND ends based on the "where" tuple.

        for row in enumerate(shape.matrix):
            for slot in enumerate(row[1]):
                my_x = where[0] + slot[0]
                my_y = where[1] + row[0]
                #NOTE: DO NOT, I REPEAT, DO NOT MISTAKE COLUMNS FOR ROWS AND ROWS FOR COLUMNS. MATRIX NUMBER OF ROWS (Y), MATRIX[0] NUMBER OF COLUMNS (X)
                if (my_x >=  len(self.matrix[0]) or my_y >= len(self.matrix)) or (my_x < 0 or my_y < 0):
                    return False
                # print("{0},{1}".format(my_x,my_y))
                # print(self.readPoint((my_x,my_y)), slot[1])
                if not(self.examinePoint(self.empty, (my_x,my_y))) and slot[1] == shape.SHAPING:
                    return False
        return True

    # this function should be intergated into matrix as a generic static function as this would prove useful
    def place_shape(self, shape:Shape, where : tuple):
        """a function for placing a block where you want to onto the grid
            returns 0 if it succeeds, returns 1 for failure
            
            Args:
                * shape (Shape) : the shape you want to put into the matrix, should desireably have "." as it's blanks
                * where (tuple) : the coordinates of where you want to put the TOPLEFT OF THE MATRIX you want to place down, on the greater matrix.
                what this means is that the (0,0) of the placing shape, is going there, and the rest go reletivly onto it.
            Return:
                * 0 for success
                * 1 for failure"""

        if self.is_it_clear(shape, where):
            for row in enumerate(shape.matrix):
                # print(row)
                for slot in enumerate(row[1]):
                    if slot[1] == shape.FILLER:
                        continue
                    my_x = where[0] + slot[0]
                    my_y = where[1] + row[0]
                    self.writeToPointSR(slot[1], (my_x,my_y))
            return True
        else:
            return False

class Packing_Puzzle():
    """a small class to contain the shape and grid puzzle. for ease of interface"""
    def __init__(self, grid_size : str, list_of_shapes : list[tuple]):
        """blah blah
        
        predetermined formating is ("apple", "#") drawn formatting is (int:rows, int:slots, "#", list:array_of_my_shape)


        ARGS:
            * grid_size (str) : the size of the grid, small/medium/large
            * list_of_shapes (list[tuple]) : the list of shapes for the puzzle, to give them over,
            have the list be full of predetermined shape init args (aka just a string and proper shaping), or drawn shape args (the whole shibang)
            """
        
        self.game_shapes : list[Shape]
        print(grid_size)
        #TODO : this is broke
        self.game_grid = GameGrid(grid_size,".")
        print(self.game_grid)
        self.game_shapes = []
        self.shape_used = []
        if type(list_of_shapes[0]) != Shape:
            for entry in list_of_shapes:
                if len(entry) == 2:
                    #do predetermined logic
                    self.game_shapes.append(Shape(0,0,0,entry[1],".",[],entry[0]))
                else:
                    #do drawn logic
                    self.game_shapes.append(Shape(entry[0],entry[1],1,entry[2],".",entry[3]))
                self.shape_used.append(False)
        else:
            for shape in list_of_shapes:
                self.game_shapes.append(shape)
                self.shape_used.append(False)

        print("Game ready!!")

    def show_game_state(self) -> None:
        """prints the game state"""

        print(self.game_grid)

        for shape in enumerate(self.game_shapes):
            print(shape[1])
            print(self.shape_used[shape[0]])

    def place_block(self, index : int, where : tuple) -> bool:
        """places a block into the gamegrid"""
        worked = self.game_grid.place_shape(self.game_shapes[index], where)
        if worked == True:
            self.shape_used[index] = True
        return worked
    
    def place_arbitrary_block(self, block : Shape, where : tuple) -> bool:
        """allows for any sort of block to be placed, if owned or not"""
    
    def remove_block(self, index : int):
        """removes a block from the game grid"""
        #make sure to update the used index
        target = self.game_shapes[index].SHAPING
        self.shape_used[index] = False
        self.game_grid.replace(target,self.game_grid.empty)
    
    def show_game_grid(self):
        print(self.game_grid)

    def rotate_block(self, index : int, left0_right1 : bool):
        """rotates the desired block once counter/clockwise"""
        self.game_shapes[index] = Shape.matrix_to_shape(S.Matrix.rotate(self.game_shapes[index],left0_right1),self.game_shapes[index].SHAPING,self.game_shapes[index].FILLER)

    def snap_shot(self) -> tuple:
        """returns a copy of the current game state of this packing puzzle. so it saves what it is.
        essentally acting like a save method, this exists for the wizard to have a hold on previous
        game states."""

        import copy

        return copy.deepcopy(self)

class Packing_Puzzle_data():
    """a glorified array to make life easier"""

    def __init__(data, size : int, shapes : list):
        data.size = size
        data.shapes = shapes

    @staticmethod
    def txt_to_data(path_to_file):
        """takes inputed directory route to make puzzle data
            ensure the path is correct, the location of this file will
            be used reletively, so make the file in the shared directory
            or in a sub folder
            
            returns a packing puzzle data"""
    
        import pathlib
        pathnerd = pathlib.Path(__file__).parent / path_to_file

        size : str
        shapesdata : list

        with open(pathnerd) as lot:
            lot = open(pathnerd, 'r')
            size = lot.readline() #size got
            size = size[0:-1]
            #get the rest of the file
            shapesdata = lot.read().split("\n")
            for sh in enumerate(shapesdata):
                shapesdata[sh[0]] = sh[1].split(",")
            print(shapesdata)
            for sh in enumerate(shapesdata):
                shapesdata[sh[0]] = Shape(0,0,0,sh[1][1],".",[],sh[1][0])
        
        return Packing_Puzzle_data(size,shapesdata)

# test = Packing_Puzzle("small",(("3_tall",1),("bad_apple",2),("small_T",3),("horse",4),("small_back_L",5),("small_square",6)))
# # test.show_game_state()
# marly : Packing_Puzzle_data
# marly = Packing_Puzzle_data.txt_to_data("ePuzzle.txt")
# garly = Packing_Puzzle(marly.size,marly.shapes)
# garly.show_game_state()
# test.show_game_state()

# test.place_block(0,(0,2))
# test.show_game_grid()
# test.place_block(1,(1,2))
# test.show_game_grid()
# test.rotate_block(2,1)
# test.place_block(2,(2,1))
# # best : Packing_Puzzle
# # best = test.snap_shot()
# test.show_game_grid()
# test.place_block(3,(2,0))
# test.show_game_grid()
# test.place_block(4,(3,2))
# test.show_game_grid()
# test.place_block(5,(0,0))
# test.show_game_grid()