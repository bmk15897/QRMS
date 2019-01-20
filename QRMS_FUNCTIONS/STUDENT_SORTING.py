def sorting_on_an_attribute(attribute_to_consider,sort_ascending,axis,inPlace,data_to_sort):
    data_to_sort.sort_values(by=[attribute_to_consider],ascending=sort_ascending,axis=axis,inplace=inPlace)
