# Taxonomia funcional de UI/UX — checklist de cobertura

O catálogo **não** equivale à cópia das bibliotecas listadas. Ele é um inventário da funcionalidade que o agente deve saber planejar, escolher e implementar quando solicitada.

## Navegação
Global header, mobile nav, breadcrumbs, mega menu, sidebar, accordion navigation, tree navigation, command palette, tabs, jump links, pagination, prev/next, sticky section index, route transitions, profile menu, search navigation, accessible skip links.

## Inputs e formulários
Text, email, password, OTP, masked input, number, currency, date, time, date-range, select, combobox, multi-select, search, autocomplete, radio, checkbox, switch, range slider, file input, drag-and-drop upload, rich text, code editor, field array, wizard, form summary, validation, save draft, autosave, resend invitation, reset password and expired link states.

## Feedback e mensagens
Inline error, toast, snackbar, alert, error boundary, confirmation dialog, modal, sheet, optimistic update, skeleton, progress, spinner, status button, activity log, undo action, retry, empty state, partial failure, access-denied state, session timeout, offline state.

## Apresentação de dados
Metric card, sparkline, trendline, area/bar/line/pie charts, heatmap, scatter plot, gauge, progress ring, segmented bar, cohort visualization, target/budget comparisons, waterfall, decomposition, table, virtualized grid, filters, sorting, drilldown, export, crossfilter, period picker, annotations, tooltips, change legend, provenance and refresh timestamps.

## Conteúdo e marketing
Hero, product screenshot, editorial media, feature grid, asymmetric bento, visual timeline, process steps, testimonial, logo strip, quote, comparison, pricing, FAQ, blog, portfolio case, timeline, team, careers, changelog, CTA, contact form, integrated footer, localization, SEO and social preview.

## Motion e acabamento
Loading/transitions, staggered reveal, text masks, hover affordance, scroll-tied effects, parallax, marquee, expandable cards, animated tabs, scrolling progress, animated counters, morphing label, shimmer, border glow, cursor response, 3D scene, shader, particles, animation state machine and reduced-motion fallback.

## Identidade e assets
Logo mark, pictogram, Lucide icon system, illustration, product photography, mockup, typography scale, pairing, CSS font loading, palette exploration, perceptual color consistency, semantic tokens, dark mode, contrast, layout grid, spacing, surface, shadow and motion tokens.

## Apps complexos
Role-based shell, permissions, invitation onboarding, user profile, notifications center, approval flow, audit log, dashboard, course catalog, lesson player, progress tracking, certificate, e-commerce product listing, search, checkout, account area, settings, team management, integrations, activity feed and real-time updating.

## Qualidade transversal
A11y keyboard focus, screen-reader semantics, touch targets, responsive layout, dark/light mode, localization, high zoom, slow networks, browser support, reduced motion, performance budgets, visual regression, testing, privacy, asset rights, error recovery, observability and component documentation.

## Método de uso do inventário
Escolher apenas funcionalidades relevantes à tarefa, registrar **componente → estado → comportamento → papel → teste**. Uma funcionalidade só entra no escopo quando há fluxo de usuário e dado/ação correspondente. Não adicionar features meramente para preencher a página.
