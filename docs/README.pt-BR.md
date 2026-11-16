# Atelier UI Agent Kit — guia em português

[Início](../README.md) · [English](README.en.md) · [Exemplos](../examples/README.pt-BR.md)

## O que é

Uma coleção de oito skills e fluxos de trabalho para melhorar projetos frontend
desenvolvidos com agentes de IA. Reúne conhecimento de UI/UX, diretrizes de
implementação, critérios de qualidade, referências e scripts auxiliares. Ajuda o
agente a diagnosticar uma interface, definir decisões visuais e implementar
mudanças sem perder funcionalidades existentes.

Não é um serviço de geração de interfaces, uma biblioteca pronta de componentes
ou um substituto para sua stack de desenvolvimento. A execução depende das
ferramentas e permissões do agente. As instruções das skills são principalmente
em português, com descrições de descoberta em inglês.

Autor: [Guilherme Miranda](https://github.com/guilhermiranda25). Versão: 1.0.0.

## As oito skills

| Skill | Objetivo e quando usar | Trabalho orientado e exemplo |
| --- | --- | --- |
| `atelier-ui-director` | Coordenar projetos novos ou redesigns amplos | Inspecionar o frontend, organizar briefing, propor direções, definir critérios e coordenar entrega. Exemplo: site institucional com identidade própria. |
| `atelier-ui-research` | Avaliar recursos antes de adotar dependências | Comparar referências, licenças, compatibilidade e manutenção. Exemplo: escolher entre adaptar um seletor existente e incorporar um componente externo. |
| `atelier-ui-design-system` | Criar ou consolidar fundamentos visuais | Mapear tokens, tipografia, cores semânticas, temas e estados. Exemplo: unificar formulários de vários módulos. |
| `atelier-ui-marketing` | Construir páginas públicas | Trabalhar mensagem, composição editorial, provas reais, CTAs e mobile. Exemplo: landing page de consultoria. |
| `atelier-ui-product` | Melhorar aplicações orientadas a tarefas | Planejar navegação, filtros, tabelas, formulários, permissões e estados. Exemplo: painel operacional ou plataforma de cursos. |
| `atelier-ui-motion` | Comunicar mudanças por movimento | Definir transições, feedback, timings e fallback acessível. Exemplo: abrir um drawer preservando foco e respeitando movimento reduzido. |
| `atelier-ui-assets` | Selecionar recursos visuais coerentes | Organizar ícones, imagens, ilustrações, fontes e paletas com origem e otimização. Exemplo: padronizar iconografia sem inflar o bundle. |
| `atelier-ui-audit` | Avaliar antes e depois de mudanças | Conferir screenshots, teclado, contraste, estados, responsividade, desempenho e testes. Exemplo: identificar regressões no checkout mobile. |

Cada diretório em `skills/` mantém seu `SKILL.md` e os materiais complementares.
Não é preciso carregar tudo ao mesmo tempo. Um fluxo comum é director →
design-system → marketing ou product → motion/assets quando necessários → audit.
Research entra em decisões sobre recursos externos. Em aplicações existentes,
comece pela audit para registrar o comportamento atual.

## Princípios de design

A identidade nasce do produto, do conteúdo e das necessidades do público. O kit
orienta composições originais, tipografia com hierarquia clara, componentes
consistentes e microinterações que comuniquem estado. Evitar *AI slop* significa
questionar soluções repetidas sem contexto: o mesmo hero, os mesmos cards e os
mesmos efeitos aplicados a produtos diferentes.

Qualidade visual deve acompanhar qualidade técnica: semântica, acessibilidade,
responsividade, foco visível, contraste, performance e manutenção. Desktop e
mobile precisam manter uma experiência coerente, com prioridades adaptadas ao uso.
Preserve APIs, permissões e regras de negócio. Uma animação não deve impedir a
leitura nem substituir feedback funcional.

## Preparar o ambiente

1. Instale Python 3.10+ e confira `py --version` no Windows.
2. Para clonar, instale Git e confira `git --version`.
3. Se ainda não utiliza um agente, instale e autentique o
   [Codex](https://developers.openai.com/codex/quickstart) ou o
   [Claude Code](https://code.claude.com/docs/en/setup) seguindo as fontes oficiais.
   A instalação isolada das skills não precisa da CLI, Node.js ou Git.
4. Obtenha o kit e entre na pasta:

```powershell
git clone https://github.com/guilhermiranda25/atelier-ui-agent-kit.git
cd atelier-ui-agent-kit
```

Também é possível extrair o código-fonte da release ou baixar seus assets.
Mantenha o restaurador e `uiux-skillpack.zip` juntos. O ZIP portátil contém apenas
skills e manifesto; os restauradores são assets separados e também estão no clone.
No Linux/macOS, use `python3` no lugar de `py`. A restauração completa é voltada ao Windows.

## Instalar e usar no Codex

```powershell
py restaurar_codex.py --somente-uiux --dry-run
py restaurar_codex.py --somente-uiux
```

O escopo padrão é usuário: `%USERPROFILE%\.agents\skills\atelier-ui-*`.
É uma instalação global para seus projetos. `CODEX_HOME` controla a configuração
da CLI no restaurador, mas não muda esse destino de skills.

Para um projeto específico:

```powershell
py restaurar_codex.py --somente-uiux --uiux-escopo projeto --uiux-projeto "C:\projetos\meu-app" --dry-run
py restaurar_codex.py --somente-uiux --uiux-escopo projeto --uiux-projeto "C:\projetos\meu-app"
```

O destino é `<projeto>\.agents\skills\`. Sem `--uiux-projeto`, usa a pasta atual;
indique o caminho para não instalar no clone do kit por engano. A pasta pode ser
criada se ainda não existir. Abra uma nova sessão do Codex no projeto e confira:

```powershell
Get-ChildItem "$env:USERPROFILE\.agents\skills\atelier-ui-*\SKILL.md"
# Para instalação por projeto:
Get-ChildItem "C:\projetos\meu-app\.agents\skills\atelier-ui-*\SKILL.md"
```

Na conversa, peça `Use atelier-ui-audit para revisar este frontend`. Clientes
com seleção explícita de skills também podem aceitar `$atelier-ui-audit`.
A interface varia por versão; consulte a
[documentação oficial de skills](https://developers.openai.com/codex/skills).
Este kit não depende de um comando de terminal `codex install-skill`.
`.codex-plugin/plugin.json` é uma camada de compatibilidade preservada, não uma
instalação de plugin validada em todos os clientes. Prefira o restaurador Python.

## Instalar e usar no Claude Code

```powershell
py restaurar_claude.py --somente-uiux --dry-run
py restaurar_claude.py --somente-uiux

# Alternativa por projeto:
py restaurar_claude.py --somente-uiux --uiux-escopo projeto --uiux-projeto "C:\projetos\meu-app" --dry-run
py restaurar_claude.py --somente-uiux --uiux-escopo projeto --uiux-projeto "C:\projetos\meu-app"
```

O destino de usuário é `%USERPROFILE%\.claude\skills\`, ou
`%CLAUDE_CONFIG_DIR%\skills\` quando definido. Por projeto, é
`<projeto>\.claude\skills\`. Reinicie a sessão, confira os `SKILL.md` com
`Get-ChildItem` e solicite a skill pelo nome. A autenticação do agente é separada.

### Alternativa: marketplace/plugin

Escolha este método em vez de copiar as mesmas skills pelo restaurador:

```powershell
claude plugin marketplace add guilhermiranda25/atelier-ui-agent-kit
claude plugin install atelier-ui@atelier-ui-marketplace --scope user
```

Para um plugin de projeto, execute no projeto e use `--scope project`. O manifesto
e o fluxo foram conferidos com Claude Code 2.1.325; o
[registro de validação](validation.md) distingue os testes locais e remotos.
No Claude, skills de plugin usam namespace, como `/atelier-ui:atelier-ui-audit`.
Confira a descoberta na versão instalada. O validador avisa sobre ícone ausente
para catálogo público; isso não impediu a instalação pelo marketplace próprio.

Copiar skills, registrar plugins e configurar servidores MCP são operações
distintas. A instalação isolada não registra plugins nem configura MCPs.

## Exemplos de conversa

```text
Use atelier-ui-director, atelier-ui-marketing e atelier-ui-audit para criar
uma landing page de uma consultoria de arquitetura. Proponha uma identidade
editorial própria, conteúdo verificável e componentes responsivos, com
microinterações sutis. Não dependa de componentes pagos.
```

```text
Use atelier-ui-product e atelier-ui-design-system para construir um dashboard
com os dados e contratos existentes. Priorize indicadores com unidades e período,
filtros, tabelas e gráficos legíveis. Audite teclado e mobile.
```

```text
Use atelier-ui-audit para diagnosticar esta aplicação React. Depois melhore
hierarquia, formulários e navegação com atelier-ui-product. Preserve rotas,
regras de negócio e APIs. Valide os fluxos atuais antes e depois das alterações.
```

```text
Use atelier-ui-design-system para inventariar os estilos do projeto e consolidar
tokens semânticos, tipografia, espaçamento e contratos de componentes.
Migre uma tela representativa, registre as decisões e confira seus estados.
```

```text
Use atelier-ui-audit para revisar acessibilidade e responsividade nas rotas
principais. Verifique foco, teclado, contraste, zoom e overflow em mobile.
Liste evidências e severidade, corrija os problemas e repita os casos afetados.
```

```text
Use atelier-ui-motion para melhorar o feedback dos botões e as transições
de drawers existentes. Respeite prefers-reduced-motion, preserve foco e teclado
e evite mudanças de layout. Meça o que for possível e registre as limitações.
```

Os [quatro cenários completos](../examples/README.pt-BR.md) detalham objetivos,
prompts, resultados esperados e validação. São receitas adaptáveis, não quatro
aplicações prontas incluídas no pacote.

## Release, instalação remota e integridade

A origem oficial é o [GitHub](https://github.com/guilhermiranda25/atelier-ui-agent-kit).
A [release v1.0.0](https://github.com/guilhermiranda25/atelier-ui-agent-kit/releases/tag/v1.0.0)
distribui o ZIP, os dois restauradores, o manifesto e `SHA256SUMS.txt`.
Com o restaurador obtido do clone ou dos assets, use a URL e o hash fixos:

```powershell
py restaurar_codex.py --somente-uiux --uiux-url "https://github.com/guilhermiranda25/atelier-ui-agent-kit/releases/download/v1.0.0/uiux-skillpack.zip" --uiux-sha256 "d4b587421435cb15fb06a89ae8f62a4c02979e881768d5d61f62773325c8b7c0"
py restaurar_claude.py --somente-uiux --uiux-url "https://github.com/guilhermiranda25/atelier-ui-agent-kit/releases/download/v1.0.0/uiux-skillpack.zip" --uiux-sha256 "d4b587421435cb15fb06a89ae8f62a4c02979e881768d5d61f62773325c8b7c0"
```

Também funciona por variáveis na sessão do PowerShell:

```powershell
$env:UIUX_SKILL_URL = "https://github.com/guilhermiranda25/atelier-ui-agent-kit/releases/download/v1.0.0/uiux-skillpack.zip"
$env:UIUX_SKILL_SHA256 = "d4b587421435cb15fb06a89ae8f62a4c02979e881768d5d61f62773325c8b7c0"
py restaurar_codex.py --somente-uiux
# Remova para voltar ao pacote local:
Remove-Item Env:UIUX_SKILL_URL
Remove-Item Env:UIUX_SKILL_SHA256
```

As opções prevalecem sobre variáveis. `--uiux-origem` seleciona ZIP ou pasta local
e prevalece sobre a URL. Sem origem explícita, URL ou variáveis, usa o ZIP ao lado
do script; na ausência dele, usa `skills/` com manifesto. O hash externo verifica
o ZIP, não uma pasta. O manifesto interno verifica arquivos em ambos os casos.

```powershell
Get-FileHash .\uiux-skillpack.zip -Algorithm SHA256
```

Compare com o hash da release confiável. SHA-256 identifica os bytes esperados;
o manifesto interno detecta inconsistências, mas não autentica sozinho a origem.
O download sem hash continua aceito por compatibilidade; forneça-o em automações.
URL e hash precisam pertencer à mesma versão. `--dry-run` apenas mostra o plano:
não baixa nem verifica o conteúdo do ZIP.

## Backup, recuperação e atualização

A instalação substitui somente os oito diretórios `atelier-ui-*`. O conteúdo
anterior fica em `~/restauracao-agentes/<agente>-<data>/uiux-previous/`. O mesmo
diretório contém `resultado.json` e `LEIA-ME.txt`; saída 2 indica pendências.
Não há backup de uma skill que ainda não existia. Outras skills permanecem no destino.

Para recuperar uma personalização, feche o agente e copie a pasta da skill de
`uiux-previous/` para o destino. Para voltar a uma versão conhecida, reinstale o
ZIP daquela release com seu hash. Em uma falha de substituição, o instalador tenta
restaurar o conteúdo anterior; falhas de disco ou permissão também podem afetar
essa recuperação. Inspecione o backup nesses casos. Não publique relatórios e
backups da restauração completa, que podem conter configurações pessoais.

Para atualizar um clone sem sobrescrever alterações locais:

```powershell
git status --short
git pull --ff-only
py scripts/build_skillpack.py --check
py restaurar_codex.py --somente-uiux --dry-run
py restaurar_codex.py --somente-uiux
# Ou, para Claude:
py restaurar_claude.py --somente-uiux
```

Revise o changelog e a versão. Para reprodutibilidade, use uma tag publicada em
um clone limpo (`git switch --detach v1.0.0`) ou URL de release e hash fixos.
Evite links `latest` em automações críticas. Atualize URL e hash das variáveis
juntos, ou remova-os para usar o ZIP do clone. Reinicie o agente após instalar.
Modificações locais nas oito skills serão substituídas, com backup.

Se utiliza plugin Claude, atualize pelo gerenciador, sem duplicar via restaurador:

```powershell
claude plugin marketplace update atelier-ui-marketplace
claude plugin update atelier-ui@atelier-ui-marketplace
```

## Restauração completa: operação separada

```powershell
py restaurar_codex.py --dry-run
py restaurar_claude.py --dry-run
# Execute somente se quiser o catálogo completo:
py restaurar_codex.py
py restaurar_claude.py
```

Sem `--somente-uiux`, os scripts restauram também o catálogo anterior de plugins,
skills, ferramentas e MCPs. Podem instalar ou atualizar CLIs, dependências npm/pip
e ferramentas de navegador. Exigem Git e Node.js 22.20+ além de Python; integrações
podem exigir programas locais e autenticação posterior. O catálogo consulta fontes
externas que podem mudar. Veja `--help` para `--sem-ferramentas`, `--manter-cli`
e `--sem-uiux`. O fluxo amplo foi preservado, mas não foi executado nesta publicação.

## Onze referências de UI/UX

| Referência independente | Papel no projeto |
| --- | --- |
| [21st.dev](https://21st.dev) | Pesquisa de componentes, padrões e temas |
| [Designeer](https://designeer.xyz) | Referências de composição e direção visual |
| [React Bits](https://reactbits.dev) | Estudo de animações e componentes React |
| [Magic UI](https://magicui.design) | Componentes animados e páginas de marketing |
| [Uiverse](https://uiverse.io) | Pesquisa de microcomponentes e estados HTML/CSS |
| [Hairline UI](https://hairlineui.com) | Referências de componentes, templates e padrões |
| [Lucide](https://lucide.dev) | Iconografia consistente e funcional |
| [unDraw](https://undraw.co) | Ilustrações contextualizadas |
| [Shots](https://shots.so) | Apresentação de screenshots próprios em mockups |
| [Coolors](https://coolors.co) | Exploração de paletas para tokens de cor |
| [Fontshare](https://fontshare.com) | Pesquisa tipográfica e hierarquia |

O pacote não inclui as bibliotecas, componentes ou recursos desses serviços e não
tem afiliação com eles. Cada material depende da licença de sua origem. Gratuidade
de acesso não autoriza redistribuição indiscriminada. Veja [fontes e direitos](sources-and-rights.md)
e [integrações opcionais](integrations.md). Os exemplos não exigem componentes pagos.

## Problemas comuns e limites

| Sintoma | Verificação e ação |
| --- | --- |
| `py` não encontrado | Instale Python; confira `python --version` e use o executável correto. No Linux/macOS, use `python3`. |
| Launcher procura `python3.exe` inexistente | Confira se baixou o restaurador atualizado; use `py -3.14` se essa versão estiver instalada. |
| Skill não aparece | Confira escopo, destino e os oito `SKILL.md`. Abra nova sessão no projeto correto e consulte a descoberta de skills do cliente. |
| Skills duplicadas | Evite instalar as mesmas skills globalmente, por projeto e por plugin no mesmo agente. |
| SHA-256 ou manifesto inválido | Confira versão, URL, variáveis e checksum. Não ignore a falha; baixe de uma release confiável. |
| ZIP ausente | Mantenha ZIP e restaurador juntos ou use URL com hash; uma pasta local exige manifesto. |
| Download falha | Confira rede, proxy, certificado TLS e URL do asset. Não desative TLS. |
| Arquivo bloqueado ou sem permissão | Feche processos que usem os arquivos; confira escrita no destino e no backup. |

Os instaladores não executam código do ZIP. Rejeitam traversal, symlinks de entrada,
duplicatas, nomes Windows não portáveis e volumes acima dos limites. Skills ainda
contêm instruções: revise sua origem. Scripts de contraste e estrutura são auxiliares,
não certificação WCAG nem SAST. Exemplos React/Playwright precisam da stack e das
rotas do projeto consumidor. Veja [validação](validation.md) e [manutenção](maintenance.md).
