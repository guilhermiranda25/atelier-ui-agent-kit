# Tokens e contratos de movimento

## Duração e curva
- 100–160ms: estado simples (hover, focus enhancement, pressed).
- 160–240ms: toggle, toast, badge, seleção.
- 240–400ms: drawer, dialog, accordion, panel reveal.
- >400ms: reservado para narrativa pontual, não navegação crítica.

Timings são hipóteses iniciais, não valores absolutos. Easing de saída pode ser mais rápido que entrada; mover container em vez de animar individualmente 40 filhos.

## Especificação de um componente
`event`, `initial`, `target`, `exit`, `time`, `curve`, `stagger`, `trigger`, `interrupt`, `reduced_motion`, `keyboard`, `touch`, `loading`, `error`, `test_cases`.

## Exemplos de intenção
- Entrada de diálogo: backdrop + painel, sem deslocar tudo.
- Salvamento de form: feedback de pendência e confirmação, mantendo foco contextual.
- Filter changes: estado ativo visível, suave transição de lista se não atrasar resultados.
- Hover media: zoom <= ~1.03, motion reduzida, legibilidade de captions constante.
- Marquee: pausar em hover/foco, controle de usuário se crítico; nunca único meio de leitura.

## Bibliotecas de referência
React Bits: componentes animados, text effects, backgrounds e microinterações; escolher flavor TypeScript + Tailwind/CSS adequado. Magic UI: shimmer, marquees, grids, text reveal e focus effects. Uiverse: ideias micro CSS e affordances. Hairline UI: status buttons, controls e efeitos de baixa intensidade.

## Testes
Com motion normal e reduced motion: abrir modal, navegar por teclado, mudar tabs, carregar lento, clicar rapidamente, sair da página no meio da animação; monitorar Console e React warnings.
