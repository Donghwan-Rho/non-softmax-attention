import torch
import torch.nn.functional as F
import torch.nn as nn
import math



a = 1
a = (1 + a/(2 ** 16))
print('a', a)
for i in range(16):
    a *= a
print('a', a)
a = (1 + 1/(2 ** 16))
print('a', a ** (2 ** 16))
print('a', torch.exp(torch.tensor([1])))


a = (1 + -100/(2 ** 16))
for i in range(16):
    a *= a
print('a', a)
a = (1 + -100/(2 ** 16))
print('a', a ** (2 ** 16))
print('a', torch.exp(torch.tensor([-100])))