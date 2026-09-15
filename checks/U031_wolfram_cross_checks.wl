(* Stateless exact corroboration only; the universal arguments are in the note.
   Run in a Wolfram Language kernel with a 30-second cap. *)
ClearAll[ep,z,c,q,r];
om={1,1,1,1}/2; u={1,1,-1,-1}/2;
v={1,-1,1,-1}/2; w={1,-1,-1,1}/2;
out[a_,b_]:=Outer[Times,a,b];
mat=out[om,om]+(out[u,u]+out[w,w])/4+(1-ep)out[v,v]
    +ep(out[u,v]+out[v,u])/4;
qq=IdentityMatrix[4]-out[om,om]-out[u,u];
red=Simplify[qq.mat.qq];
powers=NestList[Expand[red.#]&,IdentityMatrix[4],5];
nodes=Range[1,4]/10; slow=63/64;
ls=Table[Times@@Table[If[j==i,1,(slow-nodes[[j]])/(nodes[[i]]-nodes[[j]])],
                     {j,1,4}],{i,1,4}];
wt=1/(8(1+Max[Abs[ls]])); ws=ConstantArray[1/4,4]-wt ls;
<|"Version"->$Version,
  "CharacteristicPolynomial"->Factor[Det[z IdentityMatrix[4]-mat]],
  "MemoryResiduals"->Table[Factor[u.mat.qq.powers[[j]].qq.mat.u
                         -ep^2(1-ep)^(j-1)/16],{j,1,6}],
  "MomentResiduals"->Table[Together[ws.(nodes^j)+wt slow^j-Total[nodes^j]/4],
                          {j,0,3}],
  "AddedWeight"->wt,
  "PositiveWeights"->And@@Thread[ws>0],
  "WeightedGeometricResidual"->Together[c/(q-r)
                  -(c/q)Total[Table[(r/q)^j,{j,0,5}]]-c(r/q)^6/(q-r)]|>
