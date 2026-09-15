(* Exact finite corroboration; not an independent Wilson proof. *)
ClearAll[c,t,a,b,k,ratio,target,r,q,m];
c={{4,1},{1,4}}; k=c.DiagonalMatrix[{t,1}].c;
ratio=Together[k[[1,1]] k[[2,2]]/(k[[1,2]] k[[2,1]])];
target=(17/8)^2;
<|"Version"->$Version,"TwoStepKernel"->k,
"CrossRatioMargin"->Factor[target-ratio],
"EqualWeightPowerCheck"->Table[With[{v=MatrixPower[c,m]},Together[(v[[1,1]]-v[[1,2]])/(v[[1,1]]+v[[1,2]])-(3/5)^m]],{m,1,6}],
"TwoColumnsTwoStepsRate"->Together[2 (3/5)^2/(1+(3/5)^4)],
"AggregateBoundResidual"->Factor[a+b-(a+b)/(1+a b)],
"WeightedTailResiduals"->Table[Factor[r/(q-r)-Sum[(r/q)^k,{k,1,m}]-(r/q)^(m+1)/(1-r/q)],{m,1,6}]|>
