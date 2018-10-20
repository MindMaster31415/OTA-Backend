import scorer

def sorter(algorithm_num, gps_coordinates, user_preference):
    data = scorer.master_scorer(gps_coordinates, user_preference)
    if algorithm_num == 0:
        output = sort_0(data)
    elif algorithm_num == 1:
        output = sort_1(data)
    elif algorithm_num == 2:
        output = sort_2(data)
    elif algorithm_num == 3:
        output = sort_3(data)
    return output

def sort_0(raw_data):
    return(overall_sort(scorer.final_scorer((1/3), (1/3), (1/3), raw_data)))

def sort_1(raw_data):
    return(overall_sort(scorer.final_scorer((1/4), (1/2), (1/4), raw_data)))

def sort_2(raw_data):
    return(overall_sort(scorer.final_scorer((1/4), (1/4), (1/2), raw_data)))

def sort_3(raw_data):
    return(overall_sort(scorer.final_scorer((1/2), (1/4), (1/4), raw_data)))

def overall_sort(raw_data):
    dummy, final = [], []
    for item in raw_data ['rows']:
        dummy.append((item ['score'], item ['id']))
    dummy.sort(reverse = True)
    for (score, index) in dummy:
        for item2 in raw_data ['rows']:
            if index == item2 ['id']:
                final.append(item2)
                break
    output = {'rows': final}
    return output
