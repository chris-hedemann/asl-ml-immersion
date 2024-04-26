# Copyright 2021 Google LLC

# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at

# https://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS"
# BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.
"""Extract BQ dataset function."""

# TODO 3: Import necessary modules
from kfp.dsl import Artifact, Input, component

# from google_cloud_pipeline_components.types.artifact_types import BQTable


# TODO 3: add component decorator.
# Use "gcr.io/ml-pipeline/google-cloud-pipeline-components:2.8.0" for base image
@component(
    base_image="gcr.io/ml-pipeline/google-cloud-pipeline-components:2.8.0"
)
def extract_bq_op(
    bq_table: Input[Artifact],
    data_location: str,
    destination_uri: str,
    # TODO 3: Add inputs
):
    # pylint: disable=import-outside-toplevel
    from google.cloud import bigquery

    client = bigquery.Client(bq_table.metadata["projectId"])

    dataset_ref = bigquery.DatasetReference(
        bq_table.metadata["projectId"], bq_table.metadata["datasetId"]
    )
    table_ref = dataset_ref.table(bq_table.metadata["tableId"])

    extract_job = client.extract_table(
        table_ref,
        location=data_location,
        destination_uris=[destination_uri],
    )  # API request
    extract_job.result()  # Waits for job to complete.

    # print(
    #     "Exported {}:{}.{} to {}".format(project_id, dataset_id, table_id, destination_uri)
    # )
    # TODO 3: Define function
