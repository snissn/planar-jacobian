# Parallel Batch Workflow

Parallelism is allowed for issue-owned scientific construction. Mutation of canonical shared surfaces is serialized.

## Preferred round shape

```text
preflight governance check
    -> parallel issue-owned research workers
    -> one serialized postflight integration maintainer
    -> exact-main remote verification
```

## Preflight

The governance maintainer records live `main`, open pull requests, active issues, reserved owned paths, and the expected integration order. Each worker receives a distinct issue and path.

## Parallel workers

Workers may independently edit only their manifest-declared owned paths. They use issue-local labels, run issue-specific checks, perform the declared review, and produce one non-draft integration-ready PR. They do not allocate global IDs or edit shared ledgers, graphs, queues, README, STATUS, generated views, or permanent workflows.

## Serialized postflight

The integration maintainer:

1. resolves current `main`;
2. inventories all integration-ready worker PRs;
3. closes duplicate or stale PRs before replacements;
4. selects an integration order based on dependencies;
5. for each packet, transplants only owned files onto current `main` when needed;
6. allocates final claim and graph IDs dynamically;
7. reconciles shared surfaces field by field;
8. runs the packet and complete repository suites;
9. merges one PR;
10. verifies exact `main` and records a receipt before continuing;
11. runs a final whole-batch postflight;
12. updates issue #2 with final `main`, remaining leaves, and validation evidence.

## Conflict rules

- Global IDs are assigned only by the integrator in merge order.
- Published issue-local labels remain provenance and are not rewritten.
- Unrelated branch history is never merged to resolve a conflict.
- A packet that becomes stale is rebuilt by transplant from its owned path.
- One issue-owned path may have at most one open pull request.
