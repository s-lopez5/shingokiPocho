%#const n = 1.
%size(n).
%row(1..n).
%col(1..n).




%Celdas y adyacentes
celda(c (X,Y)) :-row(X),col(Y). %celda (()) para decir pares ??,tb celda(c())??
adyacente(c(X,Y) ,c(X+1,Y)) :-celda(c(X,Y)), celda(c(X+1,Y)).
adyacente(c(X,Y) ,c(X,Y+1)) :-celda(c(X,Y)), celda(c(X,Y+1)).
adyacente(C,C') :- adyacente(C',C).

