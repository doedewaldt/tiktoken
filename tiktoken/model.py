from __future__ import annotations

from .core import Encoding
from .registry import get_encoding

mymodels ={
    "ada": 2048,
    "ada-code-search-code": 1024,
    "ada-code-search-text": 512,
    "ada-search-document": 4096,
    "ada-search-query": 256,
    "ada-similarity": 2048,
    "ada:2020-05-03": 2048,
    "babbage": 2048,
    "babbage-code-search-code": 2048,
    "babbage-code-search-text": 512,
    "babbage-search-document": 2048,
    "babbage-search-query": 2048,
    "babbage-similarity": 2048,
    "babbage:2020-05-03": 2048,
    "code-davinci-edit-001": 2048,
    "code-search-ada-code-001": 1024,
    "code-search-ada-text-001": 512,
    "code-search-babbage-code-001": 1024,
    "code-search-babbage-text-001": 2048,
    "curie": 2048,
    "curie-instruct-beta": 2048,
    "curie-search-document": 2048,
    "curie-search-query": 2048,
    "curie-similarity": 2048,
    "curie:2020-05-03": 2048,
    "cushman:2020-05-03": 2048,
    "davinci": 2048,
    "davinci-if:3.0.0": 2048,
    "davinci-instruct-beta": 2048,
    "davinci-instruct-beta:2.0.0": 2048,
    "davinci-search-document": 2048,
    "davinci-search-query": 2048,
    "davinci-similarity": 2048,
    "davinci:2020-05-03": 2048,
    "gpt-3.5-turbo": 2048,
    "gpt-3.5-turbo-0301": 2048,
    "if-curie-v2": 2048,
    "if-davinci-v2": 2048,
    "if-davinci:3.0.0": 2048,
    "text-ada-001": 2048,
    "text-ada:001": 4096,
    "text-babbage-001": 2048,
    "text-babbage:001": 2048,
    "text-curie-001": 2048,
    "text-curie:001": 2048,
    "text-davinci-001": 2048,
    "text-davinci-002": 2048,
    "text-davinci-003": 2048,
    "text-davinci-edit-001": 2048,
    "text-davinci:001": 2048,
    "text-embedding-ada-002": 512,
    "text-search-ada-doc-001": 2048,
    "text-search-ada-query-001": 2048,
    "text-search-babbage-doc-001": 2048,
    "text-search-babbage-query-001": 2048,
    "text-search-curie-doc-001": 2048,
    "text-search-curie-query-001": 1024,
    "text-search-davinci-doc-001": 2048,
    "text-search-davinci-query-001": 2048,
    "text-similarity-ada-001": 512,
    "text-similarity-babbage-001": 2048,
    "text-similarity-curie-001": 2048,
    "text-similarity-davinci-001": 2048,
    "whisper-1": 2048
}

# TODO: these will likely be replaced by an API endpoint
MODEL_PREFIX_TO_ENCODING: dict[str, str] = {
    # chat
    "ada": "r50k_base",  # e.g., ada-code-search-code, ada-search-document, ada:2020-05-03 etc.
    "babbage": "r50k_base",  # e.g., babbage-code-search-code, babbage-search-document, babbage:2020-05-03 etc.
    "code-davinci-": "p50k_base", # e.g., code-davinci-edit-001
    "code-search-": "r50k_base",  # e.g., code-search-ada-code-001, code-search-ada-text-001, code-search-babbage-code-001, code-search-babbage-text-001
    "curie": "r50k_base",  # e.g., curie-instruct-beta, curie-search-document, curie:2020-05-03 etc.
    "davinci": "r50k_base",  # e.g., davinci-code-search-code, davinci-search-document, davinci:2020-05-03 etc.
    "gpt-": "cl100k_base",  # e.g., gpt-4-0314, etc., plus gpt-3.5-turbo-0301, -0401, etc.
    "if": "r50k_base",  # e.g., if-curie-v2, if-davinci-v2, if-davinci:3.0.0
    "text-ada-": "r50k_base",  # e.g., text-ada-001, text-ada:001
    "text-babbage-": "r50k_base",  # e.g., text-babbage-001, text-babbage:001
    "text-curie-": "r50k_base",  # e.g., text-curie-001, text-curie:001
    "text-davinci-": "p50k_base",  # e.g., text-davinci-001, text-davinci-002, text-davinci-003, text-davinci-edit-001, text-davinci:001
    "text-embedding-": "r50k_base",  # e.g., text-embedding-ada-002
    "text-search-": "r50k_base",  # e.g., text-search-ada-doc-001, text-search-ada-query-001, text-search-babbage-doc-001, text-search-babbage-query-001, text-search-curie-doc-001, text-search-curie-query-001, text-search-davinci-doc-001, text-search-davinci-query-001
    "text-similarity-": "r50k_base",  # e.g., text-similarity-ada-001, text-similarity-babbage-001, text-similarity-curie-001, text-similarity-davinci-001
    "whisper": "r50k_base",  # e.g., whisper-1
}

MODEL_TO_ENCODING: dict[str, str] = {
    # chat
    "gpt-4": "cl100k_base",
    "gpt-3.5-turbo": "cl100k_base",
    # text
    "text-davinci-003": "p50k_base",
    "text-davinci-002": "p50k_base",
    "text-davinci-001": "r50k_base",
    "text-curie-001": "r50k_base",
    "text-babbage-001": "r50k_base",
    "text-ada-001": "r50k_base",
    "davinci": "r50k_base",
    "curie": "r50k_base",
    "babbage": "r50k_base",
    "ada": "r50k_base",
    # code
    "code-davinci-002": "p50k_base",
    "code-davinci-001": "p50k_base",
    "code-cushman-002": "p50k_base",
    "code-cushman-001": "p50k_base",
    "davinci-codex": "p50k_base",
    "cushman-codex": "p50k_base",
    # edit
    "text-davinci-edit-001": "p50k_edit",
    "code-davinci-edit-001": "p50k_edit",
    # embeddings
    "text-embedding-ada-002": "cl100k_base",
    # old embeddings
    "text-similarity-davinci-001": "r50k_base",
    "text-similarity-curie-001": "r50k_base",
    "text-similarity-babbage-001": "r50k_base",
    "text-similarity-ada-001": "r50k_base",
    "text-search-davinci-doc-001": "r50k_base",
    "text-search-curie-doc-001": "r50k_base",
    "text-search-babbage-doc-001": "r50k_base",
    "text-search-ada-doc-001": "r50k_base",
    "code-search-babbage-code-001": "r50k_base",
    "code-search-ada-code-001": "r50k_base",
    # open source
    "gpt2": "gpt2",
}


def encoding_for_model(model_name: str) -> Encoding:
    """Returns the encoding used by a model."""
    encoding_name = None
    if model_name in MODEL_TO_ENCODING:
        encoding_name = MODEL_TO_ENCODING[model_name]
    else:
        # Check if the model matches a known prefix
        # Prefix matching avoids needing library updates for every model version release
        # Note that this can match on non-existent models (e.g., gpt-3.5-turbo-FAKE)
        for model_prefix, model_encoding_name in MODEL_PREFIX_TO_ENCODING.items():
            if model_name.startswith(model_prefix):
                return get_encoding(model_encoding_name)

    if encoding_name is None:
        raise KeyError(
            f"Could not automatically map {model_name} to a tokeniser. "
            "Please use `tiktoken.get_encoding` to explicitly get the tokeniser you expect."
        ) from None

    return get_encoding(encoding_name)
