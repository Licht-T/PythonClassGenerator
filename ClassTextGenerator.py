

class ClassTextGenerator:
    def __init__(self, className, indent='    '):
        self.__className = className
        self.__indent = indent
        self.functions = {
                '__init__': {
                    'args': None,
                    'return': False,
                    'lines': []
                    }
                }
        self.__hiddenVals = []

    def addFunction(self, functionName, lines, args=None, returnVal=False):
        self.functions[functionName] = {
                'args': args,
                'return': returnVal,
                'lines': lines
                }

    def addHiddenVal(self, line):
        self.__hiddenVals.append(line)

    def generate(self):
        classTextList = ['class {0}:'.format(self.__className)]

        for val in self.__hiddenVals:
            string = self.__indent + val
            classTextList.append(string)

        for functionName, data in self.functions.items():
            functionArgsList = ['self']
            if data['args'] is not None:
                functionArgsList = functionArgsList + data['args']
            functionDefString = 'def {0}({1}):'.format(functionName, ', '.join(functionArgsList))
            classTextList.append(self.__indent + functionDefString)

            for line in data['lines']:
                classTextList.append(self.__indent*2 + line)

            if data['return'] is False:
                classTextList.append(self.__indent*2 + 'return')

        return '\n'.join(classTextList)
