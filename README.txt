block puzzle wizard

by monkeycoder

goal: create a algorithm/program to automatically solve "put the shapes into the grid" type puzzles

requirements:
    > a class for the board
    > a class for shapes
    > a class to handle interaction between shapes and board (game master)
    > a class/function that does the puzzle
    
    > for some challenge make a window to display all this. for the fun of making windows

the solving method in theory:

    #FROM BEGINNING OF PROJECT, DOESNT EXACTLY MIMIC MODERN IMPLEMENTATION

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



class structure:

    SHAPES:
        the "shape" class is a class that defines a subset of a "bounding grid" that makes it's form. for example:

        ..#
        ..#
        ###

        this shape above is a "backwards L" shaped by "#", in a 3x3 grid, filled by ".". this is the simple way I will
        be defining shapes. so the class would be defined by:
        
            >a grid of x by y size, who's data is correctly done in.
            >the shaping symbol
            >the filling symbol
        
    BOARD:
        the "board" is a grid who cares about what is empty or full. basically meaning it will share some concepts
        with Shape. it will require:

            >a grid to store everything
            >the filling symbol (for empty spots)

        the reason it lacks a shaping symbol is because you will be cramming in shapes, so 

FINAL RESULT:
    a game for the user to play where they can try the block puzzle for themselves. 
    the wizard is also an option (maybe a button) they user can press to have it solve the puzzle
    for them. it will have a nice GUI done in py window or whatever its called.

    the program should have some man made built in puzzles (tailor made)
    it should also have a way to generate random puzzles


finding from study:

    first iteration that did work took way to long to find a valid RESULT

    second iteration used some refactoring that made it so placing a block saves the position

    third iteration fixed a bug that was slowing the computing process (accumulator conversion fuck up)

    i learned alot about numbers

    i can possibly explain everything as just the sum of sums, this whole thing was really
    a whole lot of math and addition

    the order of which you feed the blocks in a puzzle file effects
    how fast the computer can figure it out

    the computer will always eventually figure out a solution, the length
    of time it takes will be heavily changed by order of blocks in file

    giving the computer an unsolveable puzzle will more than likely make it loop
    forever

    time complexity of moving an already placed block:
        
        imagine with already placed block N and we are trying to place block
        N + 1. N + 1 fails to place, so we increment N's accumulator once and 
        replace N. lets assume that no matter where we put N, we need to move
        N - 1 to a new spot for the correct placements. that would mean we would
        have to fully accumulate N to determine it's unplaceable and we must go back
        to N - 1. this is only a simple example of a real problem with this algorithm

        the order of shapes in the line can cause an earlier block to be in such a 
        bad place that later blocks will be stuck incrementing for an eternity until
        we can address the ealier block.

        imagine we placed block 1, the first block. then, we place block 2,3,4... up
        to N. N + 1 fails to place; so we lift N, and increment by 1 and try again.
        suppose block 1 is in such a bad spot that it is required to be moved. the algorithm
        will have to fully shift N out to move N-1 once, just to place N again, just to 
        remove it and move N-1 once more. like the worlds slowest counter just to get to
        N - 2 you would have to increment N - 1 fully, which is a herculian task as N would
        be required to increment fully.

        this problem block that I will call the "selfish little fuck at the beginning" (or SLFatB)
        is the reason why the order of which you put blocks in the puzzle blocks in the TXTs
        affects the speed of the calculation so dramatically. 

a change in approach:

    originally I had a memory stack of old gamegrids saved instead of the accumulator solution
    this is because it followed the same general idea of:

    "if the current block is unplaceable, remove the previous block and move that"

    the previous approach took that idea in a direct fashion. the main issue with the memory
    stack was that the top thing on the stack was a ditto of the current board, which is the main
    problem. it led to an infinite loop where it would undo a move, just to do the exact fucking thing
    even with an incrementing value for movement, that was bust too. the accumulator in the older approach
    was just 1 value, not multiple for each block respectively. obviousely (with the power of foresight)
    having one shared accumulator sucked for remembering where each block wanted to be. so I now used
    multiple accumulators.

the solving algorithm used now:

    (written in psudo-code)

    accumulators = dict()

    while(not all blocks used)
        index = get_unused_block_from_list()
        
        if index not in accumulators:
            accumulators.update(index:0)
        
        broken_accumulator = break_down_accumulator(accumulators,puzzle.dimensions)
        
        worked = jam_puzzle_block_in(puzzle,index,broken_accumulator)

        if worked = false
            remove_block()
            accumulators[index - 1] ++
            accumulators[index] = 0
        else:
            accumulators[index] = reassemble_acummulator(rotation,xmove,ymove,puzzle.dimensions)

    NOTE: an admittedly simple algorithm but it gets the job done.

what are the accumulators used for?

    the accumulators are used to keep track of the transformation done on A
    shape as a single value (int). this is useful for 2 reasons:

    1. to change the transformation done, increment accumulator
    2. saves on having to do a bunch of indexing nonsense for a result

    here is a basic break down of how accumulators store and unstore
    the trasnformation value.
    
    lets say we rotated a block 1 time, moved it 2 times right, and 
    3 times down. so it's RXY (rotation,Xmove,Ymove) would look like:

    123

    to turn that into an accumulator value we must have a conversion rate
    between transformations. for me it went as follows:

    4 rotations = 1 Xmove
    N Xmove = 1 Ymove

    where N is the width/slots/columns of the grid. so taking our
    RXY of 123 and converting it by simple addition:

    1R + 2X * 4R + 3Y * NX * 4R = accumulator

    Y is as valuable as NXs which by themselves are as valuable as 4R
    X is as valuable as 4R which by themselves are as valuable as 1R
    1R is 1R

    this makes the ammount of rotations the basic baseline for accumulator

    lets actually solve for the above problem, lets say the grid has 5 columns:

    1R + 2 * 4R + 3 * 5 * 4R = 1 + 8 + 60 = 69 

    so the accumulator has a value of 69. to convert back into transformations
    we would do what we did in reverse. though, to be frank, I just used a counting
    function to do it. just as 10 pennies make a dime, NX makes a Y. so if you simple
    count a tally, you will get the resulting transformations. 

    in plain english I just took the number, in this case 69, and incremented R by 1
    if R equalled 4, increment X, if X equalled N, increment Y

    thats the long and short of it. accumulators made remembering the location of
    previous block placements easy, and not reliant on saving previous game states.
    the use of accumulators also saves on memory, instead of saving a whole game_grid,
    only an int was saved. the only catch being I must translate that int back into an
    RXY to be used.
