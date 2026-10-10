istr = lambda: input().strip()
istrl = lambda: input().strip().split()
iint = lambda: int(input())
iintl = lambda: list(map(int, input().strip().split()))


def mergePrefix(prefixes):
    ans = ''
    for p in prefixes:
        if len(p) > len(ans):
            ans = p
    for p in prefixes:
        if ans.find(p) != 0:
            return None
    return ans


def mergeSuffix(suffixes):
    ans = mergePrefix([s[::-1] for s in suffixes])
    if ans is None:
        return ans
    return ans[::-1]


def solve(N, strs):
    patterns = [s.split('*') for s in strs]
    prefix = mergePrefix([p[0] for p in patterns])
    suffix = mergeSuffix([p[-1] for p in patterns])
    if prefix is None or suffix is None:
        return '*'
    ans = prefix
    for p in patterns:
        ans += ''.join(p[1:-1])
    ans += suffix
    return ans


if __name__ == '__main__':
    T = iint()
    for t in range(1, T + 1):
        N = iint()
        ans = solve(N, [istr() for _ in range(N)])
        print('Case #{}: {}'.format(t, ans))
