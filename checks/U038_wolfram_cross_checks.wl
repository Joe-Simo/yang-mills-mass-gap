(* Exact corroboration of submitted algebra, not independent proof verification. *)
ClearAll[n,x];
With[{m=6 n^2(n+1)^2,l=4 n(n+1)^3,b=24 n(n+1)^2,stars=4 n(n-1)^3},
 <|"BoundaryRatio"->Cancel[b/m],"LinkRatio"->Cancel[l/m],
 "FixedBoundaryCollar"->Expand[m-(m/.n->n-2)],
 "FullStarRatio"->Factor[6 stars/(4m)],
 "HaarBallDerivativeResidual"->FullSimplify[D[(x-Sin[2x]/2)/Pi,x]-2 Sin[x]^2/Pi],
 "SixthRootIdentity"->FullSimplify[MatrixPower[DiagonalMatrix[{(1+I Sqrt[3])/2,(1-I Sqrt[3])/2}],6]],
 "TwoDimensionalFluxAction"->36(1-Cos[Pi/3]),
 "FourDimensionalCompetitorMargin"->((m/12-2(m-(m/.n->n-2)))/.n->256)|>]
