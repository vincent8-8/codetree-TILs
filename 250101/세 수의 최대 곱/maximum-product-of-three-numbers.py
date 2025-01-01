n = int(input())
_list = list(map(int, input().split()))
_list.sort()

n_n_p = _list[0] * _list[1] * _list[-1]
p_p_n = _list[-1] * _list[-2] * _list[0]
n_n_n = _list[0] * _list[1] * _list[2]
p_p_p = _list[-1] * _list[-2] * _list[-3]


print(max(n_n_n, p_p_p, n_n_p, p_p_n))