python_sources(
    name="lib",
    sources=["__init__.py"], 
    resolve=parametrize("resolve_a", "resolve_b")
)

python_distribution(
    name="dist",
    dependencies=[
        ":lib@resolve=resolve_a",
        ":lib@resolve=resolve_b",
    ],
    provides=setup_py(
        name="pants-test-shared",
        version="0.1.0",
        description="shared",
    ),
)