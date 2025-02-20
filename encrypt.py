import random


def is_prime(number):
  if number <= 1:
    return False
  if number <= 3:
    return True
  if number % 2 == 0 or number % 3 == 0:
    return False

  i = 5
  while i * i <= number:
    if number % i == 0 or number % (i + 2) == 0:
      return False
    i += 6

  return True

def find_factors(number):
  factors = []
  while number > 1:
    for divisor in range(2, int(number**0.5) + 1):
      if number % divisor == 0:
        factors.append(divisor)
        number //= divisor
        break
    else:
      factors.append(number)
      break

  return factors

def find_e(phi):
  factor=find_factors(phi)
  found=False
  while found==False:
    num=random.randint(3,phi)

    factor_2=find_factors(num)

    if set(factor).intersection(set(factor_2)):
      pass
    else:
      found=True
  
  return num

def multiplicative_inverse(e, phi):
    original_phi = phi
    x0, x1 = 0, 1

    while e > 1:
        q = e // phi
        e, phi = phi, e % phi
        x0, x1 = x1 - q * x0, x0
    
    if x1 < 0:
        x1 += original_phi
    
    return x1

def encrypt_words(e:int,n:int,arr:list):
  new_ar=[]
  for ar in arr:
    if ar==" ":
      new_ar.append(" ")
    else:
      new_ar.append((ar**e)%n)
  return new_ar


def encrypt_text(p,q,arr):
  if is_prime(p)==False or is_prime(q)==False:
    raise ValueError("Please Enter Odd Numbers")
  
  return_values=[]
  n=p*q
  return_values.append(n)
  phi=(p-1)*(q-1)
  return_values.append(phi)
  e=find_e(phi)
  return_values.append(e)
  d = multiplicative_inverse(e, phi)
  return_values.append(d)

  enc_sol=encrypt_words(e,n,arr)
  return_values.append(enc_sol)

  return return_values

