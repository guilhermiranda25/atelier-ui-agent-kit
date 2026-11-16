# Biblioteca de padrões operacionais

## Shell e navegação
Sidebar persistente no desktop e navegação móvel por drawer; breadcrumb onde a profundidade exigir; action bar contextual; estados ativos explícitos; combinações de tooltip e label, não sidebar só com ícone sem affordance.

## Tabelas
Sort real e reversível; cabeçalho com `<th scope=col>`; filtro com badge e limpar; rows identificáveis; export com escopo explícito (visível/tudo); seleção com confirmação; skeleton proporcional; estados de carregamento e erro sem deslocar tabela toda.

## Busca/combobox
Debounce onde necessário, teclado arrows/enter/esc, estado sem resultado, indicação de filtros ativos, tratamento de 0 resultados e mensagens assíncronas. Evite chamadas de banco a cada tecla sem limitação/cancelamento.

## CRUD
Create: título e descrição, required, hints e validação. Edit: dirty state, preservação de inputs e confirmação de saída quando necessário. Delete: confirmação proporcional a risco, reautenticação quando sensível, mensagem reversível quando possível. Log de atividade em operações críticas.

## Fluxo de aprovação
Item + contexto + decisão + comentários obrigatórios quando necessário + trilha de decisão; ações com estados `pending`, `success`, `failed`, `revoked`. A UI protege contra duplo submit com idempotência real no backend.

## Notificações
Inbox/sino com count de não lidas, ordenação por relevância/tempo, filtragem, marcação de leitura, deep link, paginação, ACL e políticas de retenção; notificar somente usuários com permissão. Evitar polling agressivo: considerar push/realtime com fallback eficiente.

## Formulários
- Erros inline junto a campos, resumo quando extenso, focus para primeiro erro.
- Mask não substitui validação; datas/números/decimais adaptados ao locale.
- Seletores com milhares de itens usam busca servidor/paginação/virtualização quando necessário.
- Evitar autofill quebrado e mudança de label durante digitação.

## Arquivos
Extensão, MIME e tamanho revisados no servidor; exibir progresso/cancelamento; scans quando apropriado; downloads autorizados, sem URL exposta sensível.

## Observabilidade UX
Mensagens de erro úteis sem expor stack trace; correlation ID quando backend tem; performance dos endpoints e estados de loading instrumentados; logs sem PII ou tokens.
