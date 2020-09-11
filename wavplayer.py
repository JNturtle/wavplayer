"""
只能播放 .wav 檔，並且使用多進程播放而不會卡住主線程。
導入時，主程式必須添加以下，才不會報錯
if __name__ == "__main__":
    pass
"""
import winsound
import multiprocessing as mtp

class WAVPLYAER():
    def __init__(self, numberPre = "", numberUnit = "", numberEnd = ""):
        self.numberPre = ""
        self.numberUnit = ""
        self.numberEnd = ""
        self.processings = []

    def playNumberVoice(self, number, digital = 3):
        """
        播放數字的語音，目前最多到 10**3 位，也就是千。
        """
        if self.numberPre: winsound.PlaySound(self.numberPre, winsound.SND_FILENAME)
        while digital >= 0:
            if number // 10**digital >= 1:
                nowDigital = str(number//10**digital)[-1]
                if not(digital == 0 and nowDigital == '0'):
                    winsound.PlaySound('sound/number/'+ nowDigital +'.wav', winsound.SND_FILENAME)
                if 10**digital > 1 and nowDigital != '0': 
                    winsound.PlaySound('sound/number/'+ str(10**digital) + '.wav', winsound.SND_FILENAME)
            digital -= 1
        if self.numberUnit: winsound.PlaySound(self.numberUnit, winsound.SND_FILENAME)
        if self.numberEnd: winsound.PlaySound(self.numberEnd, winsound.SND_FILENAME)
        
    def playFile(self, path):
        """播放 path 的 wav"""
        self.processings.append(mtp.Process(target=winsound.PlaySound, args=(path, winsound.SND_FILENAME,)))
        self.processings[-1].start()

    def playNumber(self, number, digital = 3):
        """播放數字的語音"""
        self.processings.append(mtp.Process(target=self.playNumberVoice, args=(number, 3, )))
        self.processings[-1].start()

    def clearProcessing(self):
        """清理已經結束的進程"""
        for i in range(len(self.processings)-1, -1, -1):
            if self.processings[i].is_alive() == False:
                del self.processings[i]
        return 1

if __name__ == "__main__" :  
    player().playNumber(123)
    for i in range(10):
        print(i)
    #play_number_voice(567)

