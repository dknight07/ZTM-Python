
Why Numpy is Faster than List?

This is due to fixed type.
Ex: For an Integer, using Numpy we could specify the memory size to store like int32, int16 etc
which are 4 bytes, 3 bytes etc.

For Lists, to store as built-in integer type it need to store 4 values like size,Reference count,Object Type
and Object Value which defaults to 8 bytes.

Reasons:
Faster to read less bytes of memory.
No Type Checking when iterating through Objects
Contiguous Memory for Numpy where as for Lists - The values are just pointers of reference
in the computer memory which are scattered randomly
Numpy has all the data side-by-side

Due to  Contiguous Memory 2 Advantages - (Single Instruction Multiple Data) Vector Processing
and Cache Utilization

Item Wise Computations.

Application of Numpy:
MATLAB Replacement
Plotting
Backend(Pandas)
ML
