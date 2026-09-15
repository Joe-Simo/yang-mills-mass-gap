(* Stateless exact corroboration; no independent full-proof verification. *)
Clear[x,z,nu,r,b,l,u];
rr = Sqrt[1+((nu+1/2)/z)^2]-(nu+1/2)/z;
<|"Version"->$Version,
"RiccatiRootResidual"->FullSimplify[rr^2+(2nu+1)rr/z-1,Assumptions->{z>0,nu>0}],
"ScaleMonotonicityResidual"->FullSimplify[D[ArcSinh[x]-x/Sqrt[1+x^2],x]-x^2/(1+x^2)^(3/2),Assumptions->x>0],
"CompleteCharacterTail"->Sum[(l+1)^2/27^l,{l,1,Infinity}],
"TailBelowQuarter"->(709/4394<1/4),
"TiltedBridgeTVUpper"->Together[((5/3)(24/23)-1)/((5/3)(24/23)+1)],
"WeightedInfluenceUpper"->12(1/192)8,
"SusceptibilitySlack"->Factor[256b/3-16(4b-1)/(1-(4b-1)/(16b))],
"WeightedTimeSum"->FullSimplify[2 Sum[x^u,{u,0,b-1}]/(1-x^b/2)-1,Assumptions->{b>0,x>1}],
"BlockBenchmarks"->Table[{z,Ceiling[3Max[1,z]],1/(192Ceiling[3Max[1,z]])},{z,{1/2,2,8,32,128}}]|>
