#!/usr/bin/env python

def  chainCodeTransform(matrix, m, n):
    # This function returns the chain code
    # transform of the m*n matrix argument 
    transform = list()
    print 'Rows: {0}\n Columns: {1}'.format(range(0,n), range(0,m))
    for row in range(n):
        print '   Row:{0}'.format(row)
        currTarget = 0
        currCount = 0
        transformedRow = list()
        for col in range(m):
            print '      Before:Column:{0} Val:{2} Target:{1} Count:{3}'.format(col,currTarget,matrix[col][row], currCount)
            if matrix[col][row] == currTarget:
                currCount = currCount + 1
            else:
                transformedRow.append(currCount)
                currTarget = currTarget ^ 1
                currCount = 1
            print '      After:Column:{0} Val:{2} Target:{1} Count:{3}'.format(col,currTarget,matrix[col][row], currCount)
            if col == m-1:
                transformedRow.append(currCount)
            print '    Res:{0}'.format(transformedRow)
        transform.append(transformedRow)
    return transform

# def chainCodeSearch(toSearch, toMatch):
#     # This function takes the m*n matrix toMatch and exhaustively searches 
#     # the p*q matrix toSearch for a match. Matrices are column-major
#     m = len(toMatch)
#     n = len(toMatch[0])
#     p = len(toSearch)
#     q = len(toSearch[0])
#     matches = list()

#     # Only search the candidate matrix cells which can contain
#     # the matrix we're searching for
#     candidates = [(x,y) for x in range(0,p-m+1) for y in range(0,q-n+1)]
#     for (iCol, iRow) in candidates:
#         jCol = 0
#         jRow = 0 
#         while(toSearch[iCol + jCol][iRow + jRow] == toMatch[jCol][jRow]):
#             if (jCol == m-1) and (jRow == n-1):
#                 print '        Match = iCol:{0}|iRow:{1}'.format(iCol,iRow)
#                 matches.append((iCol,iRow))
#                 break
#             jCol = jCol + 1
#             if (jCol > m - 1):
#                 jCol = 0
#                 jRow = jRow + 1
#                 if (jRow > n - 1):
#                     print '        Break = iCol:{0}|iRow:{1}'.format(iCol,iRow)
#                     break ## End of search matrix, and no match found
#     return matches

# def chainCodeSearchSelfTest():
#     a = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
#     b = [[1, 0], [0, 0]]
#     c = [[0, 0], [0, 0]]
#     d = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
#     print 'Search for b in a'
#     r = bruteForceSearch(a, b)
#     print r

#     print 'Search for c in a'
#     r = bruteForceSearch(a, c)
#     print r
    
#     print 'Search for b in d'
#     r = bruteForceSearch(d, b)
#     print r

#     print 'Search for c in d'
#     r = bruteForceSearch(d, c)
#     print r

def chainCodeTransformSelfTest():
    a = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
    b = [[1, 0], [0, 0]]
    c = [[0, 0], [0, 0]]
    d = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]

    print 'Chain Code Transform of a'
    r = chainCodeTransform(a, 4, 4)
    print r

    print 'Chain Code Transform of b'
    r = chainCodeTransform(b, 2, 2)
    print r

    print 'Chain Code Transform of c'
    r = chainCodeTransform(c, 2, 2)
    print r

    print 'Chain Code Transform of d'
    r = chainCodeTransform(d, 3, 3)
    print r


if __name__ == '__main__':
    chainCodeTransformSelfTest()
