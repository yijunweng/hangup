
# region 副本数据集
class Dxc: 
    def __init__(self, name, index, region, dxcPosition):
        self.name = name
        self.index = index
        self.region = region
        self.dxcPosition = dxcPosition

region_positions = {
    "dbdl_position": {
        "regionName": "东部大陆",
        "position": [15, 83]
    },
    "xkly_position": {
        "regionName": "虚空领域",
        "position": [33, 83]
    },

    "bfdl_position": {
        "regionName": "冰封大陆",
        "position": [49, 83]
    },
    "yszd_position": {
        "regionName": "元素之地",
        "position": [66, 83]
    },
    "mwdl_position": {
        "regionName": "迷雾大陆",
        "position": [83, 83]
    }
}

# 地下城一页展示十个豆腐块
dxc_positions = [
    [28, 24], [70, 24],
    [28, 36], [70, 36],
    [28, 47], [70, 47],
    [28, 60], [70, 60],
    [28, 70], [70, 70]
]

# 东部大陆
dbdl = [
    Dxc("噩梦洞穴", 1, region_positions["dbdl_position"], dxc_positions[0]), Dxc("野猪人高地", 2, region_positions["dbdl_position"], dxc_positions[1]),
    Dxc("机械要塞", 3, region_positions["dbdl_position"], dxc_positions[2]), Dxc("盗贼矿井", 4, region_positions["dbdl_position"], dxc_positions[3]),
    Dxc("巨石密室", 5, region_positions["dbdl_position"], dxc_positions[4]), Dxc("诅咒教堂", 6, region_positions["dbdl_position"], dxc_positions[5]),
    Dxc("巨魔墓地", 7, region_positions["dbdl_position"], dxc_positions[6]), Dxc("水晶庭院", 8, region_positions["dbdl_position"], dxc_positions[7]),
    Dxc("沉默的神庙", 9, region_positions["dbdl_position"], dxc_positions[8]), Dxc("精灵遗迹", 10, region_positions["dbdl_position"], dxc_positions[9]),
    Dxc("龙人塔", 11, region_positions["dbdl_position"], dxc_positions[6]), Dxc("火焰之心", 12,  region_positions["dbdl_position"], dxc_positions[7]),
    Dxc("黑龙巢穴", 13, region_positions["dbdl_position"], dxc_positions[8]), Dxc("亡灵要塞", 14, region_positions["dbdl_position"], dxc_positions[9])
    # # 第11,12,13,14需要拖动列表，最终位置和7,8,9,10副本坐标一致
]

# 虚空领域
xkly = [
    Dxc("地狱火堡垒", 1, region_positions["xkly_position"], dxc_positions[0]),Dxc("沼泽水库", 2, region_positions["xkly_position"], dxc_positions[1]),
    Dxc("亡者之城", 3, region_positions["xkly_position"], dxc_positions[2]), Dxc("山丘城堡", 4, region_positions["xkly_position"], dxc_positions[3]),
    Dxc("虚空舰", 5, region_positions["xkly_position"], dxc_positions[4]), Dxc("守护者之塔下层", 6, region_positions["xkly_position"], dxc_positions[5]),
    Dxc("守护者之塔上层", 7, region_positions["xkly_position"], dxc_positions[6]), Dxc("海底神殿", 8, region_positions["xkly_position"], dxc_positions[7]),
    Dxc("虚空要塞", 9, region_positions["xkly_position"], dxc_positions[8]), Dxc("圣山战场", 10, region_positions["xkly_position"], dxc_positions[9]),
    Dxc("黑暗神殿", 11, region_positions["xkly_position"], dxc_positions[8]), Dxc("魔法之井", 12, region_positions["xkly_position"], dxc_positions[9])
    # 第11,12需要拖动列表，最终位置和9,10副本坐标一致
]

# 冰封大陆
bfdl = []

# 元素之地
yszd = []

# 迷雾大陆
mwdl = []

# endregion

# region 广告数据集
ad_posistions = [
    [15, 30], [32, 30], [49 ,30], [67 ,30]
]
# endregion