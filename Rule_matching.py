#Import Yara rules package
import yara
#Import os for directory walk
import os

#Compile rules in a text file, needed for processing
zero_l_rules = yara.compile('Rules/zero_l_rule.txt')
s_f_rules = yara.compile('Rules/zero_l_rule.txt')

#Define function to scan full build folder
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

    #Return result
    return output


#Match zero_l_rules against FFMP builds
zero_l_vuln_bin_match = scan_and_report("FFMP_commits/Builds/0-l-vuln_build",zero_l_rules)
zero_l_fix_bin_match = scan_and_report("FFMP_commits/Builds/0-l-fix_build",zero_l_rules)

#Match s_f_rules against FFMP builds
s_f_vuln_bin_match = scan_and_report("FFMP_commits/Builds/s-f-vuln_build",s_f_rules)
s_f_fix_bin_match = scan_and_report("FFMP_commits/Builds/s-f-fix_build",s_f_rules)


#Print arrays, empty if no match, otherwise shows which rule(s) are a hit
print("zero_l_vuln bin match:",zero_l_vuln_bin_match)
print("zero_l_fix bin match:",zero_l_fix_bin_match)
print("s_f_vuln bin match:",s_f_vuln_bin_match)
print("s_f_fix bin match:",s_f_fix_bin_match)

#Match zero_l_rules against FFMP source code
zero_l_vuln_code_match = scan_and_report("FFMP_commits/Extracts/0-l-vuln",zero_l_rules)
zero_l_fix_code_match = scan_and_report("FFMP_commits/Extracts/0-l-fix",zero_l_rules)

#Match s_f_rules against FFMP source code
s_f_vuln_code_match = scan_and_report("FFMP_commits/Extracts/s-f-vuln",s_f_rules)
s_f_fix_code_match = scan_and_report("FFMP_commits/Extracts/s-f-fix",s_f_rules)

#Print arrays, empty if no match, otherwise shows which rule(s) are a hit
print("zero_l_vuln code match:",zero_l_vuln_code_match)
print("zero_l_fix code match:",zero_l_fix_code_match)
print("s_f_vuln code match:",s_f_vuln_code_match)
print("s_f_fix code match:",s_f_fix_code_match)
