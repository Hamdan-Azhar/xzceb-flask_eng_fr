from deep_translator import MyMemoryTranslator,GoogleTranslator

def englishToFrench(englishText):
    frenchText = GoogleTranslator(source='english',
    target='french').translate(englishText)
    return frenchText

def frenchToEnglish(frenchText):
    englishText = MyMemoryTranslator(source='French',
    target='English').translate(frenchText)
    return englishText