# -*- coding: utf-8 -*-
"""2475 검증수.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/gemjh/954fbc2823f5bf18906bfc4ad7dae3d9/2475.ipynb
"""

nums=list(map(int,input().split()))
nums_mul=[]
for i in nums:
  n=i**2
  nums_mul.append(n)

print(sum(nums_mul)%10)