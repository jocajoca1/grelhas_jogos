"""Gera o livro 'PULSO — O Jornal dos Enigmas' (HTML pronto a imprimir em A4)."""
import puzzles as P

# ------------------------------------------------------------------ dados dos desafios
CESAR_MSG = "A REDE MOVEL E O WIFI DO RECINTO ESTIVERAM EM BAIXO DAS NOVE AS DEZ DA NOITE"
SOPA_MSG = "OSACODESALESTAVANOBOLSODEUMCASACO"
SOPA_PAL = ["PICANTE", "MALAGUETA", "PANELA", "CEBOLA", "FEIJAO", "TOMATE", "COENTROS", "ALHO",
            "JURADO", "CONCURSO", "ROULOTTE", "COLHER", "PIMENTA", "CARNE", "LIMAO", "CHILI",
            "TACHO", "MOLHO", "FOGAO", "PIMENTO", "CHEF", "TACOS", "ARROZ"]
SUD_MARCAS = [(0, 5), (2, 1), (3, 4), (5, 2)]
LAB_MSG = "OLADRAOSAIUNAESTACAODASFLORES"
BIN_MSG = "CORUJA NA FILA TRES"
VIG_MSG = "ESTIVE EM TODAS AS EDICOES DESTE JORNAL"
VIG_CHAVE = "NOTICIA"

sopa_g, sopa_usadas = P.sopa(SOPA_PAL, SOPA_MSG, n=10, seed=7)
sud_puz, sud_sol = P.sudoku(SUD_MARCAS, [2, 3, 1, 4], seed=5, min_pistas=15)
lab_aberto, lab_cam, lab_let = P.labirinto(8, 8, LAB_MSG, seed=4)
assert len(P.grelha_solucoes()) == 1
assert P.vigenere(P.vigenere(VIG_MSG, VIG_CHAVE), VIG_CHAVE, -1) == VIG_MSG

ANAGRAMAS = [  # (palavra, letra assinalada (1-based), baralhada, pista)
    ("CAVALETE", 1, "VELTACEA", "Suporte de madeira onde se pousa a tela"),
    ("PALETA", 2, "TALEPA", "Tábua onde o pintor mistura as cores"),
    ("PINCEL", 3, "CLIPEN", "Tem pelos e espalha a tinta"),
    ("GUACHE", 5, "CHAGUE", "Tinta opaca que se dilui em água"),
    ("MOLDURA", 2, "RUMLODA", "Caixilho que rodeia o quadro"),
    ("RETRATO", 3, "TATORRE", "Pintura do rosto de alguém"),
    ("ESBOCO", 4, "COBOSE", "Desenho rápido, antes da obra final"),
]
assert "".join(w[i - 1] for w, i, *_ in ANAGRAMAS) == "CANHOTO"
for w, i, b, _ in ANAGRAMAS:
    assert sorted(w) == sorted(b), w

