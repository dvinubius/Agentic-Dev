# PRD: Personal Board MVP

## Problem Statement

Auth is done, but Kanbando still has no board. A signed-in user lands on an
empty placeholder and cannot do the one thing the app exists for: capture work
as todos and move it across a Kanban board. We need the first end-to-end board
capability so the product delivers its core value and the `todos` data +
drag-and-drop foundation later features extend.

## Solution

Deliver the full lifecycle of a **personal todo** (a todo with no candidates,
visible only to its creator) on the three fixed lanes — **New**, **In
Progress**, **Done**. A user can create a todo, see it on the board, drag it
between lanes (lane = status) and reorder it within a lane, open its detail,
edit its brief (with the original preserved), and delete it. Collaboration,
deadlines, thumbnails, notes, outcome, archiving, and notifications are out of
scope this iteration and build on top of this slice later.

## User Stories

1. As a signed-in user, I want to create a todo with a title (required) and an
   optional description, so that I can capture work; it appears in the New lane.
2. As a user, I want my board to show my active personal todos in three lanes
   with per-lane counts and clear empty-lane states, so that I can see my work
   at a glance.
3. As a user, I want to drag a card between lanes, so that moving it to a lane
   sets its status (New / In Progress / Done) — there is no separate status
   control.
4. As a user, I want to reorder cards within a lane by dragging, so that my
   board reflects my own priority; this order is private to me and persists.
5. As a user, I want to open a todo's detail in a modal from its card, so that I
   can read its full brief; status is read-only here (only drag changes lanes).
6. As a creator, I want to edit a todo's title/description, so that I can refine
   it; the original brief is preserved and viewable, and an edited todo is
   marked as edited.
7. As a creator, I want to delete a todo with a confirmation step, so that I can
   permanently remove work I no longer track.

## Implementation Decisions

- **Schema:** add a `todos` table owned by `server/src/db/`: `id`, `creator_id`
  (FK → users), `title`, `description`, `lane` (`new` | `in_progress` | `done`),
  a within-lane `position` for ordering, original-brief fields to support the
  edited/original toggle (`original_title`, `original_description`, an
  `edited_at`/`is_edited` signal), and created/updated timestamps. Generated via
  `drizzle-kit generate`; applied by the existing runtime migrator.
- **Private ordering model:** personal todos have a single viewer (the creator),
  so within-lane private order is stored as a `position` on the todo itself,
  scoped per creator + lane. This satisfies the spec for personal todos. A
  per-viewer ordering structure for *collaborative* todos is explicitly deferred
  to the collaboration iteration and noted as such.
- **Service layer:** a new HTTP-agnostic `server/src/todos/service.ts` owns
  create / list-board / move (lane + position) / edit-brief / delete, mirroring
  the auth service/route split. All operations are authorized to the creator;
  the route layer never bypasses this. Input validation lives in a todos
  `validation.ts` (server-authoritative; client mirrors a subset).
- **API (all behind the auth guard, scoped to the current user):**
  - `POST /todos` — create (body: title required, optional description) → todo.
  - `GET /todos` — the caller's active board (their personal todos), ordered by
    lane + position.
  - `PATCH /todos/:id/move` — set lane and/or within-lane position.
  - `PATCH /todos/:id` — edit brief (title/description); preserves original.
  - `DELETE /todos/:id` — permanent delete (server enforces creator ownership).
  - Errors use the existing shared `ApiError` shape; 401 unauthenticated, 403
    for non-owner, 404 unknown, 400 validation.
- **Shared types:** add `Todo`, `TodoLane`, create/move/edit request + response
  types to `@kanbando/shared`, consumed by both sides.
- **Client API + state:** extend the typed `api` client (`client/src/api/`) with
  the todo calls; a board data layer (e.g. `client/src/board/`) owns load +
  optimistic move/reorder and reconciles with the server. Components never call
  `fetch` directly.
- **Board UI:** implement the Board route (`/`) per `design/` — three lane
  columns, compact cards, per-lane counts, empty-lane states — using only token
  CSS variables (no hard-coded visual values).
