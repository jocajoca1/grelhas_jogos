"""Geradores e verificadores dos desafios do livro PULSO."""
import itertools
import random
import string

A = string.ascii_uppercase


# ---------- Cifras ----------
def cesar(texto, n):
    return "".join(A[(A.index(c) + n) % 26] if c in A else c for c in texto)


def vigenere(texto, chave, sinal=1):
    out, i = [], 0
    for c in texto:
        if c in A:
            k = A.index(chave[i % len(chave)])
            out.append(A[(A.index(c) + sinal * k) % 26])
            i += 1
        else:
            out.append(c)
    return "".join(out)


def binario(texto):
    palavras = texto.split()
    return [[format(A.index(c) + 1, "05b") for c in p] for p in palavras]


# ---------- Sopa de letras ----------
DIRS = [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (-1, 1)]


def sopa(palavras, mensagem, n=10, seed=1, tentativas=200000):
    rnd = random.Random(seed)
    alvo = len(mensagem)
    for _ in range(tentativas):
        g = [[None] * n for _ in range(n)]
        usadas = []
        ordem = palavras[:]
        rnd.shuffle(ordem)
        for p in ordem:
            livres = sum(c is None for r in g for c in r)
            if livres == alvo:
                break
            opcoes = []
            for r in range(n):
                for c in range(n):
                    for dr, dc in DIRS:
                        er, ec = r + dr * (len(p) - 1), c + dc * (len(p) - 1)
                        if not (0 <= er < n and 0 <= ec < n):
                            continue
                        ok, novas = True, 0
                        for i, ch in enumerate(p):
                            x = g[r + dr * i][c + dc * i]
                            if x is None:
                                novas += 1
                            elif x != ch:
                                ok = False
                                break
                        if ok and 0 < novas and livres - novas >= alvo:
                            opcoes.append((r, c, dr, dc))
            if not opcoes:
                continue
            r, c, dr, dc = rnd.choice(opcoes)
            for i, ch in enumerate(p):
                g[r + dr * i][c + dc * i] = ch
            usadas.append((p, r, c, dr, dc))
        livres = sum(c is None for r in g for c in r)
        if livres == alvo and len(usadas) >= 12:
            it = iter(mensagem)
            for r in range(n):
                for c in range(n):
                    if g[r][c] is None:
                        g[r][c] = next(it)
            # cada palavra tem de aparecer exatamente uma vez
            if all(conta(g, p) == 1 for p, *_ in usadas):
                return g, usadas
    raise RuntimeError("sem sopa")


def conta(g, p):
    n, t = len(g), 0
    for r in range(n):
        for c in range(n):
            for dr, dc in [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (-1, 1), (1, -1), (-1, -1)]:
                if all(0 <= r + dr * i < n and 0 <= c + dc * i < n and g[r + dr * i][c + dc * i] == ch
                       for i, ch in enumerate(p)):
                    t += 1
    return t


# ---------- Sudoku 6x6 (caixas 2x3) ----------
def sud_ok(g, r, c, v):
    if v in g[r] or any(g[i][c] == v for i in range(6)):
        return False
    br, bc = r // 2 * 2, c // 3 * 3
    return all(g[i][j] != v for i in range(br, br + 2) for j in range(bc, bc + 3))


def sud_resolve(g, limite=2):
    sols = []

    def rec():
        for r in range(6):
            for c in range(6):
                if g[r][c] == 0:
                    for v in range(1, 7):
                        if sud_ok(g, r, c, v):
                            g[r][c] = v
                            rec()
                            g[r][c] = 0
                            if len(sols) >= limite:
                                return
                    return
        sols.append([row[:] for row in g])

    rec()
    return sols


