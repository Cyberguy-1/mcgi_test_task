#Import huggingface inference client
from huggingface_hub import InferenceClient

#Read HuggingFace API key
hf_key= "UNDEFINED"
with open("HF_API_KEY") as f:
    hf_key = f.read()

MODEL = "google/gemma-2-2b-it"
PROVIDER = "nebius"


#Define messages to be sent to the Inference API
messages_ = [
    {
        "role":"user",
        "content":"Can you generate yara rules?"
    }
]

#Initialize API client
#@params: 
#   provider: a valid huggingface model hosting service
#   api_key: a valid huggingface api key 
client = InferenceClient(
    provider = PROVIDER,
    api_key = hf_key
)

#Call the inference model with defined message
LLM_chat = client.chat_completion(
    messages = messages_,

    #Define model
    model = MODEL,

    #Define max tokens in response
    max_tokens = 500
    )

#Print LLM response
print(LLM_chat.choices[0].message)