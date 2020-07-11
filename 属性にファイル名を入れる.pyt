import arcpy

class Toolbox(object):
    def __init__(self):
        self.label =  "属性にファイル名を入れる toolbox"
        self.alias  = "FileName_Cal"

        # List of tool classes associated with this toolbox
        self.tools = [FileNameCal] 

class FileNameCal(object):
    def __init__(self):
        self.label       = "FileName_Calculate"
        self.description = "FileNameというフィールドを追加してファイル名を入力します。"

    def getParameterInfo(self):
        #Define parameter definitions

        # Input Features parameter
        in_features = arcpy.Parameter(
            displayName="入力するフィーチャー",
            name="in_features",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input")
        
        # in_features.filter.list = ["Point"]
        
        # Derived Output Features parameter
        out_features = arcpy.Parameter(
            displayName="Output Features",
            name="out_features",
            datatype="GPFeatureLayer",
            parameterType="Derived",
            direction="Output")
        
        out_features.parameterDependencies = [in_features.name]
        out_features.schema.clone = True

        parameters = [in_features, out_features]
        
        return parameters

    def isLicensed(self): #optional
        return True

    def updateParameters(self, parameters): #optional
        if parameters[0].altered:
            parameters[1].value = arcpy.ValidateFieldName(parameters[1].value,
                                                          parameters[0].value)
        return

    def updateMessages(self, parameters): #optional
        return

    def execute(self, parameters, messages):
        # 処理するフィーチャーを格納
        inFeatures  = parameters[0].valueAsText
        
        desc = arcpy.Describe(inFeatures)
        # messages.addMessage(desc.name)
        
        # LayerNameをフィーチャーフィールドに追加するpyhonスクリプト
        # 一旦フィールドを削除する
        arcpy.DeleteField_management(inFeatures, ["FileName"])

        # フィールドを追加
        arcpy.AddField_management(inFeatures, "FileName", "TEXT")
        
        # 演算式を格納
        Expression = "\"" + desc.name + "\""
        Expression = Expression.replace(".shp", "")
        
        # 演算
        arcpy.CalculateField_management(inFeatures, "FileName", Expression, "PYTHON")

