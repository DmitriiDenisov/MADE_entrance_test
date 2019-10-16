dict_new = {}
list = ['/etc/sudoers',
        '/root/readme',
        '/etc/zshrc',
        '/bin/curl',
        '/etc/ntp/keys'
        ]

max_depth = max(list)



def create_dict(dict_, el):
    if len(el) == 1:
        if dict_.get(-1):
            dict_[-1].extend(el)
        else:
            dict_[-1] = el
    else:
        if not dict_.get(el[0]):
            dict_[el[0]] = {}
        dict_[el[0]] = create_dict(dict_[el[0]], el[1:])
    return dict_


dict_ = {}
for el in list:
    temp = el.split("/")
    dict_ = create_dict(dict_, temp[1:])
print(dict_)


def one_step_into(dict_, sum):
    if dict_.get(-1):
        sum += len(dict_.get(-1))
        del dict_[-1]

    for key in dict_.keys():
        sum += 1
        sum = one_step_into(dict_[key], sum)
    return sum + 1


sum = one_step_into(dict_, 0)
print(sum)
