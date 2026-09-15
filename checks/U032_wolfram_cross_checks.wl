(* Stateless exact corroboration, not a derivation of the Wilson theorem.
   Executed with a 20-second cap after an earlier limit-containing call warned. *)
Clear[t,q,r,m];
c=KroneckerProduct[{{4,1},{1,4}},{{4,1},{1,4}}];
h={t,1,1,t}; v=c.h;
kk=DiagonalMatrix[1/v].c.DiagonalMatrix[h];
f={1,0,0,-1}; lam=15t/(17t+8);
h0={1,2,3,5}; v0=c.h0; pi0=h0*v0/(h0.v0);
k0=DiagonalMatrix[1/v0].c.DiagonalMatrix[h0];
pp=Table[If[Quotient[i-1,2]==Quotient[j-1,2],
 pi0[[j]]/Total[pi0[[2Quotient[i-1,2]+{1,2}]]],0],{i,4},{j,4}];
qq=IdentityMatrix[4]-pp; dd=qq.k0.qq;
<|"Version"->$Version,
 "BatchEigenResidual"->Map[Together,kk.f-lam f],
 "BatchExcessOverSingle"->Factor[lam-3/5],
 "WeightedReversibilityResidual"->DiagonalMatrix[pi0].k0-Transpose[k0].DiagonalMatrix[pi0],
 "MemoryNotTruePowerResidual"->qq.k0.k0.qq-dd.dd-qq.k0.pp.k0.qq,
 "MemoryDifferenceTrace"->Tr[qq.k0.pp.k0.qq],
 "SingleRateRational"->(4-1)/(4+1),
 "BatchRateRational"->(16-1)/(16+1)|>
