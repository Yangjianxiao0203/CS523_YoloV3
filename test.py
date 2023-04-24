import torch
a=torch.ones((3,10)).cuda(0)
b=torch.ones((3,10)).cuda(0)
print(a+b)
