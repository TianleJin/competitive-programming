it = lambda: list(map(int, input().strip().split()))
INF = float('inf')


def case():
    pass


def brute():
    pass


def solve():
    N = int(input())
    A = it()

    ans = 0
    mx = -INF
    for i in range(N):
        if A[i] > mx and (i + 1 == N or A[i] > A[i + 1]):
            ans += 1
        mx = max(mx, A[i])
    return ans


if __name__ == '__main__':
    T = int(input())
    for tt in range(1, T + 1):
        ans = solve()
        print('Case #{}: {}'.format(tt, ans))
