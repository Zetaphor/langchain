"""All different types of document loaders."""

from langchain.document_loaders.directory import DirectoryLoader
from langchain.document_loaders.docx import UnstructuredDocxLoader
from langchain.document_loaders.email import UnstructuredEmailLoader
from langchain.document_loaders.gcs_directory import GCSDirectoryLoader
from langchain.document_loaders.gcs_file import GCSFileLoader
from langchain.document_loaders.googledrive import GoogleDriveLoader
from langchain.document_loaders.gutenberg import GutenbergLoader
from langchain.document_loaders.html import UnstructuredHTMLLoader
from langchain.document_loaders.notion import NotionDirectoryLoader
from langchain.document_loaders.obsidian import ObsidianLoader
from langchain.document_loaders.pdf import UnstructuredPDFLoader
from langchain.document_loaders.powerpoint import UnstructuredPowerPointLoader
from langchain.document_loaders.readthedocs import ReadTheDocsLoader
from langchain.document_loaders.roam import RoamLoader
from langchain.document_loaders.s3_directory import S3DirectoryLoader
from langchain.document_loaders.s3_file import S3FileLoader
from langchain.document_loaders.unstructured import UnstructuredFileLoader
from langchain.document_loaders.youtube import YoutubeLoader

__all__ = [
    "UnstructuredFileLoader",
    "DirectoryLoader",
    "NotionDirectoryLoader",
    "ReadTheDocsLoader",
    "GoogleDriveLoader",
    "UnstructuredHTMLLoader",
    "UnstructuredPowerPointLoader",
    "UnstructuredPDFLoader",
    "ObsidianLoader",
    "UnstructuredDocxLoader",
    "UnstructuredEmailLoader",
    "RoamLoader",
    "YoutubeLoader",
    "S3FileLoader",
    "S3DirectoryLoader",
    "GCSFileLoader",
    "GCSDirectoryLoader",
    "GutenbergLoader",
]