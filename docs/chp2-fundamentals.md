
the first section covers using the accumulators, the conditional skip line op, and handling basic i/o including separators. the first important code is on page 21 and included here as [pg21.mac](../msc/to-tape/pg21.mac). it multiplies two one or two digit decimal numbers and the emphasis is on understanding exactly what is happening in the accumulators, mentally, on paper, and in ddt. so this is an excellent time to work with ddt.

meanwhile, we're also curious about the small errors accumulating in algebr.mac relative to algebr.for since the fortran version is clearly a slightly better match with feynman's table 22-3. the differences are so small that it seems to have to be small rounding effects, but why? in the assembly the arithematic is done by opcodes. in the fortran by language functions. it seems the language functions have better numerical properties? a possibility is the fortran is getting double precision and the assembly is single.

    .ex algebr.for
    FORTRAN: ALGEBR
    0.99999   0.00450
    0.99996   0.00900
    0.99984   0.01800
    0.99935   0.03599
    0.99741   0.07194
    0.98965   0.14350
    0.95881   0.28404
    0.83865   0.54468
    0.40666   0.91358
    -0.66926   0.74304

    .ex algebr.mac
    MACRO:	.MAIN
    .99997 .00449
    .99992 .00899
    .99977 .01799
    .99923 .03598
    .99717 .07192
    .98917 .14343
    .95789 .28376
    .83704 .54363
    .40510 .91010
    -.66417 .73737
