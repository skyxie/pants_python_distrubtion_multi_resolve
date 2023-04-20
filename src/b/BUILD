python_requirement(
    name="pandas",
    requirements=["pandas>=1.5"],
    resolve="resolve_b"
)

python_sources(
    name="lib",
    sources=["__init__.py"],
    dependencies=[":pandas", "src/shared:lib"],
    resolve="resolve_b"
)