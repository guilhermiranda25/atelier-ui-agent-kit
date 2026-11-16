# Direção de arte de produto digital

## Sistema de diferenciação (escolher e justificar)

### 1. Narrativa
A homepage responde: quem, o que muda, prova, como funciona, ação e risco percebido. Landing pages de impacto intercalam **demonstração do produto** e **provas**, em vez de coleções de features indistintas. Texto orientado à decisão e específico ao produto; proibir claims sem suporte.

### 2. Gramática de composição
- Editorial: manchete com peso tipográfico, grid generoso, imagens documentais, separadores e contraste deliberado.
- Técnico-industrial: números dominantes, labels monoespaçados somente em metadados, diagonais ou grades precisas, ilustrações funcionais.
- Quiet luxury: superfície clara, relevo discreto, 1–2 cores de acento, foco em tipografia e fotografia contextual.
- Instrumental SaaS: grid de produto, miniaturas de funcionalidades reais, densidade controlada, action bar persistente.
- Experimental: animação ou máscara sofisticada **em um elemento focal**, com fallback estático.
- Cultura/marca: linguagem gráfica conceitual, sistema de capas, traços, estampas e composição autorais.

### 3. Matriz de decisões
| Dimensão | Opção A | Opção B | O que perguntar |
| --- | --- | --- | --- |
| Hierarquia | editorial | product-first | A compra exige inspiração ou prova? |
| Densidade | airy | compact | É marketing ou operação intensiva? |
| Tipos | neo-grotesk | contrast display | Qual credibilidade precisa transmitir? |
| Superfície | white canvas | dark interfaces | Trabalho diurno ou sensação imersiva? |
| Motion | quase imóvel | narrativa guiada | O movimento esclarece o produto? |
| Visual | editorial photography | artifact/diagram | O valor está na experiência ou na função? |

### 4. Anti-slop — indicadores de revisão
- A interface poderia ser de **qualquer** startup com troca de logo? Falha.
- Todos os blocos possuem mesmo fundo, raio e espaçamento? Falha.
- Fonte system/sans default sem hierarquia? Reavaliar.
- CTA do topo não descreve ação concreta? Reescrever.
- Ícones são decorativos sem ajudar scanning? Reduzir.
- Cada seção possui uma informação, evidência ou interação própria? Validar.
- Trocar cores resolveria todo o design? Então não existe uma composição distintiva.
- Há mais de duas animações competindo ao mesmo tempo? Reduzir.
- Glassmorphism desnecessário, gradientes fluorescentes, sombras chapadas e excesso de blur: exigir justificativa.

### 5. Especificações de composicão
Começar por um grid de 12 colunas no desktop e 4 no mobile como referência, não regra universal. `max-width` 1200–1440px para sites, painéis mais fluidos. Espaçamentos preferencialmente em escala coerente de 4/8px com exceções deliberadas. Tipografia fluida com `clamp()` e limites. Usar alinhamento óptico em logos, ícones e cap height. Visualizar em 360, 390, 768, 1024, 1280, 1440 e 1920 onde relevante.

### 6. Direções contrastantes — exemplo abstrato
**Arquitetural editorial:** contrastes de serif/sans, editorial photography, white space e módulos assimétricos. **Instrument panel:** superfície precisa, contexto de produto em destaque, indicadores e tipografia robusta. **Cinematic dark:** tratamento fotográfico profundo e uma única camada de luz/movimento funcional. Estas são categorias, não templates para reprodução mecânica.

### 7. Polimento 5 passagens
1. Alinhamento/espacamento; 2. Tipografia; 3. Conteúdo/compreensão; 4. Estados/feedback; 5. Motion/desempenho. Nunca pular da primeira para a quinta.
