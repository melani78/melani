data=[["yes","yes","yes"],
      ["yes","No","yes"],
      ["no","yes","no"]]

S=["0","0"]
G=["?","?"]
print("S",S)
print("G",G)
print("-"*40)

for example in data:
    attributes=example[:-1]
    label=example[-1]
    if label=="yes":
       for i in range(2):
            if  S[i]=="0":
                S[i]=attributes[i]
            elif S[i]!=attributes[i]:
                S[i]="?"
    else:
        new_G=[]
        for i in range(2):
            if S[i]!=attributes[i]:
                h=["?","?","?"]
                h[i]=S[i]
                new_G.append(h)
                G=new_G
    print("After example:",example)
    print("S=",S)
    print("G=",G)
    print("-"*40)
    print("final S=",S)
    print("final G=",G)
    



                
                






