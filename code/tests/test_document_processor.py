import pytest
from backend.batch.utilities.helpers.embedders.push_embedder import (
    PushEmbedder,
)
from backend.batch.utilities.helpers.config.config_helper import ConfigHelper
from backend.batch.utilities.helpers.azure_blob_storage_client import (
    AzureBlobStorageClient,
)

document_url = "https://dagrs.berkeley.edu/sites/default/files/2020-01/sample.pdf"
url = "https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search"
docx_url = "https://csciblob.blob.core.windows.net/rag-sol-acc/What is Azure OpenAI Service.docx"


@pytest.mark.azure("This test requires Azure")
def test_push_embedder_layout():
    push_embedder = PushEmbedder(AzureBlobStorageClient())
    processors = list(
        filter(
            lambda x: x.document_type == "pdf",
            ConfigHelper.get_active_config_or_default().document_processors,
        )
    )
    keys = push_embedder.embed_file(source_url=document_url, processor=processors)
    assert isinstance(keys, list)
    assert len(keys) > 0
    assert all(isinstance(key, str) and key for key in keys)


@pytest.mark.azure("This test requires Azure")
def test_push_embedder_read():
    push_embedder = PushEmbedder(AzureBlobStorageClient())
    processors = list(
        filter(
            lambda x: x.document_type == "pdf",
            ConfigHelper.get_active_config_or_default().document_processors,
        )
    )
    keys = push_embedder.embed_file(source_url=document_url, processors=processors)
    assert isinstance(keys, list)
    assert len(keys) > 0
    assert all(isinstance(key, str) and key for key in keys)


@pytest.mark.azure("This test requires Azure")
def test_push_embedder_web():
    push_embedder = PushEmbedder(AzureBlobStorageClient())
    processors = list(
        filter(
            lambda x: x.document_type == "url",
            ConfigHelper.get_active_config_or_default().document_processors,
        )
    )
    keys = push_embedder.embed_file(source_url=url, processors=processors)
    assert isinstance(keys, list)
    assert len(keys) > 0
    assert all(isinstance(key, str) and key for key in keys)


@pytest.mark.azure("This test requires Azure")
def test_push_embedder_docx():
    push_embedder = PushEmbedder(AzureBlobStorageClient())
    processors = list(
        filter(
            lambda x: x.document_type == "docx",
            ConfigHelper.get_active_config_or_default().document_processors,
        )
    )
    keys = push_embedder.embed_file(source_url=docx_url, processors=processors)
    assert isinstance(keys, list)
    assert len(keys) > 0
    assert all(isinstance(key, str) and key for key in keys)
