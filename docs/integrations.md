# Integrações para componentes de verdade

As skills são autosuficientes e **não** precisam de serviços externos. Se quiser que agentes busquem componentes em tempo real, habilite cada integração explicitamente. Confirme comandos nas documentações porque o ecossistema muda.

## Validation scope / Escopo da valida??o

The commands below are optional provider workflows, not requirements for installing
Atelier UI. Their official documentation was consulted on 2026-11-16, but no
third-party installer, login or live MCP operation was executed. Recheck the
provider's current instructions and license before use. The complete restoration
catalog may configure some integrations; isolated installation does not.

Os comandos abaixo s?o opcionais e n?o foram executados nesta publica??o.
As skills orientam a sele??o; elas n?o concedem acesso a contas ou planos.

## 21st
Documentação: https://docs.21st.dev/mcp

```sh
npm i -g @21st-dev/cli
21st login
21st search "pricing table"
# Confirmar o slug do resultado antes de instalar
21st add <slug-confirmado>
# Opcional: habilidades oficiais da 21st no agente
npx @21st-dev/cli install-skill
```

MCP `https://21st.dev/api/mcp` requer autenticação conforme cliente. Não salvar token no código. Planos podem limitar downloads/geração.

## Hairline UI
MCP público `https://hairlineui.com/api/mcp`.

```sh
claude mcp add --transport http --scope user hairline-ui https://hairlineui.com/api/mcp
# Alternativa Codex, se a CLI instalada suportar:
codex mcp add hairline-ui --url https://hairlineui.com/api/mcp
```

As chamadas do servidor são de consulta; a instalação real no projeto é efetuada explicitamente pelo shadcn CLI após avaliação.

## Magic UI

```sh
npx shadcn@latest init  # somente se o projeto não está configurado
npx shadcn@latest add @magicui/blur-fade
```

Fonte: https://magicui.design/docs/installation . MCP próprio documentado em https://magicui.design/docs/mcp . Não habilitar `shadcn` MCP sem checar integração já existente.

## React Bits

No `components.json` do projeto:

```json
{
  "registries": {
    "@react-bits": "https://reactbits.dev/r/{name}.json"
  }
}
```

Confirmar o nome da variante JS/TS/CSS/TW na fonte antes do `shadcn add`; não misturar Pro sem licença.

## Uiverse
Copiar **somente** snippets selecionados manualmente e aprovados, isolar estilos e reescrever para conformidade semântica, teclado e acessibilidade. Não instalar toda a biblioteca no global.

## Lucide

```sh
npm install lucide-react
```

Usar imports nomeados; não fazer import abrangente de todos os ícones.

## Fontshare / unDraw / Shots / Coolors
Uso por curadoria e download pontual conforme termos. Não configurar crawlers para baixar material em massa. Usar ferramentas manualmente quando necessário e converter decisões em tokens/arquivos próprios.
