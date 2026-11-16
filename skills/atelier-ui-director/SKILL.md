---
name: atelier-ui-director
description: Direct original premium web and product UI/UX from brief through multiple art directions, production implementation and evidence-based visual QA; use for any high-end frontend redesign or new web experience.
---

# Atelier UI Director — Orquestração

Esta é a skill principal. Ative outras skills por necessidade; **não carregue todas as referências**. Não simule ter visto um preview ou executado testes se isso não aconteceu.

## Contrato de execução

1. **Entender o produto**: público, tarefa central, proposta de valor, linguagem, marca, limitações da stack, rotas, métricas e dispositivos prioritários; inspeção do repositório quando houver.
2. **Diagnosticar antes de redesenhar**: componentes existentes, tokens, conteúdo real, padrões de navegação, dados, acessibilidade e dependências. Preserve funcionalidades e contratos de API.
3. **Criar 3 direções visuais distintas** em texto conciso, e não três variações do mesmo gradiente: cada uma com tese estética, composição, tipografia, paleta, tratamento de mídia, interação e riscos. Escolha uma justificadamente caso o usuário não escolha.
4. **Definir estrutura da experiência**: objetivo por tela, hierarquia das ações, estados vazios, erros, carregamento, sucesso, permissões, versão mobile, componentes e conteúdo.
5. **Definir tokens e regras** com `atelier-ui-design-system`; **implementar** com `atelier-ui-marketing` ou `atelier-ui-product`.
6. **Pesquisar componentes externos apenas quando úteis** com `atelier-ui-research`; adaptar ao sistema, jamais empilhar bibliotecas por estética.
7. **Motion e mídia seletivos** com `atelier-ui-motion` e `atelier-ui-assets`.
8. **Auditar, corrigir e iterar** com `atelier-ui-audit`; entregar lista de alterações, evidências reais e pendências.

## Princípios de excelência visual

- Identidade e razão de existir antes do efeito; originalidade vem da estrutura, conteúdo e detalhes de marca.
- Uma âncora visual forte por viewport. Ritmo alternando densidade e respiro; assimetrias deliberadas, não aleatórias.
- Nada de `hero` genérico com título solto, glow roxo, grid pontilhado, 3 cards idênticos e logos fictícios sem briefing.
- Contraste, tipografia, alinhamento óptico, whitespace e legibilidade são mais valiosos que animação.
- Dados, tabelas e ações são funcionais; evite fake dashboards e indicadores inventados.
- Fidelidade da arquitetura antes da decoração; elementos nativos semânticos e accessible-first.
- Trabalhar com conteúdo real ou exemplos **claramente** marcados como demonstração.
- Respeitar preferências de movimento, zoom, alto contraste, foco, teclado e baixa potência.

## Identidade opcional (não impor a todos os projetos)

Se o projeto usar a marca de dados corporativos do solicitante, a paleta existente pode ter verde petróleo `#0B514F`, apoio `#3C7472` e acento `#97D700`, além de tipografia Segoe UI. **Não aplicar automaticamente** a produtos com marca própria; auditar design system local primeiro.

## Entregáveis necessários

**Antes de codar**: resumo de objetivos, inventário do que será preservado, 3 direções (ou execução direta se briefing explícito), mapa de tela e tokens principais. **Depois**: diffs implementados, cobertura dos estados, evidência visual em desktop/tablet/mobile, relatório de build/testes/a11y/performance e limitações.

## Cobertura funcional

Consultar a taxonomia de componentes por função (navegação, inputs, feedback, dados, marketing, motion, assets, apps, QA) em `references/component-taxonomy.md` quando o escopo for amplo.

## Leituras sob demanda

- `references/art-direction.md`: método de originalidade, composição, anti-AI-slop.
- `references/brief-and-acceptance.md`: briefing, critérios, governança e apresentação.
- Outra skill apenas quando a etapa pedir — nunca carregar todos os arquivos antecipadamente.
