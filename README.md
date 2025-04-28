# mcgi_test_task

## Contents
  - Rules: Contains yara rules used for testing and scanning. Test rule is a dummy always-fire rule, chatgpt rules have been generated on the chatgpt website to gauge how good a state of the art model is (without any api complexity added), s_f and zero_l rule correspond to the rules created by the latest HF api call with the git diffs of the corresponding CVE-fixing commits (see commit URLs)
  - Tests: Contains various code testing files for the different functionalities: Git diff requests, HF inference calls, rule testing (this latest one contains yara rule tests on chatgpt-generated rules and the test rule)
  - HF_API_KEY: contains the api key for huggingface (obfuscated online)
  - Instructions.txt: Contains task instructions
  - Results.md: Overview of results
  - Rule_creation.py: First python script referenced in instructions, acquires git commit diffs, calls HF model at provider with selected prompt to create yara rules for the s-f and zero_l CVE commits, saves the rules in Rules folder.
  - Rule_matching.py: Tests generated yara rules against builds (binaries) and source code of vulnerable and patched commits
  - FFMP_sec_commits_urls.txt: The URLs of security commits of interest which fix a known CVE


  ## Contents not uploaded
  #### FFMP_commits: 
  A folder containing the zips, code extracts, and binary code builds of the following FFMpeg versions:
  - FFMP_latest (current)
  - s_f vuln (2012), vulnerable to support frame CVE 2012-2782
  - s_f fix (2012), commit that fixes CVE 2012-2782
  - 0-l vuln (2021), commit vulnerable to 0-lambda CVE 2020-20453
  - 0-l fix (2021) commit that fixes CVE 2020-20453
