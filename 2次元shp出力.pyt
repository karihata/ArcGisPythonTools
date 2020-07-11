# 2次元shp出力.pyt
#
# 修正履歴
# 2020/04/23 新規作成 harita
#
#

import arcpy, os

class Toolbox(object):
    def __init__(self):
        self.label =  "2次元shp出力 toolbox"
        self.alias  = "FeatureTo2D_Shp"

        # List of tool classes associated with this toolbox
        self.tools = [FeatureTo2D_Shp] 

class FeatureTo2D_Shp(object):
    def __init__(self):
        self.label       = "FeatureTo2D_Shp"
        self.description = "フィーチャクラスを3次元属性を引き抜いた2次元データとしてshp出力します。Z値とM値を無効にして出力します。"
        
    def getParameterInfo(self):
        #Define parameter definitions
        
        # 2次元データにしたいフィーチャクラス
        in_feature = arcpy.Parameter(
            displayName="入力フィーチャークラス",
            name="in_feature",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input",
            multiValue=True)
        
        output_workspace = arcpy.Parameter(
            displayName="出力先フォルダ",
            name="output_workspace",
            datatype="DEWorkspace",
            parameterType="Required",
            direction="Input")
        
        
        parameters = [in_feature, output_workspace]
        
        return parameters
        
    def execute(self, parameters, messages):
        # 進捗表示
        messages.addMessage("FeatureTo2D_Shp実行中")
        
        # Z値とM値を無効にする
        arcpy.env.outputZFlag = "Disabled"
        arcpy.env.outputMFlag = "Disabled"
        
        # 入力フィーチャークラスのパラメータからシングルクォーテーションを削除する
        multi_input_parameter = parameters[0].valueAsText.replace("'","")
        
        # 入力フィーチャークラスのパラメータをセミコロンで区切って配列にする
        Input_Features = multi_input_parameter.split(";")
        
        # フィーチャー出力
        arcpy.FeatureClassToShapefile_conversion(Input_Features, parameters[1].valueAsText)
        
        # 進捗表示
        messages.addMessage("処理完了")
        
