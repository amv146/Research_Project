import tensorflow as tf

class FileProcessor:
    def __init__(self) -> None:
        self.inputs = []
        self.outputs = []

    def read_all_files(self, num_cases=-1, num_outputs=-1, include_wv=False):
        self.num_cases = num_cases
        input_num = self.read_all_input_files()
        output_num = self.read_all_output_files(include_wv=include_wv, num_outputs=num_outputs)

        if input_num != output_num:
            print('ERROR: Unequal number of input files to output files (' + str(input_num) + ' to ' + str(output_num) + ')')
            return None, None
        else:
            return tf.convert_to_tensor(self.inputs), tf.convert_to_tensor(self.outputs)

    def read_all_input_files(self):
        file_string = 'Variables-Case-'
        file_name = file_string + '1.txt'
        file_num = 1

        while self.read_input_file(file_name) and file_num - 1 != self.num_cases:
            file_num += 1
            file_name = file_string + str(file_num) + '.txt'

        return file_num

    def read_all_output_files(self, include_wv=False, num_outputs=-1):
        file_string = 'SParam-MultiLayered-Surface-Case-'
        file_name = file_string + '1.txt'
        file_num = 1

        while self.read_output_file(file_name, include_wv=include_wv, num_values=num_outputs) and file_num - 1 != self.num_cases:
            file_num += 1
            file_name = file_string + str(file_num) + '.txt'

        return file_num

    def read_input_file(self, file_name):
        file = self.__try_open_file__("data/" + file_name)

        if (file == None):
            return False
        
        input_list = []
        in_num = 0
        for line in file:
            if line != '':
                try:
                    input_list.append(float(line))
                    in_num += 1
                except ValueError:
                    pass

        self.in_num = in_num
        self.inputs.append(input_list)

        return True
        
    def read_output_file(self, file_name, include_wv=False, num_values=-1):
        file = self.__try_open_file__("data/" + file_name)

        if (file == None):
            return False

        output_list = [] 
        out_num = 0
        for line in file:
            if (out_num == num_values):
                break
            if line != '':
                line_values = line.split()
                if include_wv:
                    line_outputs = []
                    try:
                        line_outputs.append(float(line_values[0]))
                        line_outputs.append(float(line_values[1]))

                        output_list.append(line_outputs)
                    except ValueError or IndexError:
                        pass
                else:
                    try:
                        output_list.append(float(line_values[1]))
                    except ValueError or IndexError:
                        pass
            out_num += 1
        self.out_num = out_num
        self.outputs.append(output_list)

        return True

    def __try_open_file__(self, file_name):
        try:
            return open(file_name)
        except OSError:
            return None
