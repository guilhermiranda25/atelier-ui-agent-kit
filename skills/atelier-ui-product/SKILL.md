---
name: atelier-ui-product
description: Architect high-utility premium product interfaces: analytics dashboards, enterprise web apps, complex forms, data tables, authentication, learning platforms and role-based operational tools; use for authenticated product UI.
---

# Atelier UI Product — aplicação orientada à tarefa

## Princípio

Design premium de software operacional = reduzir esforço cognitivo e erro, não somente enfeitar o dashboard. Preservar regras de negócio, papéis, permissões, logs e contratos de dados.

## Workflow
1. Identificar papéis, tarefas frequentes, decisões, entradas/saídas, risco de erro e tempo de operação.
2. Mapear arquitetura informacional, navegação, busca, filtros, drill-down e ações.
3. Definir estados completos para cada fluxo: inicial, carregando, vazio, filtrado vazio, erro, parcial, indisponível, sem permissão, sucesso, offline quando aplicável.
4. Definir densidade por contexto (painéis/dados ≠ marketing), sticky regions, foco e responsividade adaptativa.
5. Desenhar componentes com hierarquia: overview → exploração → ação → confirmação → auditoria.
6. Implementar com tipagem, semântica, validação de formulário, autorização no backend e feedback de operação.
7. Cobrir fluxos críticos e teclado com testes; monitorar performance com payload real.

## Aplicações

- **Dashboard de BI**: resumo acionável, comparações coerentes, filtros visíveis, estados de refresh, números/unidades, contexto temporal, drilldowns e tabela de detalhe.
- **Sistema empresarial**: shell, módulos, workflows aprovativos, notificações in-app, leitura/edição, audit trail, permissões e consistência cross-feature.
- **LMS**: catálogo, vídeo acessível, progresso, módulos, retomar aula, busca, notas, avaliações, perfil e opções de privacidade.
- **Autenticação**: onboarding, convite, verificação, reset, expiração de link, sessão e feedback anti-enumeration, sem mostrar segredos.
- **Tabelas densas**: filtros, sorting, export, colunas, paginação, loading sem layout shift, empty/error separadamente.

## Exigir

- Esconder ação no frontend **não é** autorização; verificação de permissões real precisa estar no servidor.
- Dashboard deve evidenciar cálculo, fonte, data de atualização e contexto — não inventar indicadores para preencher layout.
- Feedback de aprovação/notificação exige estado de leitura, destino, permissão, persistência, paginação e limpeza, sem atualizar silenciosamente dados.
- Inputs complexos necessitam validação no cliente para UX e no servidor para segurança.
- Responsivo em painéis significa reestruturar prioridade e fluxo, não simplesmente encolher a tabela.

## Referências

- `references/patterns-and-states.md`: tabela de padrões detalhados e estados.
- `references/dashboard-and-learning.md`: dashboards, cursos e UI data-intensive.
