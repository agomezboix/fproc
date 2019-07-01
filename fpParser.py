
from os import listdir
from os.path import isfile, join


class FPparser(object):
    fp = {}
    fpPath = ""
    listFonts = ["Andale Mono", "AppleGothic", "Arial", "Arial Black", "Arial Hebrew", "Arial MT", "Arial Narrow", "Arial Rounded MT Bold", "Arial Unicode MS", "Bitstream Vera Sans Mono", "Book Antiqua", "Bookman Old Style", "Calibri", "Cambria", "Cambria Math", "Century", "Century Gothic", "Century Schoolbook", "Comic Sans", "Comic Sans MS", "Consolas", "Courier", "Courier New", "Garamond", "Geneva", "Georgia", "Helvetica", "Helvetica Neue", "Impact", "Lucida Bright", "Lucida Calligraphy", "Lucida Console", "Lucida Fax", "LUCIDA GRANDE", "Lucida Handwriting", "Lucida Sans", "Lucida Sans Typewriter", "Lucida Sans Unicode", "Microsoft Sans Serif", "Monaco", "Monotype Corsiva", "MS Gothic", "MS Outlook", "MS PGothic", "MS Reference Sans Serif", "MS Sans Serif", "MS Serif", "MYRIAD", "MYRIAD PRO", "Palatino", "Palatino Linotype", "Segoe Print", "Segoe Script", "Segoe UI", "Segoe UI Light", "Segoe UI Semibold", "Segoe UI Symbol", "Tahoma", "Times", "Times New Roman", "Times New Roman PS", "Trebuchet MS", "Verdana", "Wingdings", "Wingdings 2", "Wingdings 3"]

    def __init__(self, path):
        self.fpPath = path
        self.loadFP()
    
    def loadFP(self):
        fp = {}
        fpFile = open(self.fpPath + "fp", "r")
        for line in fpFile:
            kv = line.split(":")
            fp[kv[0]] = kv[1][:len(kv[1]) - 1]
        fpFile.close()
        self.fp=fp

        
    def getDetectedFonts(self):
        listDetecFonts = self.fp['fontsJs']
        detectedFonts = []
        index = 0
        for i in range(0, len(listDetecFonts), 3):
            fi = listDetecFonts[i:i + 3]
            if "t" in fi:
                detectedFonts.append(self.listFonts[index])  # .lower().replace(" ", "").replace("-", "").replace("_", ""))
                index = index + 1

        return detectedFonts
    
    def getFileDetectedFonts(self, fontsPath):
        detected = self.getDetectedFonts()
        detectedFonts = []
        for font in detected:
            detectedFonts.append(font.lower().replace(" ", "").replace("-", "").replace("_", ""))
        files = [f for f in listdir(fontsPath) if isfile(join(fontsPath, f))]
        fileFonts = []
        for file in files:
            name = file.split(".")[0]
            if name in detectedFonts:
               fileFonts.append(file)
        
        return fileFonts
    
    def getTimeZone(self):
        timezoneOffset = self.fp['timezoneJs']
        timezoneDict = {'-840':'Pacific/Kiritimati', '-14':'Pacific/Kiritimati',
                        '-780':'Pacific/Tongatapu', '-13':'Pacific/Tongatapu',
                        '-765':'Pacific/Chatham', '-12.75':'Pacific/Chatham',
                        '-720':'Asia/Anadyr', '-12':'Asia/Anadyr',
                        '-660':'Asia/Srednekolymsk', '-11':'Asia/Srednekolymsk',
                        '-630':'Australia/Lord_Howe', '-10.5':'Australia/Lord_Howe',
                        '-600':'Australia/Melbourne', '-10':'Australia/Melbourne',
                        '-570':'Australia/Adelaide', '-9.5':'Australia/Adelaide',
                        '-540':'Asia/Tokyo', '-9':'Asia/Tokyo',
                        '-525':'Australia/Eucla', '-8.75':'Australia/Eucla',
                        '-480':'Asia/Shanghai', '-8':'Asia/Shanghai',
                        '-420':'Asia/Jakarta', '-7':'Asia/Jakarta',
                        '-390':'Asia/Yangon', '-6.5':'Asia/Yangon',
                        '-360':'Asia/Dhaka', '-6':'Asia/Dhaka',
                        '-345':'Asia/Kathmandu', '-5.75':'Asia/Kathmandu',
                        '-330':'Asia/Kolkata', '-5.5':'Asia/Kolkata',
                        '-300':'Asia/Tashkent', '-5':'Asia/Tashkent',
                        '-270':'Asia/Tehran', '-4.5':'Asia/Tehran',
                        '-240':'Asia/Dubai', '-4':'Asia/Dubai',
                        '-180':'Europe/Moscow', '-3':'Europe/Moscow',
                        '-120':'Europe/Brussels', '-2':'Europe/Brussels',
                        '-60':'Europe/London', '-1':'Europe/London',
                        '0':'Africa/Accra', '0':'Africa/Accra',
                        '60':'Atlantic/Cape_Verde', '1':'Atlantic/Cape_Verde',
                        '120':'America/Godthab', '2':'America/Godthab',
                        '150':'America/St_Johns', '2.5':'America/St_Johns',
                        '180':'America/Argentina/Buenos_Aires', '3':'America/Argentina/Buenos_Aires',
                        '240':'America/New_York', '4':'America/New_York',
                        '300':'America/Mexico_City', '5':'America/Mexico_City',
                        '360':'America/Guatemala', '6':'America/Guatemala',
                        '420':'America/Los_Angeles', '7':'America/Los_Angeles',
                        '480':'America/Anchorage', '8':'America/Anchorage',
                        '540':'America/Adak', '9':'America/Adak',
                        '570':'Pacific/Marquesas', '9.5':'Pacific/Marquesas',
                        '600':'Pacific/Honolulu', '10':'Pacific/Honolulu'}
        # missing UTC-11 and UTC-12
        return timezoneDict[timezoneOffset]
    
    def getLanguages(self):
        lan = self.fp['languageHttp']
        languages = []
        listLang=lan.split(",")
        for l in listLang:
            languages.append(l.split(";")[0])
        
        return languages
    
    def doNotTrack(self):
        dnt = self.fp['dntJs']
        return  "yes" if dnt[0]=='1' or dnt[0]=='y' or dnt[0]=='Y' else "no"

    def adBlocker(self):
        print(self.fp['adBlock'])
        dnt = self.fp['adBlock']
        return  "yes" if dnt[0]=='t' or dnt[0]=='T' or dnt[0]=='Y' or dnt[0]=='y' else "no"
 