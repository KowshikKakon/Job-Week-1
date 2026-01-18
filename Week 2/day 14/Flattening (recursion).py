
def flattenList(nestedList):

    if not(bool(nestedList)):
        return nestedList

     
    if isinstance(nestedList[0], list):

        
        return flattenList(*nestedList[:1]) + flattenList(nestedList[1:])

    
    return nestedList[:1] + flattenList(nestedList[1:])


# Driver Code
nestedList = [[8, 9], [10, 11, 'kowshik'], [13]]
print('Nested List:\n', nestedList)

print("Flattened List:\n", flattenList(nestedList))