# 2����shp�o��.pyt
#
# �C������
# 2020/04/23 �V�K�쐬 harita
#
#

import arcpy, os

class Toolbox(object):
    def __init__(self):
        self.label =  "2����shp�o�� toolbox"
        self.alias  = "FeatureTo2D_Shp"

        # List of tool classes associated with this toolbox
        self.tools = [FeatureTo2D_Shp] 

class FeatureTo2D_Shp(object):
    def __init__(self):
        self.label       = "FeatureTo2D_Shp"
        self.description = "�t�B�[�`���N���X��3��������������������2�����f�[�^�Ƃ���shp�o�͂��܂��BZ�l��M�l�𖳌��ɂ��ďo�͂��܂��B"
        
    def getParameterInfo(self):
        #Define parameter definitions
        
        # 2�����f�[�^�ɂ������t�B�[�`���N���X
        in_feature = arcpy.Parameter(
            displayName="���̓t�B�[�`���[�N���X",
            name="in_feature",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input",
            multiValue=True)
        
        output_workspace = arcpy.Parameter(
            displayName="�o�͐�t�H���_",
            name="output_workspace",
            datatype="DEWorkspace",
            parameterType="Required",
            direction="Input")
        
        
        parameters = [in_feature, output_workspace]
        
        return parameters
        
    def execute(self, parameters, messages):
        # �i���\��
        messages.addMessage("FeatureTo2D_Shp���s��")
        
        # Z�l��M�l�𖳌��ɂ���
        arcpy.env.outputZFlag = "Disabled"
        arcpy.env.outputMFlag = "Disabled"
        
        # ���̓t�B�[�`���[�N���X�̃p�����[�^����V���O���N�H�[�e�[�V�������폜����
        multi_input_parameter = parameters[0].valueAsText.replace("'","")
        
        # ���̓t�B�[�`���[�N���X�̃p�����[�^���Z�~�R�����ŋ�؂��Ĕz��ɂ���
        Input_Features = multi_input_parameter.split(";")
        
        # �t�B�[�`���[�o��
        arcpy.FeatureClassToShapefile_conversion(Input_Features, parameters[1].valueAsText)
        
        # �i���\��
        messages.addMessage("��������")
        
