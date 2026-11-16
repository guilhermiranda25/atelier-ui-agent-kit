# Sistema visual — especificações de implementação

## Hierarquia de tokens
`primitive.color.teal.800` → `semantic.color.brand.primary` → `component.button.primary.bg`. Evitar construir design system apenas com `--green-500`. Tema claro/escuro mapeia semânticos para primitives.

## Cor (padrões iniciais, calibrar por marca)
- Neutros: surface/background/text e bordas derivadas de escala perceptual; não usar cinza puro em todas as superfícies.
- Cor principal: aplicada em primário, links e foco; evitar 3 CTA igualmente dominantes.
- Cor de feedback: `positive`, `notice`, `negative`, `info`; sempre texto ou ícone junto.
- Estado desabilitado: não depender só de baixa opacidade para explicar uma restrição; `aria-disabled` e texto de ajuda quando importante.
- Contraste: texto normal 4.5:1, texto grande 3:1, UI não textual essencial 3:1 (WCAG AA); verifique contexto real e overlays.

## Tipo
- Display: só onde há headline; `clamp()` 40–78 px conforme layout e métrica da fonte, `line-height` em torno de 0.95–1.12 quando seguro.
- H1 marketing: faixa aproximada 40–64 px; H1 produto: 28–40 px.
- H2: 24–44 px conforme densidade; H3: 18–28 px; body: 14–18 px para sistemas, 16–20 px para leitura editorial.
- Texto de ajuda/metadata: evite menos de 12 px, preferir 13–14; não usar 10px para caber dashboard.
- Limitar largura de parágrafos longos a ~60–75 caracteres; headings podem ter linha mais estreita.
- Numerais tabulares em dashboards; labels claros de unidades, períodos e fonte.
- Revisar português BR, acentos, caracteres, pesos disponíveis e fallback.

## Spacing e grid
Spacing base 4 px, passos 4,8,12,16,20,24,32,40,48,64,80,96,120. Aceitar exceção onde o layout precisa, mas evitar dezenas de magic numbers.
Desktop: colunas e gutters fluidos; mobile: margem mínima 16–20px; tablet: 24–32px; desktop: 32–64px conforme largura. Painéis podem ser fluidos e evitar `max-width` baixo.

## Radius/sombra
Raio é um vocabulário: pequena = 6–8, média 10–14, grande 16–24, pill para controle específico. Escolher perfil coerente com marca. Sombras devem variar blur/offset/alpha e corresponder a z-layer; algumas marcas pedem layout flat com borders.

## Motion tokens
`instant` 0–100ms, `fast` 120–180ms, `normal` 180–260ms, `slow` 280–440ms. Não animar propriedades de layout em listas grandes. `prefers-reduced-motion` interrompe efeito não essencial e simplifica movimento.

## Temas
Definir background, foreground, surface, input, border, focus, chart series e status tokens por tema. Checar estados em light/dark com um mesmo componente. Tokens semânticos para charts devem ter testes de contraste e alternativas para daltonismo.

## Checklist de typography pass
Quebras intencionais, rag balance, altura uniforme de botões, largura de texto, abreviações, números, idioma, legibilidade em 200% zoom, métricas da fonte ao carregar e sem shift perceptível.
