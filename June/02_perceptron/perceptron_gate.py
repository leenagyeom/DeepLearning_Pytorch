"""

단층 퍼셉트론 이용한 AND, NAND, OR 게이트 구현

1. AND
- 두 개의 입력 값이 모두1인 경우만 output 1 아닌경우 0
  input : x1, x2 / output : y
  w1 , w2 , b 라고 하면 (w 가중치 , b 편향 값)
  편향값과 가중치는 표준으로 내놓은 값이 있다.

"""

def AND_gate(x1, x2):
    w1 = 0.5
    w2 = 0.5
    b = -0.7

    result = x1 * w1 + x2 * w2 + b # 단층 퍼셉트론 공식
    # result = x1 * w1 + b
    # 입력이 x1만 있으면 x2, w2가 빠진다 = x1 * w1 + b
    print("result >> ", result)

    if result <= 0:
        return 0
    else:
        return 1


"""
2. NAND (Not AND)
- 두개의 입력값이 1인 경우에만 출력값이 0 나머지 쌍에 대해서는 모두 출력 값 1 
"""

def NAND_gate(x1, x2):
    w1 = -0.5
    w2 = -0.5
    b = 0.7

    result = x1 * w1 + x2 * w2 + b  # 단층 퍼셉트론 공식

    if result <= 0:
        return 0
    else:
        return 1


"""
3. OR 
- 두값이 0 , 0 - >  0 / 0, 1 -> 1 두값이 서로 다르면 1 
"""

def OR_gate(x1, x2):
    w1 = 0.5
    w2 = 0.5
    b = -0.4

    result = x1 * w1 + x2 * w2 + b  # 단층 퍼셉트론 공식

    if result <= 0:
        return 0
    else:
        return 1



# p0, 0], [0, 1], [1, 0], [1, 1]

and_test = AND_gate(1, 1)
print(" AND gate Test>>", and_test)

nand_test = NAND_gate(1, 0)
print(" NAND gate Test>>", nand_test)

or_test = OR_gate(0, 0)
print(" OR gate Test>>", or_test)