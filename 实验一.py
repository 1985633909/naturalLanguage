import numpy as np
import torch
import pandas as pd

score=np.array([[79,90],[72,50],[81,95]])
a=score>80
print(a)
score[:,0]=score[:,0]+5
print(score)

s=pd.Series(np.random.randn(4))
print(s)

x=torch.rand(5,3)
print(x)
print(torch.cuda.is_available())
