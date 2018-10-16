import os

folders = [f.path for f in os.scandir("results") if f.is_dir()]
folders = [f for f in folders if os.path.isfile(f+"/0.0.monitor.csv")]
print(folders)


names = []
for folder in folders:
    name=folder.split("/")[1]
    name_params=name.split("_")
    if len(name_params)==4:
    	names.append(name_params[0]+"_"+name_params[1]+"_"+name_params[3])
    elif len(name_params)==5:
    	names.append(name_params[0]+"_"+name_params[1]+"_"+name_params[3]+"_"+name_params[4])
    else:
    	print("error: name params not recognised")
for name in names:
	print(name)

print("folders: ",len(folders))
print("names: ", len(names))
