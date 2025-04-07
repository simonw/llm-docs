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


def docs_loader(package: str) -> llm.Fragment:
    # Without a specified template_path we default to the current version for LLM
    if not package or package == "llm":
        package = "llm"
        package_version = version("llm")
    else:
        # Use latest stable version of specified package
        index = httpx.get(INDEX_URL).json()
        if package not in index:
            raise ValueError(f"Package {package} not found in index")
        package_version = index[package]["stable"]
    docs_url = URL.format(package=package, version=package_version)
    response = httpx.get(docs_url)
    response.raise_for_status()
    return llm.Fragment(
        response.text,
        docs_url,
    )
