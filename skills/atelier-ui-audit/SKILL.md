---
name: atelier-ui-audit
description: Perform evidence-based frontend UI/UX quality audits with visual regression, mobile breakpoints, accessibility, interaction states, Lighthouse, design consistency and automated checks; use before shipping any frontend.
---

# Atelier UI Audit — critério de entrega

## Evidência, não opinião

Nunca declarar que um design está "100% funcional", "perfeito" ou que passou nos testes sem executá-los. Inspeção visual precisa de screenshots reais da aplicação, não somente leitura de código.

## Workflow verificável
1. Inventariar páginas/rotas e fluxos críticos; conferir baseline antes de mudar UI.
2. Validar build, types, lint e unit tests disponíveis (sem desativar checks para passar).
3. Rodar aplicação e inspecionar screenshots: desktop, tablet, mobile e condições como long text, empty/error/loading.
4. Avaliar overflow/cortes, zoom 200%, contraste, hierarquia, tipografia, dark mode, foco/teclado, legendas, forms e `prefers-reduced-motion`.
5. Testar fluxos com Playwright ou harness existente, inclusive 400/500, timeout, erro de autenticação, respostas lentas, toque e navegação por teclado.
6. Medir performance em ambiente comparável: LCP, CLS, INP e bundle quando possível; identificar gargalo sem inventar números.
7. Classificar achados por severidade e corrigir. Reexecutar os casos afetados e demonstrar o que realmente foi resolvido.

## Severidade
- P0: perda de dados, segurança, fluxo core bloqueado, inacessibilidade crítica.
- P1: visual quebrado, ação incorreta, cortes, navegação importante inacessível.
- P2: inconsistência de hierarquia, feedback fraco, desempenho local ruim.
- P3: ajuste de polimento, detalhe perceptual, sugestão estética sem impacto funcional.

## Fontes de verificação

- `references/quality-gates.md` — checklist completo e rubrica de pontuação.
- `references/test-matrix.md` — estados e telas por ambiente.
- `scripts/check_contrast.py` — rotina CLI de cálculo WCAG, sem dependências.
- `scripts/audit_structure.py` — scanner estrutural estático do repositório; **não substitui testes de acessibilidade, SAST ou browser**.
- `assets/playwright-visual.spec.ts` — exemplo de Playwright, deve ser adaptado às rotas reais e suíte existente.

## Saída

| Tela/fluxo | Problema | Evidência | Severidade | Correção | Resultado/reteste |
| --- | --- | --- | --- | --- | --- |

Indicar explicitamente o que não pôde testar e por quê.
