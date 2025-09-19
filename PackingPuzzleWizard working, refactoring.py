"""the solving method in theory:
    a rough idea of the method I will be using to solve the problem, along with describing the method i will use.

    when you place a block in the grid, what you effectivly did was make a smaller "problem" to be solved. asking
    "can i fit n-1 blocks into the grid." you can from there recursivly solve the problem using this. the issue is that
    one in real life can misplace a block and fail the puzzle early, requiring an undo and or possible total restart.
    the computer will handle it by placing blocks until it is stuck, if it can no longer place a block validly, then
    step backwards until it finds a moment where it could have played differently. this programs down fall is the 
    massive ammount of time it can take on larger puzzles. the program FOR NOW, cannot account for rotations of blocks,
    ONLY translations of the blocks on the grid.

    this is  DYNAMIC PROGRAMMING problem!!

    keep memory of previous plays in a LIST/STACK and have some variable to know our current plays. so there will
    be many remembered grids and arrays of blocks in som arrangement. though in practice, the LIST/STACK will just
    be bouncing in sizes as it runs through possibilities.

    basic frame:
    
    take a block
    can you put it into the grid?
    no?
        move it slightly and try again.
    no still?
        then there is no valid spot. return to previous incarnation
    yes?
        insert block and continue to next block to put

    mor refined frame:

    get puzzle

    look at the grid
    take a block
    put it in (moving it around to find a working location)
    write the current game state to stack
    cannot put block in?
        rotate block and check every possible spot
        cannot put block in still?
        go back a game state and change where you put the last block, and how
    continue until all blocked are used, or if it finds out the puzzle is impossible

"""
import Shape_GameGrid_PackingPuzzle as SGP


#consider making this class just inherate from puzzle

