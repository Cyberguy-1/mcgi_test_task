# mcgi_test_task

## Contents
  - Rules: Contains yara rules used for testing and scanning. Test rule is a dummy always-fire rule, chatgpt rules have been generated on the chatgpt website to gauge how good a state of the art model is (without any api complexity added), s_f and zero_l rule correspond to the rules created by the latest HF api call with the git diffs of the corresponding CVE-fixing commits (see commit URLs)
  - Tests: Contains various code testing files for the different functionalities: Git diff requests, HF inference calls, rule testing (this latest one contains yara rule tests on chatgpt-generated rules and the test rule)
  - HF_API_KEY: contains the api key for huggingface (obfuscated online)
  - Instructions.txt: Contains task instructions
  - Results.md: Overview of results
  - Rule_creation.py: First python script referenced in instructions, acquires git commit diffs, calls HF model at provider with selected prompt to create yara rules for the s-f and zero_l CVE commits, saves the rules in Rules folder.
  - Rule_matching.py: Tests generated yara rules against builds (binaries) and source code of vulnerable and patched commits
  
