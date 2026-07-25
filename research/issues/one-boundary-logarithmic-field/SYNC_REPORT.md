# Synchronization report

```text
source_main: 114aefeaf98429a3bd08ca9429b4ceebd3d21e08
candidate_revision: 02547f9a1c8c72486ad2bb07a06a10fde1351af4
review_revision: 3a96a48280228a7e38a4ca488109f90147d59b1c
rebuilt_tree_parent: 179b318fb1920ca9be3b1b564b5f165a800a64eb
allocated_claims: CLM-067 through CLM-072
leaf_status: OPEN
scientific_status: SUBCLASS_EXCLUSION_WITH_EXACT_REDUCTION
```

The synchronization allocates candidate claims, adds one active reduction node,
updates the open `L03` and supporting `L11` frontier, regenerates maintained
views, and adds exact-revision validation for the issue-owned symbolic checks.
It does not edit general governance files, mark the leaf reviewed, or create a
terminal edge to `JC_2`.

The adapter-authored successor to `rebuilt_tree_parent` exists solely to trigger
the permanent exact-revision repository workflow after GitHub-token publication.
No temporary synchronization workflow remains in the integration tree.