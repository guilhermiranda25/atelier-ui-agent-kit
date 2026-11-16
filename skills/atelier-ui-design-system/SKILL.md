---
name: atelier-ui-design-system
description: Design semantic tokens, typography, color, spacing, grids, component specifications, dark mode and brand governance for polished React or web UIs; use when designing or standardizing frontend visual foundations.
---

# Atelier UI Design System

## Objetivo

Criar um sistema expressivo e escalável, sem ditar uma estética única. Primeiro inventariar tokens do projeto; consolidar em vez de substituir arbitrariamente.

## Sequência

1. Documentar identidade e usos: produtos, contexto, público e marcas.
2. Definir primitives (`color`, `spacing`, `type`, `radius`, `shadow`, `duration`, `breakpoints`, `z-index`).
3. Mapear **tokens semânticos** (`background`, `surface`, `surface-raised`, `text-primary`, `text-muted`, `border`, `focus`, `accent`, `success`, `warning`, `danger`).
4. Definir escalas responsivas, famílias tipográficas, line-height, letter-spacing, numerais tabulares para tabelas e cards KPI.
5. Descrever states de cada primitivo: hover, focus-visible, pressed, selected, disabled, loading, error e read-only.
6. Validar contraste e modos light/dark (dark não é inversão automática); criar modelo com CSS variables ou theme provider já existente.
7. Registrar decisões e revisar com screenshots representativas, não somente swatches.

## Diretrizes

- Paleta por **papel**, não por cor isolada. Um único acento mais forte, salvo necessidade real.
- Escala de espaços coerente; grids devem surgir do conteúdo e da hierarquia.
- Tipografia é parte da identidade; incluir números, tabelas, formulários e títulos sem truncamento indevido.
- Definir 1–2 famílias principais; evitar mais que 3 pesos efetivos num mesmo componente.
- Bordas sutis para separação; sombras só quando expressam elevação real.
- Relações de contraste WCAG AA como baseline de texto; cor nunca é a única informação de estado.
- Não codificar cores diretamente em centenas de componentes; centralizar tokens.

## Recursos

- `references/tokens-and-typography.md` — especificações e escalas de produção.
- `references/component-contracts.md` — anatomia, variantes, estados e documentação.
- `assets/tokens.css` — exemplo original de tokens para adaptar, **não** aplicar sem revisar.
- `scripts/check_contrast.py` — contraste de duas cores e avaliação AA/AAA.
