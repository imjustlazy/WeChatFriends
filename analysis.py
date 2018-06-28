import itchat
import matplotlib.pyplot as plt
import pdb

itchat.auto_login(hotReload=True)

friends = itchat.get_friends(update=True)

def analysis_sex():
    sex = {"Male": 0, "Female": 0, "Unknown": 0}
    for f in friends:
        if f["Sex"] == 1:
            sex["Male"] += 1
        elif f["Sex"] == 2:
            sex["Female"] += 1
        else:
            sex["Unknown"] += 1
    for k in sex:
        plt.bar(k, sex[k])
    plt.show()


analysis_sex()

pdb.set_trace()