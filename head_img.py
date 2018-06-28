import itchat
import pdb

itchat.auto_login(hotReload=True)

friends = itchat.get_friends(update=True)

def download_headimgs():
    for i, f in enumerate(friends):
        img = itchat.get_head_img(userName=f["UserName"]) # itchat.get_head_img() 获取到头像二进制
        imgfile = open("img//" + str(i) + f["RemarkName"] + ".jpg", 'wb')
        imgfile.write(img)
        imgfile.close()

download_headimgs()

pdb.set_trace()