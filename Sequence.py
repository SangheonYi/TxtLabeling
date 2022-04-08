class Sequence():
    def __init__(self, file) -> None:
        self.tokens_list = []
        self.labels_list = []
        for line in file:
            tokens, labels = line.split()
            self.tokens_list.append(tokens.split())
            self.labels_list.append(labels.split())

    def get_line(self, index):
        token_part = ' '.join(self.tokens_list[index])
        label_part = ' '.join(self.labels_list[index])
        return f"{token_part}\t{label_part}"
