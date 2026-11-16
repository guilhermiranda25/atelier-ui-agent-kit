# Movimento acessível e performance

```css
@media (prefers-reduced-motion: reduce) {
  .nonessential-motion {
    animation: none !important;
    transition: none !important;
  }
}
```

Não usar esse seletor para silenciar **todo** feedback funcional, apenas movimento não essencial. `prefers-reduced-motion` deve produzir conteúdo final visível, não elemento com opacity=0 permanentemente.

## Performance
- Animated gradients e filtros full-screen podem custar GPU; medir.
- CSS `will-change` somente próximo da interação e por curto período; global `will-change: transform` gera layers demais.
- Canvas/WebGL com FPS adaptativo, resize observer, pause fora da viewport ou tab oculta, cleanup e fallback estático.
- `requestAnimationFrame` para trabalho visual e cleanup; evitar setInterval por widget animado.
- Virtualize listas com milhares de linhas; não animar cada célula.
- Evitar re-render de árvore inteira por `mousemove`; preferir CSS variables localizadas ou external motion value conforme stack.
- Import dinâmico de módulos pesados somente quando tela utiliza.

## Evidência
Testar em viewport mobile com throttling, duração de load, Lighthouse e perfil de performance quando disponível. Não declarar "60fps" sem medição.