#this class needs some fundimental reworking
class PackingPuzzleWizard():
    """a class that WORKS WITH PUZZLES
    * IT DOESN'T OWN A PUZZLE\n
    LETS MAKE THAT CLEAR.\n
    THIS CLASS WORKS WITH PUZZLES TO SOLVE AND
    MANIPULATE THEM"""

    #get a block from the inputted puzzle to use
    @staticmethod
    def get_block_unused(puzzle : SGP.Packing_Puzzle) -> int:
        """get unused shape, returns -1 if all are used"""
        for shape in enumerate(puzzle.shape_used):
            if shape[1] == False:
                return shape[0]
        else:
            return -1

    #go back a game state in the puzzle, as we cannot do an action
    #do it as manually here
    # > remove the block, index
    # > remove the used flag, infrinced from index
    # > 

    @staticmethod
    def take_most_recent_block_out(puzzle : SGP.Packing_Puzzle):
        """takes the most recently block out, sets used to false as well"""
        recently_placed_block = PackingPuzzleWizard.get_block_unused(puzzle) - 1
        puzzle.remove_block(recently_placed_block) #already sets the used false
    
    #jam a block into grid by any means, saves the RXY used for insertion, and a copy of the grid
    #this is recursive until it works
    #NOTE: for the future, make this a while loop
    @staticmethod
    def jam_puzzle_block_in(puzzle : SGP.Packing_Puzzle, index,Rotate,Xmove,Ymove) -> bool:
            """returns false if fails, returns true if it worked
            \n if it failed the first time, it will continue to try until total failure\n
            also gives the values it used to get the job done"""
            done = puzzle.place_block(index,(Xmove,Ymove))
            if done == False:
                puzzle.rotate_block(index, 0)
                Rotate = Rotate + 1
                if Rotate == 4:
                    Rotate = 0 
                    Xmove = Xmove + 1
                    if Xmove >= puzzle.game_grid.columns:
                        Xmove = 0
                        Ymove = Ymove + 1
                        if Ymove >= puzzle.game_grid.rows:
                            return False, -1,-1,-1
            else:
                return True, Rotate,Xmove,Ymove
            return PackingPuzzleWizard.jam_puzzle_block_in(puzzle,index,Rotate,Xmove,Ymove)

    def jam_puzzle_counter(Rotate : int,Xmove : int,Ymove : int):
        """a test function for the previous counter algorithm"""
        print(Rotate,Xmove,Ymove)
        Rotate = Rotate + 1
        if Rotate == 4 :
            Rotate = 0 
            Xmove = Xmove + 1
            if Xmove == 5:
                    Xmove = 0
                    Ymove = Ymove + 1
                    if Ymove == 5:
                        return False
        PackingPuzzleWizard.jam_puzzle_counter(Rotate,Xmove,Ymove)

    def break_down_accumulator(accumulated : int, puzzle : SGP.Packing_Puzzle):
        """returns a tuple as:\n
        (rotatiom,Xmove,Ymove)
        """
        R_tally = 0
        X_tally = 0
        Y_tally = 0
        for num in range(accumulated):
            R_tally += 1
            if R_tally == 4:
                R_tally = 0
                X_tally += 1
                if X_tally == puzzle.game_grid.columns:
                    X_tally = 0
                    Y_tally += 1
        
        return(R_tally,X_tally,Y_tally)

    def reassemble_accumulator(R,X,Y, puzzle : SGP.Packing_Puzzle):
        """(R,X,Y) => accumulator"""
        sum  =  R
        sum += X * 4
        sum += Y * puzzle.game_grid.columns * 4
        return sum

    def reassemble_accumulator_counter(R,X,Y,testX):
        sum  = R
        sum += X * 4
        sum += Y * testX * 4
        return sum


    def break_down_accumulator_counter(accumulated,testX):
        R_tally = 0
        X_tally = 0
        Y_tally = 0
        for num in range(accumulated):
            R_tally += 1
            if R_tally == 4:
                R_tally = 0
                X_tally += 1
                if X_tally == testX:
                    X_tally = 0
                    Y_tally += 1

        return(R_tally,X_tally,Y_tally)

    #main

    #NOTE: each block will have it's own accumulator
    #use index as the key to retrieve your desired accumulator value
    #set the accumulator value to the proper location
    @staticmethod
    def solve_puzzle_loop(puzzle :SGP.Packing_Puzzle):
        """asumes the puzzle is possible"""
        print("one dot per 100 loops")
        print("working",end="")
        accumulators = dict()
        chugging = 0
        chugged = 0

        while(PackingPuzzleWizard.get_block_unused(puzzle) != -1):
            chugging = chugging + 1
            chugged = chugged + 1
            if chugging == 100:
                chugging = 0
                print(".",end="")
                # puzzle.show_game_grid()
            index : int
            broken_accumulator : tuple
            index = PackingPuzzleWizard.get_block_unused(puzzle)
            # print(puzzle.game_shapes[index])
            #attempt to add a new accumulator, if an accumulator key value already exists
            #for the block, then DO NOTHING, move on
            #if it doesn't, create a fresh accumulator value
            if not(index in accumulators):
                accumulators.update({index:0})
                
            broken_accumulator = PackingPuzzleWizard.break_down_accumulator(accumulators.get(index),puzzle)
            # print("the broken down accumulator is: {0}\nthe literal accumulator is: {1}".format(PackingPuzzleWizard.break_down_accumulator(accumulators.get(index),puzzle), accumulators.get(index)))
            # print("trying to place block \n{0}".format(puzzle.game_shapes[index]))
            worked = PackingPuzzleWizard.jam_puzzle_block_in(puzzle,index,*broken_accumulator)
            if worked[0] == False:
                PackingPuzzleWizard.take_most_recent_block_out(puzzle)
                accumulators.update({index - 1 : accumulators.get(index - 1) + 1})
                # print("previous block removed!!")
                accumulators.update({index: 0})
                # puzzle.show_game_grid()
            else:
                # print("generic print...")
                # puzzle.show_game_grid()
                # input()
                #this one line saves SO MUCH computational time
                accumulators[index] = PackingPuzzleWizard.reassemble_accumulator(worked[1],worked[2],worked[3],puzzle)
        print("\n")
        puzzle.show_game_grid()
        for acummulator in enumerate(accumulators):
            print("{0} accumulator used a value of: {1}".format(puzzle.game_shapes[acummulator[0]].SHAPING,accumulators.get(acummulator[1])))
        print("the solution was chugged for a total of {0} while loops.".format(chugged))
        pass

test = SGP.Packing_Puzzle_data.txt_to_data("mPuzzle.txt")
test = SGP.Packing_Puzzle(test.size,test.shapes)

for shape in test.game_shapes:
    print(shape)

PackingPuzzleWizard.solve_puzzle_loop(test)

# 69 = R 4 X 2 Y 3

# for medium grid (5x7) the dimensions would be wonky, check if the methods can handle that
# print(PackingPuzzleWizard.break_down_accumulator_counter(69,5))
# print(PackingPuzzleWizard.reassemble_accumulator_counter(1,2,3,5))