# -------------------------------------------------------------------------
# Copyright (c) Microsoft.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# --------------------------------------------------------------------------
import unittest

from azure.cosmosdb.common import CloudStorageAccount
from samples.advanced import (
    AuthenticationSamples,
    ClientSamples,
)
from samples.table import (
    TableSasSamples,
    TableEncryptionSamples,
    TableSamples,
)


@unittest.skip('Skip sample tests.')
class SampleTest(unittest.TestCase):
    def setUp(self):
        super(SampleTest, self).setUp()
        try:
            from samples.config import config
        except:
            raise ValueError('Please specify configuration settings in config.py.')

        if config.IS_EMULATED:
            self.account = CloudStorageAccount(is_emulated=True)
        else:
            # Note that account key and sas should not both be included
            account_name = config.STORAGE_ACCOUNT_NAME
            account_key = config.STORAGE_ACCOUNT_KEY
            sas = config.SAS
            self.account = CloudStorageAccount(account_name=account_name,
                                               account_key=account_key,
                                               sas_token=sas)

    def test_table_samples(self):
        table = TableSamples(self.account)
        table.run_all_samples()

    def test_table_sas_samples(self):
        sas = TableSasSamples(self.account)
        sas.run_all_samples()

    def test_authentication_samples(self):
        auth = AuthenticationSamples()
        auth.run_all_samples()

    def test_client_samples(self):
        client = ClientSamples()
        client.run_all_samples()

    def test_table_encryption_samples(self):
        encryption = TableEncryptionSamples(self.account)
        encryption.run_all_samples()


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
