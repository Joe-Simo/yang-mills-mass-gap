(* Stateless exact corroboration only; no independent full-proof verification. *)
Clear[p1,p2,p3,gg,ll];
cmat={{0,-p3,p2},{p3,0,-p1},{-p2,p1,0}};
pvec={{p1},{p2},{p3}};
lambda=p1^2+p2^2+p3^2;
qq=lambda/2+Sinh[gg] Coth[ll gg];
rr=Sinh[gg] Csch[ll gg];
<|
 "HodgeResidual" -> FullSimplify[Transpose[cmat].cmat-(lambda IdentityMatrix[3]-pvec.Transpose[pvec])],
 "SymmetricParityResidual" -> FullSimplify[(qq-rr)-(lambda/2+Sinh[gg] Tanh[ll gg/2]), Assumptions->{gg>0,ll>0}],
 "AntisymmetricParityResidual" -> FullSimplify[(qq+rr)-(lambda/2+Sinh[gg] Coth[ll gg/2]), Assumptions->{gg>0,ll>0}],
 "ZeroModeSymmetricLimit" -> FullSimplify[Limit[(qq-rr)/.lambda->2(Cosh[gg]-1),gg->0], Assumptions->ll>0],
 "ZeroModeAntisymmetricLimit" -> FullSimplify[Limit[(qq+rr)/.lambda->2(Cosh[gg]-1),gg->0], Assumptions->ll>0],
 "OptimizedPerturbationExponent" -> 7/26-2/13
|>
