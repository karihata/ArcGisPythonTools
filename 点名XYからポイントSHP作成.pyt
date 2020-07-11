# 点名XYからポイントSHP作成.pyt
#
# 修正履歴
# 2020/03/05 新規作成 harita
#
#

import arcpy, os

class Toolbox(object):
    def __init__(self):
        self.label =  "点名XYからSHPファイルを作成 toolbox"
        self.alias  = "PointXY2SHP"

        # List of tool classes associated with this toolbox
        self.tools = [PointXY2SHP] 

class PointXY2SHP(object):
    def __init__(self):
        self.label       = "PointXY2SHP"
        self.description = "点名、X座標、Y座標の形式になっているテーブルデータからポイントSHPを作成します。\nXとYを反転させる必要はありません。\nテーブルと同じ場所にSHPファイルを作成します。\nなおArcで使えない文字がある場合は置換えるので100%同じファイル名では作成できません。"
        
    def getParameterInfo(self):
        #Define parameter definitions
        
        # CSV等の点名XYが入ったデータ
        in_feature = arcpy.Parameter(
            displayName="点名XYテーブル",
            name="in_feature",
            datatype="DETable",
            parameterType="Required",
            direction="Input")
        
        # X座標の項目
        XFieldName = arcpy.Parameter(
            displayName="X座標の項目",
            name="X",
            datatype="Field",
            parameterType="Required",
            direction="Input")
        
        # Y座標の項目
        YFieldName = arcpy.Parameter(
            displayName="Y座標の項目",
            name="Y",
            datatype="Field",
            parameterType="Required",
            direction="Input")
        
        XFieldName.parameterDependencies = [in_feature.name]
        YFieldName.parameterDependencies = [in_feature.name]
        
        parameters = [in_feature, XFieldName, YFieldName]
        
        return parameters
        
    def execute(self, parameters, messages):
        # 進捗表示
        messages.addMessage("PointXY2SHP実行中")
        
        # 一時的なレイヤ名を格納
        out_layer = arcpy.Describe(parameters[0].valueAsText).name
        
        # SHPフラグを初期化
        SHP_FLG = True
        
        # ファイルジオデータベースやMDBの場合は「.shp」にはできないのでフラグを設ける
        if os.path.dirname(parameters[0].valueAsText)[-3:] == r"gdb" \
            or os.path.dirname(parameters[0].valueAsText)[-3:] == r"mdb":
            
            SHP_FLG = False
        
        
        # 作業フォルダを変更
        arcpy.env.workspace = os.path.dirname(parameters[0].valueAsText)
        
        # 点名XYのデータからXYイベントレイヤを作成
        arcpy.MakeXYEventLayer_management(parameters[0].valueAsText, parameters[2].valueAsText, parameters[1].valueAsText, out_layer)
        
        # 出力名を格納
        out_file = os.path.dirname(parameters[0].valueAsText) + r"/" + arcpy.ValidateTableName(os.path.basename(parameters[0].valueAsText))
        
        # SHPフラグがTrueの場合、テーブルと同じフォルダにSHPを出力するようにする
        # SHPフラグがFalseの場合 ジオDBと同じフォルダにSHPを出力するようにする
        if SHP_FLG:
            out_file = os.path.dirname(parameters[0].valueAsText) + r"/" + arcpy.ValidateTableName(os.path.basename(parameters[0].valueAsText))
        else:
            out_file = os.path.dirname(os.path.dirname(parameters[0].valueAsText)) + r"/" + arcpy.ValidateTableName(os.path.basename(parameters[0].valueAsText))
        
        # ポイントSHPが既にある場合は既存のポイントSHPを削除する
        if arcpy.Exists(out_file + r".shp"):
            arcpy.Delete_management(out_file + r".shp")
        
        # ポイント出力
        arcpy.FeatureToPoint_management(out_layer, out_file + r".shp")
        
        # 不要な属性を削除
        arcpy.DeleteField_management(out_file + r".shp", ["ORIG_FID"])
        
        # ゴミファイルを削除 (拡張子がprj、sbn、sbx、shp.xmlになっているファイルを削除)
        os.remove(out_file + r".prj")
        os.remove(out_file + r".sbn")
        os.remove(out_file + r".sbx")
        os.remove(out_file + r".shp.xml")
        
        # 進捗表示
        messages.addMessage("処理完了")
        
