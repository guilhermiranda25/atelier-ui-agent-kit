---
name: atelier-ui-assets
description: "Curate brand-safe visuals and assets: Lucide icons, unDraw illustrations, Shots mockups, Coolors palettes, Fontshare typography and genuine product imagery; use for premium UI asset and typography selection."
---

# Atelier UI Assets — sistema visual e de conteúdo

## Objetivo

Selecionar assets que **explicam o produto** e reforçam a identidade. Fotos e ilustrações não são preenchimento de espaço vazio. Não colocar imagens/fonts de terceiros no repositório sem verificar permissões específicas.

## Trabalho
1. Definir o papel de cada mídia: ilustrar conceito, demonstrar interface, fornecer contexto, explicar processo, provar resultado.
2. Inventariar assets locais, direitos, formato e necessidade de atualização.
3. Criar plano de iconografia (Lucide consistente), ilustração (unDraw por seleção manual), screenshot (do próprio produto), paleta (Coolors) e tipo (Fontshare).
4. Gerar um artboard de análise com escala, composição, contraste e responsividade.
5. Otimizar: imagem com largura/altura, WebP/AVIF quando apropriado, lazy loading fora da dobra, `srcset/sizes`, SVG seguro, carregamento de fonte e fallback.
6. Atribuição/licença e registro de origem quando exigidos, sem copiar em massa.

## Regras por categoria
- **Icones Lucide**: import nomeado; 16–20px comuns para UI; 24px quando precisa ser símbolo de ação, stroke consistente e alt/aria-label em controles somente com ícone.
- **unDraw**: escolher representação pertinente, paleta ajustada manualmente, não confundir ilustração abstrata com representação de dados do produto.
- **Shots**: apresentar *screenshots verdadeiros* em mockups para portfólio/marketing; usar fallback simples dentro do produto (não mockup pesado em dashboard).
- **Coolors**: usar como exploração de paletas; validação de contraste no ambiente real separada de harmonia subjetiva.
- **Fontshare**: verificar licença da família; planejar display + body + fallback; evitar baixar e versionar todas as famílias.

## Outputs

Asset manifest com nome, propósito, licença, origem, versão, modo de uso e otimização; tipografia e ícones com tokens; checklist de autenticidade.

Consulte `references/asset-workflows.md` e `atelier-ui-research/references/licensing-security.md` para limites legais.
