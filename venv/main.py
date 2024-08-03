import json
# input json文件
with open('./json_files/test.json') as data_file:
    raw_data = json.load(data_file)
result_list = []
error_list = []
yes_list = []
no_list = []

for data_obj in raw_data:
    input_id = data_obj.get('id')
    input_str = data_obj.get('input').lower()
    headlines = input_str.split('\n\n')
    index = 0
    while index < len(headlines):
        headline = headlines[index]
        headline_id = str(input_id) + '_' + str(index)
        # requires further improvement.
        headline_list = headline.split('question: ')
        if len(headline_list) <= 1:
            error_data = {
                'id': headline_id,
                "content": headline,
            }
            error_list.append(error_data)
            index += 1
            continue
        content = headline_list[1]
        core_content = content.split('? ')
        question = core_content[0]
        if len(core_content) > 1:
            answer = core_content[1]
            if answer == 'yes':
                yes_list.append(headline_id)
            else:
                no_list.append(headline_id)
        else:
            answer = ''
        # construct data object
        processed_data = {
            'id': headline_id,
            'question': question,
            'answer': answer
        }
        result_list.append(processed_data)
        index += 1

# print(len(result_list))
# print(len(error_list))
print(len(yes_list))
print(len(no_list))
json.dump(result_list, open('json_files/result/test_result.json', 'w'), indent=4)
json.dump(error_list, open('json_files/result/error_result.json', 'w'), indent=4)