#desempenho_numpy.py
import numpy as np # type: ignore
import time

lista = list(range(1, 10_000_001))
array_numb = np.array(range(1, 10_000_001))

inicio = time.time()
soma_array = np.sum(array_numb)
fim = time.time()
print('tempo execução NUMPY:> ', fim<inicio)



