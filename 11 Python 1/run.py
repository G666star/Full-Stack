# 3 METHODS OF IMPORT ARE USED
#	1> FROM X IMPORT FUNC(), THEN CALL FUNC()
#	2> IMPORT X, THEN CALL X.FUNC()
#	3> IMPORT X AS Y, THEN CALL Y.FUNC()



from Part9_Functions_soln_by_me import count_evens

f = count_evens([1, 2, 3, 4])
print(f)

from Part9_Functions_soln_by_me import no_teen_sum
e = no_teen_sum(1,14,15)
print(e)

from Part9_Functions_soln_by_me import doubleChar
d = doubleChar('Hi-There')
print(d)

from Part9_Functions_soln_by_me import end_other
c = end_other('abc', 'abXabc')
print(c)

import Part9_Functions_soln_by_me
b = Part9_Functions_soln_by_me.stringBits('Heeololeo')
print(b)

import Part9_Functions_soln_by_me as p9f
a = p9f.arrayCheck([1,1,2,1,2,3])
print(a)