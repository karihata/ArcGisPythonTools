import arcpy, os

class Toolbox(object):
    def __init__(self):
        self.label =  "アノテーションtoポイント toolbox"
        self.alias  = "AnnotationToPoint_Cal"

        # List of tool classes associated with this toolbox
        self.tools = [AnnotationToPoint] 

class AnnotationToPoint(object):
    def __init__(self):
        self.label       = "Annotation_To_Point_And_Calculate"
        self.description = "アノテーションをポイントに変換してKKCS提供用に属性を加工します。水平位置：中央、垂直位置：中央のみの処理です。"

    def getParameterInfo(self):
        #Define parameter definitions
        
        # Input Features parameter
        in_feature = arcpy.Parameter(
            displayName="変換するアノテーションフィーチャーパス",
            name="in_feature",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input")
        
        # Derived Output Features parameter
        out_features = arcpy.Parameter(
            displayName="変換後のポイントシェープファイルパス",
            name="out_features",
            datatype="DEShapefile",
            parameterType="Required",
            direction="Output")
        
        out_features.parameterDependencies = [in_feature.name]
        out_features.schema.clone = True

        parameters = [in_feature, out_features]
        
        return parameters


    def execute(self, parameters, messages):
        # 進捗表示
        messages.addMessage("アノテーションToポイント変換中")
        
        # 処理するフィーチャーを格納
        inFeature  = os.path.basename(parameters[0].valueAsText)
        
        # 出力フィーチャーパスを格納
        outFeature = parameters[1].valueAsText
        
        # 作業フォルダを変更
        arcpy.env.workspace = os.path.dirname(parameters[0].valueAsText)
        
        # アノテーションをポイントに変換
        arcpy.FeatureToPoint_management(inFeature, outFeature)
        
        # 進捗表示
        messages.addMessage("不要属性削除中")
        
        # 作業フォルダを変更
        arcpy.env.workspace = os.path.dirname(parameters[1].valueAsText)
        
        # 不要なフィールド削除中
        arcpy.DeleteField_management(outFeature,
        [
            "Annotation",
            "FeatureID",
            "ORIG_FID",
            "SHAPE_Area",
            "SHAPE_Leng",
            "Status",
            "SymbolID",
            "ZOrder"
        ])
        
        # 進捗表示
        messages.addMessage("処理完了")
        
