class FlipPhone:
    def __init__(self):
        self.digit_mapping = [[],[],['a','b','c'],['d','e','f'],['g','h','i']]

    def all_possible_mappings(self, input):
        i = 0
        output = []
        if (input == None) or (len(input) < 1) :
            return output

        output = self.digit_mapping[int(input[i])]
        i += 1
        while(i < len(input)):
            new_output = []
            for combination in output:
                for character in self.digit_mapping[int(input[i])]:
                    new_output.append(combination + character)
            output = new_output
            i += 1

        print(output)
        return output


jamies_phone = FlipPhone()

assert jamies_phone.all_possible_mappings('1') == []
assert jamies_phone.all_possible_mappings('2') == ['a','b','c']
assert jamies_phone.all_possible_mappings('') == []
assert jamies_phone.all_possible_mappings(None) == []
