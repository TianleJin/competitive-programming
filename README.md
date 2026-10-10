# Competitive Programming

My solutions to algorithmic contests and problem sets, written in C++ and Python, plus a small library of reusable algorithm templates.

## Layout

```
.
├── library/                  Reusable templates
│   ├── algorithms/           Graph algorithms (C++): Dinic, Edmonds-Karp, Hopcroft-Karp, bridges, cut vertices
│   └── data-structures/      Python: segment tree, BIT, suffix array, rolling hash, Manacher, BST, heap, ... (with unit tests)
├── problem-sets/
│   └── cses/                 CSES Problem Set, grouped by section (graph, tree, range queries, maths, strings, geometry, ...)
└── contests/                 One folder per contest round, one file per problem (a, b, c, ...)
    ├── atcoder/
    ├── codeforces/
    ├── facebook-hacker-cup/
    ├── google-code-jam/      <year>/<round>/
    ├── google-kickstart/     <year>/<round>/
    └── leetcode/             weekly (contest-N) and biweekly contests
```

Within a contest folder, `a`, `b`, `c`, ... match the problem order of the round. The file extension shows the language used (`.py` or `.cpp`). Some CSES problems have several approaches (e.g. `*_sol_i`, `*_sol_ii`).

## Running

C++ solutions read from stdin:

```bash
g++ -std=c++17 -O2 -o sol contests/codeforces/round-709-div-2/a.cpp && ./sol < input.txt
```

Python solutions likewise:

```bash
python contests/codeforces/global-round-9/a.py < input.txt
```

Tests for the data structures (run from their directory, since they import modules by name):

```bash
cd library/data-structures && python -m unittest
```

## Code style

Python is formatted and linted with [Ruff](https://docs.astral.sh/ruff/) (`ruff.toml`), C++ is formatted with [clang-format](https://clang.llvm.org/docs/ClangFormat.html) (`.clang-format`).

```bash
uvx ruff format . && uvx ruff check .
git ls-files '*.cpp' | xargs uvx clang-format -i
```
