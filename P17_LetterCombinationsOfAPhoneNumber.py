def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if digits == "":
        return []
    letters = {"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
    results = []
    totalPossible = 1
    for digit in digits:
        totalPossible *= len(letters[digit])
        
    for i in range(totalPossible):
        results.append("")
            
    for digit in digits:
        currentLetters = letters[digit]
        num = totalPossible / len(currentLetters)
        currentCharIndex = 0
        for i in range(len(results)):
            #add char at currentCharIndex for num items in results
            results[i] += currentLetters[currentCharIndex]
            num -= 1
            if num == 0:
                num = totalPossible / len(currentLetters)
                currentCharIndex += 1
                if currentCharIndex >= len(currentLetters):
                    currentCharIndex = 0
        totalPossible /= len(currentLetters)
        
    print(results)
    return results

letterCombinations("23")