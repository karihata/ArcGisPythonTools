import arcpy

class Toolbox(object):
    def __init__(self):
        self.label =  "Len,MLen,PLenAno付与 toolbox"
        self.alias  = "PLenAno_Field_Add"

        # List of tool classes associated with this toolbox
        self.tools = [CalculatePLenAno] 

class CalculatePLenAno(object):
    def __init__(self):
        self.label       = "Add_Calculate_Len_MLen_PLenAno"
        self.description = "Len,MLen,PLenAnoのフィールドを追加・演算をします。"

    def getParameterInfo(self):
        #Define parameter definitions

        # Input Features parameter
        in_features = arcpy.Parameter(
            displayName="付与するラインフィーチャー",
            name="in_features",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input")
        
        in_features.filter.list = ["Polyline"]
        
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
        
        # Len、MLen、PLenAnoをフィーチャーフィールドに追加するpyhonスクリプト
        # 一旦フィールドを削除する
        arcpy.DeleteField_management(inFeatures, ["Len", "MLen", "PLenAno"])

        # フィールドを追加
        arcpy.AddField_management(inFeatures, "Len", "DOUBLE")
        arcpy.AddField_management(inFeatures, "MLen", "TEXT")
        arcpy.AddField_management(inFeatures, "PLenAno", "TEXT")

        # 演算式を格納
        LenExpression = "!shape.length@meters!"
        MLenExpression = "'{:.3f}'.format( math.floor((math.ceil( !Len! *1000)/1000) *1000)/1000)"
        PLenAnoExpression = "'{:.2f}'.format( math.floor( !Len! *100)/100 )"

        # 演算
        arcpy.CalculateField_management(inFeatures, "Len", LenExpression, "PYTHON")
        arcpy.CalculateField_management(inFeatures, "MLen", MLenExpression, "PYTHON")
        arcpy.CalculateField_management(inFeatures, "PLenAno", PLenAnoExpression, "PYTHON")


