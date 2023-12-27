class Dxc: 
    def __init__(self, name, index, position1, position2):
        self.name = name
        self.index = index
        self.position1 = position1
        self.position2 = position2

dbdl_position = [18, 83] # 东部大陆
xkly_position = [32, 83] # 虚空领域
bfdl_position = [46, 83] # 冰封大陆
yszd_position = [60, 83] # 元素之地
mwdl_position = [73, 83] # 迷雾大陆

# 东部大陆
dbdl = [
    Dxc("噩梦洞穴", 1, dbdl_position, [28, 27]),Dxc("噩梦洞穴", 1, dbdl_position, [28, 27]),
    Dxc("野猪人高地", 2, dbdl_position, [64, 26]), Dxc("野猪人高地", 2, dbdl_position, [64, 26]),
    Dxc("机械要塞", 3, dbdl_position, [27, 38]), Dxc("机械要塞", 3, dbdl_position, [27, 38]),
    Dxc("盗贼矿井", 4, dbdl_position, [64, 38]), Dxc("盗贼矿井", 4, dbdl_position, [64, 38]),
    Dxc("巨石密室", 5, dbdl_position, [28, 49]), Dxc("巨石密室", 5, dbdl_position, [28, 49]),
    Dxc("诅咒教堂", 6, dbdl_position, [64, 49]),  Dxc("诅咒教堂", 6, dbdl_position, [64, 49]),
    # 上面这6个本每天可以免费打2次
    Dxc("巨魔墓地", 7, dbdl_position, [28, 60]), Dxc("水晶庭院", 8, dbdl_position, [64, 60]),
    Dxc("沉默的神庙", 9, dbdl_position, [27, 72]), Dxc("精灵遗迹", 10, dbdl_position, [64, 72]),
    Dxc("龙人塔", 11, dbdl_position, [28, 60]), Dxc("火焰之心", 12,  dbdl_position, [64, 60]),
    Dxc("黑龙巢穴", 13, dbdl_position, [27, 72]), Dxc("亡灵要塞", 14, dbdl_position, [64, 72])
    # # 第11,12,13,14需要拖动列表，最终位置和7,8,9,10副本坐标一致
]

# 虚空领域
xkly = [
    Dxc("地狱火堡垒", 1, xkly_position, [28, 27]),Dxc("沼泽水库", 2, xkly_position, [64, 26]),
    Dxc("亡者之城", 3, xkly_position, [27, 38]), Dxc("山丘城堡", 4, xkly_position, [64, 38]),
    Dxc("虚空舰", 5, xkly_position, [28, 49]), Dxc("守护者之塔下层", 6, xkly_position, [64, 49]),
    Dxc("守护者之塔上层", 7, xkly_position, [28, 60]), Dxc("海底神殿", 8, xkly_position, [64, 60]),
    Dxc("虚空要塞", 9, xkly_position, [27, 72]), Dxc("圣山战场", 10, xkly_position, [64, 72]),
    Dxc("黑暗神殿", 11, xkly_position, [27, 72]), Dxc("魔法之井", 12, xkly_position, [64, 72])
    # 第11,12需要拖动列表，最终位置和9,10副本坐标一致
]