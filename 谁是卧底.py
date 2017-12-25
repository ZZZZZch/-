import random
from time import sleep

"""涉及知识点有：
    【字典】
    【列表】
    【元组】
    【循环】
    【函数】
    【列表推导式】
    【索引】
    【随机方法】
    【递归】
"""
def default():
    print("【数据初始化】")
    accounts = {"zzz": "123"}
    return accounts

def login(accounts):
    print("【登录游戏】")
    account = input("请输入账号")
    code = input("请输入密码")

    if account in accounts:
        if accounts[account] == code:
            print("登录成功")
        else:
            print("密码错误")
            choice = input("是否重新注册【yes/no】")
            if choice == "yes":
                signup(accounts)
            else:
                login(accounts)
    else:
        print("账号不存在，请注册……注册页面自动跳转中……")
        signup(accounts)

def signup(accounts):
    print("【注册账号】")
    account_reg = input("请输入您要注册的账号：")
    if account_reg in accounts:
        print("账号已存在，请更换账号")
        signup(accounts)
    else:
        code_reg = input("请输入您账号所使用的密码：")
        accounts[account_reg] = code_reg
        print("注册成功！自动进入游戏……")

def makecard_setplayers():
    print("【游戏卡片制作】")
    words_pair_tmp = input("请输入本局游戏词语对【以空格作为分割】")
    words_pair = words_pair_tmp.split(" ")
    print("您制作的词语对为 【%s】和【%s】"%(words_pair[0],words_pair[1]))

    player_num = int(input("请输入参与玩家数目："))
    print("玩家数为%d人……"%player_num)
    return words_pair, player_num

def generate_info(words_pair, player_num):
    print("【角色分配中】")
    sleep(1)
    undercover_player_id = random.randint(1,player_num)
    undercover_card_id = random.randint(0,len(words_pair)-1)

    if undercover_card_id == 1:
        normal_card_id = 0

    if undercover_card_id == 0:
        normal_card_id = 1

    print("卧底玩家为【%d】号玩家\n他的卡片是【%s】"%(undercover_player_id,
                                words_pair[undercover_card_id]))
    print("平民玩家卡片是【%s】"%words_pair[normal_card_id])

    return(undercover_player_id, words_pair[undercover_card_id],
           words_pair[normal_card_id])

def speech(player_num):
    print("【发言环节】")
    for player in range(player_num):
        print("%d号玩家开始发言……"%(player))
        sleep(1)

def vote(undercover_player_id, player_num):
    print("【投票环节】")
    players = [player for player in range(player_num)]
    while True:
        vote_ls = []
        max_value = 0
        max_player = 0

        for player in players:
            vote_id = random.randint(0,player_num-1)
            while True:
                if (vote_id != player) and (vote_id in players):
                    print("%d号玩家认为%d号玩家是卧底……"%(player, vote_id))
                    vote_ls.append(vote_id)
                    sleep(1)
                    break
                else:
                    vote_id = random.randint(0, player_num-1)

        print("【展示投票结果】")

        for player in range(player_num):
            print("%d号玩家：%d票"%(player, vote_ls.count(player)))
            if vote_ls.count(player) > max_value:
                max_value = vote_ls.count(player)
                max_player = player

        if max_player == undercover_player_id:
            print("【%d号玩家出局，他是卧底。】" % max_player)
            print("【游戏结束，平民胜利！】")
            break
        else:
            print("【%d号玩家出局，被冤死。】" % max_player)
            players.remove(max_player)
            if len(players)==2:
                print("【游戏结束，卧底胜利！】")
                break

def main():
    print("欢迎来到'谁是卧底'！")

    accounts = default()
    login(accounts)

    print("游戏开始……")

    words_pair, player_num = makecard_setplayers()
    undercover_player_id , undercover_card, normal_card = \
        generate_info(words_pair, player_num)
    speech(player_num)
    vote(undercover_player_id, player_num)

if __name__ == "__main__":
    main()