import arcpy
import csv

class Toolbox(object):
    def __init__(self):
        # List of tool classes associated with this toolbox
        self.tools = [FunabashiDoroMergeCalculate] 

class FunabashiDoroMergeCalculate(object):
    def __init__(self):
        self.label       = "Funabashi_Merge_And_Calculate_To_Doro_Daicho_Data"
        self.description = "船橋市道路台帳データをMQX変換に対応するためのマージと演算をします。"

    def getParameterInfo(self):
        #Define parameter definitions

        # Input Features parameter
        in_features_path = arcpy.Parameter(
            displayName="格納先フォルダパス",
            name="in_Workspace",
            datatype="DEWorkspace",
            parameterType="Required",
            direction="Input")

        parameters = [in_features_path]

        return parameters

    def isLicensed(self): #optional
        return True

    def updateMessages(self, parameters): #optional
        return

    def execute(self, parameters, messages):
        
        # 作業フォルダを変更
        arcpy.env.workspace = parameters[0].valueAsText
        
        # ■3320_起終点_起終点■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # 進捗表示
        messages.addMessage("3320_起終点_起終点" "の処理を開始")
        
        CodeBlock = """def CodeCalc(CHIBUTSU):
    if CHIBUTSU == 910400:
        return 124
    elif CHIBUTSU == 910500:
        return 125
    else:
        return 0"""
        
        # shpファイルが揃っている場合のみ処理を行う
        if arcpy.Exists("D9104_起点記号_S.shp") and arcpy.Exists("D9105_終点記号_S.shp"):
            outFeature = u"3320_起終点_起終点.shp"
            
            arcpy.env.workspace = parameters[0].valueAsText + u"\ポイント"
            arcpy.Delete_management("3320_起終点_起終点.shp")
            arcpy.env.workspace = parameters[0].valueAsText
            
            # unicode文字と連結するので連結する文字もunicodeにする
            OutputShape = parameters[0].valueAsText + u"\ポイント\\" + outFeature
            
            
            # マージ実行
            arcpy.Merge_management(
            ["D9104_起点記号_S.shp",
            "D9105_終点記号_S.shp"],
            OutputShape)
            
            # 作業フォルダを変更
            arcpy.env.workspace = parameters[0].valueAsText + u"\ポイント"
            
            # フィールドを追加
            arcpy.AddField_management(outFeature, "CODE", "LONG")
            
            # 演算式を格納
            Expression = "CodeCalc(!CHIBUTSU!)"
            
            
            # 演算
            arcpy.CalculateField_management(outFeature, "CODE", Expression, "PYTHON", CodeBlock)
            
            # 処理が終わったものを加工済みフォルダに移動
            arcpy.env.workspace = parameters[0].valueAsText
            movementFeature = u"D9104_起点記号_S.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\加工済み\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            movementFeature = u"D9105_終点記号_S.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\加工済み\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            
            # 進捗表示
            messages.addMessage("3320_起終点_起終点" "の処理を終了")
        else:
            # 進捗表示
            messages.addMessage("3320_起終点_起終点" "必要ファイルが無いため処理をしません")
        
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        
        
        # 作業フォルダを変更
        arcpy.env.workspace = parameters[0].valueAsText
        
        # ■3333_幅員_値■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # 進捗表示
        messages.addMessage("3333_幅員_値" "の処理を開始")
        
        CodeBlock = """def CodeCalc(CHIBUTSU):
    if CHIBUTSU == 911106:
        return 287
    elif CHIBUTSU == 911103:
        return 132
    elif CHIBUTSU == 911105:
        return 142
    elif CHIBUTSU == 911102:
        return 122
    elif CHIBUTSU == 911104:
        return 137
    else:
        return 0"""
        
        # shpファイルが揃っている場合のみ処理を行う
        if arcpy.Exists("D9111_道路部幅員値_T.shp") and arcpy.Exists("D9111_歩道部幅員値_T.shp") and arcpy.Exists("D9111_階段部幅員値_T.shp") and arcpy.Exists("D9111_車道部幅員値_T.shp") and arcpy.Exists("D9111_中央分離帯幅員値_T.shp"):
        
            outFeature = u"3333_幅員_値.shp"
            
            arcpy.env.workspace = parameters[0].valueAsText + u"\テキスト"
            arcpy.Delete_management("3333_幅員_値.shp")
            arcpy.env.workspace = parameters[0].valueAsText
            
            # unicode文字と連結するので連結する文字もunicodeにする
            OutputShape = parameters[0].valueAsText + u"\テキスト\\" + outFeature
            
            # マージ実行
            arcpy.Merge_management(
            ["D9111_道路部幅員値_T.shp",
            "D9111_歩道部幅員値_T.shp",
            "D9111_階段部幅員値_T.shp",
            "D9111_車道部幅員値_T.shp",
            "D9111_中央分離帯幅員値_T.shp"],
            OutputShape)
            
            # 作業フォルダを変更
            arcpy.env.workspace = parameters[0].valueAsText + u"\テキスト"
            
            # フィールドを追加
            arcpy.AddField_management(outFeature, "CODE", "LONG")
            
            # 演算式を格納
            Expression = "CodeCalc(!CHIBUTSU!)"
            
            # 演算
            arcpy.CalculateField_management(outFeature, "CODE", Expression, "PYTHON", CodeBlock)
            
            # 処理が終わったものを加工済みフォルダに移動
            arcpy.env.workspace = parameters[0].valueAsText
            movementFeature = u"D9111_道路部幅員値_T.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\加工済み\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            movementFeature = u"D9111_歩道部幅員値_T.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\加工済み\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            movementFeature = u"D9111_階段部幅員値_T.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\加工済み\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            movementFeature = u"D9111_車道部幅員値_T.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\加工済み\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            movementFeature = u"D9111_中央分離帯幅員値_T.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\加工済み\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            
            
            # 進捗表示
            messages.addMessage("3333_幅員_値" "の処理を終了")
        else:
            # 進捗表示
            messages.addMessage("3333_幅員_値" "必要ファイルが無いため処理をしません")
        
        
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        
        # 作業フォルダを変更
        arcpy.env.workspace = parameters[0].valueAsText
        
        # ■3331_幅員_線■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # 進捗表示
        messages.addMessage("3331_幅員_線" "の処理を開始")
        
        CodeBlock = """def CodeCalc(CHIBUTSU):
    if CHIBUTSU == 911206:
        return 286
    elif CHIBUTSU == 911203:
        return 131
    elif CHIBUTSU == 911205:
        return 141
    elif CHIBUTSU == 911202:
        return 121
    elif CHIBUTSU == 911204:
        return 136
    else:
        return 0"""
        
        
        # shpファイルが揃っている場合のみ処理を行う
        if arcpy.Exists("D9112_歩道部幅員線_L.shp") and arcpy.Exists("D9112_階段部幅員線_L.shp") and arcpy.Exists("D9112_車道部幅員線_L.shp") and arcpy.Exists("D9112_中央分離帯幅員線_L.shp") and arcpy.Exists("D9112_道路部幅員線_L.shp"):
            
            outFeature = u"3331_幅員_線.shp"
            
            arcpy.env.workspace = parameters[0].valueAsText + u"\ライン"
            arcpy.Delete_management("3331_幅員_線.shp")
            arcpy.env.workspace = parameters[0].valueAsText
            
            # unicode文字と連結するので連結する文字もunicodeにする
            OutputShape = parameters[0].valueAsText + u"\ライン\\" + outFeature
            
            # マージ実行
            arcpy.Merge_management(
            ["D9112_歩道部幅員線_L.shp",
             "D9112_階段部幅員線_L.shp",
             "D9112_車道部幅員線_L.shp",
             "D9112_中央分離帯幅員線_L.shp",
             "D9112_道路部幅員線_L.shp"],
            OutputShape)
            
            # 作業フォルダを変更
            arcpy.env.workspace = parameters[0].valueAsText + u"\ライン"
            
            # フィールドを追加
            arcpy.AddField_management(outFeature, "CODE", "LONG")
            
            # 演算式を格納
            Expression = "CodeCalc(!CHIBUTSU!)"
            
            # 演算
            arcpy.CalculateField_management(outFeature, "CODE", Expression, "PYTHON", CodeBlock)
            
            # 処理が終わったものを加工済みフォルダに移動
            arcpy.env.workspace = parameters[0].valueAsText
            movementFeature = u"D9112_歩道部幅員線_L.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\加工済み\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            movementFeature = u"D9112_階段部幅員線_L.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\加工済み\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            movementFeature = u"D9112_車道部幅員線_L.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\加工済み\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            movementFeature = u"D9112_中央分離帯幅員線_L.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\加工済み\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            movementFeature = u"D9112_道路部幅員線_L.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\加工済み\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            
            # 進捗表示
            messages.addMessage("3331_幅員_線" "の処理を終了")
        else:
            # 進捗表示
            messages.addMessage("3331_幅員_線" "必要ファイルが無いため処理をしません")
        
        
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        
        # 作業フォルダを変更
        arcpy.env.workspace = parameters[0].valueAsText
        
        # ■3304_側溝_側溝■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # 進捗表示
        messages.addMessage("3304_側溝_側溝" "の処理を開始")
        
        CodeBlock = """def CodeCalc(CHIBUTSU):
    if CHIBUTSU == 913101:
        return 150
    elif CHIBUTSU == 913102:
        return 151
    elif CHIBUTSU == 913103:
        return 152
    elif CHIBUTSU == 913102:
        return 156
    elif CHIBUTSU == 913107:
        return 158
    elif CHIBUTSU == 913108:
        return 159
    elif CHIBUTSU == 913109:
        return 151
    else:
        return 0"""
        
        # shpファイルが揃っている場合のみ処理を行う
        if arcpy.Exists("D9131_側溝ライン_L.shp"):
        
            outFeature = u"3304_側溝_側溝.shp"
            
            arcpy.env.workspace = parameters[0].valueAsText + u"\ライン"
            arcpy.Delete_management("3304_側溝_側溝.shp")
            arcpy.env.workspace = parameters[0].valueAsText
            
            # unicode文字と連結するので連結する文字もunicodeにする
            OutputShape = parameters[0].valueAsText + u"\ライン\\" + outFeature
            
            # コピー実行
            arcpy.Copy_management("D9131_側溝ライン_L.shp", OutputShape)
            
            # 作業フォルダを変更
            arcpy.env.workspace = parameters[0].valueAsText + u"\ライン"
            
            # フィールドを追加
            arcpy.AddField_management(outFeature, "CODE", "LONG")
            
            # 演算式を格納
            Expression = "CodeCalc(!CHIBUTSU!)"
            
            # 演算
            arcpy.CalculateField_management(outFeature, "CODE", Expression, "PYTHON", CodeBlock)
            
            # 処理が終わったものを加工済みフォルダに移動
            arcpy.env.workspace = parameters[0].valueAsText
            movementFeature = u"D9131_側溝ライン_L.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\加工済み\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            
            # 進捗表示
            messages.addMessage("3304_側溝_側溝" "の処理を終了")
        else:
            # 進捗表示
            messages.addMessage("3304_側溝_側溝" "必要ファイルが無いため処理をしません")
        
        
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        
        # 作業フォルダを変更
        arcpy.env.workspace = parameters[0].valueAsText
        
        # ■3306_防護柵_防護柵■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # 進捗表示
        messages.addMessage("3306_防護柵_防護柵" "の処理を開始")
        
        CodeBlock = """def CodeCalc(CHIBUTSU):
    if CHIBUTSU == 913301:
        return 160
    elif CHIBUTSU == 913305:
        return 161
    elif CHIBUTSU == 913303:
        return 162
    elif CHIBUTSU == 913302:
        return 163
    elif CHIBUTSU == 913304:
        return 164
    elif CHIBUTSU == 913307:
        return 165
    else:
        return 0"""
        
        # shpファイルが揃っている場合のみ処理を行う
        if arcpy.Exists("D9133_防護柵ライン_L.shp"):
        
            outFeature = u"3306_防護柵_防護柵.shp"
            
            arcpy.env.workspace = parameters[0].valueAsText + u"\ライン"
            arcpy.Delete_management("3306_防護柵_防護柵.shp")
            arcpy.env.workspace = parameters[0].valueAsText
            
            # unicode文字と連結するので連結する文字もunicodeにする
            OutputShape = parameters[0].valueAsText + u"\ライン\\" + outFeature
            
            # コピー実行
            arcpy.Copy_management("D9133_防護柵ライン_L.shp", OutputShape)
            
            # 作業フォルダを変更
            arcpy.env.workspace = parameters[0].valueAsText + u"\ライン"
            
            # フィールドを追加
            arcpy.AddField_management(outFeature, "CODE", "LONG")
            
            # 演算式を格納
            Expression = "CodeCalc(!CHIBUTSU!)"
            
            # 演算
            arcpy.CalculateField_management(outFeature, "CODE", Expression, "PYTHON", CodeBlock)
            
            # 処理が終わったものを加工済みフォルダに移動
            arcpy.env.workspace = parameters[0].valueAsText
            movementFeature = u"D9133_防護柵ライン_L.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\加工済み\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            
            # 進捗表示
            messages.addMessage("3306_防護柵_防護柵" "の処理を終了")
        else:
            # 進捗表示
            messages.addMessage("3306_防護柵_防護柵" "必要ファイルが無いため処理をしません")
        
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        
        # 作業フォルダを変更
        arcpy.env.workspace = parameters[0].valueAsText
        
        # ■3344_橋梁_注記■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # 進捗表示
        messages.addMessage("3344_橋梁_注記" "の処理を開始")
        
        # shpファイルが揃っている場合のみ処理を行う
        if arcpy.Exists("D9141_橋梁寸法_T.shp") and arcpy.Exists("D9141_橋梁番号_T.shp") and arcpy.Exists("D9141_橋梁名称_T.shp"):
            outFeature = u"3344_橋梁_注記.shp"
            
            # unicode文字と連結するので連結する文字もunicodeにする
            OutputShape = parameters[0].valueAsText + u"\テキスト\\" + outFeature
            
            arcpy.env.workspace = parameters[0].valueAsText + u"\テキスト"
            arcpy.Delete_management("3344_橋梁_注記.shp")
            arcpy.env.workspace = parameters[0].valueAsText
            
            # マージ実行
            arcpy.Merge_management(
            ["D9141_橋梁寸法_T.shp",
             "D9141_橋梁番号_T.shp",
             "D9141_橋梁名称_T.shp"],
            OutputShape)
            
            # 処理が終わったものを加工済みフォルダに移動
            arcpy.env.workspace = parameters[0].valueAsText
            movementFeature = u"D9141_橋梁寸法_T.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\加工済み\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            movementFeature = u"D9141_橋梁番号_T.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\加工済み\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            movementFeature = u"D9141_橋梁名称_T.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\加工済み\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            
            # 進捗表示
            messages.addMessage("3344_橋梁_注記" "の処理を終了")
        else:
            # 進捗表示
            messages.addMessage("3344_橋梁_注記" "必要ファイルが無いため処理をしません")
        
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        
        # ■3347_鉄道交差_注記■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # 進捗表示
        messages.addMessage("3347_鉄道交差_注記" "の処理を開始")
        
        # shpファイルが揃っている場合のみ処理を行う
        if arcpy.Exists("D9142_鉄道交差寸法_T.shp") and arcpy.Exists("D9142_鉄道交差番号_T.shp") and arcpy.Exists("D9142_鉄道交差名称_T.shp"):
            
            outFeature = u"3347_鉄道交差_注記.shp"
            
            arcpy.env.workspace = parameters[0].valueAsText + u"\テキスト"
            arcpy.Delete_management("3347_鉄道交差_注記.shp")
            arcpy.env.workspace = parameters[0].valueAsText
            
            # unicode文字と連結するので連結する文字もunicodeにする
            OutputShape = parameters[0].valueAsText + u"\テキスト\\" + outFeature
            
            # マージ実行
            arcpy.Merge_management(
            ["D9142_鉄道交差寸法_T.shp",
             "D9142_鉄道交差番号_T.shp",
             "D9142_鉄道交差名称_T.shp"],
            OutputShape)
            
            # 処理が終わったものを加工済みフォルダに移動
            arcpy.env.workspace = parameters[0].valueAsText
            movementFeature = u"D9142_鉄道交差寸法_T.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\加工済み\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            movementFeature = u"D9142_鉄道交差番号_T.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\加工済み\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            movementFeature = u"D9142_鉄道交差名称_T.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\加工済み\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            
            # 進捗表示
            messages.addMessage("3347_鉄道交差_注記" "の処理を終了")
        else:
            # 進捗表示
            messages.addMessage("3347_鉄道交差_注記" "必要ファイルが無いため処理をしません")
        
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        
        # ■3335_延長計測線_延長計測線■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # 進捗表示
        messages.addMessage("3335_延長計測線_延長計測線" "の処理を開始")
        
        CodeBlock = """def CodeCalc(CHIBUTSU):
    if CHIBUTSU == 932112:
        return 1015
    elif CHIBUTSU == 932111:
        return 1014
    elif CHIBUTSU == 932104:
        return 1016
    elif CHIBUTSU == 932105:
        return 1009
    elif CHIBUTSU == 932100:
        return 11
    elif CHIBUTSU == 932102:
        return 1009
    elif CHIBUTSU == 932103:
        return 1008
    elif CHIBUTSU == 932109:
        return 1011
    elif CHIBUTSU == 932114:
        return 1013
    elif CHIBUTSU == 932113:
        return 1012
    elif CHIBUTSU == 932101:
        return 1010
    else:
        return 0"""
        
        # shpファイルが揃っている場合のみ処理を行う
        if arcpy.Exists("Z9321_道路中心線（橋梁）_L.shp") and arcpy.Exists("Z9321_道路中心線（鉄道交差）_L.shp") and arcpy.Exists("Z9321_道路中心線_L.shp") and arcpy.Exists("Z9321_道路中心線重用下位_L.shp") and arcpy.Exists("Z9321_道路中心線分割橋_L.shp") and arcpy.Exists("Z9321_道路中心線未供用_L.shp"):
            
            outFeature = u"3335_延長計測線_延長計測線.shp"
            
            arcpy.env.workspace = parameters[0].valueAsText + u"\ライン"
            arcpy.Delete_management("3335_延長計測線_延長計測線.shp")
            arcpy.env.workspace = parameters[0].valueAsText
            
            # unicode文字と連結するので連結する文字もunicodeにする
            OutputShape = parameters[0].valueAsText + u"\ライン\\" + outFeature
            
            # マージ実行
            arcpy.Merge_management(
            ["Z9321_道路中心線（橋梁）_L.shp",
             "Z9321_道路中心線（鉄道交差）_L.shp",
             "Z9321_道路中心線_L.shp",
             "Z9321_道路中心線重用下位_L.shp",
             "Z9321_道路中心線分割橋_L.shp",
             "Z9321_道路中心線未供用_L.shp"],
            OutputShape)
            
            # 作業フォルダを変更
            arcpy.env.workspace = parameters[0].valueAsText + u"\ライン"
            
            # フィールドを追加
            arcpy.AddField_management(outFeature, "CODE", "LONG")
            
            # 演算式を格納
            Expression = "CodeCalc(!CHIBUTSU!)"
            
            # 演算
            arcpy.CalculateField_management(outFeature, "CODE", Expression, "PYTHON", CodeBlock)
            
            # 処理が終わったものを加工済みフォルダに移動
            arcpy.env.workspace = parameters[0].valueAsText
            movementFeature = u"Z9321_道路中心線（橋梁）_L.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\加工済み\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            movementFeature = u"Z9321_道路中心線（鉄道交差）_L.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\加工済み\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            movementFeature = u"Z9321_道路中心線_L.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\加工済み\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            movementFeature = u"Z9321_道路中心線重用下位_L.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\加工済み\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            movementFeature = u"Z9321_道路中心線分割橋_L.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\加工済み\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            movementFeature = u"Z9321_道路中心線未供用_L.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\加工済み\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            
            # 進捗表示
            messages.addMessage("3335_延長計測線_延長計測線" "の処理を終了")
        else:
            # 進捗表示
            messages.addMessage("3335_延長計測線_延長計測線" "必要ファイルが無いため処理をしません")
        
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        
        # 作業フォルダを変更
        arcpy.env.workspace = parameters[0].valueAsText
        
        # ■3318_歩道_線■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # 進捗表示
        messages.addMessage("3318_歩道_線" "の処理を開始")
        
        CodeBlock = """def CodeCalc(CHIBUTSU):
    if CHIBUTSU == 935200:
        return 170
    elif CHIBUTSU == 935300:
        return 176
    elif CHIBUTSU == 935301:
        return 176
    else:
        return 0"""
        
        # shpファイルが揃っている場合のみ処理を行う
        if arcpy.Exists("Z9352_歩道ライン_L.shp") and arcpy.Exists("Z9353_準歩道ライン_L.shp"):
            
            outFeature = u"3318_歩道_線.shp"
            
            arcpy.env.workspace = parameters[0].valueAsText + u"\ライン"
            arcpy.Delete_management("3318_歩道_線.shp")
            arcpy.env.workspace = parameters[0].valueAsText
            
            # unicode文字と連結するので連結する文字もunicodeにする
            OutputShape = parameters[0].valueAsText + u"\ライン\\" + outFeature
            
            # マージ実行
            arcpy.Merge_management(
            ["Z9352_歩道ライン_L.shp",
             "Z9353_準歩道ライン_L.shp"],
            OutputShape)
            
            # 作業フォルダを変更
            arcpy.env.workspace = parameters[0].valueAsText + u"\ライン"
            
            # フィールドを追加
            arcpy.AddField_management(outFeature, "CODE", "LONG")
            # 演算式を格納
            Expression = "CodeCalc(!CHIBUTSU!)"
            
            # 演算
            arcpy.CalculateField_management(outFeature, "CODE", Expression, "PYTHON", CodeBlock)
            
            # 処理が終わったものを加工済みフォルダに移動
            arcpy.env.workspace = parameters[0].valueAsText
            movementFeature = u"Z9352_歩道ライン_L.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\加工済み\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            movementFeature = u"Z9353_準歩道ライン_L.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\加工済み\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            
            # 進捗表示
            messages.addMessage("3318_歩道_線" "の処理を終了")
        else:
            # 進捗表示
            messages.addMessage("3318_歩道_線" "必要ファイルが無いため処理をしません")
        
        
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        
        # 作業フォルダを変更
        arcpy.env.workspace = parameters[0].valueAsText
        
        
        # ■3301_道路_道路■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # 進捗表示
        messages.addMessage("3301_道路_道路" "の処理を開始")
        
        CodeBlock = """def CodeCalc(CHIBUTSU):
    if CHIBUTSU == 935100:
        return 120
    elif CHIBUTSU == 935108:
        return 1123
    else:
        return 0"""
        
        # shpファイルが揃っている場合のみ処理を行う
        if arcpy.Exists("Z9351_道路縁_L.shp"):
            
            outFeature = u"3301_道路_道路.shp"
            
            arcpy.env.workspace = parameters[0].valueAsText + u"\ライン"
            arcpy.Delete_management("3301_道路_道路.shp")
            arcpy.env.workspace = parameters[0].valueAsText
            
            # unicode文字と連結するので連結する文字もunicodeにする
            OutputShape = parameters[0].valueAsText + u"\ライン\\" + outFeature
            
            # コピー実行
            arcpy.Copy_management("Z9351_道路縁_L.shp", OutputShape)
            
            # 作業フォルダを変更
            arcpy.env.workspace = parameters[0].valueAsText + u"\ライン"
            
            # フィールドを追加
            arcpy.AddField_management(outFeature, "CODE", "LONG")
            # 演算式を格納
            Expression = "CodeCalc(!CHIBUTSU!)"
            
            # 演算
            arcpy.CalculateField_management(outFeature, "CODE", Expression, "PYTHON", CodeBlock)
            
            # 処理が終わったものを加工済みフォルダに移動
            arcpy.env.workspace = parameters[0].valueAsText
            movementFeature = u"Z9351_道路縁_L.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\加工済み\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            
            # 進捗表示
            messages.addMessage("3301_道路_道路" "の処理を終了")
        else:
            # 進捗表示
            messages.addMessage("3301_道路_道路" "必要ファイルが無いため処理をしません")
        
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        
        # 作業フォルダを変更
        arcpy.env.workspace = parameters[0].valueAsText
        
        # ■3336_区間_区間■■■■■■■■■■■■■■■■■■■■■■■■■■■
        # 進捗表示
        messages.addMessage("3336_区間_区間" "の処理を開始")
        
        # shpファイルが揃っている場合のみ処理を行う
        if arcpy.Exists("Z9302_道路部_P.shp"):
            
            outFeature = u"3336_区間_区間.shp"
            
            arcpy.env.workspace = parameters[0].valueAsText + u"\エリア"
            arcpy.Delete_management("3336_区間_区間.shp")
            arcpy.env.workspace = parameters[0].valueAsText
            
            arcpy.env.workspace = parameters[0].valueAsText + u"\※属性"
            arcpy.Delete_management("3336_区間_区間.csv")
            arcpy.env.workspace = parameters[0].valueAsText
            
            # unicode文字と連結するので連結する文字もunicodeにする
            OutputShape = parameters[0].valueAsText + u"\エリア\\" + outFeature
            
            # コピー実行
            arcpy.Copy_management("Z9302_道路部_P.shp", OutputShape)
            
            # 作業フォルダを変更
            arcpy.env.workspace = parameters[0].valueAsText + u"\エリア"
            
            # フィールドを追加
            arcpy.AddField_management(outFeature, "UserID", "LONG")
            
            # 演算式を格納
            Expression = "[FID] + 1"
            
            # 演算
            arcpy.CalculateField_management(outFeature, "UserID", Expression)
            
            # SLINKIDとUserIDをCSVで出力する
            arcpy.TableToTable_conversion(u"3336_区間_区間.dbf", parameters[0].valueAsText + u"\※属性", u"3336_区間_区間.csv")
            
            # 処理が終わったものを加工済みフォルダに移動
            arcpy.env.workspace = parameters[0].valueAsText
            movementFeature = u"Z9302_道路部_P.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\加工済み\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            
            # 進捗表示
            messages.addMessage("3336_区間_区間" "の処理を終了")
        else:
            # 進捗表示
            messages.addMessage("3336_区間_区間" "必要ファイルが無いため処理をしません")
        
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        
        # 作業フォルダを変更
        arcpy.env.workspace = parameters[0].valueAsText + u"\エリア"
        
        # ■3337_区間_番号■■■■■■■■■■■■■■■■■■■■■■■■■
        # 進捗表示
        messages.addMessage("3337_区間_番号" "の処理を開始")
        
        # shpファイルが揃っている場合のみ処理を行う
        if arcpy.Exists("3336_区間_区間.shp"):
            
            outFeature = u"3337_区間_番号.shp"
            
            arcpy.env.workspace = parameters[0].valueAsText + u"\テキスト"
            arcpy.Delete_management("3337_区間_番号.shp")
            arcpy.env.workspace = parameters[0].valueAsText + u"\エリア"
            
            # unicode文字と連結するので連結する文字もunicodeにする
            OutputShape = parameters[0].valueAsText + u"\テキスト\\" + outFeature
            
            # 区間ポリゴンをポイントに変換
            arcpy.FeatureToPoint_management(u"3336_区間_区間.shp", OutputShape, "CENTROID")
            
            # 作業フォルダを変更
            arcpy.env.workspace = parameters[0].valueAsText + u"\テキスト"
            
            # フィールドを追加
            arcpy.AddField_management(outFeature, "NFONTSIZE", "LONG")
            arcpy.AddField_management(outFeature, "NLABELANGL", "LONG")
            arcpy.AddField_management(outFeature, "NSYMBOLID", "LONG")
            arcpy.AddField_management(outFeature, "SFONTNAME", "TEXT")
            arcpy.AddField_management(outFeature, "SLABEL", "TEXT")
            arcpy.AddField_management(outFeature, "kukan", "TEXT")
            
            # 不要なフィールドを削除
            arcpy.DeleteField_management(outFeature, "UserID")
            arcpy.DeleteField_management(outFeature, "ORIG_FID")
            
            # 演算
            arcpy.CalculateField_management(outFeature, "CHIBUTSU", "921200")
            arcpy.CalculateField_management(outFeature, "NFONTSIZE", "30")
            arcpy.CalculateField_management(outFeature, "NLABELANGL", "0")
            arcpy.CalculateField_management(outFeature, "NLEVEL", "500")
            arcpy.CalculateField_management(outFeature, "NSYMBOLID", "6")
            arcpy.CalculateField_management(outFeature, "SFONTNAME", "\"ＭＳ ゴシック\"")
            arcpy.CalculateField_management(outFeature, "SLABEL", "Mid( [SLINKID] , 8 , Len( [SLINKID] ) -7 )")
            arcpy.CalculateField_management(outFeature, "kukan", "[SLABEL]")
            
            # 進捗表示
            messages.addMessage("3337_区間_番号" "の処理を終了")
        else:
            # 進捗表示
            messages.addMessage("3337_区間_番号" "必要ファイルが無いため処理をしません")
        
        # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
