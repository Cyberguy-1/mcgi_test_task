#Import Yara rules package
import yara
#Import os for directory walk
import os

#define test rules
test_rules = yara.compile("Rules/test_rule.txt")
cgpt_z_l_code_rule = yara.compile("Rules/chatgpt_z_l_code_rule.txt")
cgpt_z_l_bin_rule = yara.compile("Rules/chatgpt_z_l_bin_rule.txt")

#Define function to scan full folder and check for rule match on all files
def scan_and_report(directory:str, rule:yara.Rules):
    output = set()

    #Iterate through directory
    for root,dir,files in os.walk(directory):
            
            #For all files
            for f in files:

                #Compute rule match on file
                match = rule.match(os.path.join(root,f))

                #Add match result to total output
                for m in match:
                     output.add(m)

    #Return True if match, else False
    return not len(output) ==0

#Match dummy test rule against all bins
zero_l_vuln_match_test = scan_and_report("FFMP_commits/Builds/0-l-vuln_build",test_rules)
zero_l_fix_match_test = scan_and_report("FFMP_commits/Builds/0-l-fix_build",test_rules)
s_f_vuln_match_test = scan_and_report("FFMP_commits/Builds/s-f-vuln_build",test_rules)
s_f_fix_match_test = scan_and_report("FFMP_commits/Builds/s-f-fix_build",test_rules)

#Print results
print("zero_l_vuln bin match test rule:",zero_l_vuln_match_test)
print("zero_l_fix bin match test rule:",zero_l_fix_match_test)
print("s_f_vuln bin match test rule:",s_f_vuln_match_test)
print("s_f_fix bin match test rule:",s_f_fix_match_test)

#Match bin and code cgpt rules against z_l bins
zero_l_vuln_bin_match_cgpt_bin = scan_and_report("FFMP_commits/Builds/0-l-vuln_build",cgpt_z_l_bin_rule)
zero_l_fix_bin_match_cgpt_bin = scan_and_report("FFMP_commits/Builds/0-l-fix_build",cgpt_z_l_bin_rule)
zero_l_vuln_bin_match_cgpt_code = scan_and_report("FFMP_commits/Builds/0-l-vuln_build",cgpt_z_l_code_rule)
zero_l_fix_bin_match_cgpt_code = scan_and_report("FFMP_commits/Builds/0-l-fix_build",cgpt_z_l_code_rule)

#Print results
print("zero_l_vuln bin match cgpt z_l bin rule:",zero_l_vuln_bin_match_cgpt_bin)
print("zero_l_fix bin match cgpt z_l bin rule:",zero_l_fix_bin_match_cgpt_bin)
print("zero_l_vuln bin match cgpt z_l code rule:",zero_l_vuln_bin_match_cgpt_code)
print("zero_l_fix bin cgpt z_l code rule:",zero_l_fix_bin_match_cgpt_code)

#Match bin and code cgpt rules against code
zero_l_vuln_code_match_cgpt_bin = scan_and_report("FFMP_commits/Extracts/0-l-vuln",cgpt_z_l_bin_rule)
zero_l_fix__code_match_cgpt_bin = scan_and_report("FFMP_commits/Extracts/0-l-fix",cgpt_z_l_bin_rule)
zero_l_vuln_code_match_cgpt_code = scan_and_report("FFMP_commits/Extracts/0-l-vuln",cgpt_z_l_code_rule)
zero_l_fix_code_match_cgpt_code = scan_and_report("FFMP_commits/Extracts/0-l-fix",cgpt_z_l_code_rule)

#Print results
print("zero_l_vuln code match cgpt z_l bin rule:",zero_l_vuln_code_match_cgpt_bin)
print("zero_l_fix code match cgpt z_l bin rule:",zero_l_fix__code_match_cgpt_bin)
print("zero_l_vuln code match cgpt z_l code rule:",zero_l_vuln_code_match_cgpt_code)
print("zero_l_fix code cgpt z_l code rule:",zero_l_fix_code_match_cgpt_code)