# ------------------------------------------------------------------ estilos
CSS = r"""
@page { size: A4; margin: 0; }
:root { --ink:#111; --paper:#fffdf8; --acc:#ff2e88; --acc2:#ffd60a; --soft:#fff0f7; }
* { box-sizing: border-box; }
html, body { margin:0; padding:0; background:#d9d9d9; color:var(--ink);
  font-family: 'Inter', 'Helvetica Neue', Arial, sans-serif; font-size: 9.6pt; line-height:1.38; }
.page { font-size:9.6pt; width:210mm; height:297mm; margin:8mm auto; background:var(--paper); position:relative;
  padding:11mm 12mm 12mm; overflow:hidden; page-break-after:always; break-after:page;
  box-shadow:0 2px 14px rgba(0,0,0,.18); }
@media print { html, body { background:none; } .page { margin:0; box-shadow:none; } }
h1,h2,h3,.disp { font-family:'Archivo Black','Arial Black',Impact,sans-serif; font-weight:400; margin:0; }
.mono { font-family:'Space Mono','Courier New',monospace; }
p { margin:0 0 2.2mm; }

/* cabeçalho */
.mast { display:flex; align-items:stretch; border-bottom:3px solid var(--ink); padding-bottom:2mm; margin-bottom:3mm; }
.logo { font-family:'Archivo Black',sans-serif; font-size:4.792em; line-height:.9; letter-spacing:-2px;
  background:var(--ink); color:#fff; padding:2mm 4mm 1mm; }
.logo span { color:var(--acc); }
.mast-mid { flex:1; padding:0 4mm; display:flex; flex-direction:column; justify-content:center; }
.slogan { font-weight:800; text-transform:uppercase; letter-spacing:2px; font-size:0.833em; color:var(--acc); }
.edinfo { font-size:0.833em; margin-top:1mm; }
.nivel { text-align:right; display:flex; flex-direction:column; justify-content:center; }
.nivel b { font-family:'Archivo Black'; font-size:0.938em; text-transform:uppercase; }
.dots { display:flex; gap:1.2mm; margin-top:1mm; justify-content:flex-end; }
.dots i { width:3.4mm; height:3.4mm; border-radius:50%; border:1.5px solid var(--ink); display:block; }
.dots i.on { background:var(--acc); border-color:var(--acc); }
.ticker { background:var(--acc2); font-weight:800; font-size:0.833em; text-transform:uppercase; letter-spacing:.5px;
  padding:1.3mm 3mm; margin-bottom:3mm; }
.ticker em { font-style:normal; background:var(--ink); color:var(--acc2); padding:0 2mm; margin-right:2mm; }

.kicker { display:inline-block; background:var(--acc); color:#fff; font-weight:800; text-transform:uppercase;
  font-size:0.833em; letter-spacing:1px; padding:1mm 2.5mm; margin-bottom:2mm; }
.headline { font-size:2.812em; line-height:1.02; letter-spacing:-.5px; margin-bottom:2.5mm; }
.headline .hl { background:linear-gradient(transparent 58%, var(--acc2) 58%); }
.lead { font-size:1.167em; font-weight:600; line-height:1.35; margin-bottom:3mm; border-left:5px solid var(--acc); padding-left:3mm; }
.byline { font-size:0.792em; text-transform:uppercase; letter-spacing:1px; font-weight:700; color:#555; margin-bottom:2mm; }
.byline b { color:var(--acc); }
.cols2 { column-count:2; column-gap:6mm; }
.cols3 { column-count:3; column-gap:5mm; }
.cols2 p, .cols3 p { text-align:justify; hyphens:auto; }
.grid2 { display:grid; grid-template-columns:1fr 1fr; gap:4mm; }
.grid3 { display:grid; grid-template-columns:1fr 1fr 1fr; gap:3.5mm; }
.grid-6-4 { display:grid; grid-template-columns:1.5fr 1fr; gap:4.5mm; }
.box { border:2px solid var(--ink); padding:3mm; background:#fff; break-inside:avoid; }
.box h3 { font-size:1.094em; text-transform:uppercase; margin-bottom:1.6mm; }
.box.acc { background:var(--soft); border-color:var(--acc); }
.box.yel { background:var(--acc2); }
.box.ink { background:var(--ink); color:#fff; }
.box.ink h3 { color:var(--acc2); }
.tag { display:inline-block; font-size:0.729em; font-weight:800; text-transform:uppercase; letter-spacing:1px;
  background:var(--ink); color:#fff; padding:.5mm 1.8mm; margin-bottom:1.5mm; }
.sus { display:grid; grid-template-columns:repeat(4,1fr); gap:3mm; margin-top:3mm; }
.sus .card { border:2px solid var(--ink); background:#fff; break-inside:avoid; }
.sus .card .ph { height:19mm; background:var(--acc); color:#fff; display:flex; align-items:center; justify-content:center;
  font-family:'Archivo Black'; font-size:2.083em; position:relative; }
.sus .card .ph::after { content:''; position:absolute; inset:0;
  background:repeating-linear-gradient(45deg, rgba(255,255,255,.12) 0 3px, transparent 3px 7px); }
.sus .card:nth-child(2) .ph { background:var(--ink); }
.sus .card:nth-child(3) .ph { background:var(--acc2); color:var(--ink); }
.sus .card:nth-child(4) .ph { background:#777; }
.sus .card .tx { padding:2mm; font-size:0.875em; }
.sus .card .nm { font-weight:800; font-size:0.979em; }
.sus .card .rl { font-size:0.771em; text-transform:uppercase; letter-spacing:.5px; color:var(--acc); font-weight:800; margin-bottom:1mm; }
.quote { font-style:italic; }

.desafio { border:3px solid var(--ink); background:#fff; position:relative; padding:4.5mm 4mm 3.5mm; margin-top:6mm; }
.desafio .lock { position:absolute; top:-3.6mm; left:4mm; background:var(--ink); color:#fff; font-family:'Archivo Black';
  font-size:8.6pt; padding:.8mm 3mm; text-transform:uppercase; letter-spacing:1px; white-space:nowrap; }
.desafio .lock b { color:var(--acc2); font-weight:400; }
.desafio h3 { font-size:1.354em; margin:1.5mm 0 1.5mm; }
.pergunta { background:var(--ink); color:#fff; padding:3.5mm 4mm; display:flex; gap:4mm; align-items:center; }
.pergunta .q { font-family:'Archivo Black'; font-size:1.302em; line-height:1.15; flex:1; }
.pergunta .q span { color:var(--acc2); }
.pergunta .lin { flex:1; border-bottom:1.5px dashed #fff; height:9mm; }
.fantasma { font-size:0.833em; border-top:2px dotted var(--ink); margin-top:3mm; padding-top:1.6mm; font-style:italic; }
.fantasma b { font-style:normal; }
.foot { position:absolute; bottom:5mm; left:12mm; right:12mm; display:flex; justify-content:space-between;
  font-size:0.729em; text-transform:uppercase; letter-spacing:1px; border-top:1px solid var(--ink); padding-top:1mm; }
.small { font-size:0.854em; }
.tbl { border-collapse:collapse; width:100%; font-size:0.896em; }
.tbl th, .tbl td { border:1.2px solid var(--ink); padding:1mm 1.6mm; text-align:left; }
.tbl th { background:var(--ink); color:#fff; font-weight:700; }
.tbl tr:nth-child(even) td { background:var(--soft); }
.write { display:inline-block; border-bottom:1.3px solid var(--ink); min-width:30mm; }

/* puzzles */
.cifra { font-family:'Space Mono',monospace; font-size:1.302em; letter-spacing:2px; line-height:1.7; background:var(--soft);
  padding:3mm; border:1.5px dashed var(--acc); word-spacing:4mm; }
.alfa { display:grid; grid-template-columns:repeat(26,1fr); border:1.5px solid var(--ink); margin-top:2.5mm; }
.alfa div { text-align:center; font-family:'Space Mono',monospace; font-size:0.896em; border-right:1px solid #bbb; height:5.5mm; line-height:5.5mm; }
.alfa div:last-child { border:0; }
.alfa.top div { background:var(--acc2); font-weight:700; }
.sopa { border-collapse:collapse; margin:0 auto; }
.sopa td { width:9.5mm; height:9.5mm; text-align:center; font-family:'Space Mono',monospace; font-weight:700; font-size:1.354em;
  border:1px solid #ccc; }
.sopa { border:2.5px solid var(--ink); }
.palavras { columns:2; font-family:'Space Mono',monospace; font-size:0.938em; }
.palavras div::before { content:'□ '; color:var(--acc); }
.sud { border-collapse:collapse; margin:0 auto; border:3px solid var(--ink); }
.sud td { width:13mm; height:13mm; text-align:center; font-family:'Archivo Black'; font-size:1.771em; border:1px solid #999; position:relative; }
.sud td.br { border-right:3px solid var(--ink); }
.sud tr.bb td { border-bottom:3px solid var(--ink); }
.sud td.mk { background:var(--acc2); }
.sud td.mk::before { content:attr(data-l); position:absolute; top:.5mm; left:1mm; font-family:'Inter'; font-size:0.729em; font-weight:800; color:var(--acc); }
.codebox { display:flex; gap:2mm; align-items:center; justify-content:center; font-family:'Archivo Black'; font-size:1.562em; margin-top:3mm; }
.codebox i { width:11mm; height:13mm; border:2.5px solid var(--ink); display:flex; align-items:flex-start; justify-content:flex-start;
  font-style:normal; font-family:'Inter'; font-weight:800; font-size:0.729em; color:var(--acc); padding:.5mm 1mm; background:#fff; }
.anag { display:grid; grid-template-columns:7.4em 1fr; gap:1.5mm 3mm; align-items:center; }
.anag .scr { font-family:'Space Mono',monospace; font-weight:700; font-size:1.146em; letter-spacing:1.5px; background:var(--acc2); padding:.5mm 1.5mm; text-align:center; }
.anag .cells { display:flex; gap:1mm; align-items:center; }
.anag .cells i { width:6.6mm; height:6.6mm; border:1.5px solid var(--ink); display:block; background:#fff; }
.anag .cells i.c { border-radius:50%; border:2.5px solid var(--acc); background:var(--soft); }
.anag .hint { font-size:0.812em; margin-left:2mm; color:#444; }
.bin { font-family:'Space Mono',monospace; font-size:1.094em; line-height:1.9; background:#0c0c0c; color:#39ff88; padding:3.5mm;
  letter-spacing:.5px; }
.bin .w { display:inline-block; margin-right:5mm; }
.bin .w span { margin-right:2.2mm; }
.bin .sep { color:#ff2e88; margin-right:5mm; }
.bitkey { display:flex; gap:0; margin-top:2mm; font-family:'Space Mono'; font-size:0.896em; }
.bitkey div { border:1.5px solid var(--ink); padding:1mm 2.5mm; text-align:center; }
.bitkey div b { display:block; font-size:1.146em; }
.lg { border-collapse:collapse; font-size:0.792em; }
.lg td, .lg th { border:1px solid #888; width:5.8mm; height:5.8mm; text-align:center; padding:0; }
.lg th { background:var(--soft); font-weight:700; }
.lg th.rot { height:20mm; vertical-align:bottom; }
.lg th.rot div { writing-mode:vertical-rl; transform:rotate(180deg); white-space:nowrap; margin:0 auto; padding-bottom:1mm; }
.lg th.rn { width:auto; text-align:right; padding:0 1.5mm; white-space:nowrap; }
.lg .gap { border:0; background:transparent; width:2mm; }
.lg .thick { border-left:2.5px solid var(--ink); }
.lg tr.tt td, .lg tr.tt th { border-top:2.5px solid var(--ink); }
.clues { counter-reset:c; margin:0; padding:0; list-style:none; }
.clues li { counter-increment:c; position:relative; padding-left:7mm; margin-bottom:1.6mm; }
.clues li::before { content:counter(c); position:absolute; left:0; top:0; background:var(--acc); color:#fff; font-weight:800;
  width:5mm; height:5mm; border-radius:50%; text-align:center; line-height:5mm; font-size:0.781em; }
.tabula { border-collapse:collapse; font-family:'Space Mono',monospace; font-size:0.740em; margin:0 auto; }
.tabula td { width:5.9mm; height:4.6mm; text-align:center; border:1px solid #ddd; padding:0; }
.tabula tr:first-child td, .tabula td:first-child { background:var(--ink); color:var(--acc2); font-weight:700; }
.tabula tr:nth-child(odd) td:not(:first-child) { background:#fffbe0; }

/* capa */
.capa { background:var(--ink); color:#fff; padding:0; }
.capa .stripe { height:20mm; display:flex; }
.capa .stripe div { flex:1; }
.capa .inner { padding:16mm 16mm; }
.capa .big { font-family:'Archivo Black'; font-size:12.292em; line-height:.82; letter-spacing:-6px; }
.capa .big span { color:var(--acc); }
.capa .sub { font-family:'Archivo Black'; font-size:2.292em; line-height:1.05; margin-top:6mm; }
.capa .sub em { font-style:normal; background:var(--acc2); color:var(--ink); padding:0 2mm; }
.capa .chips { display:flex; flex-wrap:wrap; gap:2.5mm; margin-top:10mm; }
.capa .chips span { border:2px solid #fff; padding:1.5mm 3mm; font-weight:800; text-transform:uppercase; font-size:0.938em; letter-spacing:1px; }
.capa .heads { margin-top:12mm; display:grid; grid-template-columns:1fr 1fr; gap:4mm; }
.capa .heads div { border-top:4px solid; padding-top:2mm; font-family:'Archivo Black'; font-size:1.146em; line-height:1.15; }
.capa .heads div small { display:block; font-family:'Inter'; font-weight:800; font-size:0.781em; letter-spacing:1.5px; margin-bottom:1mm; }
.sol h2 { font-size:1.562em; margin:0 0 1.5mm; }
.sol .item { border-left:5px solid var(--c); padding:1.5mm 0 1.5mm 3mm; margin-bottom:3mm; break-inside:avoid; }
.sol .item h3 { font-size:1.094em; margin-bottom:1mm; }
.sol .item h3 span { color:var(--c); }
.sol .ans { font-family:'Space Mono'; font-weight:700; background:#f2f2f2; padding:.4mm 1.5mm; }
"""

TEMAS = {
    1: ("#ff2e88", "#ffd60a", "#fff0f7"),
    2: ("#ff6b00", "#00d1ff", "#fff3e8"),
    3: ("#00b4d8", "#ff4fd8", "#e8fbff"),
    4: ("#4cc71e", "#ff2e88", "#f0fde9"),
    5: ("#8b3dff", "#ffd60a", "#f4edff"),
    6: ("#ff1f3d", "#39ff88", "#fff0f2"),
    7: ("#00a6a6", "#ff8a00", "#e6fafa"),
    8: ("#111111", "#ffd60a", "#fffbe0"),
}

DATAS = ["Segunda-feira, 2 de novembro de 2026", "Terça-feira, 3 de novembro de 2026",
         "Quarta-feira, 4 de novembro de 2026", "Quinta-feira, 5 de novembro de 2026",
         "Sexta-feira, 6 de novembro de 2026", "Sábado, 7 de novembro de 2026",
         "Domingo, 8 de novembro de 2026", "Segunda-feira, 9 de novembro de 2026"]


def tema(n):
    a, b, s = TEMAS[n]
    return f'style="--acc:{a};--acc2:{b};--soft:{s}"'


def mast(n, ticker):
    dots = "".join(f'<i class="{"on" if i < n else ""}"></i>' for i in range(8))
    return f"""
<div class="mast">
  <div class="logo">PUL<span{' style="color:var(--acc2)"' if n == 8 else ""}>S</span>O</div>
  <div class="mast-mid"><div class="slogan">O jornal que investiga · Edição de enigmas</div>
  <div class="edinfo"><b>N.º {n}</b> · {DATAS[n-1]} · 1,20 €</div></div>
  <div class="nivel"><b>Nível {n}</b><div class="dots">{dots}</div></div>
</div>
<div class="ticker"><em>ÚLTIMA HORA</em>{ticker}</div>"""


def foot(n, pag):
    if n == 0:
        return f'<div class="foot"><span>PULSO · O Jornal dos Enigmas</span><span>{pag}</span></div>'
    return f'<div class="foot"><span>PULSO · N.º {n}</span><span>Caso {n} de 8</span><span>{pag}</span></div>'


def suspeitos(lista):
    cards = ""
    for nome, papel, txt in lista:
        ini = "".join(p[0] for p in nome.split()[:2])
        cards += f"""<div class="card"><div class="ph">{ini}</div><div class="tx">
<div class="nm">{nome}</div><div class="rl">{papel}</div><div class="quote">{txt}</div></div></div>"""
    return f'<div class="sus">{cards}</div>'


