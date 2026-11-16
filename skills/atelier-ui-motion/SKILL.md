---
name: atelier-ui-motion
description: Design, implement and verify meaningful React/CSS motion and microinteractions inspired by React Bits and Magic UI, respecting reduced motion, GPU limits, semantics and accessibility; use for interactive frontend polish.
---

# Atelier UI Motion — movimento com intenção

## Abordagem
1. Nomear o **evento de UX**: entrada, confirmação, mudança de estado, relação espacial, atenção, narrativa ou delight discreto.
2. Definir comportamento **sem animação** primeiro; funcionalidade não depende de JS motion.
3. Selecionar técnica de menor custo: CSS transitions → transform/opacity CSS → Motion → canvas/WebGL apenas para efeito que de fato exige.
4. Especificar trigger, timing, easing, delay, estado intermediário, reversibilidade, cancelamento e fallback.
5. Adaptar `prefers-reduced-motion: reduce`, dispositivos limitados, focus e touch; não deixar conteúdo invisível ao usuário reduzido.
6. Verificar performance de CPU/GPU, CLS, interação simultânea, perda de frames e contraste sobre backgrounds animados.

## Regras de motion premium
- Movimento ajuda a entender origem/destino e mudança, não disputa atenção com conteúdo.
- Hover tem equivalente em teclado (`focus-visible`) quando apresenta affordance importante.
- Animação de entrada não atrasa acesso ao conteúdo nem impede scroll/focus.
- Evitar auto-rotating carousels, exageros de spring, mouse follower em áreas funcionais e 3 backgrounds animados simultâneos.
- Evitar layout thrash (leituras e writes DOM no mesmo frame); preferir `transform`, `opacity`.
- Áreas críticas de dashboards priorizam feedback instantâneo e estados estáveis.

## Catálogo por uso
- **Marketing**: hero reveal único, progress indicator, ticker real, hover imagem, marquee com pausa.
- **Produto**: botão loading/success, toasts com contexto, item adicionado, tabs suaves, expand/collapse, feedback de atualização.
- **Data viz**: transição entre estados com eixo estável e acessibilidade, sem falsificar tendência.
- **Empty state**: microanimação não essencial, clara e pausável.

## Referências

`references/motion-specs.md` e `references/reduced-motion-and-performance.md`.
