def decrypt_text(d:int,n:int,new_ar:list):
  dec_arr=[]
  for ar in new_ar:
    if ar==" ":
      dec_arr.append(" ")
    else:
      dec_arr.append((ar**d)%n)
  return dec_arr