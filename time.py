n=6
Arr= [900,940,950,1100,1500,1800]
Dep= [910,1200,1120,1130,1900,2000]
i=0
j=0
plateform=0
maxplateform=0

while i<n and j<n:
    if Arr[i]<Dep[j]:
        plateform+=1
        if plateform > maxplateform:
            maxplateform=plateform
        i+=1
    else:
        plateform-=1
        j+=1
print(f"Max Plateform: {maxplateform}")