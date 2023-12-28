# 副本数据集

class Dxc: 
    def __init__(self, name, index, region, dxcPosition):
        self.name = name
        self.index = index
        self.region = region
        self.dxcPosition = dxcPosition

positions = {
    "dbdl_position": {
        "regionName": "东部大陆",
        "position": [18, 83]
    },
    "xkly_position": {
        "regionName": "虚空领域",
        "position": [32, 83]
    },

    "bfdl_position": {
        "regionName": "冰封大陆",
        "position": [46, 83]
    },
    "yszd_position": {
        "regionName": "元素之地",
        "position": [60, 83]
    },
    "mwdl_position": {
        "regionName": "迷雾大陆",
        "position": [73, 83]
    }
}


# 东部大陆
dbdl = [
    Dxc("噩梦洞穴", 1, positions["dbdl_position"], [28, 27]), Dxc("野猪人高地", 2, positions["dbdl_position"], [64, 26]),
    Dxc("机械要塞", 3, positions["dbdl_position"], [27, 38]), Dxc("盗贼矿井", 4, positions["dbdl_position"], [64, 38]),
    Dxc("巨石密室", 5, positions["dbdl_position"], [28, 49]), Dxc("诅咒教堂", 6, positions["dbdl_position"], [64, 49]),
    # 上面这6个本每天可以免费打2次
    Dxc("巨魔墓地", 7, positions["dbdl_position"], [28, 60]), Dxc("水晶庭院", 8, positions["dbdl_position"], [64, 60]),
    Dxc("沉默的神庙", 9, positions["dbdl_position"], [27, 72]), Dxc("精灵遗迹", 10, positions["dbdl_position"], [64, 72]),
    Dxc("龙人塔", 11, positions["dbdl_position"], [28, 60]), Dxc("火焰之心", 12,  positions["dbdl_position"], [64, 60]),
    Dxc("黑龙巢穴", 13, positions["dbdl_position"], [27, 72]), Dxc("亡灵要塞", 14, positions["dbdl_position"], [64, 72])
    # # 第11,12,13,14需要拖动列表，最终位置和7,8,9,10副本坐标一致
]

# 虚空领域
xkly = [
    Dxc("地狱火堡垒", 1, positions["xkly_position"], [28, 27]),Dxc("沼泽水库", 2, positions["xkly_position"], [64, 26]),
    Dxc("亡者之城", 3, positions["xkly_position"], [27, 38]), Dxc("山丘城堡", 4, positions["xkly_position"], [64, 38]),
    Dxc("虚空舰", 5, positions["xkly_position"], [28, 49]), Dxc("守护者之塔下层", 6, positions["xkly_position"], [64, 49]),
    Dxc("守护者之塔上层", 7, positions["xkly_position"], [28, 60]), Dxc("海底神殿", 8, positions["xkly_position"], [64, 60]),
    Dxc("虚空要塞", 9, positions["xkly_position"], [27, 72]), Dxc("圣山战场", 10, positions["xkly_position"], [64, 72]),
    Dxc("黑暗神殿", 11, positions["xkly_position"], [27, 72]), Dxc("魔法之井", 12, positions["xkly_position"], [64, 72])
    # 第11,12需要拖动列表，最终位置和9,10副本坐标一致
]

# 冰封大陆
bfdl = []

# 元素之地
yszd = []

# 迷雾大陆
mwdl = []