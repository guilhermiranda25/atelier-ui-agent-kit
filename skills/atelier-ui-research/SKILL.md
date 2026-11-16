---
name: atelier-ui-research
description: Research and evaluate premium UI components, visual references and licenses across 21st.dev, designeer.xyz, reactbits.dev, magicui.design, uiverse.io and hairlineui.com; use before adopting external frontend patterns.
---

# Atelier UI Research — Curadoria e engenharia de referência

## Estratégia

- Primeiro audite o projeto: qual problema não foi resolvido pelos componentes e tokens existentes?
- Pesquise **intenções de interação**, não somente nomes ('filterable combobox accessible', não 'cool dropdown').
- Procure no catálogo de fontes e registre `nome`, `URL oficial`, `finalidade`, `compatibilidade`, `licença`, `dependências`, `ações de manutenção`, `estados e acessibilidade`, `custo de bundle`, `última verificação`.
- Compare pelo menos dois caminhos quando dependências ou licenças não forem claras: componente terceiro vs implementação própria.
- Priorize código explícito e pequenas dependências; só importe partes necessárias. Não clonar sites nem copiar UI comercial inteira.
- Teste o snippet em um sandbox/repo antes de produção; a galeria não garante qualidade, segurança ou WCAG.
- Links e nomes de componentes mudam; consulte a fonte oficial no momento da implementação se acesso web disponível.

## Fontes e especialidades

| Fonte | Melhor uso |
| --- | --- |
| 21st.dev | Exploração semântica de componentes React/Tailwind/shadcn, templates e temas, revisão de padrões |
| designeer.xyz | Direções visuais, layout, motion, branding, portfólios e crítica comparativa |
| reactbits.dev | Text motion, microinterações, fundos, transições e componentes reativos |
| magicui.design | Elementos de destaque de marketing, provas sociais e motion refinado |
| uiverse.io | Microcomponentes CSS/HTML, estados hover/focus, experimentos isolados |
| hairlineui.com | Controles utilitários de aplicação e motion discretíssimo, registry/MCP |
| lucide.dev | Iconografia funcional consistente, sem misturar famílias |
| undraw.co | Ilustrações contextualizadas, respeitando licença e seleção manual |
| shots.so | Composição e exportação de mockups do próprio produto |
| coolors.co | Ideação e teste de paletas, contraste e exploração de variações |
| fontshare.com | Fontes profissionais com licença por família |

## Integrações e permissões

Leia `references/source-playbook.md` e `references/licensing-security.md`. Não presumir que `free`, `open-source` ou `copy-paste` significa direito de redistribuir. Para componentes de terceiros: consultar licença específica do autor e registrar link/versão. Para assets: não fazer scraping, baixar em massa ou usar como datasets de IA.

## Resultado obrigatório

Entregar uma **decisão fundamentada** (adotar/adaptar/criar), não um catálogo indiscriminado. Informar nomes/links reais e requisitos de instalação. Não inventar slug ou URL de componente.
