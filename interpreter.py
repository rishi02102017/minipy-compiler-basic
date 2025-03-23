class MiniPyVM:
    def __init__(self, bytecode):
        self.bytecode = bytecode
        self.env = {}
        self.stack = []
        self.labels = self._map_labels()

    def _map_labels(self):
        labels = {}
        pc = 0
        while pc < len(self.bytecode):
            line = self.bytecode[pc]
            if line.endswith(':'):
                labels[line[:-1]] = pc
                self.bytecode.pop(pc)
                continue
            pc += 1
        return labels

    def run(self):
        pc = 0
        while pc < len(self.bytecode):
            line = self.bytecode[pc]
            parts = line.split()

            if parts[0] == 'PUSH':
                self.stack.append(int(parts[1]))
            elif parts[0] == 'STORE':
                self.env[parts[1]] = self.stack.pop()
            elif parts[0] == 'LOAD':
                self.stack.append(self.env[parts[1]])
            elif parts[0] == 'PRINT':
                print(self.stack.pop())
            elif parts[0] in {'+', '-', '*', '/', '<'}:
                b = self.stack.pop()
                a = self.stack.pop()
                if parts[0] == '+': self.stack.append(a + b)
                if parts[0] == '-': self.stack.append(a - b)
                if parts[0] == '*': self.stack.append(a * b)
                if parts[0] == '/': self.stack.append(a // b)
                if parts[0] == '<': self.stack.append(int(a < b))
            elif parts[0] == 'JZ':
                if self.stack.pop() == 0:
                    pc = self.labels[parts[1]]
                    continue
            elif parts[0] == 'JMP':
                pc = self.labels[parts[1]]
                continue

            pc += 1
