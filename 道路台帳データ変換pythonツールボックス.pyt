import arcpy
import csv

class Toolbox(object):
    def __init__(self):
        # List of tool classes associated with this toolbox
        self.tools = [FunabashiDoroMergeCalculate] 

class FunabashiDoroMergeCalculate(object):
    def __init__(self):
        self.label       = "Funabashi_Merge_And_Calculate_To_Doro_Daicho_Data"
        self.description = "�D���s���H�䒠�f�[�^��MQX�ϊ��ɑΉ����邽�߂̃}�[�W�Ɖ��Z�����܂��B"

    def getParameterInfo(self):
        #Define parameter definitions

        # Input Features parameter
        in_features_path = arcpy.Parameter(
            displayName="�i�[��t�H���_�p�X",
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
        
        # ��ƃt�H���_��ύX
        arcpy.env.workspace = parameters[0].valueAsText
        
        # ��3320_�N�I�__�N�I�_����������������������������������������������������������
        # �i���\��
        messages.addMessage("3320_�N�I�__�N�I�_" "�̏������J�n")
        
        CodeBlock = """def CodeCalc(CHIBUTSU):
    if CHIBUTSU == 910400:
        return 124
    elif CHIBUTSU == 910500:
        return 125
    else:
        return 0"""
        
        # shp�t�@�C���������Ă���ꍇ�̂ݏ������s��
        if arcpy.Exists("D9104_�N�_�L��_S.shp") and arcpy.Exists("D9105_�I�_�L��_S.shp"):
            outFeature = u"3320_�N�I�__�N�I�_.shp"
            
            arcpy.env.workspace = parameters[0].valueAsText + u"\�|�C���g"
            arcpy.Delete_management("3320_�N�I�__�N�I�_.shp")
            arcpy.env.workspace = parameters[0].valueAsText
            
            # unicode�����ƘA������̂ŘA�����镶����unicode�ɂ���
            OutputShape = parameters[0].valueAsText + u"\�|�C���g\\" + outFeature
            
            
            # �}�[�W���s
            arcpy.Merge_management(
            ["D9104_�N�_�L��_S.shp",
            "D9105_�I�_�L��_S.shp"],
            OutputShape)
            
            # ��ƃt�H���_��ύX
            arcpy.env.workspace = parameters[0].valueAsText + u"\�|�C���g"
            
            # �t�B�[���h��ǉ�
            arcpy.AddField_management(outFeature, "CODE", "LONG")
            
            # ���Z�����i�[
            Expression = "CodeCalc(!CHIBUTSU!)"
            
            
            # ���Z
            arcpy.CalculateField_management(outFeature, "CODE", Expression, "PYTHON", CodeBlock)
            
            # �������I��������̂����H�ς݃t�H���_�Ɉړ�
            arcpy.env.workspace = parameters[0].valueAsText
            movementFeature = u"D9104_�N�_�L��_S.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\���H�ς�\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            movementFeature = u"D9105_�I�_�L��_S.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\���H�ς�\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            
            # �i���\��
            messages.addMessage("3320_�N�I�__�N�I�_" "�̏������I��")
        else:
            # �i���\��
            messages.addMessage("3320_�N�I�__�N�I�_" "�K�v�t�@�C�����������ߏ��������܂���")
        
        # ������������������������������������������������������������������
        
        
        # ��ƃt�H���_��ύX
        arcpy.env.workspace = parameters[0].valueAsText
        
        # ��3333_����_�l����������������������������������������������������������
        # �i���\��
        messages.addMessage("3333_����_�l" "�̏������J�n")
        
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
        
        # shp�t�@�C���������Ă���ꍇ�̂ݏ������s��
        if arcpy.Exists("D9111_���H�������l_T.shp") and arcpy.Exists("D9111_�����������l_T.shp") and arcpy.Exists("D9111_�K�i�������l_T.shp") and arcpy.Exists("D9111_�ԓ��������l_T.shp") and arcpy.Exists("D9111_���������ѕ����l_T.shp"):
        
            outFeature = u"3333_����_�l.shp"
            
            arcpy.env.workspace = parameters[0].valueAsText + u"\�e�L�X�g"
            arcpy.Delete_management("3333_����_�l.shp")
            arcpy.env.workspace = parameters[0].valueAsText
            
            # unicode�����ƘA������̂ŘA�����镶����unicode�ɂ���
            OutputShape = parameters[0].valueAsText + u"\�e�L�X�g\\" + outFeature
            
            # �}�[�W���s
            arcpy.Merge_management(
            ["D9111_���H�������l_T.shp",
            "D9111_�����������l_T.shp",
            "D9111_�K�i�������l_T.shp",
            "D9111_�ԓ��������l_T.shp",
            "D9111_���������ѕ����l_T.shp"],
            OutputShape)
            
            # ��ƃt�H���_��ύX
            arcpy.env.workspace = parameters[0].valueAsText + u"\�e�L�X�g"
            
            # �t�B�[���h��ǉ�
            arcpy.AddField_management(outFeature, "CODE", "LONG")
            
            # ���Z�����i�[
            Expression = "CodeCalc(!CHIBUTSU!)"
            
            # ���Z
            arcpy.CalculateField_management(outFeature, "CODE", Expression, "PYTHON", CodeBlock)
            
            # �������I��������̂����H�ς݃t�H���_�Ɉړ�
            arcpy.env.workspace = parameters[0].valueAsText
            movementFeature = u"D9111_���H�������l_T.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\���H�ς�\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            movementFeature = u"D9111_�����������l_T.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\���H�ς�\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            movementFeature = u"D9111_�K�i�������l_T.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\���H�ς�\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            movementFeature = u"D9111_�ԓ��������l_T.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\���H�ς�\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            movementFeature = u"D9111_���������ѕ����l_T.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\���H�ς�\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            
            
            # �i���\��
            messages.addMessage("3333_����_�l" "�̏������I��")
        else:
            # �i���\��
            messages.addMessage("3333_����_�l" "�K�v�t�@�C�����������ߏ��������܂���")
        
        
        # ������������������������������������������������������������������
        
        # ��ƃt�H���_��ύX
        arcpy.env.workspace = parameters[0].valueAsText
        
        # ��3331_����_������������������������������������������������������������
        # �i���\��
        messages.addMessage("3331_����_��" "�̏������J�n")
        
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
        
        
        # shp�t�@�C���������Ă���ꍇ�̂ݏ������s��
        if arcpy.Exists("D9112_������������_L.shp") and arcpy.Exists("D9112_�K�i��������_L.shp") and arcpy.Exists("D9112_�ԓ���������_L.shp") and arcpy.Exists("D9112_���������ѕ�����_L.shp") and arcpy.Exists("D9112_���H��������_L.shp"):
            
            outFeature = u"3331_����_��.shp"
            
            arcpy.env.workspace = parameters[0].valueAsText + u"\���C��"
            arcpy.Delete_management("3331_����_��.shp")
            arcpy.env.workspace = parameters[0].valueAsText
            
            # unicode�����ƘA������̂ŘA�����镶����unicode�ɂ���
            OutputShape = parameters[0].valueAsText + u"\���C��\\" + outFeature
            
            # �}�[�W���s
            arcpy.Merge_management(
            ["D9112_������������_L.shp",
             "D9112_�K�i��������_L.shp",
             "D9112_�ԓ���������_L.shp",
             "D9112_���������ѕ�����_L.shp",
             "D9112_���H��������_L.shp"],
            OutputShape)
            
            # ��ƃt�H���_��ύX
            arcpy.env.workspace = parameters[0].valueAsText + u"\���C��"
            
            # �t�B�[���h��ǉ�
            arcpy.AddField_management(outFeature, "CODE", "LONG")
            
            # ���Z�����i�[
            Expression = "CodeCalc(!CHIBUTSU!)"
            
            # ���Z
            arcpy.CalculateField_management(outFeature, "CODE", Expression, "PYTHON", CodeBlock)
            
            # �������I��������̂����H�ς݃t�H���_�Ɉړ�
            arcpy.env.workspace = parameters[0].valueAsText
            movementFeature = u"D9112_������������_L.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\���H�ς�\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            movementFeature = u"D9112_�K�i��������_L.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\���H�ς�\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            movementFeature = u"D9112_�ԓ���������_L.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\���H�ς�\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            movementFeature = u"D9112_���������ѕ�����_L.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\���H�ς�\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            movementFeature = u"D9112_���H��������_L.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\���H�ς�\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            
            # �i���\��
            messages.addMessage("3331_����_��" "�̏������I��")
        else:
            # �i���\��
            messages.addMessage("3331_����_��" "�K�v�t�@�C�����������ߏ��������܂���")
        
        
        # ������������������������������������������������������������������
        
        # ��ƃt�H���_��ύX
        arcpy.env.workspace = parameters[0].valueAsText
        
        # ��3304_���a_���a������������������������������������������������������
        # �i���\��
        messages.addMessage("3304_���a_���a" "�̏������J�n")
        
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
        
        # shp�t�@�C���������Ă���ꍇ�̂ݏ������s��
        if arcpy.Exists("D9131_���a���C��_L.shp"):
        
            outFeature = u"3304_���a_���a.shp"
            
            arcpy.env.workspace = parameters[0].valueAsText + u"\���C��"
            arcpy.Delete_management("3304_���a_���a.shp")
            arcpy.env.workspace = parameters[0].valueAsText
            
            # unicode�����ƘA������̂ŘA�����镶����unicode�ɂ���
            OutputShape = parameters[0].valueAsText + u"\���C��\\" + outFeature
            
            # �R�s�[���s
            arcpy.Copy_management("D9131_���a���C��_L.shp", OutputShape)
            
            # ��ƃt�H���_��ύX
            arcpy.env.workspace = parameters[0].valueAsText + u"\���C��"
            
            # �t�B�[���h��ǉ�
            arcpy.AddField_management(outFeature, "CODE", "LONG")
            
            # ���Z�����i�[
            Expression = "CodeCalc(!CHIBUTSU!)"
            
            # ���Z
            arcpy.CalculateField_management(outFeature, "CODE", Expression, "PYTHON", CodeBlock)
            
            # �������I��������̂����H�ς݃t�H���_�Ɉړ�
            arcpy.env.workspace = parameters[0].valueAsText
            movementFeature = u"D9131_���a���C��_L.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\���H�ς�\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            
            # �i���\��
            messages.addMessage("3304_���a_���a" "�̏������I��")
        else:
            # �i���\��
            messages.addMessage("3304_���a_���a" "�K�v�t�@�C�����������ߏ��������܂���")
        
        
        # ������������������������������������������������������������������
        
        # ��ƃt�H���_��ύX
        arcpy.env.workspace = parameters[0].valueAsText
        
        # ��3306_�h���_�h��򁡁���������������������������������������������������
        # �i���\��
        messages.addMessage("3306_�h���_�h���" "�̏������J�n")
        
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
        
        # shp�t�@�C���������Ă���ꍇ�̂ݏ������s��
        if arcpy.Exists("D9133_�h��򃉃C��_L.shp"):
        
            outFeature = u"3306_�h���_�h���.shp"
            
            arcpy.env.workspace = parameters[0].valueAsText + u"\���C��"
            arcpy.Delete_management("3306_�h���_�h���.shp")
            arcpy.env.workspace = parameters[0].valueAsText
            
            # unicode�����ƘA������̂ŘA�����镶����unicode�ɂ���
            OutputShape = parameters[0].valueAsText + u"\���C��\\" + outFeature
            
            # �R�s�[���s
            arcpy.Copy_management("D9133_�h��򃉃C��_L.shp", OutputShape)
            
            # ��ƃt�H���_��ύX
            arcpy.env.workspace = parameters[0].valueAsText + u"\���C��"
            
            # �t�B�[���h��ǉ�
            arcpy.AddField_management(outFeature, "CODE", "LONG")
            
            # ���Z�����i�[
            Expression = "CodeCalc(!CHIBUTSU!)"
            
            # ���Z
            arcpy.CalculateField_management(outFeature, "CODE", Expression, "PYTHON", CodeBlock)
            
            # �������I��������̂����H�ς݃t�H���_�Ɉړ�
            arcpy.env.workspace = parameters[0].valueAsText
            movementFeature = u"D9133_�h��򃉃C��_L.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\���H�ς�\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            
            # �i���\��
            messages.addMessage("3306_�h���_�h���" "�̏������I��")
        else:
            # �i���\��
            messages.addMessage("3306_�h���_�h���" "�K�v�t�@�C�����������ߏ��������܂���")
        
        # ������������������������������������������������������������������
        
        # ��ƃt�H���_��ύX
        arcpy.env.workspace = parameters[0].valueAsText
        
        # ��3344_����_���L����������������������������������������������������������
        # �i���\��
        messages.addMessage("3344_����_���L" "�̏������J�n")
        
        # shp�t�@�C���������Ă���ꍇ�̂ݏ������s��
        if arcpy.Exists("D9141_�������@_T.shp") and arcpy.Exists("D9141_�����ԍ�_T.shp") and arcpy.Exists("D9141_��������_T.shp"):
            outFeature = u"3344_����_���L.shp"
            
            # unicode�����ƘA������̂ŘA�����镶����unicode�ɂ���
            OutputShape = parameters[0].valueAsText + u"\�e�L�X�g\\" + outFeature
            
            arcpy.env.workspace = parameters[0].valueAsText + u"\�e�L�X�g"
            arcpy.Delete_management("3344_����_���L.shp")
            arcpy.env.workspace = parameters[0].valueAsText
            
            # �}�[�W���s
            arcpy.Merge_management(
            ["D9141_�������@_T.shp",
             "D9141_�����ԍ�_T.shp",
             "D9141_��������_T.shp"],
            OutputShape)
            
            # �������I��������̂����H�ς݃t�H���_�Ɉړ�
            arcpy.env.workspace = parameters[0].valueAsText
            movementFeature = u"D9141_�������@_T.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\���H�ς�\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            movementFeature = u"D9141_�����ԍ�_T.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\���H�ς�\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            movementFeature = u"D9141_��������_T.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\���H�ς�\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            
            # �i���\��
            messages.addMessage("3344_����_���L" "�̏������I��")
        else:
            # �i���\��
            messages.addMessage("3344_����_���L" "�K�v�t�@�C�����������ߏ��������܂���")
        
        # ������������������������������������������������������������������
        
        # ��3347_�S������_���L����������������������������������������������������������
        # �i���\��
        messages.addMessage("3347_�S������_���L" "�̏������J�n")
        
        # shp�t�@�C���������Ă���ꍇ�̂ݏ������s��
        if arcpy.Exists("D9142_�S���������@_T.shp") and arcpy.Exists("D9142_�S�������ԍ�_T.shp") and arcpy.Exists("D9142_�S����������_T.shp"):
            
            outFeature = u"3347_�S������_���L.shp"
            
            arcpy.env.workspace = parameters[0].valueAsText + u"\�e�L�X�g"
            arcpy.Delete_management("3347_�S������_���L.shp")
            arcpy.env.workspace = parameters[0].valueAsText
            
            # unicode�����ƘA������̂ŘA�����镶����unicode�ɂ���
            OutputShape = parameters[0].valueAsText + u"\�e�L�X�g\\" + outFeature
            
            # �}�[�W���s
            arcpy.Merge_management(
            ["D9142_�S���������@_T.shp",
             "D9142_�S�������ԍ�_T.shp",
             "D9142_�S����������_T.shp"],
            OutputShape)
            
            # �������I��������̂����H�ς݃t�H���_�Ɉړ�
            arcpy.env.workspace = parameters[0].valueAsText
            movementFeature = u"D9142_�S���������@_T.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\���H�ς�\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            movementFeature = u"D9142_�S�������ԍ�_T.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\���H�ς�\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            movementFeature = u"D9142_�S����������_T.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\���H�ς�\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            
            # �i���\��
            messages.addMessage("3347_�S������_���L" "�̏������I��")
        else:
            # �i���\��
            messages.addMessage("3347_�S������_���L" "�K�v�t�@�C�����������ߏ��������܂���")
        
        # ������������������������������������������������������������������
        
        # ��3335_�����v����_�����v��������������������������������������������������������������
        # �i���\��
        messages.addMessage("3335_�����v����_�����v����" "�̏������J�n")
        
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
        
        # shp�t�@�C���������Ă���ꍇ�̂ݏ������s��
        if arcpy.Exists("Z9321_���H���S���i�����j_L.shp") and arcpy.Exists("Z9321_���H���S���i�S�������j_L.shp") and arcpy.Exists("Z9321_���H���S��_L.shp") and arcpy.Exists("Z9321_���H���S���d�p����_L.shp") and arcpy.Exists("Z9321_���H���S��������_L.shp") and arcpy.Exists("Z9321_���H���S�������p_L.shp"):
            
            outFeature = u"3335_�����v����_�����v����.shp"
            
            arcpy.env.workspace = parameters[0].valueAsText + u"\���C��"
            arcpy.Delete_management("3335_�����v����_�����v����.shp")
            arcpy.env.workspace = parameters[0].valueAsText
            
            # unicode�����ƘA������̂ŘA�����镶����unicode�ɂ���
            OutputShape = parameters[0].valueAsText + u"\���C��\\" + outFeature
            
            # �}�[�W���s
            arcpy.Merge_management(
            ["Z9321_���H���S���i�����j_L.shp",
             "Z9321_���H���S���i�S�������j_L.shp",
             "Z9321_���H���S��_L.shp",
             "Z9321_���H���S���d�p����_L.shp",
             "Z9321_���H���S��������_L.shp",
             "Z9321_���H���S�������p_L.shp"],
            OutputShape)
            
            # ��ƃt�H���_��ύX
            arcpy.env.workspace = parameters[0].valueAsText + u"\���C��"
            
            # �t�B�[���h��ǉ�
            arcpy.AddField_management(outFeature, "CODE", "LONG")
            
            # ���Z�����i�[
            Expression = "CodeCalc(!CHIBUTSU!)"
            
            # ���Z
            arcpy.CalculateField_management(outFeature, "CODE", Expression, "PYTHON", CodeBlock)
            
            # �������I��������̂����H�ς݃t�H���_�Ɉړ�
            arcpy.env.workspace = parameters[0].valueAsText
            movementFeature = u"Z9321_���H���S���i�����j_L.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\���H�ς�\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            movementFeature = u"Z9321_���H���S���i�S�������j_L.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\���H�ς�\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            movementFeature = u"Z9321_���H���S��_L.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\���H�ς�\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            movementFeature = u"Z9321_���H���S���d�p����_L.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\���H�ς�\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            movementFeature = u"Z9321_���H���S��������_L.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\���H�ς�\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            movementFeature = u"Z9321_���H���S�������p_L.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\���H�ς�\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            
            # �i���\��
            messages.addMessage("3335_�����v����_�����v����" "�̏������I��")
        else:
            # �i���\��
            messages.addMessage("3335_�����v����_�����v����" "�K�v�t�@�C�����������ߏ��������܂���")
        
        # ������������������������������������������������������������������
        
        # ��ƃt�H���_��ύX
        arcpy.env.workspace = parameters[0].valueAsText
        
        # ��3318_����_������������������������������������������������������������
        # �i���\��
        messages.addMessage("3318_����_��" "�̏������J�n")
        
        CodeBlock = """def CodeCalc(CHIBUTSU):
    if CHIBUTSU == 935200:
        return 170
    elif CHIBUTSU == 935300:
        return 176
    elif CHIBUTSU == 935301:
        return 176
    else:
        return 0"""
        
        # shp�t�@�C���������Ă���ꍇ�̂ݏ������s��
        if arcpy.Exists("Z9352_�������C��_L.shp") and arcpy.Exists("Z9353_���������C��_L.shp"):
            
            outFeature = u"3318_����_��.shp"
            
            arcpy.env.workspace = parameters[0].valueAsText + u"\���C��"
            arcpy.Delete_management("3318_����_��.shp")
            arcpy.env.workspace = parameters[0].valueAsText
            
            # unicode�����ƘA������̂ŘA�����镶����unicode�ɂ���
            OutputShape = parameters[0].valueAsText + u"\���C��\\" + outFeature
            
            # �}�[�W���s
            arcpy.Merge_management(
            ["Z9352_�������C��_L.shp",
             "Z9353_���������C��_L.shp"],
            OutputShape)
            
            # ��ƃt�H���_��ύX
            arcpy.env.workspace = parameters[0].valueAsText + u"\���C��"
            
            # �t�B�[���h��ǉ�
            arcpy.AddField_management(outFeature, "CODE", "LONG")
            # ���Z�����i�[
            Expression = "CodeCalc(!CHIBUTSU!)"
            
            # ���Z
            arcpy.CalculateField_management(outFeature, "CODE", Expression, "PYTHON", CodeBlock)
            
            # �������I��������̂����H�ς݃t�H���_�Ɉړ�
            arcpy.env.workspace = parameters[0].valueAsText
            movementFeature = u"Z9352_�������C��_L.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\���H�ς�\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            movementFeature = u"Z9353_���������C��_L.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\���H�ς�\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            
            # �i���\��
            messages.addMessage("3318_����_��" "�̏������I��")
        else:
            # �i���\��
            messages.addMessage("3318_����_��" "�K�v�t�@�C�����������ߏ��������܂���")
        
        
        # ������������������������������������������������������������������
        
        # ��ƃt�H���_��ύX
        arcpy.env.workspace = parameters[0].valueAsText
        
        
        # ��3301_���H_���H������������������������������������������������������
        # �i���\��
        messages.addMessage("3301_���H_���H" "�̏������J�n")
        
        CodeBlock = """def CodeCalc(CHIBUTSU):
    if CHIBUTSU == 935100:
        return 120
    elif CHIBUTSU == 935108:
        return 1123
    else:
        return 0"""
        
        # shp�t�@�C���������Ă���ꍇ�̂ݏ������s��
        if arcpy.Exists("Z9351_���H��_L.shp"):
            
            outFeature = u"3301_���H_���H.shp"
            
            arcpy.env.workspace = parameters[0].valueAsText + u"\���C��"
            arcpy.Delete_management("3301_���H_���H.shp")
            arcpy.env.workspace = parameters[0].valueAsText
            
            # unicode�����ƘA������̂ŘA�����镶����unicode�ɂ���
            OutputShape = parameters[0].valueAsText + u"\���C��\\" + outFeature
            
            # �R�s�[���s
            arcpy.Copy_management("Z9351_���H��_L.shp", OutputShape)
            
            # ��ƃt�H���_��ύX
            arcpy.env.workspace = parameters[0].valueAsText + u"\���C��"
            
            # �t�B�[���h��ǉ�
            arcpy.AddField_management(outFeature, "CODE", "LONG")
            # ���Z�����i�[
            Expression = "CodeCalc(!CHIBUTSU!)"
            
            # ���Z
            arcpy.CalculateField_management(outFeature, "CODE", Expression, "PYTHON", CodeBlock)
            
            # �������I��������̂����H�ς݃t�H���_�Ɉړ�
            arcpy.env.workspace = parameters[0].valueAsText
            movementFeature = u"Z9351_���H��_L.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\���H�ς�\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            
            # �i���\��
            messages.addMessage("3301_���H_���H" "�̏������I��")
        else:
            # �i���\��
            messages.addMessage("3301_���H_���H" "�K�v�t�@�C�����������ߏ��������܂���")
        
        # ������������������������������������������������������������������
        
        # ��ƃt�H���_��ύX
        arcpy.env.workspace = parameters[0].valueAsText
        
        # ��3336_���_��ԁ�����������������������������������������������������
        # �i���\��
        messages.addMessage("3336_���_���" "�̏������J�n")
        
        # shp�t�@�C���������Ă���ꍇ�̂ݏ������s��
        if arcpy.Exists("Z9302_���H��_P.shp"):
            
            outFeature = u"3336_���_���.shp"
            
            arcpy.env.workspace = parameters[0].valueAsText + u"\�G���A"
            arcpy.Delete_management("3336_���_���.shp")
            arcpy.env.workspace = parameters[0].valueAsText
            
            arcpy.env.workspace = parameters[0].valueAsText + u"\������"
            arcpy.Delete_management("3336_���_���.csv")
            arcpy.env.workspace = parameters[0].valueAsText
            
            # unicode�����ƘA������̂ŘA�����镶����unicode�ɂ���
            OutputShape = parameters[0].valueAsText + u"\�G���A\\" + outFeature
            
            # �R�s�[���s
            arcpy.Copy_management("Z9302_���H��_P.shp", OutputShape)
            
            # ��ƃt�H���_��ύX
            arcpy.env.workspace = parameters[0].valueAsText + u"\�G���A"
            
            # �t�B�[���h��ǉ�
            arcpy.AddField_management(outFeature, "UserID", "LONG")
            
            # ���Z�����i�[
            Expression = "[FID] + 1"
            
            # ���Z
            arcpy.CalculateField_management(outFeature, "UserID", Expression)
            
            # SLINKID��UserID��CSV�ŏo�͂���
            arcpy.TableToTable_conversion(u"3336_���_���.dbf", parameters[0].valueAsText + u"\������", u"3336_���_���.csv")
            
            # �������I��������̂����H�ς݃t�H���_�Ɉړ�
            arcpy.env.workspace = parameters[0].valueAsText
            movementFeature = u"Z9302_���H��_P.shp"
            arcpy.Copy_management(movementFeature, parameters[0].valueAsText + u"\���H�ς�\\" + movementFeature)
            arcpy.Delete_management(movementFeature)
            
            # �i���\��
            messages.addMessage("3336_���_���" "�̏������I��")
        else:
            # �i���\��
            messages.addMessage("3336_���_���" "�K�v�t�@�C�����������ߏ��������܂���")
        
        # ������������������������������������������������������������������
        
        # ��ƃt�H���_��ύX
        arcpy.env.workspace = parameters[0].valueAsText + u"\�G���A"
        
        # ��3337_���_�ԍ���������������������������������������������������
        # �i���\��
        messages.addMessage("3337_���_�ԍ�" "�̏������J�n")
        
        # shp�t�@�C���������Ă���ꍇ�̂ݏ������s��
        if arcpy.Exists("3336_���_���.shp"):
            
            outFeature = u"3337_���_�ԍ�.shp"
            
            arcpy.env.workspace = parameters[0].valueAsText + u"\�e�L�X�g"
            arcpy.Delete_management("3337_���_�ԍ�.shp")
            arcpy.env.workspace = parameters[0].valueAsText + u"\�G���A"
            
            # unicode�����ƘA������̂ŘA�����镶����unicode�ɂ���
            OutputShape = parameters[0].valueAsText + u"\�e�L�X�g\\" + outFeature
            
            # ��ԃ|���S�����|�C���g�ɕϊ�
            arcpy.FeatureToPoint_management(u"3336_���_���.shp", OutputShape, "CENTROID")
            
            # ��ƃt�H���_��ύX
            arcpy.env.workspace = parameters[0].valueAsText + u"\�e�L�X�g"
            
            # �t�B�[���h��ǉ�
            arcpy.AddField_management(outFeature, "NFONTSIZE", "LONG")
            arcpy.AddField_management(outFeature, "NLABELANGL", "LONG")
            arcpy.AddField_management(outFeature, "NSYMBOLID", "LONG")
            arcpy.AddField_management(outFeature, "SFONTNAME", "TEXT")
            arcpy.AddField_management(outFeature, "SLABEL", "TEXT")
            arcpy.AddField_management(outFeature, "kukan", "TEXT")
            
            # �s�v�ȃt�B�[���h���폜
            arcpy.DeleteField_management(outFeature, "UserID")
            arcpy.DeleteField_management(outFeature, "ORIG_FID")
            
            # ���Z
            arcpy.CalculateField_management(outFeature, "CHIBUTSU", "921200")
            arcpy.CalculateField_management(outFeature, "NFONTSIZE", "30")
            arcpy.CalculateField_management(outFeature, "NLABELANGL", "0")
            arcpy.CalculateField_management(outFeature, "NLEVEL", "500")
            arcpy.CalculateField_management(outFeature, "NSYMBOLID", "6")
            arcpy.CalculateField_management(outFeature, "SFONTNAME", "\"�l�r �S�V�b�N\"")
            arcpy.CalculateField_management(outFeature, "SLABEL", "Mid( [SLINKID] , 8 , Len( [SLINKID] ) -7 )")
            arcpy.CalculateField_management(outFeature, "kukan", "[SLABEL]")
            
            # �i���\��
            messages.addMessage("3337_���_�ԍ�" "�̏������I��")
        else:
            # �i���\��
            messages.addMessage("3337_���_�ԍ�" "�K�v�t�@�C�����������ߏ��������܂���")
        
        # ������������������������������������������������������������������
