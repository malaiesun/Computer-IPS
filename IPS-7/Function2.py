def game(S):
  if S == S[::-1]:  
          return len(S) 
      else:
          return S[::-1]
print(game(input()))
