def study():
    a = input()
    S = a.lower()
    s_dict = {}

    for _s in S:
        try:
            s_dict[_s] += 1
        except:
            s_dict[_s] = 1

    val_lst = list(s_dict.values())
    max_val = max(val_lst)

    if val_lst.count(max_val) >= 2:
        return '?'

    for s, val in s_dict.items():
        if val == max_val:
            return s.upper()

print(study())

