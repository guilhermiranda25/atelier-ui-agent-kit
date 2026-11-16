# Receitas de execução para agentes

## 1. SaaS de dados, landing pública
Use director → research → design-system → marketing → motion (somente visual focal) → assets → audit. Objetivo: credibilidade e demonstração real. Exigir produto em contexto, prova, CTA, page states e mobile.

## 2. Plataforma de cursos
Use product → design-system → assets → audit. Fluxos: catálogo, busca, detalhes, inscrição, aulas, player, progresso, perfil, onboarding. Testar player lento e expirado, conteúdos longos, sem matrícula e progresso real.

## 3. BI e gestão operacional
Use product → design-system → audit. KPI contextualizado, filtros claros, drilldown por área/contrato/período, tabela detalhada, dark/light, resultados sem cor única e dados reais. Evitar animações que disputem atenção com dados.

## 4. Portfólio de analista/design engineer
Use director → marketing → assets → audit. Incluir cases com problema/decisão/resultado em vez de logo-grid de skills. Evidências autorizadas e mockups de tela real.

## 5. Aplicativo de aprovação e notificações
Use product → design-system → motion → audit. Estados pendente/aprovado/reprovado, feedback, marcação lida, deep link, papel/ACL servidor, erros e trilha de auditoria. Testar duas sessões, contas com perfis diferentes e erros.

## 6. Redesign de app legado
Use audit antes de director; inventariar e preservar rotas, API, permissões, atalhos, formulários e testes. Mudar tokens/camadas por fatias, screenshot baseline e rollback. Não reescrever todos os componentes por capricho.

## 7. Site com alto nível de motion
Use director → motion → marketing → audit. Selecione uma grande interação, implemente fallback estático e reduza payload sob mobile/throttling. Medição antes de afirmar melhora.

## Formato de prompt mínimo

```text
Use atelier-ui-director e as skills filhas estritamente necessárias.
Produto e público: <...>. Stack existente: <...>. Páginas e fluxos: <...>.
Identidade: <...>. Nível visual: editorial/premium, original, sem AI slop.
Preserve todas as funcionalidades, rotas, permissões e contratos existentes.
Pesquise fontes oficiais apenas para componentes necessários e valide licenças.
Implemente com semântica, tokens, states, mobile-first e reduced motion.
Execute build, testes, screenshots e relatório de auditoria; não invente testes.
```