- **Modals as layered route state:** Create Todo (`/?new=1`) and Todo Detail
  (`/?todo=:id`) are modal states over the Board route per the IA, deep-linkable
  and Esc-closable, leaving the board mounted underneath.
- **Drag-and-drop:** DECIDED — native HTML5 Drag and Drop API, no DnD
  dependency (ADR 0003). Mouse-first, consistent with the design's accepted
  "no committed keyboard DnD" decision; optimistic move in the board data layer
  persisted via `PATCH /todos/:id/move`; lift/tilt animation gated behind
  `prefers-reduced-motion`.

## Testing Decisions

- **Server (Vitest, in-memory migrated DB seam):** todos service unit tests —
  create defaults to New lane + tail position; list returns only the caller's
  todos ordered by lane+position; move updates lane/position; edit preserves the
  original brief and flags edited; delete removes only when the caller owns it.
  Route tests — authz (401 unauthenticated, 403 non-owner, 404 unknown), happy
  paths, and validation (missing title). Reuse the existing app-factory +
  `testDb` seams.
- **Client (RTL + jsdom):** create form validation (title required) and
  optimistic insert into New; board renders lanes/counts/empty states from board
  data; detail modal opens/closes from a card and via the route query; edit-brief
  flow shows edited marker + original toggle; delete requires confirmation.
- **Drag-and-drop:** verify reorder/move at the data-layer/reducer level
  (pure ordering + persistence calls) rather than simulating pointer drags;
  the integrated drag interaction is exercised in the main-agent preview
  walkthrough.
- **Manual (preview walkthrough, main agent):** create → New; drag across all
  lanes; reorder within a lane and reload to confirm persistence; open detail;
  edit brief + view original; delete with confirm; verify counts/empty states.

## Out of Scope

- Collaboration: candidates, taking/dropping, shared lane vs. per-viewer private
  order, taker status authority (entire `specs/collaboration.md`).
- Deadlines (absolute/relative, expiry), thumbnails, notes (posts/replies/media).
- Done outcome completed/failed reclassification.
- Archiving / the Archived page, notifications + realtime, account-settings UI.
- Rate limiting and other deferred hardening already noted for auth.

## Further Notes

- **Suggested execution plan**
  1. **Read tracer** — a real, data-driven board: lean `todos` schema +
     `service.listBoard` + `GET /todos` + shared types + `api.getBoard` + board
     data layer + the Board route rendering three live lanes (counts, empty,
     loading, error/retry states). Renders empty; every layer is live.
  2. **Write tracer** — create one todo → card → reload: `service.createTodo` +
     validation + `POST /todos` + `api.createTodo` + the compact card + a
     minimal create trigger (`/?new=1`, title + optional description) so a todo
     lands in New and persists.
  3. **Create Todo, hardened** — the designed `/?new=1` modal: focus-trap / Esc /
     return-focus, server-error surfacing, validation + edge states. Builds on
     issue 2's data path (no rebuild).
  4. **Drag** — lane move + within-lane private reorder + persistence
     (`PATCH /todos/:id/move`, native HTML5 DnD per ADR 0003, optimistic +
     reconcile).
  5. **Todo Detail modal** — brief view + edit-brief (original preserved, edited
     marker) + delete-with-confirm (`PATCH /todos/:id`, `DELETE /todos/:id`).
- **DnD resolved** in ADR 0003 (native HTML5 DnD, no dependency, mouse-first).
  `design/accessibility-notes.md` records keyboard DnD as an accepted product
  gap, so no library is needed.
- Architecture, repository-map, domain-language, and development-commands docs
  will be updated as the board lands (kept accurate to code, not ahead of it).
- Authoritative inputs: `specs/accounts-and-board.md`,
  `specs/todos-and-notes.md`, `specs/lifecycle-state-table.md`,
  `design/information-architecture.md`, plus the board/create/detail screens
  under `design/html-based/screens/`.