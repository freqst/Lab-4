stuffdict = {"r": (3, 25),
             'p': (2, 15),
             'a': (2, 15),
             'm': (2, 20),
             'i': (1, 5),
             'k':(1, 15),
             'x':(3, 20),
             't':(1, 25),
             'f': (1, 15),
             'd': (1, 10),
             's': (2, 20),
             'c': (2, 20)
             }


def get_area_and_value(stuffdict):
    size = [stuffdict[item][0] for item in stuffdict]
    spoint = [stuffdict[item][1] for item in stuffdict]
    return size, spoint



def get_memtable(stuffdict, A = 8):
    size, spoint = get_area_and_value(stuffdict)
    n = len(spoint)

    V = [[0 for a in range(A + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for a in range(A + 1):
            if i == 0 or a == 0:
                V[i][a] = 0
            elif size[i - 1] <= a:
                V[i][a] = max(spoint[i - 1] + V[i - 1][a - size[i - 1]], V[i - 1][a])
            else:
                V[i][a] = V[i - 1][a]

    return V, size, spoint


def get_selected_items_list(stuffdict, A = 8):
    V, size, spoint = get_memtable(stuffdict)
    n = len(spoint)
    res = V[n][A]
    a = A
    items_list = []

    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == V[i - 1][a]:
            continue
        else:
            items_list.append((size[i - 1], spoint[i - 1]))
            res -= spoint[i - 1]
            a -= size[i - 1]

    selected_stuff = []

    for search in items_list:
        for key, spoint in stuffdict.items():
            if spoint == search and key not in selected_stuff:
                for i in range(spoint[0]):
                    selected_stuff.append(key)
                break

    return selected_stuff

def total_spoint(stuff):
    summa = 20
    for key, spoint in stuffdict.items():
        if key in stuff:
            summa += spoint[1] * (stuff.count(key) // spoint[0])
        else:
            summa -= spoint[1]
    return summa


stuff = get_selected_items_list(stuffdict)
for i in range(4):
    print((' '.join(stuff[2 * i: 2 * (i + 1)])))

print(f"Итоговые очки выживания: {total_spoint(stuff)}")