def pergunta(q):
    return f'<div class="pergunta"><div class="q">{q}</div><div class="lin"></div></div>'


def fantasma(t):
    return f'<div class="fantasma"><b>Classificados ·</b> {t}</div>'


def alfabeto():
    top = "".join(f"<div>{c}</div>" for c in P.A)
    return f'<div class="alfa top">{top}</div><div class="alfa">{"".join("<div></div>" for _ in P.A)}</div>'


# ------------------------------------------------------------------ páginas
def capa():
    heads = [(1, "Guitarra dourada desaparece nos bastidores"), (2, "Chili sabotado no festival"),
             (3, "Óculos do futuro roubados"), (4, "Fuga pelos túneis do metro"),
             (5, "Obra-prima trocada por falsa"), (6, "Apagão na final de e-sports"),
             (7, "Colar desaparece em alto-mar"), (8, "Quem é o Fantasma?")]
    cor = lambda n: "#ffd60a" if n == 8 else TEMAS[n][0]
    hs = "".join(f'<div style="border-color:{cor(n)}"><small style="color:{cor(n)}">CASO {n} · NÍVEL {n}</small>{t}</div>' for n, t in heads)
    stripe = "".join(f'<div style="background:{cor(n)}"></div>' for n in range(1, 9))
    return f"""<section class="page capa" {tema(1)}>
<div class="stripe">{stripe}</div>
<div class="inner">
  <div class="big">PUL<span>S</span>O</div>
  <div class="sub">O JORNAL DOS ENIGMAS<br><em>8 edições · 8 crimes · 1 mistério final</em></div>
  <div class="chips"><span>Cifras</span><span>Sopa de letras</span><span>Sudoku</span><span>Labirinto</span>
  <span>Anagramas</span><span>Código binário</span><span>Grelha lógica</span><span>Vigenère</span></div>
  <div class="heads">{hs}</div>
  <div style="margin-top:16mm;border:3px solid #fff;padding:5mm 6mm;display:flex;gap:6mm;align-items:center">
   <div style="font-size:34pt">👻</div>
   <div><div class="disp" style="font-size:16pt;line-height:1.1">Sete crimes. Uma só mão nas sombras.</div>
   <div style="margin-top:1.5mm;font-size:10pt">Resolve cada caso, desbloqueia cada pista e desmascara o Fantasma na última edição.
   Dificuldade crescente, do nível 1 ao 8. Soluções no fim.</div></div>
  </div>
</div></section>"""


def instrucoes():
    linhas = "".join(f"<tr><td><b>{n}</b></td><td></td><td></td><td></td></tr>" for n in range(1, 8))
    return f"""<section class="page" {tema(8)}>
<div class="kicker">Antes de começar</div>
<h1 class="headline">Bem-vindo à redação do <span class="hl">PULSO</span></h1>
<p class="lead">Durante oito dias, o PULSO cobriu oito crimes. Cada edição traz a notícia, os suspeitos, as declarações
e as pistas — tudo o que precisas para descobrir o culpado está nas páginas do próprio jornal.</p>
<div class="grid2">
 <div class="box"><h3>🔓 O desafio de acesso</h3><p>Em cada caso há uma pista que está trancada: um bilhete cifrado,
 uma sopa de letras, um sudoku, um labirinto… Tens de resolver esse desafio para obter a informação que falta.
 Sem ele, há sempre mais de um suspeito possível.</p></div>
 <div class="box"><h3>📈 Dificuldade crescente</h3><p>O caso 1 é um aquecimento. A partir daí, cada edição sobe um nível:
 os desafios ficam mais exigentes e as pistas mais escondidas, entre fotografias, horários, mapas e até na secção de desporto.</p></div>
 <div class="box"><h3>🧠 Como investigar</h3><p>Lê tudo — legendas, caixas laterais, classificados e assinaturas dos artigos.
 Confirma os álibis, procura contradições e só depois aponta o culpado.</p></div>
 <div class="box yel"><h3>👻 O mistério final</h3><p>Alguém anda a dar ordens nas sombras. Guarda bem o <b>nome de cada culpado</b> no caderno abaixo:
 vais precisar de todos para o caso 8.</p></div>
</div>
<div class="box" style="margin-top:4mm"><h3>📓 Caderno do detetive</h3>
<table class="tbl"><tr><th style="width:12mm">Caso</th><th>Resposta do desafio</th><th>Culpado</th><th style="width:22mm">Inicial</th></tr>
{linhas}</table></div>
<p class="small" style="margin-top:3mm">As soluções completas, com o raciocínio passo a passo, estão no fim do livro. Não espreites! 😉</p>
{foot(0, "Instruções")}</section>"""


# ---------------- CASO 1
def caso1():
    n = 1
    cif = P.cesar(CESAR_MSG, 3)
    return f"""<section class="page" {tema(n)}>
{mast(n, "Festival Som do Rio · 40 mil pessoas no recinto · Concerto de Lia Montes atrasou-se 45 minutos")}
<div class="kicker">Festival Som do Rio</div>
<h1 class="headline">Guitarra dourada de Lia Montes <span class="hl">desaparece</span> dos bastidores</h1>
<p class="lead">Instrumento avaliado em 80 mil euros desapareceu da tenda dos artistas minutos antes do concerto principal.
Só quatro pessoas tinham pulseira de acesso à zona.</p>
<div class="byline">Por <b>Paulo Tinta</b> · enviado especial</div>
<div class="cols2">
<p>Eram 21h00 quando Lia Montes pousou a famosa guitarra dourada no suporte da tenda dos bastidores e saiu para a
entrevista com a rádio do festival. Quando voltou, às 21h30, o suporte estava vazio. "Pensei que alguém da equipa a tinha
levado para o palco. Ninguém a tinha levado", contou ao PULSO, ainda em lágrimas.</p>
<p>A tenda fica atrás do palco principal e só se entra com uma pulseira dourada. Segundo a organização, entre as 21h00
e as 21h30 apenas quatro pessoas tinham essa pulseira e estavam no recinto: o técnico de palco, a agente da artista,
o guitarrista de outra banda do cartaz e a fotógrafa oficial.</p>
<p>O chefe de segurança, Armando Faria, registou tudo o que de estranho aconteceu nessa noite num bilhete que entregou à
polícia. Como manda o regulamento do festival, as notas de segurança são escritas em código, para que os curiosos não as
consigam ler. O PULSO teve acesso a esse bilhete e publica-o na página seguinte.</p>
<p>O concerto acabou por começar às 22h15, com uma guitarra emprestada. A polícia não exclui que a guitarra ainda esteja
no recinto, escondida num dos carros do parque de estacionamento dos artistas.</p>
</div>
{suspeitos([
 ("Rui Peixoto", "Técnico de palco", "“Às 21h15 estava em cima do palco a afinar a bateria. Toda a gente me viu.”"),
 ("Natália Sol", "Agente da artista", "“Estive no parque de estacionamento, ao telemóvel com a editora, das 21h00 às 21h30.”"),
 ("Duarte Leal", "Guitarrista rival", "“Estava na roulotte das bifanas, a tirar selfies com fãs. Eu? Roubar? Tenho a minha.”"),
 ("Inês Cabral", "Fotógrafa oficial", "“Passei a meia hora na torre de luzes a fotografar o público. As minhas fotos têm hora.”"),
])}
{foot(n, "Página 1")}</section>

<section class="page" {tema(n)}>
<div class="grid-6-4">
 <div>
  <div class="box acc"><span class="tag">Exclusivo</span><h3>📸 O cartão de memória da Inês</h3>
  <p class="small">A polícia analisou as fotografias tiradas pela fotógrafa oficial. A hora está gravada em cada ficheiro.</p>
  <table class="tbl"><tr><th>Hora</th><th>O que mostra a foto</th></tr>
  <tr><td>21:04</td><td>O público a acender as lanternas dos telemóveis, visto de cima da torre de luzes.</td></tr>
  <tr><td>21:12</td><td>Rui Peixoto em cima do palco, a ajustar os pratos da bateria.</td></tr>
  <tr><td>21:18</td><td>Duarte Leal rodeado de fãs junto à roulotte das bifanas.</td></tr>
  <tr><td>21:26</td><td>Panorâmica da multidão tirada do topo da torre de luzes.</td></tr></table></div>
  <div class="desafio"><div class="lock">🔓 Desafio de acesso <b>· Cifra de César</b></div>
  <h3>O bilhete do chefe de segurança</h3>
  <p class="small">Cada letra foi trocada pela letra que está <b>três posições à frente</b> no alfabeto (A→D, B→E, C→F… X→A, Y→B, Z→C).
  Faz o caminho ao contrário para ler a mensagem.</p>
  <div class="cifra">{cif}</div>
  {alfabeto()}
  <p class="small" style="margin-top:2mm">Mensagem: <span class="write" style="min-width:100%;display:block;height:7mm"></span>
  <span class="write" style="min-width:100%;display:block;height:7mm"></span></p>
  </div>
 </div>
 <div>
  <div class="box"><h3>🎸 Bastidores</h3><div class="byline">Por <b>Sofia Letra</b></div>
  <p class="small">Lia Montes tocou com uma guitarra emprestada por um fã de 15 anos, que subiu ao palco no encore.
  "Foi o melhor dia da minha vida", disse o jovem. A organização garante que, para o ano, a tenda dos bastidores terá câmaras.</p></div>
  <div class="box yel" style="margin-top:3.5mm"><h3>☀️ O tempo</h3><div class="byline">Por <b>Vera Pena</b></div>
  <p class="small">Noite amena junto ao rio, 19 °C. Céu limpo, vento fraco. Ideal para festivais — e para quem quer
  passar despercebido no meio da multidão.</p></div>
  <div class="box" style="margin-top:3.5mm"><h3>📶 Nota da organização</h3>
  <p class="small">O festival pede desculpa aos visitantes pelas "falhas técnicas" de sábado à noite e promete reforçar
  os equipamentos para a próxima edição.</p></div>
  {fantasma("Procura-se pessoa discreta para trabalhos bem pagos. Não faça perguntas. Resposta ao apartado 13, a/c <b>O Fantasma</b>.")}
 </div>
</div>
<div style="margin-top:4mm">{pergunta('A tua investigação: <span>quem levou a guitarra dourada?</span> E qual foi a mentira que o denunciou?')}</div>
{foot(n, "Página 2")}</section>"""


