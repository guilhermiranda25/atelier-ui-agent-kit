# Practical usage scenarios

[Guide](../docs/README.en.md) · [Português](README.pt-BR.md)

These are copyable work recipes, not finished applications. Adapt the stack,
content and data to your project. None requires paid components. Review licensing
and compatibility before adopting any optional external dependency.

## Premium landing page

**Goal:** present an architecture consultancy through a distinct identity,
editorial typography, responsive components and subtle microinteractions.

**Skills:** director, design-system, marketing, assets, motion and audit; use
research only when needed. Full skill names have the `atelier-ui-` prefix.

```text
Use atelier-ui-director to plan and implement this architecture consultancy's
website in the existing stack. Inspect the project first. Propose three distinct
visual directions and choose one with a rationale if I do not state a preference.
Develop editorial typography, featured projects, services, process and contact,
using authorized content and images. Implement with atelier-ui-design-system
and atelier-ui-marketing; use assets and motion only where they support the
message. Do not invent clients, metrics or testimonials. Avoid paid dependencies.
Finish with atelier-ui-audit.
```

**Expected outcome:** a coherent visual identity, clear navigation, responsive
components and defined contact states. Form submission depends on the available
backend; do not describe it as working without testing the integration.

**Validate:** links and calls to action, keyboard/focus, contrast, form success
and error where integrated, responsive images, reduced motion, overflow and
existing build/tests. Inspect actual desktop, tablet and mobile screenshots.

## Corporate dashboard

**Goal:** support operational analysis with indicators, filters, tables and
readable charts while preserving calculations and data contracts.

**Skills:** product, design-system and audit; director for broader visual decisions.

```text
Use atelier-ui-product and atelier-ui-design-system to improve this corporate
dashboard. Inspect sources, contracts, calculations and permissions before
changing the UI. Organize summary indicators, period/team filters and detail
tables, with charts suited to the existing analytical questions. Show units,
time context and freshness. Preserve current filters, exports and actions.
Cover loading, empty, error and permission states. On mobile, prioritize tasks
and access to detail instead of merely shrinking the table. Validate with
atelier-ui-audit. Clearly identify any demonstration data.
```

**Expected outcome:** clear hierarchy, understandable filters, usable tables and
explicit states. The skills guide implementation; they do not provide a BI backend.

**Validate:** calculations against source data, combined/reset filters, sorting,
pagination, server-side permissions, keyboard access, units, chart alternatives
to color and performance with representative data. Record actual measurements.

## Course platform

**Goal:** organize the catalog, lessons, student area, progress, navigation and forms.

**Skills:** product, design-system, assets and audit; motion for focused feedback.

```text
Use atelier-ui-product to map and implement improvements to this course platform.
Preserve authentication, enrollment, APIs and progress rules. Address catalog
search/filters, course details, module navigation, lesson pages and the student
area. Use atelier-ui-design-system for form states, focus and feedback. Account
for long titles, empty courses, expired sessions, unavailable lessons and failed
progress saves. Do not present simulated persistence or authorization as real.
Finish with atelier-ui-audit and evidence of the checks performed.
```

**Expected outcome:** a clear path from catalog to lesson, consistent navigation,
understandable progress and usable forms. Video, certificates and payments only
belong in scope when the corresponding infrastructure exists.

**Validate:** enrolled and unenrolled flows, resuming and saving progress,
network failures, form validation, expired sessions, keyboard use, available
player controls/captions, mobile layouts and existing tests.

## Modernizing a React frontend

**Goal:** improve an existing application's interface without functional or performance regressions.

**Skills:** audit → design-system → product; director for direction and motion when needed.

```text
Start with atelier-ui-audit on this React application. Inventory routes, flows,
permissions, shortcuts, APIs, tokens and existing components. Record the tests
and screenshots you can run. Prioritize concrete issues by impact. Use
atelier-ui-design-system and atelier-ui-product to improve one screen at a time:
hierarchy, density, forms, navigation and states. Preserve business rules and
public contracts. Avoid a rewrite or new library without a demonstrated need.
Compare before/after, rerun affected tests and report validation limits.
```

**Expected outcome:** incremental, reviewable changes, consolidated tokens,
fewer inconsistencies and preserved behavior.

**Validate:** critical flows, APIs and permissions, existing build/typecheck/lint,
representative screenshots, keyboard access and mobile behavior. Compare bundle
size and performance under equivalent conditions before claiming an improvement.

## Included reference files

- [`AccessibleActionButton.tsx`](AccessibleActionButton.tsx): typed React button with a busy state; adapt styling and usage context.
- [`tokens.css`](tokens.css): starting tokens, not a mandatory theme.
- [`playwright-visual.spec.ts`](playwright-visual.spec.ts): adapt routes, snapshots and configuration to the consuming project.

There is no application, `package.json` or frontend runner in this repository.
These snippets were not executed as a complete application for this publication.
