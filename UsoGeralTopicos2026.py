import numpy as np

def metodo_inversao( N=1, invG=lambda g:-np.log(1-g) ):
  g = np.random.rand(N)
  return invG(g)


def metodo_exclusao( N=1, f=lambda x:1-np.abs(x), xI=-1, xS=+1, yM=1,\
                    NcMax=1_000_000, fatorNc=10 ):
  dX = (xS-xI)
  Xs = []
  while len(Xs) < N:
    Ns = min(NcMax, fatorNc*(N-len(Xs)))
    xc = xI + dX* np.random.rand(Ns)
    yv = yM*np.random.rand(Ns)
    Xnovo = xc[ (yv<=f(xc)) ]
    for x in Xnovo:
      Xs.append(x)
      if len(Xs) >= N:
        break
  return np.array(Xs)