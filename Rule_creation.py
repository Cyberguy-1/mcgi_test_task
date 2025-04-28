#Import huggingface inference client
from huggingface_hub import InferenceClient
#Import python requests
import requests

#Define Prompt to be used, values 0 or 1
PROMPT=0

#Define HF model and provider to query
MODEL = "Qwen/Qwen2.5-Coder-32B-Instruct"
PROVIDER = "fireworks-ai"

#FFMP zero-lambda CVE commit url
ZERO_L_DIFF_URL = "https://github.com/FFmpeg/FFmpeg/commit/a7a7f32c8ad0179a1a85d0a8cff35924e6d90be8.diff"

#FFMP support-frame CVE commit url
S_F_DIFF_URL = "https://github.com/FFmpeg/FFmpeg/commit/9e696d2e5ffaa763c564682ec18c3b51b3e5fccc.diff"

#Read HuggingFace API key
hf_key= ""
with open("HF_API_KEY") as f:
    hf_key = f.read()

#Test key loaded
if hf_key == "":
    print("No key loaded")
    quit()

#Get Diffs
zero_l_diff = requests.get(ZERO_L_DIFF_URL).text
s_f_diff = requests.get(S_F_DIFF_URL).text

#Define LLM prompt, V1
prompt1 = "You are a cybersecurity expert. Your task is to generate a YARA rule. \
     You are provided with a github diff of a commit that fixes a vulnerability.\
     The rule you generate should match if the vulnerability is present in a file.\
     This means the rule should match on the code and/or binary before the commit of\
     the provided diff, but not after. Rule title should be "

prompt2 = ". Make sure not to prepend or append any  (style or other) characters to your output which will be processed as is. Here is \
    the text of the git diff:/n"


#Define LLM prompt, V2
prompt3 = "Create a YARA rule named "

prompt4 = " based on the following git diff. It should trigger (match) \
    before the modifications have been applied but should not match after the commit.\
    Please return ONLY the yara rule with NO additional text. Thanks.\
    Here is the diff:/n"

#Choose prompt
p1 = prompt1 if PROMPT==0 else prompt3
p2 = prompt2 if PROMPT==0 else prompt4

#Define messages to be sent to the Inference API, add rule title, combine prompt parts.
zero_l_message = [
    {
        "role":"user",
        "content": p1 + "zero_l_rule" + p2 + zero_l_diff
    }
]
s_f_message = [
    {
        "role":"user",
        "content": prompt1 + "s_f_rule" + prompt2 + s_f_diff
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

def rule_gen(message:str):
    return client.chat_completion(
    messages = message,

    #Define model
    model = MODEL,

    #Define max tokens in response
    max_tokens = 500,

    #Define temperature, 0 = Deterministic
    temperature = 0

    #Define a stop sequence to ensure no appended characters (doesn't control prepended
    #characters though)
    #stop = []
    ).choices[0].message.content


#Get rules for CVE commits
zero_l_rule = rule_gen(zero_l_message).strip("`yara")
s_f_rule = rule_gen(s_f_message).strip("`yara")

#Print LLM response
print(zero_l_rule)
print(s_f_rule)

#Save the rules
with open("Rules/zero_l_rule.txt","w") as f:
    f.write(zero_l_rule)
with open("Rules/s_f_rule.txt","w") as f:
    f.write(s_f_rule)