# ---------------- CASO 2
def caso2():
    n = 2
    linhas = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in sopa_g)
    pal = "".join(f"<div>{w}</div>" for w in sorted(w for w, *_ in sopa_usadas))
    return f"""<section class="page" {tema(n)}>
{mast(n, "Festival de Food Trucks do Parque Verde · 32 roulottes · Concurso Chili de Ouro termina em escândalo")}
<div class="kicker">Concurso Chili de Ouro</div>
<h1 class="headline">Chili favorito <span class="hl">sabotado</span> com meio quilo de sal</h1>
<p class="lead">Tó Brasa, bicampeão do concurso, viu os jurados cuspirem o seu chili. Alguém despejou sal na panela
nos vinte minutos em que ficou sem vigilância.</p>
<div class="byline">Por <b>Sofia Letra</b></div>
<div class="cols2">
<p>O Festival de Food Trucks do Parque Verde tinha tudo para correr bem: sol, filas enormes e um concurso de chili
com prémio de cinco mil euros. O favorito era Tó Brasa, da roulotte "Fogo Lento", que procurava o terceiro título seguido.</p>
<p>Às 13h00, Tó deixou a panela a borbulhar e foi buscar gelo ao camião frigorífico, do outro lado do parque. Voltou às 13h20.
Às 14h00, os três jurados provaram o chili e fizeram uma careta. "Estava intragável. Parecia água do mar", disse um deles.</p>
<p>Na tampa da panela ficaram grãos de sal grosso. Tó jura que só usa flor de sal e "nunca mais do que uma pitada". Perto da
"Fogo Lento" estavam quatro roulottes de cozinheiros que também concorriam ao prémio.</p>
<p>A única testemunha é a pequena Rita, de 9 anos, que estava na fila das farturas: "Vi uma pessoa vestida de azul a mexer
na panela do senhor Tó. Não vi a cara, só a roupa azul." A polícia não encontrou o saco do sal — mas um dos voluntários
da limpeza encontrou algo curioso: um papel amarrotado com uma sopa de letras, deixado pela própria Rita, que garante
ter "escondido lá o que viu a seguir".</p>
</div>
{suspeitos([
 ("Bela Couto", "Taco Loco · avental vermelho", "“Disse que o Tó ia provar do próprio veneno? Era uma piada!”"),
 ("Octávio Reis", "Burger Bomba · casaco azul", "“Passei por lá para lhe dar os parabéns adiantados. Só isso.”"),
 ("Kátia Pires", "Wok & Roll · casaco amarelo", "“Estive o tempo todo a saltear massa no wok. Tenho 40 clientes como testemunhas.”"),
 ("Filipe Moura", "Crepe Lab · avental azul", "“Fui pedir açúcar emprestado ao Tó. Ele não estava, vim-me embora.”"),
])}
{foot(n, "Página 1")}</section>

<section class="page" {tema(n)}>
<div class="desafio" style="margin-top:2mm"><div class="lock">🔓 Desafio de acesso <b>· Sopa de letras</b></div>
<h3>A sopa de letras da Rita</h3>
<p class="small">Encontra as 13 palavras da lista (na horizontal, vertical ou diagonal; algumas estão escritas ao contrário).
Depois, <b>lê as letras que não usaste, linha a linha, da esquerda para a direita</b>: formam a mensagem secreta da Rita.</p>
<div class="grid-6-4" style="align-items:center">
 <table class="sopa">{linhas}</table>
 <div><div class="palavras">{pal}</div>
 <p class="small" style="margin-top:3mm"><b>Mensagem da Rita:</b></p>
 <span class="write" style="display:block;height:7mm;min-width:100%"></span>
 <span class="write" style="display:block;height:7mm;min-width:100%"></span>
 <span class="write" style="display:block;height:7mm;min-width:100%"></span></div>
</div></div>
<div class="grid3" style="margin-top:4mm">
 <div class="box"><h3>🌶️ Os números</h3><p class="small">32 roulottes · 11 mil visitantes · 640 litros de chili ·
 1 panela sabotada. O prémio foi entregue a Kátia Pires, com um chili de caril vermelho.</p></div>
 <div class="box acc"><h3>🗣️ Opinião</h3><div class="byline">Por <b>Henrique Prelo</b></div>
 <p class="small">Um concurso de cozinha devia ser uma festa. Que um prato seja destruído por inveja diz muito sobre a pressão
 destes eventos. A organização prometeu vigilância nas próximas edições.</p></div>
 <div class="box yel"><h3>✨ Horóscopo</h3><div class="byline">Por <b>Vera Pena</b></div>
 <p class="small"><b>Balança:</b> o equilíbrio é tudo — até no sal. <b>Escorpião:</b> quem esconde algo no bolso acaba
 por ser apanhado. <b>Peixes:</b> dia ótimo para ouvir as crianças.</p></div>
</div>
{fantasma("Agradecemos a quem respondeu ao anúncio de ontem. O primeiro trabalho correu bem. — <b>O Fantasma</b>")}
<div style="margin-top:3mm">{pergunta('A tua investigação: <span>quem salgou o chili de Tó Brasa?</span>')}</div>
{foot(n, "Página 2")}</section>"""


# ---------------- CASO 3
def caso3():
    n = 3
    letras = {m: "ABCD"[i] for i, m in enumerate(SUD_MARCAS)}
    linhas = ""
    for r in range(6):
        tds = ""
        for c in range(6):
            v = sud_puz[r][c]
            cls = []
            if c == 2:
                cls.append("br")
            if (r, c) in letras:
                cls.append("mk")
            dl = f' data-l="{letras[(r, c)]}"' if (r, c) in letras else ""
            tds += f'<td class="{" ".join(cls)}"{dl}>{v if v else ""}</td>'
        linhas += f'<tr class="{"bb" if r in (1, 3) else ""}">{tds}</tr>'
    return f"""<section class="page" {tema(n)}>
{mast(n, "NovaTech suspende apresentação mundial · Ações da empresa caem 12% · Polícia Judiciária no local")}
<div class="kicker">Tecnologia</div>
<h1 class="headline">Óculos do futuro <span class="hl">roubados</span> do cofre da NovaTech</h1>
<p class="lead">O protótipo Visio-1, uns óculos inteligentes que valiam milhões, desapareceu do cofre do laboratório
na véspera da apresentação. O cofre não foi forçado.</p>
<div class="byline">Por <b>Paulo Tinta</b></div>
<div class="cols2">
<p>Na sede da NovaTech, em Lisboa, o laboratório 3 é o lugar mais vigiado do edifício. Só se entra com cartão e cada entrada
e saída fica registada. Dentro do laboratório está o cofre onde se guardava o Visio-1, que ia ser apresentado ao mundo na
manhã seguinte.</p>
<p>Na noite do roubo, quatro pessoas da equipa estiveram no laboratório a preparar a apresentação. O cofre tem um teclado
que só funciona por dentro e o código era conhecido pelos quatro. Às 8h00, o cofre estava vazio.</p>
<p>O cofre regista a hora exata em que é aberto. Mas o engenheiro de segurança, Jorge Viegas, conhecido pelo amor aos
enigmas, configurou o sistema para que o relatório nunca mostre a hora em claro: a hora é escondida dentro de um sudoku
gerado pelo próprio cofre. "Assim, quem roubar o relatório não percebe nada", explicou. Na noite do roubo, o cofre só foi
aberto uma vez.</p>
<p>A polícia não encontrou impressões digitais no teclado. "Quem fez isto conhecia bem a casa", disse o inspetor responsável.</p>
</div>
{suspeitos([
 ("Sara Vidal", "Designer", "“Saí para jantar e voltei só para ir buscar o casaco. Nem olhei para o cofre.”"),
 ("Hugo Matos", "Programador", "“Aquela publicação dos óculos novos? Comprei uns de sol, juro!”"),
 ("Telma Ferraz", "Eng.ª de hardware", "“Estive a soldar placas. Quando estou concentrada nem dou por quem entra.”"),
 ("Tiago Alves", "Estagiário", "“Fui o último a sair. Apaguei as luzes, como sempre.”"),
])}
{foot(n, "Página 1")}</section>

<section class="page" {tema(n)}>
<div class="grid2">
 <div class="desafio" style="margin-top:2mm"><div class="lock">🔓 Desafio de acesso <b>· Sudoku 6×6</b></div>
 <h3>O relatório do cofre</h3>
 <p class="small">Preenche a grelha com os números de 1 a 6, sem repetir em nenhuma linha, coluna ou retângulo de 2×3.
 As casas amarelas <b>A, B, C, D</b> dão a hora de abertura do cofre: <b>AB:CD</b>.</p>
 <table class="sud">{linhas}</table>
 <div class="codebox"><i>A</i><i>B</i><span>:</span><i>C</i><i>D</i></div>
 </div>
 <div>
  <div class="box acc"><span class="tag">Documento</span><h3>🪪 Registo de cartões — Laboratório 3</h3>
  <table class="tbl"><tr><th>Nome</th><th>Entrada</th><th>Saída</th></tr>
  <tr><td>Sara Vidal</td><td>22:05</td><td>22:50</td></tr>
  <tr><td>Hugo Matos</td><td>22:30</td><td>23:10</td></tr>
  <tr><td>Telma Ferraz</td><td>22:55</td><td>23:30</td></tr>
  <tr><td>Tiago Alves</td><td>23:20</td><td>23:50</td></tr>
  <tr><td>Sara Vidal</td><td>23:35</td><td>23:45</td></tr></table>
  <p class="small" style="margin-top:1.5mm">A porta tranca-se sozinha: ninguém entra sem o próprio cartão.</p></div>
  <div class="box" style="margin-top:3.5mm"><h3>💻 O que é o Visio-1?</h3><div class="byline">Por <b>Vera Pena</b></div>
  <p class="small">Uns óculos que mostram legendas em tempo real de qualquer conversa, em 40 línguas. Pesam 38 gramas e
  têm bateria para dois dias. A concorrência estaria disposta a pagar fortunas para ver o protótipo por dentro.</p></div>
  <div class="box yel" style="margin-top:3.5mm"><h3>☁️ O tempo</h3><div class="byline">Por <b>Sofia Letra</b></div>
  <p class="small">Nevoeiro cerrado à noite na zona ribeirinha. Visibilidade quase nula depois das 23h.</p></div>
 </div>
</div>
<div class="box" style="margin-top:4mm"><h3>📱 Nas redes</h3>
<p class="small"><b>@hugo.codes</b> (publicado às 19h02): "Em breve vou ter uns óculos novos 😎 #mudança" — a publicação foi apagada na manhã seguinte.</p></div>
{fantasma("Segundo trabalho concluído. Os óculos já viajam. Próximo encontro: debaixo da cidade. — <b>O Fantasma</b>")}
<div style="margin-top:3mm">{pergunta('A tua investigação: <span>quem abriu o cofre e levou o Visio-1?</span>')}</div>
{foot(n, "Página 2")}</section>"""


