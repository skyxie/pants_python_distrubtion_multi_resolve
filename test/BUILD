python_tests(
    name="test_shared",
    sources=["test_shared.py"],
    dependencies=["src/shared:lib"],
    resolve="resolve_a"
)

python_tests(
    name="test_a",
    sources=["test_a.py"],
    dependencies=["src/a:lib"],
    resolve="resolve_a"
)

python_tests(
    name="test_b",
    sources=["test_b.py"],
    dependencies=["src/b:lib"],
    resolve="resolve_b"
)