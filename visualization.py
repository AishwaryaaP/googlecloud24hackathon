from google.cloud import aiplatform
from google.auth import default

# Initialize Vertex AI
def initialize_vertex_ai():
    # Authenticate using the default service account or a specific key file
    credentials, _ = default()
    aiplatform.init(credentials=credentials)

# Function to call the Gemini model
def call_gemini_model(prompt: str):
    # Define the model name or ID for the Gemini model
    model_id = 'your-gemini-model-id'  # Replace with your Gemini model ID
    project_id = 'your-project-id'     # Replace with your Google Cloud project ID
    region = 'your-region'             # Replace with your Google Cloud region (e.g., 'us-central1')

    # Create a Vertex AI client
    client = aiplatform.gapic.PredictionServiceClient()

    # Define the endpoint
    endpoint = f"projects/{project_id}/locations/{region}/endpoints/{model_id}"

    # Create the prediction request
    instance = {"content": prompt}
    instances = [instance]
    parameters = {}

    try:
        # Call the model
        response = client.predict(
            endpoint=endpoint,
            instances=instances,
            parameters=parameters
        )

        # Extract and print the result
        predictions = response.predictions
        print("Predictions:", predictions)
    except Exception as e:
        print("Error during prediction:", e)

if __name__ == "__main__":
    # Initialize Vertex AI
    initialize_vertex_ai()
    
    # Define a user prompt
    user_prompt = "What is the capital of France?"
    
    # Call the Gemini model with the user prompt
    call_gemini_model(user_prompt)
