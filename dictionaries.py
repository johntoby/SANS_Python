#dictioary uses {} to list its items
#dictionary uses key-value pairs .. e.g {"total": 21, "new": 9, "old": 88}

case_stats = {"total": 30, "new": 11, "old": 19}
print("Total cases " + str(case_stats["total"]) ) 
print("Total new cases for this year is : " + str(case_stats["new"])) 

#list inside dictionaries 

case_files = {"total": 55, "new": 20, "old": 20, "solved": 51, "month": "April", "percentage_solved": 35.876, "types": ["forensics", 'cyber', 'web app', 'cloud', 'egg shell'] } 
print("Month: " + str(case_files["month"]))  
print ("Total cases for this year is: " + str(case_files ["total"])) 
print ("Total new cases for this quarter is: " + str(case_files["new"])) 
print("The percentage of solved cases is: " + str(case_files["percentage_solved"] ) + " %")  

print( "The major Type of case encountered is: " + str(case_files["types"][2]))

print( "Types of cases encountered are: ")
print("\t" + str(case_files["types"][0]))
print('\t' + str(case_files["types"][1]))
print('\t' + str(case_files["types"][2]))

#lets build our dictionary to resemble a real code joor 
#we will combine dictionary inside dictionary plus list

case_figures = {
    'month': "June",
    'name of officer': "Timmy",
    "stats": {
        'total cases': 21,
        'solved': 15,
        'unsolved': 6,
        'percentage_solved': 57.14,
    }, 
'types': ['forensics', 'crypto', 'web app', 'mobile', 'gaming']
}

print('The first case was solved in the month of: ' + case_figures["month"])


#dictionaries inside lists 



case_stats = [
             {'employee': 'Bill', 'solved': 12, 'unsolved': 8},
             {'employee': 'Susan', 'solved': 15, 'unsolved': 5},
             {'employee': 'James', 'solved': 8, 'unsolved': 3}
]

print('employee:')
print('\t Solved cases:' + str(case_stats[0]['solved']))
print('\t Unsolved cases:' + str(case_stats[0]['unsolved']))

print('Susan:')
print('\t Solved cases:' + str(case_stats[1]['solved']))
print('\t Unsolved cases:' + str(case_stats[1]['unsolved']))

print('James:')
print('\t Solved cases:' + str(case_stats[2]['solved']))
print('\t Unsolved cases:' + str(case_stats[2]['unsolved']))



case_stats = {'month': 'June', 'total': 21, 'solved': 12, 'unsolved': 8}

print('Stats for ' + case_stats['month'] + ':')
print('\tTotal cases: ' + str(case_stats['total']))
print('\tSolved cases: ' + str(case_stats['solved']))
print('\tUnsolved cases: ' + str(case_stats['unsolved']))

case_stats['month'] = 'July'
case_stats['total'] = 22
case_stats['solved'] = 13

print('Stats for ' + case_stats['month'] + ':')
print('\tTotal cases: ' + str(case_stats['total']))
print('\tSolved cases: ' + str(case_stats['solved']))
print('\tUnsolved cases: ' + str(case_stats['unsolved']))



case_stats = {'month': 'June', 'total': 21, 'solved': 12, 'unsolved': 8}

print('Stats for ' + case_stats['month'] + ':')
print('\tTotal cases: ' + str(case_stats['total']))
print('\tSolved cases: ' + str(case_stats['solved']))
print('\tUnsolved cases: ' + str(case_stats['unsolved']))

case_stats['month'] = 'July'
case_stats['total'] = case_stats['total'] + 1
case_stats['solved'] = case_stats['solved'] + 1

print('Stats for ' + case_stats['month'] + ':')
print('\tTotal cases: ' + str(case_stats['total']))
print('\tSolved cases: ' + str(case_stats['solved']))
print('\tUnsolved cases: ' + str(case_stats['unsolved'])) 


case_stats = {}

case_stats['month'] = 'April'
print(case_stats)

case_stats['total'] = 21
print(case_stats)

case_stats['solved'] = 55
print(case_stats)

case_stats['gbese'] = 33
print(case_stats)

case_stats['total'] = 876
print(case_stats)


# to delete things from a dictionary, use del: 

case_stats = {'month': 'June', 'total': 21, 'solved': 12, 'unsolved': 8}
print(case_stats)

del case_stats['unsolved']

print(case_stats)



