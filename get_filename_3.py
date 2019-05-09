# %%
import os
import json

#%%
wr = []
for path, d, filelist in os.walk("."):
    # print(d)
    for filename in filelist:
        if os.path.splitext(filename)[1] == '.jpg' or os.path.splitext(filename)[1] == '.png' or os.path.splitext(filename)[1] == '.jpeg':
            target = (os.path.join(path, filename)[1:])
            print(target)
            wr.append(target)


with open("./fileNames.js", "w") as f:
    f.write("var fileNames = " +
            json.dumps(wr))



#%%
# wr = []
# for path, d, filelist in os.walk("."):
#     # print(d)
#     for filename in filelist:
#         if os.path.splitext(filename)[1] == '.jpg' or os.path.splitext(filename)[1] == '.png' or os.path.splitext(filename)[1] == '.jpeg':
#             print(os.path.join(os.getcwd(), filename))
#             wr.append(os.path.join(os.getcwd(), filename))


# with open("../fileNames.js", "w") as f:
#     f.write("var fileNames = " +
#             json.dumps(wr))
#%%
# wr = []
# for path, d, filelist in os.walk("."):
#     # print(d)
#     for filename in filelist:
#         if os.path.splitext(filename)[1] == '.jpg' or os.path.splitext(filename)[1] == '.png' or os.path.splitext(filename)[1] == '.jpeg':
#             target = ("images"+os.path.join(path, filename)[1:])
#             print(target)
#             wr.append(target)


# with open("../fileNames.js", "w") as f:
#     f.write("var fileNames = " +
#             json.dumps(wr))
