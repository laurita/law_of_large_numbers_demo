import law_of_large_numbers_demo as loln

def run():        
    numRolls = 2000
    lolnDemo = loln.LawOfLargeNumbersDemo(numRolls)
    
    lolnDemo.run_demo()