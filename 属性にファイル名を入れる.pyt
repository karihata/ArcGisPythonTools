import arcpy

class Toolbox(object):
    def __init__(self):
        self.label =  "�����Ƀt�@�C���������� toolbox"
        self.alias  = "FileName_Cal"

        # List of tool classes associated with this toolbox
        self.tools = [FileNameCal] 

class FileNameCal(object):
    def __init__(self):
        self.label       = "FileName_Calculate"
        self.description = "FileName�Ƃ����t�B�[���h��ǉ����ăt�@�C��������͂��܂��B"

    def getParameterInfo(self):
        #Define parameter definitions

        # Input Features parameter
        in_features = arcpy.Parameter(
            displayName="���͂���t�B�[�`���[",
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
        # ��������t�B�[�`���[���i�[
        inFeatures  = parameters[0].valueAsText
        
        desc = arcpy.Describe(inFeatures)
        # messages.addMessage(desc.name)
        
        # LayerName���t�B�[�`���[�t�B�[���h�ɒǉ�����pyhon�X�N���v�g
        # ��U�t�B�[���h���폜����
        arcpy.DeleteField_management(inFeatures, ["FileName"])

        # �t�B�[���h��ǉ�
        arcpy.AddField_management(inFeatures, "FileName", "TEXT")
        
        # ���Z�����i�[
        Expression = "\"" + desc.name + "\""
        Expression = Expression.replace(".shp", "")
        
        # ���Z
        arcpy.CalculateField_management(inFeatures, "FileName", Expression, "PYTHON")

