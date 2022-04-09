class DataTSV():
    def __init__(self, file):
        self.tokens_list = []
        self.labels_list = []
        for line in file:
            if '\t' in line:
                tokens, labels = line.split('\t')
                self.tokens_list.append(tokens.split())
                self.labels_list.append(labels.split())

    def get_line(self, index):
        token_part = ' '.join(self.tokens_list[index])
        label_part = ' '.join(self.labels_list[index])
        return f"{token_part}\t{label_part}"

class LabelFile():
    def __init__(self, file):
        self.label_domain = []
        for line in file:
            self.label_domain.append(line)

    def get_label(self, index):
        return self.label_domain[index]