# ---------------- CASO 4
def lab_svg():
    cs, w, h, m = 17, 8, 8, 20
    out = [f'<svg viewBox="0 0 {w*cs+2*m+12} {h*cs+8}" width="{(w*cs+2*m+12)*0.62}mm" xmlns="http://www.w3.org/2000/svg" style="display:block;margin:0 auto">']
    for x in range(w):
        for y in range(h):
            px, py = m + x * cs, 4 + y * cs
            out.append(f'<text x="{px+cs/2}" y="{py+cs/2+4.2}" text-anchor="middle" font-family="Space Mono, monospace" font-weight="700" font-size="11" fill="#111">{lab_let[(x,y)]}</text>')
    seg = []
    for x in range(w):
        for y in range(h):
            px, py = m + x * cs, 4 + y * cs
            if x + 1 < w and frozenset([(x, y), (x + 1, y)]) not in lab_aberto:
                seg.append((px + cs, py, px + cs, py + cs))
            if y + 1 < h and frozenset([(x, y), (x, y + 1)]) not in lab_aberto:
                seg.append((px, py + cs, px + cs, py + cs))
    W, H, T = m + w * cs, 4 + h * cs, 4
    seg += [(m, T, W, T), (m, H, W, H), (m, T + cs, m, H), (W, T, W, H - cs)]
    for a, b, c, d in seg:
        out.append(f'<line x1="{a}" y1="{b}" x2="{c}" y2="{d}" stroke="#111" stroke-width="2.4" stroke-linecap="square"/>')
    out.append(f'<path d="M{m-14} {4+cs/2} l11 0 m-3 -3 l3 3 l-3 3" stroke="var(--acc)" stroke-width="2" fill="none"/>')
    out.append(f'<text x="{m-15}" y="{4+cs/2-4}" font-size="5.5" font-family="Inter" font-weight="800" fill="#111">BANCO</text>')
    out.append(f'<path d="M{W+2} {H-cs/2} l9 0 m-3 -3 l3 3 l-3 3" stroke="var(--acc)" stroke-width="2" fill="none"/>')
    out.append(f'<text x="{W+3}" y="{H-cs/2-4}" font-size="6" font-family="Inter" font-weight="800" fill="#111">SAÍDA</text>')
    out.append("</svg>")
    return "".join(out)


def caso4():
    n = 4
    return f"""<section class="page" {tema(n)}>
{mast(n, "Banco Atlântico encerrado para perícias · Metro com perturbações na linha verde · Investigação em curso")}
<div class="kicker">Crime na Baixa</div>
<h1 class="headline">Ladrão esvazia cofre do Banco Atlântico e <span class="hl">foge pelos túneis</span> do metro</h1>
<p class="lead">Um assaltante abriu um buraco na cave do banco, levou 300 mil euros em barras de ouro e desapareceu
na rede de túneis de manutenção que corre por baixo da cidade.</p>
<div class="byline">Por <b>Vera Pena</b></div>
<div class="cols2">
<p>O alarme do Banco Atlântico disparou às 22h30 de quarta-feira. Quando a polícia chegou, encontrou um buraco aberto na
parede da cave, que dá diretamente para um antigo túnel de manutenção do metro. As barras de ouro tinham desaparecido.</p>
<p>A rede de túneis é um verdadeiro labirinto: dezenas de galerias, a maioria sem saída. Só um caminho liga a cave do banco
a uma estação. A polícia mapeou os túneis com um drone e o PULSO publica esse mapa na página seguinte. Os técnicos
encontraram, pintadas nas paredes do caminho certo, letras deixadas a giz pelo próprio ladrão para não se perder. As
paredes das galerias sem saída estão cheias de letras antigas, de outras obras.</p>
<p>A polícia recolheu as imagens das câmaras das quatro estações ligadas aos túneis. Por volta das 22h50, todas registaram
alguém de capuz a sair para a rua — o que, numa quarta à noite, não é nada raro. As descrições estão na caixa ao lado.</p>
<p>Quatro pessoas estão a ser investigadas. Todas conheciam o banco, todas sabiam da existência dos túneis e nenhuma tem
álibi confirmado: as quatro dizem ter passado a noite sozinhas, em casa.</p>
</div>
{suspeitos([
 ("Igor Santos", "Técnico do metro", "“Vivo junto à estação das Flores. Estava em casa a ver futebol.”"),
 ("Paula Mendes", "Ex-gerente do banco", "“Também moro perto das Flores. Deitei-me cedo, estava cansada.”"),
 ("Marco Freitas", "Estafeta do banco", "“Moro mesmo ao lado da estação do Cais. Não saí de casa.”"),
 ("Rosa Lemos", "Limpezas do banco", "“Vivo na Alameda. Passei a noite a fazer malha, como sempre.”"),
])}
{foot(n, "Página 1")}</section>

<section class="page" {tema(n)}>
<div class="grid-6-4" style="grid-template-columns:1.75fr 1fr">
 <div class="desafio" style="margin-top:2mm"><div class="lock">🔓 Desafio de acesso <b>· Labirinto</b></div>
 <h3>O mapa dos túneis</h3>
 <p class="small">Entra pela cave do banco (canto superior esquerdo) e encontra o único caminho até à saída.
 <b>Lê as letras por onde passas</b>, pela ordem: dizem-te onde o ladrão voltou à superfície.</p>
 {lab_svg()}
 <p class="small" style="margin-top:2mm"><b>Mensagem:</b> <span class="write" style="display:block;height:7mm;min-width:100%"></span></p>
 </div>
 <div>
  <div class="box acc"><span class="tag">Câmaras · 22h50</span><h3>🎥 Quem saiu das estações</h3>
  <p class="small"><b>Flores:</b> pessoa de capuz cinzento, mochila pesada, a coxear da perna esquerda.<br>
  <b>Cais:</b> pessoa alta de capuz preto, saco de desporto, a coxear da perna direita.<br>
  <b>Alameda:</b> pessoa baixa, de chapéu de chuva aberto, sem mochila.<br>
  <b>Rossio:</b> um casal de turistas com malas de rodinhas.</p></div>
  <div class="box" style="margin-top:3.5mm"><h3>🚲 Cidade</h3><div class="byline">Por <b>Paulo Tinta</b></div>
  <p class="small">Mais um acidente de bicicleta na ciclovia da Avenida: o estafeta Marco Freitas caiu na segunda-feira e magoou
  o joelho direito. "Continuo a trabalhar, mas a coxear", contou.</p></div>
  <div class="box yel" style="margin-top:3.5mm"><h3>⚽ Desporto</h3><div class="byline">Por <b>Sofia Letra</b></div>
  <p class="small"><b>Futsal:</b> Igor Santos, guarda-redes da equipa do Metro, torceu o tornozelo esquerdo no jogo de domingo
  e vai estar três semanas parado.<br><b>Atletismo:</b> Paula Mendes terminou a meia-maratona de domingo em 1h42, recorde pessoal.
  "Acabei sem uma única dor", garantiu.</p></div>
 </div>
</div>
{fantasma("O ouro está guardado. Quem conhece os túneis nunca se perde. — <b>O Fantasma</b>")}
<div style="margin-top:3mm">{pergunta('A tua investigação: <span>quem assaltou o cofre do Banco Atlântico?</span>')}</div>
{foot(n, "Página 2")}</section>"""


