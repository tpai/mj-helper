# mj-helper

```
# 牌型
0-8 1-9筒
9-17 1-9索
18-26 1-9萬
27 東
28 南
29 西
30 北
31 中
32 發
33 白
34 春
35 夏
36 秋
37 冬
38 梅
39 蘭
40 竹
41 菊

# 是否胡牌 (0=未胡 1=胡)
is_hu = hu_result.hu([0,0,0,1,1,2,3,4,4,4,4,5,6,6,7,8], 1)
print(is_hu)

# 胡牌台數
result = hu_result.hu_result(
  [1,1,2,3,4,4,4,4,5,6],           // mj 手牌
  [[0, [6,8,7]], [2, [0,0,0]]],    // dmj 搭 0=吃 1=明槓 2=暗槓 3=碰
  1,                               // hnum 0=閒家 1=莊家 2+=連莊
  1,                               // first_turn 回合
  [],                              // hmj 花
  0,                               // circle 圈 0=東 1=南 2=西 3=北
  0,                               // door 開門 0=東 1=南 2=西 3=北
  False,                           // bool_last 海底
  1,                               // getmj 摸到的牌
  0,                               // first_hear 1=天聽 2=地聽
  None,                            // drophu 槍牌
  False,                           // hhu 花胡
  False,                           // bool_akong 搶槓
  False                            // bool_pkong 槓上開花
)
print(result.table)
```
