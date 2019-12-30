# UNCOMMENT THESE LINES TO EXECUTE 
from prometeo import *

sizes: dimv = [[2,2], [2,2], [2,2], [2,2], [2,2]]
nx: dims = 2
nu: dims = 2
N:  dims = 5
# sizes: dim = N*[nx, nx]

class qp_data:
    C: pmat[nu,nu] = pmat(nx,nu)
    A: List[pmat, sizes]  = plist(pmat, sizes)
    B: List[pmat, sizes]  = plist(pmat, sizes)
    Q: List[pmat, sizes]  = plist(pmat, sizes)
    R: List[pmat, sizes]  = plist(pmat, sizes)
    P: List[pmat, sizes]  = plist(pmat, sizes)

    fact: List[pmat, sizes] = plist(pmat, sizes)

    def factorize(self) -> None:
        res: pmat[nx, nx] = pmat(nx, nx)
        Bt: pmat[nx, nx] = pmat(nx, nx)
        for i in range(N):
            pmt_gemm(self.P[i], self.B[i], res, res)
            pmat_tran(self.B[i], Bt)
            pmt_gemm(Bt, res, self.R[i], res)
            pmt_potrf(res, self.fact[i])
            # pmt_trsm(res, self.fact[i])

        return

def main() -> None:

    A: pmat[nu,nu] = pmat(nx, nx)
    B: pmat[nu,nu] = pmat(nx, nu)
    Q: pmat[nu,nu] = pmat(nx, nx)
    R: pmat[nu,nu] = pmat(nu, nu)
    P: pmat[nu,nu] = pmat(nx, nx)

    fact: pmat[nu,nu] = pmat(nx, nx)

    qp : qp_data = qp_data() 

    for i in range(N):
        qp.A[i] = A

    for i in range(N):
        qp.B[i] = B

    for i in range(N):
        qp.Q[i] = Q

    for i in range(N):
        qp.R[i] = R

    for i in range(N):
        qp.fact[i] = fact

    qp.factorize()