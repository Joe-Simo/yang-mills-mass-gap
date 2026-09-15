Clear[z,t,a,b,c,m,beta];
zfun=2 BesselI[1,z]/z;
ratio=BesselI[2,z]/BesselI[1,z];
quartic=-a^2/24-b^2/24-a*b/4+c*(a+b)/6;
target=-(a+b-2c)^2/24-(a*b-c^2)/6;
moments=Table[Binomial[2 k,k]/(4^k*(k+1)),{k,0,6}];
<|"Version"->$Version,
"ZSeries"->Series[zfun,{z,0,8}],
"LogZSeries"->Series[Log[zfun],{z,0,8}],
"LogDerivativeResidual"->FullSimplify[D[Log[zfun],z]-ratio,Assumptions->z>0],
"QuarticResidual"->Expand[quartic-target],
"WardMomentResiduals"->Table[Simplify[
(Binomial[2k+2,k+1]/(4^(k+1)*(k+2)))/Factorial[2k+1]
-(moments[[k+1]]-Binomial[2k+2,k+1]/(4^(k+1)*(k+2)))/(3 Factorial[2k])],{k,0,5}],
"SixStapleHessianSpectrumInUnitsBetaRatio"->Eigenvalues[IdentityMatrix[6]-ConstantArray[1/6,{6,6}]]|>
