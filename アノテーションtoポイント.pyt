import arcpy, os

class Toolbox(object):
    def __init__(self):
        self.label =  "�A�m�e�[�V����to�|�C���g toolbox"
        self.alias  = "AnnotationToPoint_Cal"

        # List of tool classes associated with this toolbox
        self.tools = [AnnotationToPoint] 

class AnnotationToPoint(object):
    def __init__(self):
        self.label       = "Annotation_To_Point_And_Calculate"
        self.description = "�A�m�e�[�V�������|�C���g�ɕϊ�����KKCS�񋟗p�ɑ��������H���܂��B�����ʒu�F�����A�����ʒu�F�����݂̂̏����ł��B"

    def getParameterInfo(self):
        #Define parameter definitions
        
        # Input Features parameter
        in_feature = arcpy.Parameter(
            displayName="�ϊ�����A�m�e�[�V�����t�B�[�`���[�p�X",
            name="in_feature",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input")
        
        # Derived Output Features parameter
        out_features = arcpy.Parameter(
            displayName="�ϊ���̃|�C���g�V�F�[�v�t�@�C���p�X",
            name="out_features",
            datatype="DEShapefile",
            parameterType="Required",
            direction="Output")
        
        out_features.parameterDependencies = [in_feature.name]
        out_features.schema.clone = True

        parameters = [in_feature, out_features]
        
        return parameters


    def execute(self, parameters, messages):
        # �i���\��
        messages.addMessage("�A�m�e�[�V����To�|�C���g�ϊ���")
        
        # ��������t�B�[�`���[���i�[
        inFeature  = os.path.basename(parameters[0].valueAsText)
        
        # �o�̓t�B�[�`���[�p�X���i�[
        outFeature = parameters[1].valueAsText
        
        # ��ƃt�H���_��ύX
        arcpy.env.workspace = os.path.dirname(parameters[0].valueAsText)
        
        # �A�m�e�[�V�������|�C���g�ɕϊ�
        arcpy.FeatureToPoint_management(inFeature, outFeature)
        
        # �i���\��
        messages.addMessage("�s�v�����폜��")
        
        # ��ƃt�H���_��ύX
        arcpy.env.workspace = os.path.dirname(parameters[1].valueAsText)
        
        # �s�v�ȃt�B�[���h�폜��
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
        
        # �i���\��
        messages.addMessage("��������")
        
