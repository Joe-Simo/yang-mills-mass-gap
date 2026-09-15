(* U026 independent Wolfram cross-checks. Kernel version observed: 15.0.1 Linux x86 (64-bit), July 2, 2026. *)
ClearAll[th, ell, u, lam];
radial = FullSimplify[Sin[th] (-1/2 (D[u[th]/Sin[th], {th, 2}] + 2 Cot[th] D[u[th]/Sin[th], th])) + (u''[th] + u[th])/2, Assumptions -> 0 < th < Pi];
norm = Integrate[Sin[Pi th/ell]^2, {th, 0, ell}, Assumptions -> ell > 0];
moment = FullSimplify[Integrate[th^2 Sin[Pi th/ell]^2, {th, 0, ell}, Assumptions -> ell > 0]/norm];
kinetic = FullSimplify[Integrate[(Pi/ell Cos[Pi th/ell])^2/2, {th, 0, ell}, Assumptions -> ell > 0]/norm];
cc = 7/Pi - Sqrt[Pi^2/3 - 1/2];
<|"Version" -> $Version, "RadialConjugationResidual" -> radial, "TrialNorm" -> norm, "TrialSecondMoment" -> moment, "TrialKineticRayleigh" -> kinetic, "GapCoefficient" -> cc, "GapCoefficientDecimalNonCertificate" -> N[cc, 20], "RationalPositivityCheck" -> {821/294 < 289/100, 49/22 - 17/10 > 1/2}|>
(* The following is a numerical corroboration, NOT an exact interval certificate. *)
ClearAll[lv];
Table[With[{z = lv}, <|"lambda" -> z, "LowestTwoUnshiftedDimensionlessEnergies" -> N[{z - 1/2 + MathieuCharacteristicB[2, -4 z]/8, z - 1/2 + MathieuCharacteristicB[4, -4 z]/8}, 50], "Gap" -> N[(MathieuCharacteristicB[4, -4 z] - MathieuCharacteristicB[2, -4 z])/8, 50]|>], {lv, {1, 16, 256, 4096}}]
