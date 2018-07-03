# Change Log

> See [BreakingChanges](BreakingChanges.md) for a detailed list of API breaks.

## Version 1.0.4
- Updated azure-storage-common dependency to >= 1.1.0, < 2.0.0

## Version 1.0.3
- Require futures package only for python versions <= 2.7

## Version 1.0.2
- Updated azure-storage-common to 1.1.0

## Version 1.0.1
- Patched the SDK to connect to the CosmosDB Table API using connection string 

## Version 1.0.0:
- GA Release

### All:
- General availability release

## Version 0.37.2:

### All:
- The CosmosDB Tables SDK takes a dependency from 'azure-storage-common' package

## Version 0.37.1:
    
### All:
- The Tables SDK has been split from azure-storage namespace and moved to the azure-cosmosdb namespace
- It can be referenced as 'azure-cosmosdb-table'
- Namespace package azure-cosmosdb-nspkg added to the cosmosdb namespace
- The other former azure-storage SDK components (blob, queue and file) can be referenced as azure-storage-blob,
azure-storage-queue and azure-storage-file
- The files formerly found under azure.storage can now be found under azure.cosmosdb.common in the azure-cosmosdb-table package

