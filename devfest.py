import httplib2
import random
from wxpy import *

bot = Bot(console_qr=True, cache_path=True)
print('okok')
main_grp = None
act_grp = None
conv_grps = []
for g in bot.groups(update=True):
    if g.self.display_name == '传话bot02':
        act_grp = g
        conv_grps.append(g)
        print(g)
    elif g.self.display_name == '传话bot01':
        conv_grps.append(g)
        print(g)
if not act_grp:
    print('act_grp not found')
    sys.exit(333)
act_member = []
act_member_phone = []
# mpqr_media_id = bot.upload_file('mpqr.png')


@bot.register(msg_types=FRIENDS)
def accept_friends(msg: Message):
    text = msg.text.strip()
    print(text)
    if msg.sender in act_grp:
        # msg.reply('请关注GDG广州微信公众号')
        # msg.reply_image('mpqr.png', mpqr_media_id)
        return
    new_friend = msg.card.accept()
    print(new_friend)
    act_member.append(new_friend)
    act_member_phone.append(text)
    act_grp.add_members(new_friend, use_invitation=True)
    print('invited')
    new_friend.send('''本次活动已截止报名，届时可前往http://t.cn/RWRgIma观看视频直播，或前往http://t.cn/Rl2kDyo观看图文直播''')


@bot.register(msg_types=[TEXT,PICTURE])
def handle_text(msg: Message):
    if msg.sender in conv_grps:
        for g in conv_grps:
            if g != msg.sender:
                msg.forward(g, prefix=msg.member.name+':')
                print(msg.member, msg)
    elif isinstance(msg.sender, Group):
        return

    text = msg.text.strip()
    print(text)
    if msg.sender in act_grp:
        # msg.reply('请关注GDG广州微信公众号')
        # msg.reply_image('mpqr.png', mpqr_media_id)
        return
    act_member.append(msg.sender)
    act_member_phone.append(text)
    act_grp.add_members(msg.sender, use_invitation=True)
    new_friend.send('活动报名地址 http://t.cn/ROAnHfV')


bot.join()
