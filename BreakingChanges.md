# Breaking Changes

> See the [Change Log](ChangeLog.md) for a summary of storage library changes.

## Version 0.37.1:

### All:
- The Tables SDK has been split from azure-storage namespace and moved to the azure-cosmosdb namespace
- It can be referenced as 'azure-cosmosdb-table'
- Namespace package azure-cosmosdb-nspkg added to the cosmosdb namespace
- The other former azure-storage SDK components (blob, queue and file) can be referenced as azure-storage-blob,
azure-storage-queue and azure-storage-file
- The files formerly found under azure.storage can now be found under azure.cosmosdb.common in the azure-cosmosdb-table package
