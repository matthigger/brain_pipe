"""Pytest config for brain_pipe tests.

Auto-discovery (`pytest` with no args) runs only fast tests. Slow tests
that re-run the dataset pipeline must be invoked by explicit path:

    pytest tests/test_repro_hcp_ya_open.py             # both repro tests
    pytest tests/test_repro_hcp_ya_open.py::test_dti_single_subject_deterministic

Add new slow test files to ``collect_ignore`` below.
"""

collect_ignore = [
    "test_repro_hcp_ya_open.py",
]
