(* Actual independent exact evaluation used in U027; Wolfram 15.0.1. *)
ClearAll[x0,x1,x2,x3,y0,y1,y2,y3,dr,kin,fx,x,y,s];
x={x0,x1,x2,x3}; y={y0,y1,y2,y3};
dr[fx_,v_,i_]:=(-v[[i+1]]D[fx,v[[1]]]+v[[1]]D[fx,v[[i+1]]]
-Sum[LeviCivitaTensor[3][[j,k,i]]v[[k+1]]D[fx,v[[j+1]]],{j,3},{k,3}])/2;
kin[fx_]:=Expand[-2 Sum[dr[dr[fx,x,i],x,i]+dr[dr[fx,y,i],y,i],{i,3}]
-Sum[dr[dr[fx,y,i],x,i],{i,3}]];
s=x1 y1+x2 y2+x3 y3;
<|"Version"->$Version,
"T_x0y0"->kin[x0 y0],"T_dot"->kin[s],
"PerimeterEigenResidual"->Expand[kin[x0 y0+s]-(9/4)(x0 y0+s)],
"OtherEigenResidual"->Expand[kin[3 x0 y0-s]-(13/4)(3 x0 y0-s)],
"NormalizedElectricBlockEigenvalues"->Eigenvalues[{{3,-Sqrt[3]/4},{-Sqrt[3]/4,5/2}}],
"QuadraticMetricEigenvalues"->Eigenvalues[{{1,1/4},{1/4,1}}],
"PhysicalLeadingGap"->2Sqrt[3]|>
(* The last field is an input expression, not an independent limit proof. *)
