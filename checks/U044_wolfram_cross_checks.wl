(* Stateless exact corroboration only; universal proofs are in U044 note. *)
Module[{tt,ss=1/2,ll=4,naa,ncc,nn,dd,cc,zz,mm,gg,bb,lap,pp1,pp2},
 naa=ll-1; ncc=ll; nn=naa+ncc;
 dd=ConstantArray[0,{ll-1,nn}];
 Do[dd[[rr,rr]]=ss; dd[[rr,naa+rr]]=1; dd[[rr,naa+rr+1]]=-1,{rr,1,ll-1}];
 cc=ConstantArray[0,{ll,nn}];
 Do[If[rr+1<=ll-1,cc[[rr+1,rr+1]]=cc[[rr+1,rr+1]]+1];
    If[rr>=1,cc[[rr+1,rr]]=cc[[rr+1,rr]]-1];
    cc[[rr+1,naa+rr+1]]=cc[[rr+1,naa+rr+1]]-ss,{rr,0,ll-1}];
 zz=Transpose[NullSpace[dd]];
 mm=Transpose[zz].Transpose[cc].cc.zz; gg=Transpose[zz].zz;
 pp1=Factor[Det[mm-tt gg]/Det[gg]];
 bb=ConstantArray[0,{ll-1,ll}]; Do[bb[[rr,rr]]=-1;bb[[rr,rr+1]]=1,{rr,1,ll-1}];
 lap=Transpose[bb].bb;
 pp2=Factor[Det[lap+ss^2 IdentityMatrix[ll]-tt IdentityMatrix[ll]]];
 <|"LongitudinalCharpolyResidual"->Factor[pp1-pp2],
   "ScaledResolventResidual"->FullSimplify[1/(x+y)-(1/x)/(1+y/x),Assumptions->{x>0,y>0}],
   "ExponentDeltaEll2"->3/26,"ExponentDeltaEll3"->1/26,"ExponentDelta2Ell2"->5/13|>
]