def sudoku(marcas, valores, seed=3, pistas_alvo=13, min_pistas=14):
    rnd = random.Random(seed)
    while True:
        g = [[0] * 6 for _ in range(6)]
        cel = [(r, c) for r in range(6) for c in range(6)]

        def fill(i=0):
            if i == 36:
                return True
            r, c = cel[i]
            vs = list(range(1, 7))
            rnd.shuffle(vs)
            for v in vs:
                if sud_ok(g, r, c, v):
                    g[r][c] = v
                    if fill(i + 1):
                        return True
                    g[r][c] = 0
            return False

        fill()
        if [g[r][c] for r, c in marcas] != valores:
            continue
        sol = [row[:] for row in g]
        puz = [row[:] for row in g]
        ordem = cel[:]
        rnd.shuffle(ordem)
        for r, c in ordem:
            if (r, c) in marcas:
                puz[r][c] = 0
                continue
            if sum(v != 0 for row in puz for v in row) <= min_pistas:
                continue
            v, puz[r][c] = puz[r][c], 0
            if len(sud_resolve([x[:] for x in puz])) != 1:
                puz[r][c] = v
        if len(sud_resolve([x[:] for x in puz])) == 1:
            pistas = sum(v != 0 for row in puz for v in row)
            if pistas <= pistas_alvo + 3:
                return puz, sol


# ---------- Labirinto ----------
def labirinto(w, h, msg, seed=0, tentativas=20000, medir=False):
    rnd = random.Random(seed)
    comps = []
    for _ in range(tentativas):
        paredes = {}  # (cell, dir) -> True se aberta
        aberto = set()
        vis = {(0, 0)}
        pilha = [(0, 0)]
        while pilha:
            x, y = pilha[-1]
            viz = [(x + dx, y + dy) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]
                   if 0 <= x + dx < w and 0 <= y + dy < h and (x + dx, y + dy) not in vis]
            if viz:
                n = rnd.choice(viz)
                aberto.add(frozenset([(x, y), n]))
                vis.add(n)
                pilha.append(n)
            else:
                pilha.pop()
        # caminho de (0,0) a (w-1,h-1)
        prev = {(0, 0): None}
        fila = [(0, 0)]
        while fila:
            cur = fila.pop(0)
            x, y = cur
            for n in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if frozenset([cur, n]) in aberto and n not in prev:
                    prev[n] = cur
                    fila.append(n)
        cam, cur = [], (w - 1, h - 1)
        while cur:
            cam.append(cur)
            cur = prev[cur]
        cam.reverse()
        comps.append(len(cam))
        if medir:
            continue
        if len(cam) == len(msg):
            letras = {}
            for cel, ch in zip(cam, msg):
                letras[cel] = ch
            iscas = "SAIUNAESTACAODASFLORESCAISROSSIOALAMEDA"
            for x in range(w):
                for y in range(h):
                    letras.setdefault((x, y), rnd.choice(iscas))
            return aberto, cam, letras
    if medir:
        return comps
    raise RuntimeError("sem labirinto")


# ---------- Grelha lógica (cruzeiro) ----------
NOMES = ["Alice", "Bruno", "Diana", "Fausto", "Glória"]
CONVES = [3, 4, 5, 7, 8]
ATIV = ["casino", "teatro", "restaurante", "biblioteca", "spa"]
ORIG = ["Porto", "Faro", "Braga", "Coimbra", "Évora"]


def grelha_solucoes():
    sols = []
    for cv in itertools.permutations(CONVES):
        for at in itertools.permutations(ATIV):
            for og in itertools.permutations(ORIG):
                P = {n: dict(c=cv[i], a=at[i], o=og[i]) for i, n in enumerate(NOMES)}
                by = lambda k, v: next(n for n in NOMES if P[n][k] == v)
                ok = (
                    # 1
                    P["Alice"]["c"] < P["Glória"]["c"]
                    and P["Glória"]["a"] == "restaurante"
                    # 2
                    and P[by("o", "Faro")]["a"] == "spa"
                    # 3
                    and P["Fausto"]["c"] == 3
                    # 4
                    and P[by("a", "casino")]["c"] == P[by("o", "Braga")]["c"] - 1
                    # 5
                    and P["Diana"]["o"] not in ("Porto", "Faro", "Braga")
                    and P["Diana"]["a"] not in ("teatro", "biblioteca", "spa")
                    # 6
                    and P[by("o", "Coimbra")]["c"] == 7
                    # 7
                    and P["Bruno"]["c"] > P[by("o", "Coimbra")]["c"]
                    # 8
                    and P[by("a", "teatro")]["o"] == "Porto"
                    # 9
                    and P["Fausto"]["a"] != "spa"
                    # 10
                    and P[by("o", "Coimbra")]["a"] != "casino"
                )
                if ok:
                    sols.append(P)
    return sols


if __name__ == "__main__":
    print(cesar("ABC XYZ", 3))
    s = grelha_solucoes()
    print(len(s), s[:1])
