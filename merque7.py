import json
file="data.txt"
dict={}
with open(file) as x:
    for d in x:
        key,value=d.strip().split(None,1)
        dict[key]=value
outfile=open("data .txt","w")
json.dump(dict,outfile,indent = 4)
outfile.close()

