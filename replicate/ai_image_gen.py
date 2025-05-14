import replicate
import os
from dotenv import load_dotenv
load_dotenv()

api_token = os.getenv("REPLICATE_API_TOKEN")
if not api_token:
    raise EnvironmentError("REPLICATE_API_TOKEN is not set!")

replicate.Client(api_token=api_token)

output = replicate.run(
  "black-forest-labs/flux-schnell",
  input={"prompt": "astronaut fighting a bear"}
)

# Save the generated image
with open('output.png', 'wb') as f:
    f.write(output[0].read())

print(f"Image saved as output.png")