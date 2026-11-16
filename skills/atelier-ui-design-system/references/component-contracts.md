# Contrato de componentes reutilizáveis

Cada componente documenta: **job to be done**, anatomia, props, variantes, estado controlado, eventos, loading, disabled, focus, teclado, mensagens assistivas, responsividade, erros, testes e dependências.

## Foundations
Button (primary/secondary/tertiary/destructive/icon), Link, Input, Textarea, Select/Combobox, Checkbox/Radio/Switch, Badge/Tag, Tooltip, Dialog/Drawer, Dropdown/Menu, Toast, Skeleton, Empty State, Pagination, Table, Tabs, Breadcrumb, Nav, Stepper, Card, Chart Wrappers, Upload, Date Picker.

## Regras transversais
- Usar `<button>` para ações e `<a>` para navegação; não falso botão com div.
- Ícone isolado com `aria-label` e tamanho de hit target adequado; símbolos decorativos `aria-hidden=true`.
- Input com label visível quando aplicável, mensagem de erro conectada por `aria-describedby`; placeholder não substitui label.
- Dialog com trap/focus restore, ESC adequado, título acessível e scroll management.
- Charts com resumo textual, unidade, legendas, tooltip acessível quando possível e alternativas de tabela.
- Data table com `th`, cabeçalhos, sorting anunciado, estado empty/filtered e paginação funcional.
- Loading não bloqueia toda a página por uma simples mudança de filtro; estados parciais mantendo contexto.
- Não quebrar contratos de componente atual durante redesign; testes de regressão.

## Integração React
Preferir TypeScript, componentes coesos por domínio, props legíveis, controlo de estado previsível e hooks custom quando há reutilização real. Não criar 200 arquivos com abstrações vazias. Performance sob medição: lazy loading de gráficos e assets, memoização apenas onde profiler indicar; effects sem loops desnecessários.
