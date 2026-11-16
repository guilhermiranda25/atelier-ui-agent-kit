# Quality gates e anti-slop scorecard

## GATE A: funcionamento obrigatório
- Rotas renderizam sem erro fatal e ações principais funcionam com dados/autorização reais.
- Formulários submetem/validam, navegação e `href` têm destino, estados não contradizem backend.
- Erro e success state completos; sem loss of state ao navegar ou redesenhar.
- Testes de regressão sobre fluxos core passam. Se não houver ambiente para rodar, reportar bloqueio em vez de passar.

## GATE B: visual e responsividade
- Sem overflow horizontal em 360px e 390px e demais breakpoints definidos.
- Sem clipping de títulos/cards/menus e sem overlays cobrindo CTA.
- CTA, headline, preview de produto e conteúdo inicial mantêm hierarquia no primeiro scroll.
- Não há superfícies iguais empilhadas sem propósito; ritmo visual reconhecível.
- Tipografia legível, responsiva, numerais claros, contraste e alinhamento consistentemente verificados.

## GATE C: acessibilidade
- Focus visível e logical tab order; controles têm nomes, labels e semântica.
- Contraste AA texto e componentes essenciais (ver contexto). Não depender somente de cor.
- Drawer/dialog/menus funcionam com teclado, ESC e focus management.
- Motion respeita preferência do sistema; vídeo tem legendas/transcript onde exigido.
- Zoom 200% sem perda de informação/funcionalidade (testar contexto).
- axe/Lighthouse ajudam, mas teste manual é indispensável.

## GATE D: performance e engenharia
- JS e imagens carregam na medida da necessidade; nenhuma animação exige GPU full-screen sem justificativa.
- Nenhum erro de console relevante; `console.error` não escondido.
- Tipagem/lint/build e testes do projeto conforme pipeline real.
- Importações, chunks, cache e hydration avaliados com a stack existente.

## Score de acabamento (0–5)
1. Composição e originalidade; 2. Tipografia e leitura; 3. Densidade e scanning; 4. Clareza dos fluxos; 5. Estados e feedback; 6. Motion; 7. Consistência cross-page; 8. A11y/responsivo; 9. Performance; 10. Evidências verificadas.

Calcule média ponderada se existir metodologia; não apresentar nota como medição objetiva de qualidade estética. **Aprovação exige gates obrigatórios**, independentemente de score de direção de arte.

## Indicadores de AI slop (negativos)
- Headline genérica, cards idênticos, glow/sombra neon sem marca, gráfico fictício, ícones de decoração, fake testimonials, gradient repetitivo, microanimação excessiva, espaçamentos copiados sem ritmo e layouts que não funcionam em mobile.

## Registro de testes
Cada execução registra comando, ambiente/branch, resultado, pass/fail, screenshot/artefato e limitações. Nunca apagar falhas do relatório.
