import unittest

from TestHelpers import *

"""
class TestRoutineWriter(unittest.TestCase,RoutineWriterTesterHelper):
    def __init__(self, methodName='runTest'):
        RoutineWriterTesterHelper.__init__(self)
        unittest.TestCase.__init__(self,methodName)
    def WriteClassCode(self,fileName,Routine,headerLines,printFuncName=False):
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        sourceCode = []
        sourceCode.extend(headerLines)
        addingLines = False
        with open(fileName, 'rU') as inputFile:
            for line in inputFile:
                if 'def' in line:
                    addingLines = False
                    if Routine in line:
                        addingLines = True
                        includingLines = True
                        if printFuncName:
                            line = line.replace('test','').replace('self','')
                            sourceCode.append(line[4:])
                        continue
                if addingLines:
                    if '# exclude' in line:
                        includingLines = False
                        continue
                    if '# include' in line:
                        includingLines = True
                        continue
                    if includingLines:
                        if printFuncName:
                            sourceCode.append(line[4:])
                        else:
                            sourceCode.append(line[8:])
        scriptName = Routine.replace('test','').replace('(self)','')
        scriptFileName=scriptName + 'Code.py'
        self.CheckRoutineWriterResult(scriptFileName,sourceCode,Routine + ' source code')
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        execfile(scriptFileName)
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        sys.stdout = old_stdout
        outputFileName = scriptName + '.po'
        if not os.path.exists(outputFileName):
            resultFile = open(outputFileName, 'w')
            resultFile.write(mystdout.getvalue())
            resultFile.close()
            self.assertTrue(False, outputFileName + ' not found')
        regressionFile = open(outputFileName, 'rU')
        regression = regressionFile.read()
        regressionFile.close()
        self.assertTrue(regression == mystdout.getvalue(), outputFileName + ' incorrect')
"""

class TestWriteClass(unittest.TestCase):
    def WriteClassCode(self,fileName,className,defName):
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        if isinstance(defName,str):
            defName=[defName]
        outputFileName=fileName.split('/')[-1].split('.')[0]+'_'+className+'_'+defName[0]+'.py'
        inClass= className is ''
        inDef=False
        addingLines=False
        sourceCode=[]
        with open(fileName, 'rU') as inputFile:
            for line in inputFile:
                if "class" in line:
                    if className == line.lstrip(' ').split(' ')[1].split('(')[0]:
                        inClass = True
                        inDef = False
                        addingLines = True
                    else:
                        inClass = False
                        inDef = False
                        addingLines = False
                elif "def" in line:
                    if inClass:
                        if any(d == line.lstrip(' ').split(' ')[1].split('(')[0] for d in defName):
                            inDef=True
                            """
                            if not addingLines:
                                sourceCode.append("...")
                            """
                            addingLines=True
                        else:
                            if addingLines:
                                sourceCode.append("...\n")
                            inDef=False
                            addingLines=False
                    else:
                        inDef=False
                        addingLines=False
                else:
                    if addingLines:
                        if not inDef:
                            addingLines=False
                if addingLines is True:
                    sourceCode.append(line)
        if not os.path.exists(outputFileName):
            with open(outputFileName, 'w') as outputFile:
                for line in sourceCode:
                    outputFile.write(line)
        with open(outputFileName, 'rU') as regressionFile:
            regression = regressionFile.readlines()
        self.assertTrue(regression == sourceCode, outputFileName + ' incorrect')


    def testWriteFrequencyResponse_ImpulseResponse(self):
        fileName="../SignalIntegrity/SParameters/FrequencyResponse.py"
        className='FrequencyResponse'
        defName=['ImpulseResponse']
        self.WriteClassCode(fileName,className,defName)
    def testWriteFrequencyResponse_Resample(self):
        fileName="../SignalIntegrity/SParameters/FrequencyResponse.py"
        className='FrequencyResponse'
        defName=['Resample']
        self.WriteClassCode(fileName,className,defName)
    def testWriteFrequencyResponse_Pad(self):
        fileName="../SignalIntegrity/SParameters/FrequencyResponse.py"
        className='FrequencyResponse'
        defName=['_Pad']
        self.WriteClassCode(fileName,className,defName)
    def testWriteFrequencyResponse_DelayBy(self):
        fileName="../SignalIntegrity/SParameters/FrequencyResponse.py"
        className='FrequencyResponse'
        defName=['_DelayBy']
        self.WriteClassCode(fileName,className,defName)
    def testWriteFrequencyResponse_Rat(self):
        fileName="../SignalIntegrity/SParameters/FrequencyResponse.py"
        className=''
        defName=['Rat']
        self.WriteClassCode(fileName,className,defName)
    def testWriteImpulseResponse_FrequencyResponse(self):
        fileName="../SignalIntegrity/SParameters/ImpulseResponse.py"
        className='ImpulseResponse'
        defName=['FrequencyResponse']
        self.WriteClassCode(fileName,className,defName)
    def testWriteImpulseResponse_TrimToThreshold(self):
        fileName="../SignalIntegrity/SParameters/ImpulseResponse.py"
        className='ImpulseResponse'
        defName=['TrimToThreshold']
        self.WriteClassCode(fileName,className,defName)
    def testWriteImpulseResponse_FirFilter(self):
        fileName="../SignalIntegrity/SParameters/ImpulseResponse.py"
        className='ImpulseResponse'
        defName=['FirFilter']
        self.WriteClassCode(fileName,className,defName)

        
if __name__ == '__main__':
    unittest.main()