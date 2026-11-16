# Roteiro por fonte (referências pesquisadas em 16/11/2026)

### 21st.dev — catálogo e integração com agentes
`https://21st.dev/` · `https://docs.21st.dev/mcp`
- Buscar componentes React/Tailwind/shadcn por função e selecionar por preview, estrutura, comportamento e dependências.
- CLI documentada: `npm i -g @21st-dev/cli`, `21st login`, `21st search "pricing table"`, `21st add <slug-verificado>`. Skills oficiais opcionais via `npx @21st-dev/cli install-skill`.
- MCP externo `https://21st.dev/api/mcp`; usa autenticação conforme cliente/plano. Não gravar chaves em repositório.
- Limites comerciais e ferramentas mudam. Não alegar acesso gratuito ilimitado a códigos de componentes.

### Designeer — inspiração, NÃO biblioteca copiável
`https://designeer.xyz/`
- Coleções editoriais: interface, motion, 3D, typography, landing, app móvel, dashboards, portfolios e identidade.
- Extrair **princípios abstratos**: por que funciona, hierarquia, grid, color depth, ritmo, tipografia e uso da mídia. Criar composição nova. Não reproduzir arte, fotografias ou layouts pixel a pixel.

### React Bits — animação como semântica
`https://reactbits.dev/` · `https://github.com/DavidHDev/react-bits`
- Categorias: text animations, animations, components, backgrounds, micro-interactions. Variantes JS/TS + CSS/Tailwind.
- Registry `@react-bits` normalmente via shadcn em `components.json`, mas nomes variam; confirmar antes de instalar.
- Testar render client/SSR, motion reduction, impacto GPU, foco e navegabilidade. Preferir entrada progressiva e baixa intensidade.

### Magic UI — marketing com clareza
`https://magicui.design/` · `https://magicui.design/docs/installation`
- Exemplos: `marquee`, `bento-grid`, `blur-fade`, `number-ticker`, `globe`, `animated-grid-pattern`, `shimmer-button`, `dot-pattern` — validar nomes atuais.
- Instalação documentada: `npx shadcn@latest add @magicui/<slug>`.
- Evitar efeitos simultâneos; testes com tema escuro/claro, reduced motion, screenshot e throttling.

### Uiverse — componentes comunitários
`https://uiverse.io/`
- Snippets HTML/CSS/Tailwind/React/Figma. Adaptar sem estilos globais conflitantes; converter `div` clicável para elemento semântico quando necessário.
- Verificar licença e atribuições por item quando fornecidas. Não presumir que qualquer componente comunitário é 100% acessível.

### Hairline UI — product-native details
`https://hairlineui.com/` · `https://hairlineui.com/ui/mcp`
- Componentes utilitários shadcn e interações discretas; exemplo oficial de registry: `npx shadcn@latest add hairlineui.com/r/status-button.json`.
- MCP read-only `https://hairlineui.com/api/mcp` e `search_components`, `find_for_screen`, `get_component`, `get_component_source`, `get_install_command` quando cliente oferece suporte.
- As informações de contagem no site podem variar. Registry ou templates pagos exigem suas licenças.

### Lucide — ícones
`https://lucide.dev/guide/react/`
- `lucide-react`; imports nomeados/tree-shakable e tamanho/stroke padronizados, `aria-hidden` decorativos e accessible name para icon-only.

### unDraw — ilustração com limites
`https://undraw.co/` · `https://undraw.co/license`
- Download pontual manual de asset adequado. Licença exclui criação de serviço concorrente, redistribuição em packs, certas integrações/scraping e uso em datasets/treinamento de IA. Não empacotar ilustrações nesta skill.

### Shots — apresentação e marketing
`https://shots.so/`
- Mockups em dispositivos, composições, animações, zoom e exportações. Usar screenshots próprios com permissões adequadas; evitar fabricar interfaces de produto inexistentes.

### Coolors — design tokens
`https://coolors.co/` · `https://www.coolors.app/`
- Paletas, imagem para cor, visualizer, contraste, gradientes e exportações. Algumas ferramentas/limites podem ser pagos. Converter paleta em tokens semânticos e verificar WCAG de novo com cores reais.

### Fontshare — tipografia
`https://fontshare.com/` · `https://www.fontshare.com/about` · `https://fontshare.com/licenses/sil-ofl`
- Famílias podem seguir ITF FFL (fechadas/gratuitas) ou SIL OFL (open source). Verificar a licença individual e regras de redistribuição/embedding. Preferir `font-display: swap`, subconjuntos e fallback robusto.

## Avaliação ponderada (0–5 por critério)
1. Aderência à função (peso 30%); 2. Acessibilidade/estados (20%); 3. Performance (15%); 4. Qualidade do código e manutenibilidade (15%); 5. Originalidade/adaptação (10%); 6. Licença/risco (10%). Eliminar candidato que viola licenças, segurança ou fluxo crítico independentemente do total.
