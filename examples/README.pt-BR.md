# Exemplos de utilização

[Guia](../docs/README.pt-BR.md) · [English](README.en.md)

São cenários de trabalho com prompts copiáveis, não aplicações prontas. Adapte
conteúdo, stack e dados ao projeto. Nenhum cenário exige componentes pagos.
Dependências externas, quando úteis, precisam de licença e compatibilidade revisadas.

## Landing page premium

**Objetivo:** apresentar uma consultoria de arquitetura com identidade própria,
tipografia editorial, componentes responsivos e microinterações discretas.

**Skills:** director, design-system, marketing, assets, motion e audit; research
apenas para referências necessárias. Os nomes completos usam o prefixo `atelier-ui-`.

```text
Use atelier-ui-director para planejar e implementar o site institucional desta
consultoria de arquitetura na stack existente. Primeiro inspecione o projeto.
Proponha três direções visuais distintas e escolha uma com justificativa caso
eu não indique preferência. Trabalhe tipografia editorial, projetos em destaque,
serviços, processo e contato, usando apenas conteúdo e imagens autorizados.
Use atelier-ui-design-system e atelier-ui-marketing na implementação; assets
e motion somente onde ajudarem a comunicação. Não invente clientes, métricas
ou depoimentos. Evite dependências pagas. Finalize com atelier-ui-audit.
```

**Resultado esperado:** composição coerente com a marca, navegação clara,
componentes adaptados ao mobile e contato com estados definidos. Integração de envio
depende do backend disponível; não declarar um formulário funcional sem testá-lo.

**Validar:** CTA e links, teclado/foco, contraste, envio e erro do formulário quando
integrado, imagens responsivas, movimento reduzido, overflow e build/testes existentes.
Inspecionar screenshots em desktop, tablet e mobile.

## Dashboard corporativo

**Objetivo:** permitir análise operacional com indicadores, filtros, tabelas e
gráficos legíveis, preservando os cálculos e contratos de dados.

**Skills:** product, design-system e audit; director para decisões visuais amplas.

```text
Use atelier-ui-product e atelier-ui-design-system para melhorar este painel
corporativo. Inspecione fontes, contratos, cálculos e permissões antes de mudar
a UI. Organize resumo de indicadores, filtros de período/equipe e tabela de
detalhes, com gráficos adequados às perguntas existentes. Mostre unidades,
contexto temporal e atualização. Preserve filtros, exportações e ações atuais.
Cubra loading, vazio, erro e ausência de permissão. Em mobile, priorize tarefas
e ofereça acesso ao detalhe sem simplesmente encolher a tabela.
Use atelier-ui-audit para validar. Dados de demonstração devem estar identificados.
```

**Resultado esperado:** leitura hierárquica, filtros compreensíveis, tabela utilizável
e estados explícitos. As skills orientam a implementação; não fornecem backend de BI.

**Validar:** cálculos contra a fonte, combinação e limpeza de filtros, ordenação,
paginação, permissões no servidor, teclado, unidades, gráficos sem depender só de
cor e desempenho com volume representativo. Registrar medidas reais quando disponíveis.

## Plataforma de cursos

**Objetivo:** organizar catálogo, aulas, área do aluno, progresso, navegação e formulários.

**Skills:** product, design-system, assets e audit; motion para feedback pontual.

```text
Use atelier-ui-product para mapear e implementar melhorias nesta plataforma
de cursos. Preserve autenticação, matrículas, APIs e regras de progresso.
Trabalhe catálogo com busca/filtros, detalhes do curso, navegação entre módulos,
página de aula e área do aluno. Use atelier-ui-design-system para estados de
formulários, foco e feedback. Considere títulos longos, curso vazio, sessão
expirada, aula indisponível e progresso salvo com erro. Não simule persistência
ou autorização como se fossem reais. Finalize com atelier-ui-audit e evidências.
```

**Resultado esperado:** percurso claro do catálogo à aula, navegação consistente,
progresso com estado compreensível e formulários utilizáveis. Vídeo, certificados e
pagamento só entram se existirem no escopo e tiverem infraestrutura correspondente.

**Validar:** fluxo com e sem matrícula, retomada e persistência do progresso,
erro de rede, validação de formulário, sessão expirada, teclado, legendas/controles
do player disponível, mobile e testes existentes.

## Modernização de frontend React

**Objetivo:** aprimorar uma aplicação existente sem regressões funcionais ou perda de desempenho.

**Skills:** audit → design-system → product, com director para direção e motion se necessário.

```text
Comece com atelier-ui-audit nesta aplicação React. Registre rotas, fluxos,
permissões, atalhos, APIs, tokens e componentes existentes, além dos testes e
screenshots que conseguir executar. Priorize problemas concretos por impacto.
Use atelier-ui-design-system e atelier-ui-product para melhorar uma tela por
vez: hierarquia, densidade, formulários, navegação e estados. Preserve regras
de negócio e contratos públicos. Evite reescrita ou nova biblioteca sem motivo.
Compare antes/depois, repita os testes afetados e relate limites da validação.
```

**Resultado esperado:** mudanças incrementais, tokens consolidados, menos
inconsistências e comportamento preservado, com diffs revisáveis.

**Validar:** regressão dos fluxos críticos, APIs e permissões, build/typecheck/lint
existentes, screenshots representativos, teclado e mobile. Compare bundle e
desempenho em condições equivalentes antes de afirmar melhora.

## Arquivos de referência incluídos

- [`AccessibleActionButton.tsx`](AccessibleActionButton.tsx): botão React tipado com estado ocupado; adapte estilos e contexto de uso.
- [`tokens.css`](tokens.css): ponto de partida de tokens, não tema obrigatório.
- [`playwright-visual.spec.ts`](playwright-visual.spec.ts): exemplo a adaptar às rotas, snapshots e configuração do projeto.

Não há aplicação, `package.json` ou runner frontend neste repositório. Esses
exemplos não foram executados como uma aplicação completa nesta publicação.
