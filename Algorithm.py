class Algorithm:

    slove_space = None

    def slove(input_item_list, weight):
        result_id_list = []

        # row = len(input_item_list)
        # col = weight

        slove_space = [len(input_item_list)][weight]

        for row_index in range(0, len(input_item_list)):
            item = input_item_list[row_index]
            current_weight = item.weight
            current_value = item.value
            for clo_index in range(0, weight):

        # for item in input_item_list:
        #     current_weight = item.weight
        #     current_value = item.value




        return result_id_list;