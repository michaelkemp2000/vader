True and True #True
False and True #False
1 == 1 and 2 == 1 #False
"test" == "test" #True
1 == 1 or 2 != 1 #True
'true' and 1 == 1 #True
False and 0 != 0 #False
True or 1 == 1 #True

#AND:  everything is false unless true
#OR: everything is true, unless false

"test" == "testing" #False
1 != 0 and 2 == 1 #False
"test" != "Testing" #False
"test" == 1 #False
not ('true' and 'false') #True
not (1 == 1 and 0 != 1) #False
not (10 == 1 or 1000 == 1000) #False
not (1 != 10 or 3 == 4) #False
not ("testing" == "testing" and "Zed" == "Cool Guy") #True
1 == 1 and not ("testing" == 1 or 1 == 0) #True
'chunky' == 'bacon' and not (3 == 4 or 3 == 3) #False
3 == 3 and not ("testing" == "testing" or "Python" == "Fun") #False