# ---------------- CASO 5
def caso5():
    n = 5
    an = ""
    for w, i, b, hint in ANAGRAMAS:
        cells = "".join(f'<i class="{"c" if k == i - 1 else ""}"></i>' for k in range(len(w)))
        an += f'<div class="scr">{b}</div><div class="cells">{cells}<span class="hint">{hint}</span></div>'
    return f"""<section class="page" {tema(n)}>
{mast(n, "Galeria Prisma reabre amanhã · Seguradora pede peritagem a todas as obras · Artista Joana Vaz “devastada”")}
<div class="kicker">Cultura</div>
<h1 class="headline">Obra-prima <span class="hl">trocada por uma falsa</span> em plena inauguração</h1>
<p class="lead">O quadro "Mar Elétrico", de Joana Vaz, foi substituído por uma cópia durante a festa de abertura da
Galeria Prisma. Ninguém deu pela troca até à manhã seguinte.</p>
<div class="byline">Por <b>Sofia Letra</b></div>
<div class="cols2">
<p>Foi a curadora Amélia Duarte, 74 anos e meio século de museus, quem deu o alarme. "Bastou-me um minuto a olhar para aquele
azul. Não era o quadro da Joana", disse. A cópia é muito boa: foi pintada com calma, dias antes, e trocada pelo original
durante a festa.</p>
<p>As câmaras da galeria mostram o momento: às 20h30, as luzes baixaram para o discurso do dono da galeria e, durante dois
minutos, a sala do "Mar Elétrico" ficou às escuras. Quando as luzes voltaram, o quadro na parede já era a cópia.</p>
<p>Amélia examinou a falsificação durante toda a manhã: as pinceladas, a assinatura, a direção dos traços. Escreveu a sua
conclusão no caderno, mas fê-lo à sua maneira: em anagramas, um velho hábito para que ninguém leia as suas notas por cima
do ombro. "A conclusão diz-vos como era a mão que pintou a cópia. O resto é com a polícia", disse ao PULSO.</p>
<p>Quatro convidados com formação em pintura estavam na festa e são suspeitos de ter pintado a cópia e feito a troca.</p>
</div>
{suspeitos([
 ("Gaspar Nunes", "Dono da galeria", "“Estava no palco a discursar, à frente de 200 pessoas. Há vídeo.”"),
 ("Cecília Rocha", "Restauradora", "“Restauro quadros, não os falsifico. Estive no bar a noite toda.”"),
 ("Bernardo Lima", "Pintor rival", "“A Joana pinta bem, admito. Mas eu não preciso de copiar ninguém.”"),
 ("Teresa Gomes", "Crítica de arte", "“Estive a tomar notas para a minha crónica. Nada me escapa.”"),
])}
{foot(n, "Página 1")}</section>

<section class="page" {tema(n)}>
<div class="grid-6-4">
 <div class="desafio" style="margin-top:2mm"><div class="lock">🔓 Desafio de acesso <b>· Anagramas</b></div>
 <h3>O caderno da curadora</h3>
 <p class="small">Volta a pôr por ordem as letras de cada palavra (todas são do mundo da pintura) e escreve-a nas casas.
 Depois, <b>lê de cima para baixo as letras que ficam nos círculos</b>: é a conclusão de Amélia.</p>
 <div class="anag">{an}</div>
 <p class="small" style="margin-top:3mm"><b>Conclusão:</b> a cópia foi pintada por alguém… <span class="write" style="min-width:45mm"></span></p>
 </div>
 <div>
  <div class="box acc"><span class="tag">Fotogaleria</span><h3>📷 A noite em imagens</h3>
  <p class="small"><b>1.</b> Gaspar Nunes ergue o copo com a mão esquerda no brinde final. É canhoto, "como Leonardo da Vinci",
  gosta de lembrar.<br><b>2.</b> Cecília Rocha assina o livro de honra da galeria, de caneta na mão esquerda.<br>
  <b>3.</b> Teresa Gomes toma notas no seu bloco, com a mão direita, encostada a uma coluna.<br>
  <b>4.</b> Bernardo Lima mostra aos convidados a mão direita manchada de tinta azul.</p></div>
  <div class="box" style="margin-top:3.5mm"><h3>🎨 Entrevista</h3><div class="byline">Por <b>Paulo Tinta</b></div>
  <p class="small"><b>Bernardo Lima:</b> "Pinto com a direita desde os quatro anos. Hoje vim direto do atelier, por isso trago a mão
  assim, azul. O azul é a minha cor."</p></div>
  <div class="box yel" style="margin-top:3.5mm"><h3>📅 Agenda cultural</h3><div class="byline">Por <b>Vera Pena</b></div>
  <p class="small">Sábado: concerto de jazz no Jardim Novo. Domingo: final do torneio de e-sports Pixel Arena, no Pavilhão Azul.
  Bilhetes quase esgotados.</p></div>
 </div>
</div>
<div class="box" style="margin-top:3.5mm"><h3>🎤 O discurso</h3><p class="small">O vídeo oficial mostra Gaspar Nunes no palco, iluminado
por um projetor, das 20h25 às 20h40, sem interrupções. O palco fica no salão principal, a duas salas do "Mar Elétrico".</p></div>
{fantasma("Um mar elétrico vale mais do que mil palavras. Obrigado pela mão firme. — <b>O Fantasma</b>")}
<div style="margin-top:3mm">{pergunta('A tua investigação: <span>quem pintou a cópia e trocou o quadro?</span>')}</div>
{foot(n, "Página 2")}</section>"""


# ---------------- CASO 6
def caso6():
    n = 6
    grupos = P.binario(BIN_MSG)
    bh = '<span class="sep">/</span>'.join(
        '<span class="w">' + "".join(f"<span>{b}</span>" for b in g) + "</span>" for g in grupos)
    return f"""<section class="page" {tema(n)}>
{mast(n, "Pixel Arena: organização anula a final · Nova partida marcada para sábado · Patrocinadores exigem explicações")}
<div class="kicker">E-sports</div>
<h1 class="headline">Apagão na final do Pixel Arena: favoritos <span class="hl">perdem a ligação</span> a 2 minutos do fim</h1>
<p class="lead">A equipa Raio Azul ia a ganhar quando os cinco computadores ficaram sem rede. Segundos depois, o ecrã
gigante do pavilhão mostrou uma mensagem estranha, feita só de zeros e uns.</p>
<div class="byline">Por <b>Paulo Tinta</b></div>
<div class="cols2">
<p>Eram 18h58 de domingo e o Pavilhão Azul estava em êxtase. A Raio Azul precisava de apenas dois minutos para vencer a final
nacional e levar 50 mil euros. De repente, os cinco ecrãs da equipa congelaram. A rede sem fios da Raio Azul tinha sido
desligada por um ataque informático.</p>
<p>Os técnicos garantem que o ataque foi feito de dentro do pavilhão, a partir de um pequeno aparelho escondido na bancada.
"Tem de estar a poucos metros da rede. Quem fez isto estava sentado no público", explicou o responsável técnico.</p>
<p>Logo a seguir, o ecrã gigante passou a mostrar uma sequência de números binários — a "assinatura" do pirata, que se quis gabar.
A polícia acredita que a mensagem revela onde o pirata estava sentado.</p>
<p>Quatro espectadores com conhecimentos de redes, todos com contas antigas na plataforma de jogo, estão a ser ouvidos.
Os perfis e os bilhetes deles estão na página seguinte.</p>
</div>
{suspeitos([
 ("Ivo Barata", "Estudante de informática", "“Vim apoiar os adversários, sim. Mas ganhar assim não tem graça.”"),
 ("Rafael Cunha", "Técnico de redes", "“Conheço a rede do pavilhão, fui eu que a montei. Por isso mesmo, não fui eu.”"),
 ("Joana Brito", "Ex-jogadora profissional", "“Fui expulsa da Raio Azul o ano passado. Isso não faz de mim pirata.”"),
 ("Sérgio Lopes", "Youtuber de jogos", "“Estava a filmar para o meu canal. A minha câmara nem saiu da mão.”"),
])}
{foot(n, "Página 1")}</section>

<section class="page" {tema(n)}>
<div class="desafio" style="margin-top:2mm"><div class="lock">🔓 Desafio de acesso <b>· Código binário</b></div>
<h3>A mensagem do ecrã gigante</h3>
<p class="small">Cada grupo de cinco dígitos é uma letra. A=1, B=2, C=3 … Z=26, escritos em binário: cada posição vale
16, 8, 4, 2 e 1, e soma-se o valor das posições que têm "1". Exemplo: <b>00110</b> = 4 + 2 = 6 = <b>F</b>. A barra separa palavras.</p>
<div class="bin">{bh}</div>
<div class="bitkey"><div><b>16</b>posição 1</div><div><b>8</b>posição 2</div><div><b>4</b>posição 3</div><div><b>2</b>posição 4</div><div><b>1</b>posição 5</div></div>
<p class="small" style="margin-top:2mm"><b>Mensagem:</b> <span class="write" style="display:block;height:7mm;min-width:100%"></span></p>
</div>
<div class="grid2" style="margin-top:4mm">
 <div class="box acc"><span class="tag">Perfis</span><h3>🎮 Os nomes de jogador</h3><div class="byline">Por <b>Henrique Prelo</b></div>
 <table class="tbl"><tr><th>Suspeito</th><th>Nome no jogo</th></tr>
 <tr><td>Ivo Barata</td><td class="mono">NightOwl</td></tr>
 <tr><td>Rafael Cunha</td><td class="mono">Mocho_PT</td></tr>
 <tr><td>Joana Brito</td><td class="mono">Raven</td></tr>
 <tr><td>Sérgio Lopes</td><td class="mono">Lynx</td></tr></table></div>
 <div class="box"><span class="tag">Bilhetes</span><h3>🎟️ Onde estavam sentados</h3>
 <p class="small">A polícia pediu a cada um que mostrasse o bilhete:</p>
 <table class="tbl"><tr><th>Suspeito</th><th>Fila</th><th>Lugar</th></tr>
 <tr><td>Ivo Barata</td><td>3</td><td>12</td></tr>
 <tr><td>Rafael Cunha</td><td>7</td><td>4</td></tr>
 <tr><td>Joana Brito</td><td>3</td><td>18</td></tr>
 <tr><td>Sérgio Lopes</td><td>1</td><td>2</td></tr></table></div>
</div>
<div class="grid2" style="margin-top:3.5mm">
 <div class="box yel"><h3>🔌 Tecnologia</h3><div class="byline">Por <b>Vera Pena</b></div>
 <p class="small">Os nomes de jogador raramente são ao acaso: muitos escolhem animais, muitas vezes em inglês. Um "lynx" é um lince,
 um "raven" é um corvo… e quem passa as noites acordado a jogar adora nomes de aves noturnas.</p></div>
 <div class="box"><h3>🏟️ A bancada</h3><p class="small">A fila 1 é a mais próxima do palco. O aparelho tinha alcance de cerca de 15 metros
 — as filas 1 a 8 estavam todas dentro do alcance.</p></div>
</div>
{fantasma("Sexto trabalho: sem rede, sem rasto. Falta só um, e será em alto-mar. — <b>O Fantasma</b>")}
<div style="margin-top:3mm">{pergunta('A tua investigação: <span>quem desligou a rede da Raio Azul?</span>')}</div>
{foot(n, "Página 2")}</section>"""


