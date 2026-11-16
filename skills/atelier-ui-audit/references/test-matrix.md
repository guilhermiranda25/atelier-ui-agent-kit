# Matriz de testes de UI/UX

| Tipo | 360/390 mobile | 768 tablet | 1280 desktop | 1920 wide |
| --- | --- | --- | --- | --- |
| Layout/clipping | sim | sim | sim | sim |
| Nav/foco/teclado | sim | sim | sim | sim |
| Form + validation | sim | sim | sim | smoke |
| Loading/empty/error | sim | sim | sim | quando útil |
| Dark/light | sim | sim | sim | opcional |
| Text at 200% zoom | sim | sim | sim | opcional |
| Reduced motion | sim | sim | sim | opcional |
| Screenshot baseline | sim | sim | sim | conforme tela |

## Jornadas específicas
**Auth:** login válido/inválido, senha esquecida, link expirado, confirmação, sessão revogada, rede instável, password manager.
**Dashboard:** filtro sem resultado, filtro parcial, dados lentos, tabela grande, export sem permissão, refresh e locale.
**LMS:** aula em vídeo com controles, erro do player, retomar progresso, mobile landscape, carregamento lento, legendas.
**Landing:** navegação mobile, links footer, CTA, form de contato, viewport baixa, imagem ausente, idioma longo.

## Playwright
Reutilize suite e baseURL existentes. Use `getByRole`, assertions por visibilidade/foco, screenshots por viewport, pixeldiff somente após baseline autorizado, rastreie console errors e falhas de rede críticas. Não tornar testes "verdes" pulando fluxo ou desabilitando asserts.

## Classificar evidência
`executado + passou`, `executado + falhou`, `inspecionado sem execução`, `não testado`. Útil separar riscos de infraestrutura de problemas de frontend.
