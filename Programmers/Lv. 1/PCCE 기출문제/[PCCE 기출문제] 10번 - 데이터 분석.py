def solution(data, ext, val_ext, sort_by):
    # data = [["코드 번호(code)", "제조일(date)", "최대 수량(maximum)", "현재 수량(remain)"], ...]
    ext_dict = {
        'code': 0,
        'date': 1,
        'maximum': 2,
        'remain': 3
    }
    
    del_idx = []
    
    for val in data:
        if val[ext_dict[ext]] >= val_ext:
            del_idx.append(data.index(val))
            
    # del_idx에 있는 인덱스 끝에서부터 remove
    del_idx.reverse()
    for idx in del_idx:
        del data[idx]
        
    data.sort(key=lambda x: x[ext_dict[sort_by]])
    
    return data
