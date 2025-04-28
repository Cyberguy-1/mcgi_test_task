## Results

### Prompt:
You are a cybersecurity expert. Your task is to generate a YARA rule. 
     You are provided with a github diff of a commit that fixes a vulnerability.
     The rule you generate should match if the vulnerability is present in a file.
     This means the rule should match on the code and/or binary before the commit of
     the provided diff, but not after. Rule title should be *Rule_name_inserted*.
Make sure not to prepend or append any  (style or other) characters to your output which will be processed as is. Here is the text of the git diff:

#### ChatGPT (no API, manual test)

Only tested for z_l CVE.
- Rule for compiled code always fires, on binary files and code files of the vulnerable and fixed builds. 
- Rule for source code never fires on binary and code files of the vulnerable and fixed builds.

#### LLAMA 3.3-70B-Instruct

No rule ever fires. 
This means, for both exploits (zero_lambda and s_f): 
- relevant rule applied to both binary and code versions of the vulnerable and fixed versions does not fire

### Prompt
Based on the following git diff, create a YARA rule that fires if the modifications have NOT been applied (before the diff) but does not match if they have (after the diff):

#### ChatGPT (no api)
Only tested for z_l CVE,
- Rule for compiled code always fires, on binary files and code files of the vulnerable and fixed builds. 
- Rule for source code never fires on binary and code files of the vulnerable and fixed builds.


### Prompt
"Create a YARA rule named *inserted* based on the following git diff. It should trigger (match) before the modifications have been applied but should not match after the commit Please return ONLY the yara rule with NO additional text. Thanks. Here is the diff:/n"

#### LLAMA 3.3-70B-Instruct
No rule fires, on binary or code for either vulnerable or fixed versions for both CVEs.




### Out of credits
I started looking for other models but ran out of credits on the HF inference API...
