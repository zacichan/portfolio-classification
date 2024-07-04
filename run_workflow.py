import sys
import os
import traceback
import torch
import warnings

# Import the functions from the scripts in the code/ directory
from code.create_embeddings import create_embeddings
from code.query_documents import query_model
from code.threshold_sample import (
    create_stratified_samples,
    calculate_threshold,
    refined_sampling,
)


def main():
    try:
        # Paths and parameters
        data_path = "data/synthetic_data.csv"
        analysis_column = "description"
        metadata_path = "metadata.json"
        embeddings_path = "embeddings.pt"
        device = "mps" if torch.backends.mps.is_available() else "cpu"
        query = "biology"  # Example query

        # Step 1: Generate Embeddings
        print("Step 1: Generating embeddings...")
        create_embeddings(
            data_path, analysis_column, metadata_path, embeddings_path, device
        )
        print("Embeddings generated successfully.")

        # Step 2: Query Documents
        print("Step 2: Querying documents...")
        df_results = query_model(query, metadata_path, embeddings_path, device)
        df_results.to_csv("ranked_results.csv", index=False)
        print("Document ranking completed. Results saved to 'ranked_results.csv'.")
        print("Document Ranking Results:")
        print(df_results.head())

        # Step 3: Create Stratified Samples
        print("Step 3: Creating stratified samples...")
        stratified_samples = create_stratified_samples(df_results)
        stratified_samples.to_csv("sample_output.csv", index=False)
        print("Stratified samples created. Samples saved to 'sample_output.csv'.")
        print("Stratified Samples for Manual Labeling:")
        print(stratified_samples.head())

        # Prompt user to label the samples manually in the output CSV (`sample_output.csv`)
        input(
            "Please label the samples in 'sample_output.csv' and save the file. Press Enter to continue..."
        )

        # Step 4: Calculate Threshold
        print("Step 4: Calculating threshold...")
        threshold = calculate_threshold("sample_output.csv")
        print(f"Calculated Threshold: {threshold}")

        # Step 5: Refine Sampling
        print("Step 5: Refining sampling...")
        refined_samples = refined_sampling(df_results, threshold)
        refined_samples.to_csv("refined_sample_output.csv", index=False)
        print(
            "Refined sampling completed. Refined samples saved to 'refined_sample_output.csv'."
        )
        print("Refined Samples:")
        print(refined_samples.head())

    except Exception as e:
        print("An error occurred during the workflow execution.")
        print(str(e))
        traceback.print_exc()


if __name__ == "__main__":
    main()
