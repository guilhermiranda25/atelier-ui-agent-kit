# Dashboards e plataformas de aprendizagem

## Dashboard
### Hierarquia em 3 níveis
1. **Resumo/decisão**: poucos KPIs realmente ligados à ação, comparação coerente e timestamp.
2. **Exploração**: cortes por contrato, disciplina, período, time, cenário ou produto; visibilidade dos filtros.
3. **Diagnóstico**: trends e tabelas detalhadas com variância, método e origem.

### Números e gráficos
Use separadores locais pt-BR, unidade explícita, valores negativos sem mascarar, percentuais com denominador; mesma escala ao comparar séries; não usar donuts para 12 categorias; não truncar eixo sem aviso. Reavaliar quando houver mistura de R$ e %, projetado e realizado. Palette apta a daltonismo, marcador além da cor. Gráficos pesados só quando a decisão justificar.

### Performance de datasets
Server-side filtering/pagination quando necessário; cancelar fetch obsoleto; cache invalidation correto; prevenir N+1; não buscar dataset inteiro quando exibe 20 registros. Layout não deve ter reflows frequentes por atualização em tempo real.

## LMS
### Modelo de experiência
Catálogo → detalhes do curso → matrícula → módulos/aulas → player → progresso → avaliação → certificado (se existir). O usuário deve retomar onde parou e ver progresso real, não visualmente forjado.

### UI do player
Vídeo responsivo com controles, legendas quando disponíveis, velocidade e qualidade conforme provedor, acesso por teclado, transcript útil, eventos pausados/retomados, feedback de erro. Não incluir URL de vídeo privado em locais públicos.

### Catálogo
Filtros por assunto, duração, nível, progresso e disponibilidade; cards com título claro, capa confiável, carga horária real, progresso e CTA contextual; favoritos e módulos somente se dados persistirem.

### Mobile
Nos dashboards, resumos priorizados + detalhes sob ação; nas aulas, player primeiro e outline acessível logo abaixo; inputs confortáveis para toque.

## Acesso e onboarding
Convites e expiração, reset de senha, antifraude, autenticação multifator quando apropriado, respostas sem enumeração de conta; endereço de e-mail exibido apenas a quem pode vê-lo; proteção de rotas e dados no backend.
