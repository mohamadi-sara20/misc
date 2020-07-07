def find_max_in_col(ar):
    max_col = []
    for i in range(len(ar)):
        max_c = ar[0][i]
        max_ind = i
        for j in range(len(ar[i])):
            if(max_c < ar[j][i]):
                max_c = ar[j][i]
                max_ind = j
        max_col.append((max_ind, i))
    return max_col






def find_saddle_point(ar):
    max_col_inds = find_max_in_col(ar)

    mind_col = []

    for i in range(len(ar)):
        min_row_item = ar[i][0]
        min_ind = 0
        for j in range(len(ar[i])):
            if(min_row_item > ar[i][j]):
                min_ind = j
                min_row_item = ar[i][j]
        mind_col.append((i, min_ind))

    inds = list(set(max_col_inds).intersection(mind_col))
    if(not inds):
        return None
    inds = inds[0]
    return ar[inds[0]][inds[1]]



print(find_saddle_point([[9,1,2], [8,5,7], [3,4,6]]))
print(find_saddle_point([[1,2,3], [4,5,6],[7,8,9]]))
print(find_saddle_point([[8,1,9], [7,2,6],[3,4,5]]))

