from llm_docs import docs_loader
import pytest


@pytest.mark.parametrize("package", (None, "sqlite-utils"))
def test_llm_docs(package):
    fragment = docs_loader(package)
    expected = package or "llm"
    assert fragment.source.startswith(
        f"https://raw.githubusercontent.com/simonw/docs-for-llms/refs/heads/main/{expected}/"
    )
