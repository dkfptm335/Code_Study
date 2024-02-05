# common이 등차수열인지 등비수열인지 체크
# 등차수열: AP, 등비수열: GS
def check(common):
    return 'AP' if common[1] - common[0] == common[2] - common[1] else 'GS'

def get_operation(common):
    if check(common) == 'AP':
        return common[1] - common[0]
    else:
        return common[1] / common[0]

def solution(common):
    if check(common) == 'AP':
        return common[-1] + get_operation(common)
    else:
        return common[-1] * get_operation(common)
    