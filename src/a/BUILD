python_requirement(
    name="pandas",
    requirements=["pandas<1.5"],
    resolve="resolve_a"
)

python_sources(
    name="lib",
    sources=["__init__.py"],
    dependencies=[":pandas", "src/shared:lib"],
    resolve="resolve_a"
)

python_distribution(
    name="dist",
    dependencies=[":lib"],
    provides=setup_py(
        name="pants-test-a",
        version="0.1.0",
        description="a",
    ),
)