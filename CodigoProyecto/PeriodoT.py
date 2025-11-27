import math
import Constante_k as ctte
def periodoT():
        k = ctte.main()
        m = 9
        return 2*math.pi*math.sqrt(m/k)
def error_periodoT():
        m = 9
        dm = 0.1
        return (periodoT()/(2*m)) *dm