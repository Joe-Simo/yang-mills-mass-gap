(* Stateless symbolic corroboration only; no independent full-proof verification. *)
x = Pi/(2 (ell+1));
nu = 4 Sin[x]^2;
mu = 2 nu;
<|
 "Nu1" -> nu,
 "MuTransverse" -> mu,
 "AtEll1" -> {nu /. ell -> 1, mu /. ell -> 1},
 "LeakageEtaUpper" -> 2 delta (ell+1),
 "LeakageSquare" -> 4 delta^2 (ell+1)^2,
 "ExponentDeltaEll" -> FullSimplify[7/26-1/13],
 "ExponentDeltaEll2" -> FullSimplify[7/26-2/13],
 "HalfGapLowerTemplate" -> 4/(ell+1)^2
|>
