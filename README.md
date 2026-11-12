# Alvarenga Art House — site

Site de portfólio de **Thomas Alvarenga** (Alvarenga Fotografia): fotografia de shows, eventos, festivais e coberturas de marca.
É um site simples, de **um arquivo só** (`index.html`), sem programas para instalar. Funciona direto no GitHub Pages.

## O que tem em cada pasta

```
alvarenga-art-house/
├── index.html            ← o site inteiro (letras, cores, textos e códigos)
├── img/                  ← AS FOTOS entram aqui (nomes exatos em docs/FOTOS.md)
│   └── mobile/           ← vídeos 9:16 da aba Mobile (aba desativada por enquanto)
├── assets/
│   ├── logos/            ← logos douradas dos artistas e das marcas (PNG transparente)
│   └── marca/            ← logo Alvarenga Art House (SVG)
├── docs/
│   ├── Alvarenga-Art-House-Brand-Book.pdf   ← identidade visual (manda em tudo)
│   ├── FOTOS.md                              ← lista dos nomes de cada foto
│   └── versions/index-com-aba-mobile.html    ← cópia do site COM a aba Mobile
├── scripts/checar-fotos.py   ← mostra quais fotos ainda faltam
├── CLAUDE.md             ← instruções para o Claude que for trabalhar neste projeto
└── README.md             ← este arquivo
```

As logos já estão **dentro** do `index.html`; a pasta `assets/` guarda as cópias soltas, caso você precise delas.

## Ver o site no seu computador

- Dê **dois cliques** no `index.html` (abre no navegador), ou
- No terminal, dentro da pasta: `python3 -m http.server 8000` e abra `http://localhost:8000`.

## Colocar as fotos

1. Salve cada foto na pasta `img/` com o nome exato, tudo minúsculo e `.jpg` (ex.: `davi-1.jpg`). A lista completa está em `docs/FOTOS.md`.
2. Rode `python3 scripts/checar-fotos.py` para ver o que ainda falta.
3. Dica de peso: fotos com até ~500 KB cada (lado maior em ~1600 px) deixam o site rápido, principalmente no iPad.

## Publicar no GitHub (do zero)

Precisa ter o **Git** instalado e uma conta no GitHub. Crie um repositório vazio no GitHub e copie o endereço dele.

```bash
cd alvarenga-art-house
git init
git add .
git commit -m "Site Alvarenga Art House"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git
git push -u origin main
```

Depois, no GitHub: **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: `main` / `(root)` → Save**.
Em cerca de 1 minuto o site abre em `https://SEU-USUARIO.github.io/NOME-DO-REPOSITORIO/`.

## Se você já tem um repositório com o site antigo

```bash
git clone https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git
# copie o conteúdo desta pasta para dentro da pasta clonada, substituindo o index.html
cd NOME-DO-REPOSITORIO
git add .
git commit -m "Nova versão do site"
git push
```

## Atualizar depois (sempre o mesmo ritmo)

```bash
git add .
git commit -m "Descrição curta do que mudou"
git push
```

## Limites e cuidados

- O GitHub aceita arquivos de até **100 MB** (pelo site do GitHub, só até 25 MB por arquivo). Comprima os vídeos.
- Os nomes são sensíveis a maiúsculas: `Davi-1.JPG` **não** funciona, `davi-1.jpg` funciona.
- Foto do iPhone costuma sair em HEIC; converta para JPG antes.
