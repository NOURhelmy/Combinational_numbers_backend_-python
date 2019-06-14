from flask import Flask, jsonify
from flask import request
import json

app = Flask(__name__)


def combs1(n, available, used):
    if len(used) == n:
        yield (list(used))
    elif len(available) <= 0:
        pass
    else:
        head = available.pop(0)
        used.append(head)
        for c in combs1(n, available[:], used[:]):
            yield c
        used.pop()
        for c in combs1(n, available[:], used[:]):
            yield c

def solve(lis):
    for x in lis:
        try:
            yield float(x)
        except ValueError:
            pass

@app.route('/<ss>/<n>/<T>')
def run(ss, n, T):
    list = ss.split()
    s = []
    list = solve(list)
    for st in list:
        s.append(float(st))
    n = float(n)
    T = float(T)
    s = s * int(n)
    i = 0
    sum = 0
    h = 0
    k = [c for c in combs1(n,s,[])]
    k = sorted(k)
    newcom = [k[i] for i in range(len(k)) if i == 0 or k[i] != k[i - 1]]

    while h < len(newcom):
        newcom[h].sort()
        h += 1

    newcom = sorted(newcom)
    ne = [newcom[i] for i in range(len(newcom)) if i == 0 or newcom[i] != newcom[i - 1]]

    c = 0
    out = []
    while i < len(ne):
        li = ne[i]
        for f in li:
            sum += f
        if sum / n == T:
            out.append(li)
            c += 1

        sum = 0
        i += 1

    return jsonify(results=out)


if __name__ == '__main__':
    app.run(debug=True)
