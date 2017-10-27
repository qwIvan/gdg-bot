import httplib2
import random
from wxpy import *

bot = Bot(console_qr=True, cache_path=True)
print('okok')
main_grp = None
act_grp = None
for g in bot.groups(update=True):
    if g.self.display_name == 'GDG':
        act_grp = g
        break
else:
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
    new_friend.send('活动地址: http://t.cn/ROAnHfV (报名已截止)')


@bot.register(msg_types=TEXT)
def handle_text(msg: Message):
    if isinstance(msg.sender, Group):
        # if msg.is_at:
            # randint = random.randint(1, 2)
            # if randint == 1:
                # msg.reply('这里是GDG广州')
            # else:
                # msg.reply('请关注GDG广州微信公众号')
                # msg.reply_image('mpqr.png', mpqr_media_id)
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
