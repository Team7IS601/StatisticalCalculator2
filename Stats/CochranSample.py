from Stats.CochranSample import sample
from math import ceil

def sample(N, cl, e, p):
    z = st.norm.ppf(1 - (1 - cl) / 2)
    n_0 = z**2 * p * (1 - p) / e**2
    n = n_0 / (1 + (n_0 - 1) / N)
    n = ceiling(n)
    return n

c_form = sample(10000, 0.95, .05, .05)