# ---------------- CASO 7
def logic_grid():
    nomes = P.NOMES
    conv = [f"Convés {c}" for c in P.CONVES]
    ativ = [a.capitalize() for a in P.ATIV]
    orig = P.ORIG
    cols = conv + ativ + orig

    def head(cs, groups):
        h = '<tr><th class="rn"></th>'
        for gi, g in enumerate(groups):
            for i, c in enumerate(g):
                cls = "rot thick" if i == 0 and gi > 0 else "rot"
                h += f'<th class="{cls}"><div>{c}</div></th>'
        return h + "</tr>"

    t = '<table class="lg">' + head(cols, [conv, ativ, orig])
    for nm in nomes:
        t += f'<tr><th class="rn">{nm}</th>' + "".join(
            f'<td class="{"thick" if i in (5, 10) else ""}"></td>' for i in range(15)) + "</tr>"
    for k, o in enumerate(orig):
        t += f'<tr class="{"tt" if k == 0 else ""}"><th class="rn">{o}</th>' + "".join(
            f'<td class="{"thick" if i in (5,) else ""}"></td>' for i in range(10)) + "</tr>"
    for k, a in enumerate(ativ):
        t += f'<tr class="{"tt" if k == 0 else ""}"><th class="rn">{a}</th>' + "".join(
            '<td></td>' for i in range(5)) + "</tr>"
    return t + "</table>"


def caso7():
    n = 7
    pistas = [
        "A cabine da Alice fica num convés mais baixo do que a da Glória, que passou a noite no restaurante.",
        "Quem veio de Faro estava no spa.",
        "O Fausto dorme no convés 3.",
        "A cabine de quem estava no casino fica exatamente um convés abaixo da cabine de quem veio de Braga.",
        "A Diana não é do Porto, nem de Faro, nem de Braga — e não estava no teatro, na biblioteca nem no spa.",
        "Quem veio de Coimbra dorme no convés 7.",
        "O Bruno dorme num convés acima do de quem veio de Coimbra.",
        "Quem estava no teatro veio do Porto.",
        "O Fausto detesta spas: nunca lá põe os pés.",
        "Quem veio de Coimbra não esteve no casino.",
    ]
    li = "".join(f"<li class='small'>{p}</li>" for p in pistas)
    return f"""<section class="page" {tema(n)}>
{mast(n, "Cruzeiro Atlântida atraca em Lisboa com 48 horas de atraso · Todos os passageiros revistados à saída")}
<div class="kicker">Em alto-mar</div>
<h1 class="headline">Colar "Estrela do Mar" <span class="hl">desaparece</span> da suíte da condessa</h1>
<p class="lead">Uma joia de diamantes e safiras, avaliada em dois milhões de euros, foi roubada da suíte real do
navio Atlântida, a meio do Atlântico. O ladrão continua a bordo.</p>
<div class="byline">Por <b>Vera Pena</b> · a bordo do Atlântida</div>
<div class="cols2">
<p>A condessa Matilde de Albuquerque deixou o colar "Estrela do Mar" no cofre da sua suíte, no convés 6, e foi ao teatro do navio.
Quando voltou, às 23h, o cofre estava aberto e vazio. Como o navio estava em alto-mar, o colar só pode estar a bordo.</p>
<p>As câmaras do corredor mostram uma figura de roupão do navio e touca de piscina a sair do elevador de serviço no convés 6,
às 22h05. O elevador de serviço só pára nos conveses 4, 5 e 6, e só se chama com o cartão-chave de um passageiro que tenha
cabine num desses três conveses.</p>
<p>Às 22h00, o casino, o teatro e o restaurante estavam cheios: dezenas de testemunhas confirmam quem lá estava e quando.
Já a biblioteca e o spa estavam vazios a essa hora — quem lá esteve não tem ninguém que o confirme.</p>
<p>O comandante reuniu os cinco passageiros que, segundo a tripulação, fizeram perguntas sobre o colar durante a viagem.
Cada um disse onde dorme, de onde vem e onde estava às 22h — mas cada um falou com um oficial diferente, e os relatórios
chegaram ao PULSO baralhados em pistas soltas.</p>
</div>
<div class="box ink" style="margin-top:3mm"><h3>👥 Os cinco passageiros</h3>
<p class="small">Alice · Bruno · Diana · Fausto · Glória. Dormem nos conveses 3, 4, 5, 7 e 8 (um por convés). São do Porto, de Faro,
de Braga, de Coimbra e de Évora (um de cada cidade). Às 22h estavam no casino, no teatro, no
restaurante, na biblioteca ou no spa (um em cada local).</p></div>
{foot(n, "Página 1")}</section>

<section class="page" {tema(n)}>
<div class="desafio" style="margin-top:2mm"><div class="lock">🔓 Desafio de acesso <b>· Grelha lógica</b></div>
<h3>Os relatórios dos oficiais</h3>
<div class="grid2" style="grid-template-columns:1fr 1.05fr;align-items:start">
 <div><p class="small">Usa as pistas para descobrir o convés, a cidade e o local de cada passageiro às 22h. Marca ✗ quando
 uma combinação é impossível e ● quando tens a certeza.</p><ol class="clues">{li}</ol></div>
 <div>{logic_grid()}</div>
</div></div>
<div class="grid3" style="margin-top:4mm">
 <div class="box acc"><h3>📋 Tabela final</h3><table class="tbl"><tr><th>Nome</th><th>Convés</th><th>Local</th></tr>
 {"".join(f"<tr><td>{nm}</td><td></td><td></td></tr>" for nm in P.NOMES)}</table></div>
 <div class="box"><h3>🛗 O elevador</h3><div class="byline">Por <b>Paulo Tinta</b></div><p class="small">Pára nos conveses 4, 5 e 6. Só responde ao cartão de quem tem cabine num desses conveses.
 Na suíte do convés 6 só dorme a condessa.</p></div>
 <div class="box yel"><h3>🌊 O tempo</h3><div class="byline">Por <b>Sofia Letra</b></div>
 <p class="small">Mar chão e lua cheia. Noite perfeita para o espetáculo no convés — e para quem prefere a calma da leitura.</p></div>
</div>
{fantasma("Sete trabalhos, sete mãos. Amanhã, quem souber ler, saberá quem eu sou. — <b>O Fantasma</b>")}
<div style="margin-top:3mm">{pergunta('A tua investigação: <span>quem roubou a "Estrela do Mar"?</span>')}</div>
{foot(n, "Página 2")}</section>"""


# ---------------- CASO 8
def tabula():
    rows = "<tr><td></td>" + "".join(f"<td>{c}</td>" for c in P.A) + "</tr>"
    for i, k in enumerate(P.A):
        rows += f"<tr><td>{k}</td>" + "".join(f"<td>{P.A[(i + j) % 26]}</td>" for j in range(26)) + "</tr>"
    return f'<table class="tabula">{rows}</table>'


def caso8():
    n = 8
    cif = P.vigenere(VIG_MSG, VIG_CHAVE)
    return f"""<section class="page" {tema(n)}>
{mast(n, "Edição especial · Os sete culpados confessaram · Todos receberam ordens da mesma pessoa")}
<div class="kicker">Edição especial</div>
<h1 class="headline">O Fantasma escreve ao PULSO: <span class="hl">"Estou mais perto do que pensam"</span></h1>
<p class="lead">Os sete culpados desta semana confessaram e contaram o mesmo: foram contratados por alguém que assinava
"O Fantasma" e comunicava através dos classificados deste jornal. Esta manhã, chegou-nos uma carta cifrada.</p>
<div class="byline">Editorial de <b>Henrique Prelo</b>, diretor</div>
<div class="cols2">
<p>Durante uma semana, o PULSO contou-vos sete crimes. Uma guitarra, um chili, uns óculos, ouro, um quadro, uma final de
e-sports e um colar. Esta manhã, a polícia confirmou o que suspeitávamos: os sete culpados nunca se conheceram, mas todos
responderam ao mesmo anúncio e todos receberam ordens de um só mandante — O Fantasma.</p>
<p>Os anúncios do Fantasma apareceram nos nossos classificados todos os dias. Pagos em dinheiro, deixados num envelope na
receção, sem nome. Isso só pode querer dizer uma coisa: o Fantasma tem acesso à nossa redação.</p>
<p>Hoje, às 7h00, encontrei em cima da minha secretária um envelope preto. Lá dentro, uma carta cifrada e uma frase escrita à mão:
<i>"A chave está nas vossas próprias páginas: as iniciais dos sete culpados, pela ordem dos casos."</i></p>
<p>Ninguém de fora entra na redação depois da meia-noite. Por isso, com muita tristeza, tenho de olhar para a minha própria equipa.
Quatro pessoas tinham a chave da porta. Uma delas sou eu — e, para que não haja dúvidas, também me ponho na lista.</p>
</div>
{suspeitos([
 ("Paulo Tinta", "Repórter", "“Escrevo neste jornal há 20 anos. Conheço cada vírgula dele.”"),
 ("Sofia Letra", "Repórter", "“Tenho artigos em quase todas as edições. Não tinha tempo para ser fantasma.”"),
 ("Vera Pena", "Colunista", "“Eu? Só escrevo o tempo e o horóscopo. Ninguém dá por mim.”"),
 ("Henrique Prelo", "Diretor", "“Quase não escrevo no jornal, só dirijo. Mas investiguem-me à vontade.”"),
])}
{foot(n, "Página 1")}</section>

<section class="page" {tema(n)}>
<div class="desafio" style="margin-top:2mm"><div class="lock">🔓 Desafio final <b>· Cifra de Vigenère</b></div>
<h3>A carta do Fantasma</h3>
<div class="grid2" style="grid-template-columns:1fr 1fr;gap:5mm">
<div>
<div class="cifra" style="font-size:12pt">{cif}</div>
<p class="small" style="margin-top:2.5mm"><b>Como decifrar:</b> escreve a chave (7 letras) por baixo da carta, letra a letra, e repete-a
as vezes que forem precisas (os espaços não contam). Para cada par, vai à linha da tabela que começa pela <b>letra da chave</b>,
procura nessa linha a <b>letra cifrada</b> e sobe até ao topo da coluna: essa é a letra verdadeira.</p>
<p class="small"><b>Exemplo</b> com a chave "SOL": a letra cifrada <b>W</b> com a chave <b>S</b> → na linha S, o W está na coluna <b>E</b>.</p>
<p class="small">Chave: <span class="write" style="min-width:40mm"></span></p>
<p class="small">Mensagem:</p>
<span class="write" style="display:block;height:7mm;min-width:100%"></span>
<span class="write" style="display:block;height:7mm;min-width:100%"></span>
</div>
<div>{tabula()}</div>
</div></div>
<div class="grid2" style="margin-top:4mm">
 <div class="box acc"><h3>🗞️ Uma pista do diretor</h3><p class="small">"Se a carta disser o que eu penso, a resposta não está nesta edição:
 está nas sete anteriores. Voltem atrás e leiam o que normalmente ninguém lê."</p></div>
 <div class="box yel"><h3>📌 Atenção</h3><p class="small">Nesta edição especial, as assinaturas não contam: o Fantasma refere-se às edições
 que já tinham saído quando a carta foi escrita.</p></div>
</div>
<div class="box" style="margin-top:4mm"><h3>🔑 A chave: as iniciais dos culpados</h3>
<div class="codebox" style="justify-content:flex-start;margin-top:1mm">{"".join(f"<i>{k}</i>" for k in range(1, 8))}</div></div>
<div style="margin-top:4mm">{pergunta('O mistério final: <span>quem é o Fantasma?</span> Que pista prova a tua resposta?')}</div>
{foot(n, "Página 2")}</section>"""


