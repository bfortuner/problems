"""
CSV Parser
Write Method that takes a string representing a CSV
And returns a data-structure like the one below.

input:

column1,column2
"a",b
"c,d","e\"f"

output:

[
   {
      column1: a
      column2: b
   },
   {
      column1: c,d
      column2: e"f
   }
]
"""


def parse_csv(input):
    input_list = input.split("\n")
    headers = input_list[0].split(",") #[col1, col2] 
    i = 1
    output_list = []
    while i < len(input_list):
        clean_data = parse_line(input_list[i])
        result_dict = get_dict(headers, clean_data)
        output_list.append(result_dict)
        i+=1
    return output_list

def parse_line(line):
    """
    Input: line as string
    Output: list of valid split entries to add to dict
    
    output = [c,d]
    "c,d", "e\"f"
    cur = ""
    """
    output_line_list = []
    inside_quotes = False
    cur_str = ""
    for i in range(len(line)):
        if not inside_quotes and line[i] == ',':
            output_line_list.append(cur_str)
            cur_str = ""
        elif i+1 < len(line) and line[i:i+2] == '\\"':
             cur_str += '"'
             i+=1
        elif line[i] != '"':
            cur_str += line[i]
        else:
            inside_quotes = not inside_quotes
    output_line_list.append(cur_str)
    return output_line_list

def get_dict(headers, data):
    result_dict = {}
    for i in range(len(headers)):
        result_dict[headers[i]] = data[i]
    return result_dict
    



# Tests

def test_parse_line():
    assert parse_line('"c,d","e\\"f"') == ['c,d', 'e"f']
    assert parse_line('"c,d","e\\"f\\"') == ['c,d', 'e"f"']
    assert parse_line('"c,d","\\"e\\"f\\"') == ['c,d', '"e"f"']

def test_get_dict():
    assert get_dict(["col1","col2"],
        ["dat1","dat2"]) == {'col2': 'dat2', 'col1': 'dat1'}

def test_parse_csv():
    assert parse_csv('column1,column2\n"a",b\n"c,d","e\\"f"') == [
    {'column1': 'a', 'column2': 'b'}, {'column1': 'c,d', 'column2': 'e"f'}]
    assert parse_csv('column1,column2\n"a",b\n"c,d","\\"e\\"f\\"') == [
    {'column1': 'a', 'column2': 'b'}, {'column1': 'c,d', 'column2': '"e"f"'}]

if __name__ == "__main__":
    test_parse_line()
    test_get_dict()
    test_parse_csv()
