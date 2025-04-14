import httpx
from llm_docs import docs_loader, docs_loader_preview, INDEX_URL
import pytest


@pytest.mark.parametrize("package", (None, "sqlite-utils"))
def test_llm_docs(package):
    fragment = docs_loader(package)
    expected = package or "llm"
    assert fragment.source.startswith(
        f"https://raw.githubusercontent.com/simonw/docs-for-llms/refs/heads/main/{expected}/"
    )


def test_llm_docs_preview():
    fragment = docs_loader_preview("datasette")
    filename = fragment.source.split("datasette/")[1]
    # Fetch index and check what it should be
    expected = httpx.get(INDEX_URL).json()["datasette"]["preview"]
    assert filename == expected + ".txt"
