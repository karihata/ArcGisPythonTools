# �_��XY����|�C���gSHP�쐬.pyt
#
# �C������
# 2020/03/05 �V�K�쐬 harita
#
#

import arcpy, os

class Toolbox(object):
    def __init__(self):
        self.label =  "�_��XY����SHP�t�@�C�����쐬 toolbox"
        self.alias  = "PointXY2SHP"

        # List of tool classes associated with this toolbox
        self.tools = [PointXY2SHP] 

class PointXY2SHP(object):
    def __init__(self):
        self.label       = "PointXY2SHP"
        self.description = "�_���AX���W�AY���W�̌`���ɂȂ��Ă���e�[�u���f�[�^����|�C���gSHP���쐬���܂��B\nX��Y�𔽓]������K�v�͂���܂���B\n�e�[�u���Ɠ����ꏊ��SHP�t�@�C�����쐬���܂��B\n�Ȃ�Arc�Ŏg���Ȃ�����������ꍇ�͒u������̂�100%�����t�@�C�����ł͍쐬�ł��܂���B"
        
    def getParameterInfo(self):
        #Define parameter definitions
        
        # CSV���̓_��XY���������f�[�^
        in_feature = arcpy.Parameter(
            displayName="�_��XY�e�[�u��",
            name="in_feature",
            datatype="DETable",
            parameterType="Required",
            direction="Input")
        
        # X���W�̍���
        XFieldName = arcpy.Parameter(
            displayName="X���W�̍���",
            name="X",
            datatype="Field",
            parameterType="Required",
            direction="Input")
        
        # Y���W�̍���
        YFieldName = arcpy.Parameter(
            displayName="Y���W�̍���",
            name="Y",
            datatype="Field",
            parameterType="Required",
            direction="Input")
        
        XFieldName.parameterDependencies = [in_feature.name]
        YFieldName.parameterDependencies = [in_feature.name]
        
        parameters = [in_feature, XFieldName, YFieldName]
        
        return parameters
        
    def execute(self, parameters, messages):
        # �i���\��
        messages.addMessage("PointXY2SHP���s��")
        
        # �ꎞ�I�ȃ��C�������i�[
        out_layer = arcpy.Describe(parameters[0].valueAsText).name
        
        # SHP�t���O��������
        SHP_FLG = True
        
        # �t�@�C���W�I�f�[�^�x�[�X��MDB�̏ꍇ�́u.shp�v�ɂ͂ł��Ȃ��̂Ńt���O��݂���
        if os.path.dirname(parameters[0].valueAsText)[-3:] == r"gdb" \
            or os.path.dirname(parameters[0].valueAsText)[-3:] == r"mdb":
            
            SHP_FLG = False
        
        
        # ��ƃt�H���_��ύX
        arcpy.env.workspace = os.path.dirname(parameters[0].valueAsText)
        
        # �_��XY�̃f�[�^����XY�C�x���g���C�����쐬
        arcpy.MakeXYEventLayer_management(parameters[0].valueAsText, parameters[2].valueAsText, parameters[1].valueAsText, out_layer)
        
        # �o�͖����i�[
        out_file = os.path.dirname(parameters[0].valueAsText) + r"/" + arcpy.ValidateTableName(os.path.basename(parameters[0].valueAsText))
        
        # SHP�t���O��True�̏ꍇ�A�e�[�u���Ɠ����t�H���_��SHP���o�͂���悤�ɂ���
        # SHP�t���O��False�̏ꍇ �W�IDB�Ɠ����t�H���_��SHP���o�͂���悤�ɂ���
        if SHP_FLG:
            out_file = os.path.dirname(parameters[0].valueAsText) + r"/" + arcpy.ValidateTableName(os.path.basename(parameters[0].valueAsText))
        else:
            out_file = os.path.dirname(os.path.dirname(parameters[0].valueAsText)) + r"/" + arcpy.ValidateTableName(os.path.basename(parameters[0].valueAsText))
        
        # �|�C���gSHP�����ɂ���ꍇ�͊����̃|�C���gSHP���폜����
        if arcpy.Exists(out_file + r".shp"):
            arcpy.Delete_management(out_file + r".shp")
        
        # �|�C���g�o��
        arcpy.FeatureToPoint_management(out_layer, out_file + r".shp")
        
        # �s�v�ȑ������폜
        arcpy.DeleteField_management(out_file + r".shp", ["ORIG_FID"])
        
        # �S�~�t�@�C�����폜 (�g���q��prj�Asbn�Asbx�Ashp.xml�ɂȂ��Ă���t�@�C�����폜)
        os.remove(out_file + r".prj")
        os.remove(out_file + r".sbn")
        os.remove(out_file + r".sbx")
        os.remove(out_file + r".shp.xml")
        
        # �i���\��
        messages.addMessage("��������")
        
