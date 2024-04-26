"""Extract BQ dataset function."""

# TODO 3: Import necessary modules
from kfp.dsl import Artifact, ClassificationMetrics, Input, Output, component

# My working
# Use "gcr.io/ml-pipeline/google-cloud-pipeline-components:2.8.0" for base image
# @component(
#     base_image="us-docker.pkg.dev/vertex-ai/training/sklearn-cpu.1-0:latest"
# )
# def calculate_confusion_matrix(
#     predictions_bq_path: str,
#     labels_csv_path: str,
#     output_metrics: Output[Classification_Metrics]
# )
#     from sklearn.metrics import confusion_matrix as generate_confusion_matrix

#     # 1. Get validation label data from .csv using pandas
#     # 2. Get prediction data from batch job bq table using pandas
#     # Use confusion_matrix = generate_confusion_matrix(y_true, y_pred)
#     n_classes = len(confusion_matrix)
#     labels = [str(ii) for ii in range(n_classes)]
#     output_metrics.log_confusion_matrix(labels, confusion_matrix)
