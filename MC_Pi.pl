loop(0, NumTries, Inside) :- Result is 4*Inside/NumTries, writeln(Result), fail.
loop(N, NumTries, Inside) :- N>0, random(0.0, 1.0, X), random(0.0, 1.0, Y), 
    Distance is X*X+Y*Y, ( Distance < 1 -> Inside2 is Inside + 1 ; Inside2 is Inside), N2 is N-1,
    loop(N2, NumTries, Inside2).

piApproximation(N) :- loop(N, N, 0).