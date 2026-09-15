ClearAll[z,ell,xx,mm,kk,pp,oo,uu,vv,ww];
mm={{6,-1,0},{-1,6,-1},{0,-1,6}};
oo={1,1,1,1}/2; uu={1,1,-1,-1}/2; vv={1,-1,1,-1}/2; ww={1,-1,-1,1}/2;
kk=Outer[Times,oo,oo]+(Outer[Times,uu,uu]+Outer[Times,vv,vv]+Outer[Times,ww,ww])/4+(Outer[Times,uu,vv]+Outer[Times,vv,uu])/8;
pp=Outer[Times,oo,oo]+Outer[Times,uu,uu];
<|"Version"->$Version,"BesselRatioSquaredSeries"->Series[(BesselI[2,z]/BesselI[1,z])^2,{z,0,6}],"AlignedPrecisionInverse"->Inverse[mm],"AlignedComponentCorrelation"->FullSimplify[Inverse[mm][[1,3]]/Inverse[mm][[1,1]]],"AlignedTraceCorrelation"->FullSimplify[(Inverse[mm][[1,3]]/Inverse[mm][[1,1]])^2],"PositiveMarkovSpectrum"->Eigenvalues[kk],"RowSums"->Total[kk,{2}],"MemoryDefectResidual"->Simplify[pp.kk.kk.pp-pp.kk.pp.kk.pp-Outer[Times,uu,uu]/64],"TailRatioResidual"->FullSimplify[(xx^(ell+1)*(ell+2)^2/Factorial[ell+2]^4)/(xx^ell*(ell+1)^2/Factorial[ell+1]^4)-xx/((ell+1)^2*(ell+2)^2),Assumptions->{ell>=0,Element[ell,Integers],xx>0}]|>
