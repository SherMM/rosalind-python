def isTransition(nbase1, nbase2):
    tr_dict = {'A':'G', 'G':'A', 'C':'T', 'T':'C'}
    if nbase1 in tr_dict:
        return tr_dict[nbase1] == nbase2
    return False


def isTransversion(nbase1, nbase2):
    tv_dict = {'A':['T', 'C'], 'C':['A', 'G'],
               'G':['T', 'C'], 'T':['A', 'G']}
    if nbase1 in tv_dict:
        return nbase2 in tv_dict[nbase1]
    return False


def getTransTravRatio(string1, string2):
    tr_count = 0
    tv_count = 0
    for i in range(len(string1)):
        if isTransition(string1[i], string2[i]):
            tr_count += 1
        else:
            if isTransversion(string1[i], string2[i]):
                tv_count += 1
    return tr_count/float(tv_count)





