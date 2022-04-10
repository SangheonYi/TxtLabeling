class DataTSV():
    def __init__(self, file):
        self.current = 0
        self.tokens_list = []
        self.labels_list = []
        for line in file:
            if '\t' in line:
                tokens, labels = line.split('\t')
                self.tokens_list.append(tokens.split())
                self.labels_list.append(labels.split())

    def get_line(self):
        if -1 < self.current < len(self.tokens_list):
            token_part = ' '.join(self.tokens_list[self.current])
            label_part = ' '.join(self.labels_list[self.current])
            return f"{token_part}\t{label_part}"
        return 'end of file'

    def get_mixed_line(self):
        mixed = []
        if -1 < self.current < len(self.tokens_list):
            for i, token in enumerate(self.tokens_list[self.current]):
                mixed.append(token + ' ' + self.labels_list[self.current][i])
            token_part = ' '.join(self.tokens_list[self.current])
            label_part = ' '.join(self.labels_list[self.current])
            return f"{token_part}\t{label_part}"
        return 'end of file'

    def next(self):
        if  self.current < len(self.tokens_list):
            self.current += 1

    def prev(self):
        if self.current > 0:
            self.current -= 1

    def go_ith_line(self, index):
        if -1 < index < len(self.tokens_list):
            self.current = index
        return self.get_line()

class LabelFile():
    def __init__(self, file):
        self.label_domain = []
        for line in file:
            self.label_domain.append(line)

    def get_label(self, index):
        return self.label_domain[index]
