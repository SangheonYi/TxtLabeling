from constants import EXCLUDE_LISTBOX, INCLUDE_LISTBOX, ORIGIN, TOKENIZED
def is_labels_in_labellist(labellist, file_labels):
    return set(labellist).intersection(set(file_labels))

def redeem_lists(tokens, labels):
    if len(tokens) < len(labels):
        for i in range(len(labels) - len(tokens)):
            labels.pop()
    elif len(tokens) > len(labels):
        for i in range(len(tokens) - len(labels)):
            labels.append('O')

class DataTSV():
    def __init__(self, file):
        self.current = 0
        self.tokens_list = []
        self.labels_list = []
        for line in file:
            if '\t' in line:
                tokens, labels = line.split('\t')
                tokens, labels = tokens.split(), labels.split()
                redeem_lists(tokens, labels)
                self.tokens_list.append(tokens)
                self.labels_list.append(labels)

    def get_line(self):
        if -1 < self.current < len(self.tokens_list):
            token_part = ' '.join(self.tokens_list[self.current])
            label_part = ' '.join(self.labels_list[self.current])
            return f"{token_part}\t{label_part}"
        return 'end of file'

    def get_ith_line(self, index):
        if -1 < index < len(self.tokens_list):
            token_part = ' '.join(self.tokens_list[index])
            label_part = ' '.join(self.labels_list[index])
            return f"{token_part}\t{label_part}"
        return 'end of file'

    def get_mixed_list(self, key):
        mixed = []
        if -1 < self.current < len(self.tokens_list):
            for i, token in enumerate(self.tokens_list[self.current]):                
                mixed.append((self.labels_list[self.current][i], token))
            return mixed
        return 'end of file'

    def is_target(self, include_labels, exclude_labels):
        target_labels = self.labels_list[self.current]
        if not (include_labels or exclude_labels):
            return True
        elif is_labels_in_labellist(include_labels, target_labels) and not is_labels_in_labellist(exclude_labels, target_labels):
            return True
        return False

    def next(self, label_listbox):
        include_labels = label_listbox[INCLUDE_LISTBOX]
        exclude_labels = label_listbox[EXCLUDE_LISTBOX]
        while self.current < len(self.tokens_list):
            self.current += 1
            if self.is_target(include_labels, exclude_labels):
                break

    def prev(self, label_listbox):
        include_labels = label_listbox[INCLUDE_LISTBOX]
        exclude_labels = label_listbox[EXCLUDE_LISTBOX]
        while self.current > 0:
            self.current -= 1
            if self.is_target(include_labels, exclude_labels):
                break

    def go_ith_line(self, index):
        if -1 < index < len(self.tokens_list):
            self.current = index
        return self.get_line()

    def set_label(self, index, new_label):
        if -1 < self.current < len(self.tokens_list):
            labels = self.labels_list[self.current]
            if -1 < index < len(labels):
                self.labels_list[self.current][index] = new_label

class LabelFile():
    def __init__(self, file):
        self.label_domain = []
        for line in file:
            self.label_domain.append(line.strip())

    def get_label(self, index):
        return self.label_domain[index]