# ---------------- soluções
def solucoes():
    sud = " · ".join("".join(str(v) for v in r) for r in sud_sol)
    cesar_c = P.cesar(CESAR_MSG, 3)
    itens1 = [
        (1, "A guitarra dourada", f"Desafio: <span class='ans'>{CESAR_MSG}</span>.",
         "As fotos da Inês (com hora) mostram o Rui no palco e o Duarte nas bifanas, e as panorâmicas foram tiradas da torre — "
         "por isso a própria Inês estava lá. Sobra a Natália, que disse ter passado a meia hora <b>ao telemóvel</b>. Mas o bilhete "
         "revela que a rede móvel e o wi-fi estavam em baixo das 21h às 22h: a chamada era impossível. <b>Culpada: Natália Sol (N).</b>"),
        (2, "O chili salgado", f"Desafio: <span class='ans'>O SACO DE SAL ESTAVA NO BOLSO DE UM CASACO</span>.",
         "A Rita viu alguém <b>de azul</b>: Octávio (casaco azul) ou Filipe (avental azul). A mensagem diz que o sal estava no bolso de "
         "um <b>casaco</b>. Só Octávio usa um casaco azul (o casaco da Kátia é amarelo). <b>Culpado: Octávio Reis (O).</b>"),
        (3, "Os óculos Visio-1", f"Desafio: hora <span class='ans'>23:14</span> (solução do sudoku por linhas: {sud}).",
         "O cofre só abre por dentro e foi aberto uma única vez, às 23h14. Nessa hora, o Hugo já tinha saído (23h10), o Tiago ainda não "
         "tinha entrado (23h20) e a Sara estava fora (saiu às 22h50, voltou às 23h35). Só a Telma estava no laboratório. A publicação do Hugo era "
         "uma pista falsa. <b>Culpada: Telma Ferraz (T).</b>"),
        (4, "O ouro do Banco Atlântico", "Desafio: <span class='ans'>O LADRÃO SAIU NA ESTAÇÃO DAS FLORES</span>.",
         "Na estação das Flores, às 22h50, saiu alguém a coxear da perna esquerda. Vivem lá a Paula e o Igor. A Paula acabou a meia-maratona "
         "\"sem uma única dor\"; o Igor torceu o tornozelo esquerdo e conhece os túneis. O Marco (joelho direito) é o isco da estação do Cais. "
         "<b>Culpado: Igor Santos (I).</b>"),
        (5, "O quadro trocado", "Desafio: CAVALETE, PALETA, PINCEL, GUACHE, MOLDURA, RETRATO, ESBOÇO → <span class='ans'>CANHOTO</span>.",
         "A cópia foi pintada por um canhoto. São canhotos o Gaspar e a Cecília (fotogaleria). Mas às 20h30, durante a troca, o Gaspar estava "
         "no palco, filmado, a duas salas do quadro. <b>Culpada: Cecília Rocha (C).</b>"),
        (6, "O apagão do Pixel Arena", "Desafio: <span class='ans'>CORUJA NA FILA TRES</span>.",
         "Na fila 3 estavam o Ivo e a Joana. \"Raven\" é corvo; \"NightOwl\" é coruja (o \"Mocho_PT\" é o isco, mas estava na fila 7). "
         "<b>Culpado: Ivo Barata (I).</b>"),
        (7, "A Estrela do Mar", "Desafio: Alice — convés 5, biblioteca, Braga · Bruno — 8, spa, Faro · Diana — 4, casino, Évora · "
         "Fausto — 3, teatro, Porto · Glória — 7, restaurante, Coimbra.",
         "O elevador só obedece a cartões dos conveses 4, 5 e 6: Diana (4) ou Alice (5). Às 22h, a Diana estava no casino, cheio de "
         "testemunhas; a Alice estava sozinha na biblioteca. <b>Culpada: Alice (A).</b>"),
        (8, "O Fantasma", f"Desafio: chave <span class='ans'>NOTICIA</span> (Natália, Octávio, Telma, Igor, Cecília, Ivo, Alice). "
         f"Carta: <span class='ans'>{P.vigenere(VIG_MSG, VIG_CHAVE)}</span> → <span class='ans'>{VIG_MSG}</span>.",
         "É preciso voltar às assinaturas das edições 1 a 7. Paulo Tinta não assina nada na edição 2; Sofia Letra não assina nada na "
         "edição 6; Henrique Prelo só assina nas edições 2 e 6. Só uma pessoa assinou em <b>todas</b> as edições: tempo, horóscopo, "
         "tecnologia, agenda… e duas manchetes. <b>O Fantasma é Vera Pena</b> — a colunista em quem \"ninguém dá por ela\"."),
    ]
    html = ""
    for n, t, d, r in itens1:
        html += f'<div class="item" style="--c:{TEMAS[n][0]}"><h3><span>Caso {n} ·</span> {t}</h3><p class="small">{d}</p><p class="small">{r}</p></div>'
    tabela = """<table class="tbl" style="margin-top:2mm"><tr><th>Edição</th><th>Paulo</th><th>Sofia</th><th>Vera</th><th>Henrique</th></tr>
<tr><td>1</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr>
<tr><td>2</td><td></td><td>✔</td><td>✔</td><td>✔</td></tr>
<tr><td>3</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr>
<tr><td>4</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr>
<tr><td>5</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr>
<tr><td>6</td><td>✔</td><td></td><td>✔</td><td>✔</td></tr>
<tr><td>7</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr></table>"""
    return f"""<section class="page sol" {tema(8)}>
<div class="kicker">Soluções</div><h1 class="headline" style="font-size:22pt">Caso encerrado: <span class="hl">as respostas</span></h1>
<div class="cols2" style="column-gap:7mm">{html}
<div class="item" style="--c:#111;break-inside:avoid"><h3>Assinaturas, edição a edição</h3>{tabela}</div></div>
{foot(0, "Soluções")}</section>"""


def build():
    corpo = capa() + instrucoes() + caso1() + caso2() + caso3() + caso4() + caso5() + caso6() + caso7() + caso8() + solucoes()
    html = f"""<!doctype html><html lang="pt"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>PULSO — O Jornal dos Enigmas</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Inter:wght@400;600;700;800&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>{corpo}<script>
function fitPages(){{
  document.querySelectorAll('.page:not(.capa)').forEach(function(pg){{
    var foot = pg.querySelector('.foot'); if(!foot) return;
    function ok(){{
      var lim = foot.getBoundingClientRect().top - 6, max = 0;
      pg.querySelectorAll('*').forEach(function(c){{ if(c.closest('.foot')) return;
        var r = c.getBoundingClientRect(); if(r.height) max = Math.max(max, r.bottom); }});
      return max <= lim && pg.scrollWidth <= pg.clientWidth + 1;
    }}
    var fs = 9.6; pg.style.fontSize = fs + 'pt';
    while (fs < 12.6) {{ pg.style.fontSize = (fs + 0.1).toFixed(1) + 'pt'; if (!ok()) break; fs += 0.1; }}
    pg.style.fontSize = fs.toFixed(1) + 'pt';
    while (!ok() && fs > 7) {{ fs -= 0.1; pg.style.fontSize = fs.toFixed(1) + 'pt'; }}
    pg.dataset.fs = fs.toFixed(1);
  }});
  document.body.dataset.fitted = '1';
}}
(document.fonts && document.fonts.ready ? document.fonts.ready : Promise.resolve()).then(fitPages);
</script></body></html>"""
    open("pulso_enigmas.html", "w", encoding="utf-8").write(html)
    print("ok", len(html))


if __name__ == "__main__":
    build()
