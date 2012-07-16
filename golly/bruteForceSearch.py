import golly

def getIndices(x):
    start = -(x / 2)
    end = (x / 2)
    if not (x % 2): #if odd
        end = end - 1
    return [start,end]

def bruteForceSearch(searchPatt):
    cols = len(searchPatt[0])
    rows = len(searchPatt)
    matches = list()

    wd = golly.getwidth()
    ht = golly.getheight()

    [startWd, endWd] = getIndices(wd)
    [startHt, endHt] = getIndices(ht)
    #formatStr = 'Width: {0}   Height: {1}\nStart Pos: ({2},{3})\nEnd Pos:{4},{5}\np,q = {6} {7} ' 
    #golly.note(formatStr.format(wd,ht,startWd,startHt,endWd,endHt,p,q))

    # Only search the candidate matrix cells which can contain
    # the matrix we're searching for
    candidates = [(x,y) for x in range(startWd,endWd-cols+2) for y in range(startHt,endHt-rows+2)]
    for (iCol, iRow) in candidates:
        jCol = 0
        jRow = 0 
        while(golly.getcell(iCol + jCol,iRow + jRow) == searchPatt[jRow][jCol]):
            if (jCol == cols-1) and (jRow == rows-1):
                print '        Match = ({0},{1})'.format(iCol,iRow)
                matches.append((iCol,iRow))
                break
            jCol = jCol + 1
            if (jCol > cols - 1):
                jCol = 0
                jRow = jRow + 1
                if (jRow > rows - 1):
                    print '        Break = ({0},{1})'.format(iCol,iRow)
                    break ## End of search space, and no match found
    return [matches, candidates]

#golly.note('Vals = {0}  {1}'.format(golly.getcell(0,0),golly.getcell(-2,0)))
searchPattern = golly.getstring("Define a pattern to search for (enter as a Python list)", "[[1,0],[1,1],[0,0]]", "Enter A Pattern")
[results, candidates] = bruteForceSearch(eval(searchPattern))
golly.note('Total Matches: {0}\nTotal Candidate Cells:{1}\n{2}'.format(
        len(results), len(candidates), results))
