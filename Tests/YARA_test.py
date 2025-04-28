#Import Yara rules package
import yara

#Compile rules in a text file, needed for processing
rules = yara.compile('Tests/test_rule.txt')

#Test compiled rule against dummy txt files
matches_1 = rules.match("Tests/YARA_Test_1.txt")
matches_2 = rules.match("Tests/YARA_Test_2.txt")

#Print arrays, empty if no match, otherwise shows which rule(s) are a hit
print("Match 1:",matches_1)
print("Match 2:",matches_2)