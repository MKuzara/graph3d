from random import randint

class BaseGraphGenerator:
    
    def __init__(self, amount=10):
        self.amount = amount
    
    def generate(self, name='example', to_file=True):
        graph = '%s {\n' % name
        for i in range(self.amount):
            second = randint(0, self.amount)
            graph += f'{i} -- {second}\n'
        
        if to_file:
            with open('generated.dot', 'w') as f:
                f.write(graph)
        else:
            return graph + '}'