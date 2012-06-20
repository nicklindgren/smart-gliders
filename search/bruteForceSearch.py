#!/usr/bin/env python

def bruteForceSearch(toSearch, toMatch):
    # This function takes the m*n matrix toMatch and exhaustively searches 
    # the p*q matrix toSearch for a match. Matrices are column-major
    m = len(toMatch)
    n = len(toMatch[0])
    p = len(toSearch)
    q = len(toSearch[0])
    matches = list()

    # Only search the candidate matrix cells which can contain
    # the matrix we're searching for
    candidates = [(x,y) for x in range(0,p-m+1) for y in range(0,q-n+1)]
    for (iCol, iRow) in candidates:
        jCol = 0
        jRow = 0 
        while(toSearch[iCol + jCol][iRow + jRow] == toMatch[jCol][jRow]):
            if (jCol == m-1) and (jRow == n-1):
                print '        Match = iCol:{0}|iRow:{1}'.format(iCol,iRow)
                matches.append((iCol,iRow))
                break
            jCol = jCol + 1
            if (jCol > m - 1):
                jCol = 0
                jRow = jRow + 1
                if (jRow > n - 1):
                    print '        Break = iCol:{0}|iRow:{1}'.format(iCol,iRow)
                    break ## End of search matrix, and no match found
    return matches

def selfTest():
    a = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
    b = [[1, 0], [0, 0]]
    c = [[0, 0], [0, 0]]
    d = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
    print 'Search for b in a'
    r = bruteForceSearch(a, b)
    print r

    print 'Search for c in a'
    r = bruteForceSearch(a, c)
    print r
    
    print 'Search for b in d'
    r = bruteForceSearch(d, b)
    print r

    print 'Search for c in d'
    r = bruteForceSearch(d, c)
    print r


if __name__ == '__main__':
    selfTest()
