#!/usr/bin/env python3
"""Mostra quais fotos ainda faltam na pasta img/ (lê as listas A e M direto do index.html)."""
import json, os, re
raiz = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
img = os.path.join(raiz, "img")
html = open(os.path.join(raiz, "index.html"), encoding="utf-8").read()
def lista(nome):
    return json.loads(re.search(r"var " + nome + r"=(\[\[.*?\]\]);", html).group(1))
def conferir(titulo, grupo):
    print(f"\n{titulo}")
    for nome, slug, qtd in grupo:
        faltam = [k for k in range(1, qtd + 1) if not os.path.exists(os.path.join(img, f"{slug}-{k}.jpg"))]
        print(f"  {nome}: " + (f"completo ✓ ({qtd} fotos)" if not faltam else f"faltam {len(faltam)} de {qtd} -> " + ", ".join(f"{slug}-{k}.jpg" for k in faltam)))
conferir("ARTISTAS", lista("A"))
conferir("MARCAS", lista("M"))
for extra in ("inicio.jpg", "thomas.jpg"):
    print(f"\n  {extra}: " + ("ok ✓" if os.path.exists(os.path.join(img, extra)) else "FALTA"))
print("\nDica: tudo minúsculo, extensão .jpg, dentro da pasta img/.")
