import sys
from LebwohlLasher_vectorization_cython import main

ITERATIONS = 50 
SIZE = 50
TEMPERATURE = 0.5
PLOTFLAG = 1

main("LebwohlLasher", ITERATIONS, SIZE, TEMPERATURE, PLOTFLAG)