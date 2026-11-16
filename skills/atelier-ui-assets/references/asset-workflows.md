# Fluxos por mídia

## Ícones
Escolher uma família consistente e estados; não misturar versões filled/stroke sem razão semântica. Objetos decorativos com `aria-hidden`; elementos interativos com nome acessível, hit target apropriado e tooltip apenas complementar. Não usar ícone no lugar de texto importante em nav compacta sem label acessível.

## Ilustração
Pedir autorização/procurar asset permitido; selecionar uma peça pontual e adaptar cor sem afetar a integridade. SVG otimizado, alt descritivo **ou** alt vazio se decorativo. Não redistribuir pacotes unDraw. Proibido usar ativos unDraw para treinamento de modelos.

## Mockups
1. Capturar tela real e limpa, sem dados pessoais e sem informação confidencial. 2. Compor uma cena de apresentação compatível com produto. 3. Exportar asset comprimido e screenshot puro para casos sem motion. 4. Testar legibilidade do conteúdo em tamanho real.

## Paleta e contraste
Começar da identidade existente; depois usar ferramenta de exploração para complementar. Testar 4.5:1 textos normais, 3:1 textos grandes e elementos gráficos essenciais; gradients e overlays verificam no ponto de pior contraste.

## Fontes
- Selecionar por métricas, personalidade, alfabeto pt-BR e numerais.
- Validar licenças SIL OFL ou ITF FFL conforme família; não assumir que fontes fechadas gratuitas podem ser redistribuídas no ZIP.
- Minimizar famílias/pesos; fallback com métricas razoavelmente alinhadas, `font-display: swap`; prevenir layout shifts.

## Manifest de assets
| Asset | Tipo | Finalidade | Fonte | Licença verificada | Uso | Alt | Formato | Peso |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| screenshot-dashboard.webp | Produto real | demonstração | equipe | próprio | hero | "Tela do painel..." | WebP | medir |

## Cuidados com dados
Capturas de dashboards, contratos e aplicações empresariais precisam de dados anonimizados e consentimento; não subir PII, API keys ou informações financeiras confidenciais em ferramenta de mockups sem autorização.
