import httpx
from importlib.metadata import version
import llm

URL = "https://raw.githubusercontent.com/simonw/docs-for-llms/refs/heads/main/{package}/{version}.txt"
INDEX_URL = (
    "https://raw.githubusercontent.com/simonw/docs-for-llms/refs/heads/main/index.json"
)


@llm.hookimpl
def register_fragment_loaders(register):
    register("docs", docs_loader)
    register("docs-preview", docs_loader_preview)


def docs_loader(package: str, preview: bool = False) -> llm.Fragment:
    """
    Fetch the latest documentation for the specified package from
    https://github.com/simonw/docs-for-llms

    Use '-f docs:' for the documentation of your current version of LLM.
    """
    # Without a specified template_path we default to the current version for LLM
    if not preview and (not package or package == "llm"):
        package = "llm"
        package_version = version("llm")
    else:
        # Use latest stable version of specified package
        index = httpx.get(INDEX_URL).json()
        if package not in index:
            raise ValueError(f"Package {package} not found in index")
        package_version = index[package]["preview" if preview else "stable"]
    docs_url = URL.format(package=package, version=package_version)
    response = httpx.get(docs_url)
    response.raise_for_status()
    return llm.Fragment(
        response.text,
        docs_url,
    )


def docs_loader_preview(package: str) -> llm.Fragment:
    """
    Similar to docs: but fetches the latest docs including alpha/beta releases.
    """
    return docs_loader(package, preview=True)
