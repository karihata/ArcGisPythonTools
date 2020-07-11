# -*- coding: utf-8 -*-
import arcpy, csv, os, sys, subprocess

CurrentPath = os.getcwd()

# ��ƃt�H���_��ύX
arcpy.env.workspace = CurrentPath
print("���������J�n���܂��B������������������������������������������")

# ��3320_�N�I�__�N�I�_����������������������������������������������������������
# �i���\��
print("3320_�N�I�__�N�I�_" "�̏������J�n")

CodeBlock = """def CodeCalc(CHIBUTSU):
    if CHIBUTSU == 910400:
        return 124
    elif CHIBUTSU == 910500:
        return 125
    else:
        return 0"""

# shp�t�@�C���������Ă���ꍇ�̂ݏ������s��
if arcpy.Exists("D9104_�N�_�L��_S.shp") and arcpy.Exists("D9105_�I�_�L��_S.shp"):
    outFeature = "3320_�N�I�__�N�I�_.shp"
    
    arcpy.env.workspace = CurrentPath + "\�|�C���g"
    arcpy.Delete_management("3320_�N�I�__�N�I�_.shp")
    arcpy.env.workspace = CurrentPath
    
    # unicode�����ƘA������̂ŘA�����镶����unicode�ɂ���
    OutputShape = CurrentPath + "\�|�C���g\\" + outFeature
    
    
    # �}�[�W���s
    arcpy.Merge_management(
    ["D9104_�N�_�L��_S.shp",
    "D9105_�I�_�L��_S.shp"],
    OutputShape)
    
    # ��ƃt�H���_��ύX
    arcpy.env.workspace = CurrentPath + "\�|�C���g"
    
    # �t�B�[���h��ǉ�
    arcpy.AddField_management(outFeature, "CODE", "LONG")
    
    # ���Z�����i�[
    Expression = "CodeCalc(!CHIBUTSU!)"
    
    
    # ���Z
    arcpy.CalculateField_management(outFeature, "CODE", Expression, "PYTHON", CodeBlock)
    
    # �������I��������̂����H�ς݃t�H���_�Ɉړ�
    arcpy.env.workspace = CurrentPath
    movementFeature = "D9104_�N�_�L��_S.shp"
    arcpy.Copy_management(movementFeature, CurrentPath + "\���H�ς�\\" + movementFeature)
    arcpy.Delete_management(movementFeature)
    movementFeature = "D9105_�I�_�L��_S.shp"
    arcpy.Copy_management(movementFeature, CurrentPath + "\���H�ς�\\" + movementFeature)
    arcpy.Delete_management(movementFeature)
    
    # �i���\��
    print("3320_�N�I�__�N�I�_" "�̏������I��")
else:
    # �i���\��
    print("3320_�N�I�__�N�I�_" "�K�v�t�@�C�����������ߏ��������܂���")

# ������������������������������������������������������������������


# ��ƃt�H���_��ύX
arcpy.env.workspace = CurrentPath

# ��3333_����_�l����������������������������������������������������������
# �i���\��
print("3333_����_�l" "�̏������J�n")

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

    outFeature = "3333_����_�l.shp"
    
    arcpy.env.workspace = CurrentPath + "\�e�L�X�g"
    arcpy.Delete_management("3333_����_�l.shp")
    arcpy.env.workspace = CurrentPath
    
    # unicode�����ƘA������̂ŘA�����镶����unicode�ɂ���
    OutputShape = CurrentPath + "\�e�L�X�g\\" + outFeature
    
    # �}�[�W���s
    arcpy.Merge_management(
    ["D9111_���H�������l_T.shp",
    "D9111_�����������l_T.shp",
    "D9111_�K�i�������l_T.shp",
    "D9111_�ԓ��������l_T.shp",
    "D9111_���������ѕ����l_T.shp"],
    OutputShape)
    
    # ��ƃt�H���_��ύX
    arcpy.env.workspace = CurrentPath + "\�e�L�X�g"
    
    # �t�B�[���h��ǉ�
    arcpy.AddField_management(outFeature, "CODE", "LONG")
    
    # ���Z�����i�[
    Expression = "CodeCalc(!CHIBUTSU!)"
    
    # ���Z
    arcpy.CalculateField_management(outFeature, "CODE", Expression, "PYTHON", CodeBlock)
    
    # �������I��������̂����H�ς݃t�H���_�Ɉړ�
    arcpy.env.workspace = CurrentPath
    movementFeature = "D9111_���H�������l_T.shp"
    arcpy.Copy_management(movementFeature, CurrentPath + "\���H�ς�\\" + movementFeature)
    arcpy.Delete_management(movementFeature)
    movementFeature = "D9111_�����������l_T.shp"
    arcpy.Copy_management(movementFeature, CurrentPath + "\���H�ς�\\" + movementFeature)
    arcpy.Delete_management(movementFeature)
    movementFeature = "D9111_�K�i�������l_T.shp"
    arcpy.Copy_management(movementFeature, CurrentPath + "\���H�ς�\\" + movementFeature)
    arcpy.Delete_management(movementFeature)
    movementFeature = "D9111_�ԓ��������l_T.shp"
    arcpy.Copy_management(movementFeature, CurrentPath + "\���H�ς�\\" + movementFeature)
    arcpy.Delete_management(movementFeature)
    movementFeature = "D9111_���������ѕ����l_T.shp"
    arcpy.Copy_management(movementFeature, CurrentPath + "\���H�ς�\\" + movementFeature)
    arcpy.Delete_management(movementFeature)
    
    
    # �i���\��
    print("3333_����_�l" "�̏������I��")
else:
    # �i���\��
    print("3333_����_�l" "�K�v�t�@�C�����������ߏ��������܂���")


# ������������������������������������������������������������������

# ��ƃt�H���_��ύX
arcpy.env.workspace = CurrentPath

# ��3331_����_������������������������������������������������������������
# �i���\��
print("3331_����_��" "�̏������J�n")

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
    
    outFeature = "3331_����_��.shp"
    
    arcpy.env.workspace = CurrentPath + "\���C��"
    arcpy.Delete_management("3331_����_��.shp")
    arcpy.env.workspace = CurrentPath
    
    # unicode�����ƘA������̂ŘA�����镶����unicode�ɂ���
    OutputShape = CurrentPath + "\���C��\\" + outFeature
    
    # �}�[�W���s
    arcpy.Merge_management(
    ["D9112_������������_L.shp",
     "D9112_�K�i��������_L.shp",
     "D9112_�ԓ���������_L.shp",
     "D9112_���������ѕ�����_L.shp",
     "D9112_���H��������_L.shp"],
    OutputShape)
    
    # ��ƃt�H���_��ύX
    arcpy.env.workspace = CurrentPath + "\���C��"
    
    # �t�B�[���h��ǉ�
    arcpy.AddField_management(outFeature, "CODE", "LONG")
    
    # ���Z�����i�[
    Expression = "CodeCalc(!CHIBUTSU!)"
    
    # ���Z
    arcpy.CalculateField_management(outFeature, "CODE", Expression, "PYTHON", CodeBlock)
    
    # �������I��������̂����H�ς݃t�H���_�Ɉړ�
    arcpy.env.workspace = CurrentPath
    movementFeature = "D9112_������������_L.shp"
    arcpy.Copy_management(movementFeature, CurrentPath + "\���H�ς�\\" + movementFeature)
    arcpy.Delete_management(movementFeature)
    movementFeature = "D9112_�K�i��������_L.shp"
    arcpy.Copy_management(movementFeature, CurrentPath + "\���H�ς�\\" + movementFeature)
    arcpy.Delete_management(movementFeature)
    movementFeature = "D9112_�ԓ���������_L.shp"
    arcpy.Copy_management(movementFeature, CurrentPath + "\���H�ς�\\" + movementFeature)
    arcpy.Delete_management(movementFeature)
    movementFeature = "D9112_���������ѕ�����_L.shp"
    arcpy.Copy_management(movementFeature, CurrentPath + "\���H�ς�\\" + movementFeature)
    arcpy.Delete_management(movementFeature)
    movementFeature = "D9112_���H��������_L.shp"
    arcpy.Copy_management(movementFeature, CurrentPath + "\���H�ς�\\" + movementFeature)
    arcpy.Delete_management(movementFeature)
    
    # �i���\��
    print("3331_����_��" "�̏������I��")
else:
    # �i���\��
    print("3331_����_��" "�K�v�t�@�C�����������ߏ��������܂���")


# ������������������������������������������������������������������

# ��ƃt�H���_��ύX
arcpy.env.workspace = CurrentPath

# ��3304_���a_���a������������������������������������������������������
# �i���\��
print("3304_���a_���a" "�̏������J�n")

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

    outFeature = "3304_���a_���a.shp"
    
    arcpy.env.workspace = CurrentPath + "\���C��"
    arcpy.Delete_management("3304_���a_���a.shp")
    arcpy.env.workspace = CurrentPath
    
    # unicode�����ƘA������̂ŘA�����镶����unicode�ɂ���
    OutputShape = CurrentPath + "\���C��\\" + outFeature
    
    # �R�s�[���s
    arcpy.Copy_management("D9131_���a���C��_L.shp", OutputShape)
    
    # ��ƃt�H���_��ύX
    arcpy.env.workspace = CurrentPath + "\���C��"
    
    # �t�B�[���h��ǉ�
    arcpy.AddField_management(outFeature, "CODE", "LONG")
    
    # ���Z�����i�[
    Expression = "CodeCalc(!CHIBUTSU!)"
    
    # ���Z
    arcpy.CalculateField_management(outFeature, "CODE", Expression, "PYTHON", CodeBlock)
    
    # �������I��������̂����H�ς݃t�H���_�Ɉړ�
    arcpy.env.workspace = CurrentPath
    movementFeature = "D9131_���a���C��_L.shp"
    arcpy.Copy_management(movementFeature, CurrentPath + "\���H�ς�\\" + movementFeature)
    arcpy.Delete_management(movementFeature)
    
    # �i���\��
    print("3304_���a_���a" "�̏������I��")
else:
    # �i���\��
    print("3304_���a_���a" "�K�v�t�@�C�����������ߏ��������܂���")


# ������������������������������������������������������������������

# ��ƃt�H���_��ύX
arcpy.env.workspace = CurrentPath

# ��3306_�h���_�h��򁡁���������������������������������������������������
# �i���\��
print("3306_�h���_�h���" "�̏������J�n")

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

    outFeature = "3306_�h���_�h���.shp"
    
    arcpy.env.workspace = CurrentPath + "\���C��"
    arcpy.Delete_management("3306_�h���_�h���.shp")
    arcpy.env.workspace = CurrentPath
    
    # unicode�����ƘA������̂ŘA�����镶����unicode�ɂ���
    OutputShape = CurrentPath + "\���C��\\" + outFeature
    
    # �R�s�[���s
    arcpy.Copy_management("D9133_�h��򃉃C��_L.shp", OutputShape)
    
    # ��ƃt�H���_��ύX
    arcpy.env.workspace = CurrentPath + "\���C��"
    
    # �t�B�[���h��ǉ�
    arcpy.AddField_management(outFeature, "CODE", "LONG")
    
    # ���Z�����i�[
    Expression = "CodeCalc(!CHIBUTSU!)"
    
    # ���Z
    arcpy.CalculateField_management(outFeature, "CODE", Expression, "PYTHON", CodeBlock)
    
    # �������I��������̂����H�ς݃t�H���_�Ɉړ�
    arcpy.env.workspace = CurrentPath
    movementFeature = "D9133_�h��򃉃C��_L.shp"
    arcpy.Copy_management(movementFeature, CurrentPath + "\���H�ς�\\" + movementFeature)
    arcpy.Delete_management(movementFeature)
    
    # �i���\��
    print("3306_�h���_�h���" "�̏������I��")
else:
    # �i���\��
    print("3306_�h���_�h���" "�K�v�t�@�C�����������ߏ��������܂���")

# ������������������������������������������������������������������

# ��ƃt�H���_��ύX
arcpy.env.workspace = CurrentPath

# ��3344_����_���L����������������������������������������������������������
# �i���\��
print("3344_����_���L" "�̏������J�n")

# shp�t�@�C���������Ă���ꍇ�̂ݏ������s��
if arcpy.Exists("D9141_�������@_T.shp") and arcpy.Exists("D9141_�����ԍ�_T.shp") and arcpy.Exists("D9141_��������_T.shp"):
    outFeature = "3344_����_���L.shp"
    
    # unicode�����ƘA������̂ŘA�����镶����unicode�ɂ���
    OutputShape = CurrentPath + "\�e�L�X�g\\" + outFeature
    
    arcpy.env.workspace = CurrentPath + "\�e�L�X�g"
    arcpy.Delete_management("3344_����_���L.shp")
    arcpy.env.workspace = CurrentPath
    
    # �}�[�W���s
    arcpy.Merge_management(
    ["D9141_�������@_T.shp",
     "D9141_�����ԍ�_T.shp",
     "D9141_��������_T.shp"],
    OutputShape)
    
    # �������I��������̂����H�ς݃t�H���_�Ɉړ�
    arcpy.env.workspace = CurrentPath
    movementFeature = "D9141_�������@_T.shp"
    arcpy.Copy_management(movementFeature, CurrentPath + "\���H�ς�\\" + movementFeature)
    arcpy.Delete_management(movementFeature)
    movementFeature = "D9141_�����ԍ�_T.shp"
    arcpy.Copy_management(movementFeature, CurrentPath + "\���H�ς�\\" + movementFeature)
    arcpy.Delete_management(movementFeature)
    movementFeature = "D9141_��������_T.shp"
    arcpy.Copy_management(movementFeature, CurrentPath + "\���H�ς�\\" + movementFeature)
    arcpy.Delete_management(movementFeature)
    
    # �i���\��
    print("3344_����_���L" "�̏������I��")
else:
    # �i���\��
    print("3344_����_���L" "�K�v�t�@�C�����������ߏ��������܂���")

# ������������������������������������������������������������������

# ��3347_�S������_���L����������������������������������������������������������
# �i���\��
print("3347_�S������_���L" "�̏������J�n")

# shp�t�@�C���������Ă���ꍇ�̂ݏ������s��
if arcpy.Exists("D9142_�S���������@_T.shp") and arcpy.Exists("D9142_�S�������ԍ�_T.shp") and arcpy.Exists("D9142_�S����������_T.shp"):
    
    outFeature = "3347_�S������_���L.shp"
    
    arcpy.env.workspace = CurrentPath + "\�e�L�X�g"
    arcpy.Delete_management("3347_�S������_���L.shp")
    arcpy.env.workspace = CurrentPath
    
    # unicode�����ƘA������̂ŘA�����镶����unicode�ɂ���
    OutputShape = CurrentPath + "\�e�L�X�g\\" + outFeature
    
    # �}�[�W���s
    arcpy.Merge_management(
    ["D9142_�S���������@_T.shp",
     "D9142_�S�������ԍ�_T.shp",
     "D9142_�S����������_T.shp"],
    OutputShape)
    
    # �������I��������̂����H�ς݃t�H���_�Ɉړ�
    arcpy.env.workspace = CurrentPath
    movementFeature = "D9142_�S���������@_T.shp"
    arcpy.Copy_management(movementFeature, CurrentPath + "\���H�ς�\\" + movementFeature)
    arcpy.Delete_management(movementFeature)
    movementFeature = "D9142_�S�������ԍ�_T.shp"
    arcpy.Copy_management(movementFeature, CurrentPath + "\���H�ς�\\" + movementFeature)
    arcpy.Delete_management(movementFeature)
    movementFeature = "D9142_�S����������_T.shp"
    arcpy.Copy_management(movementFeature, CurrentPath + "\���H�ς�\\" + movementFeature)
    arcpy.Delete_management(movementFeature)
    
    # �i���\��
    print("3347_�S������_���L" "�̏������I��")
else:
    # �i���\��
    print("3347_�S������_���L" "�K�v�t�@�C�����������ߏ��������܂���")

# ������������������������������������������������������������������

# ��3335_�����v����_�����v��������������������������������������������������������������
# �i���\��
print("3335_�����v����_�����v����" "�̏������J�n")

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
    
    outFeature = "3335_�����v����_�����v����.shp"
    
    arcpy.env.workspace = CurrentPath + "\���C��"
    arcpy.Delete_management("3335_�����v����_�����v����.shp")
    arcpy.env.workspace = CurrentPath
    
    # unicode�����ƘA������̂ŘA�����镶����unicode�ɂ���
    OutputShape = CurrentPath + "\���C��\\" + outFeature
    
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
    arcpy.env.workspace = CurrentPath + "\���C��"
    
    # �t�B�[���h��ǉ�
    arcpy.AddField_management(outFeature, "CODE", "LONG")
    
    # ���Z�����i�[
    Expression = "CodeCalc(!CHIBUTSU!)"
    
    # ���Z
    arcpy.CalculateField_management(outFeature, "CODE", Expression, "PYTHON", CodeBlock)
    
    # �������I��������̂����H�ς݃t�H���_�Ɉړ�
    arcpy.env.workspace = CurrentPath
    movementFeature = "Z9321_���H���S���i�����j_L.shp"
    arcpy.Copy_management(movementFeature, CurrentPath + "\���H�ς�\\" + movementFeature)
    arcpy.Delete_management(movementFeature)
    movementFeature = "Z9321_���H���S���i�S�������j_L.shp"
    arcpy.Copy_management(movementFeature, CurrentPath + "\���H�ς�\\" + movementFeature)
    arcpy.Delete_management(movementFeature)
    movementFeature = "Z9321_���H���S��_L.shp"
    arcpy.Copy_management(movementFeature, CurrentPath + "\���H�ς�\\" + movementFeature)
    arcpy.Delete_management(movementFeature)
    movementFeature = "Z9321_���H���S���d�p����_L.shp"
    arcpy.Copy_management(movementFeature, CurrentPath + "\���H�ς�\\" + movementFeature)
    arcpy.Delete_management(movementFeature)
    movementFeature = "Z9321_���H���S��������_L.shp"
    arcpy.Copy_management(movementFeature, CurrentPath + "\���H�ς�\\" + movementFeature)
    arcpy.Delete_management(movementFeature)
    movementFeature = "Z9321_���H���S�������p_L.shp"
    arcpy.Copy_management(movementFeature, CurrentPath + "\���H�ς�\\" + movementFeature)
    arcpy.Delete_management(movementFeature)
    
    # �i���\��
    print("3335_�����v����_�����v����" "�̏������I��")
else:
    # �i���\��
    print("3335_�����v����_�����v����" "�K�v�t�@�C�����������ߏ��������܂���")

# ������������������������������������������������������������������

# ��ƃt�H���_��ύX
arcpy.env.workspace = CurrentPath

# ��3318_����_������������������������������������������������������������
# �i���\��
print("3318_����_��" "�̏������J�n")

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
    
    outFeature = "3318_����_��.shp"
    
    arcpy.env.workspace = CurrentPath + "\���C��"
    arcpy.Delete_management("3318_����_��.shp")
    arcpy.env.workspace = CurrentPath
    
    # unicode�����ƘA������̂ŘA�����镶����unicode�ɂ���
    OutputShape = CurrentPath + "\���C��\\" + outFeature
    
    # �}�[�W���s
    arcpy.Merge_management(
    ["Z9352_�������C��_L.shp",
     "Z9353_���������C��_L.shp"],
    OutputShape)
    
    # ��ƃt�H���_��ύX
    arcpy.env.workspace = CurrentPath + "\���C��"
    
    # �t�B�[���h��ǉ�
    arcpy.AddField_management(outFeature, "CODE", "LONG")
    # ���Z�����i�[
    Expression = "CodeCalc(!CHIBUTSU!)"
    
    # ���Z
    arcpy.CalculateField_management(outFeature, "CODE", Expression, "PYTHON", CodeBlock)
    
    # �������I��������̂����H�ς݃t�H���_�Ɉړ�
    arcpy.env.workspace = CurrentPath
    movementFeature = "Z9352_�������C��_L.shp"
    arcpy.Copy_management(movementFeature, CurrentPath + "\���H�ς�\\" + movementFeature)
    arcpy.Delete_management(movementFeature)
    movementFeature = "Z9353_���������C��_L.shp"
    arcpy.Copy_management(movementFeature, CurrentPath + "\���H�ς�\\" + movementFeature)
    arcpy.Delete_management(movementFeature)
    
    # �i���\��
    print("3318_����_��" "�̏������I��")
else:
    # �i���\��
    print("3318_����_��" "�K�v�t�@�C�����������ߏ��������܂���")


# ������������������������������������������������������������������

# ��ƃt�H���_��ύX
arcpy.env.workspace = CurrentPath


# ��3301_���H_���H������������������������������������������������������
# �i���\��
print("3301_���H_���H" "�̏������J�n")

CodeBlock = """def CodeCalc(CHIBUTSU):
    if CHIBUTSU == 935100:
        return 120
    elif CHIBUTSU == 935108:
        return 1123
    else:
        return 0"""

# shp�t�@�C���������Ă���ꍇ�̂ݏ������s��
if arcpy.Exists("Z9351_���H��_L.shp"):
    
    outFeature = "3301_���H_���H.shp"
    
    arcpy.env.workspace = CurrentPath + "\���C��"
    arcpy.Delete_management("3301_���H_���H.shp")
    arcpy.env.workspace = CurrentPath
    
    # unicode�����ƘA������̂ŘA�����镶����unicode�ɂ���
    OutputShape = CurrentPath + "\���C��\\" + outFeature
    
    # �R�s�[���s
    arcpy.Copy_management("Z9351_���H��_L.shp", OutputShape)
    
    # ��ƃt�H���_��ύX
    arcpy.env.workspace = CurrentPath + "\���C��"
    
    # �t�B�[���h��ǉ�
    arcpy.AddField_management(outFeature, "CODE", "LONG")
    # ���Z�����i�[
    Expression = "CodeCalc(!CHIBUTSU!)"
    
    # ���Z
    arcpy.CalculateField_management(outFeature, "CODE", Expression, "PYTHON", CodeBlock)
    
    # �������I��������̂����H�ς݃t�H���_�Ɉړ�
    arcpy.env.workspace = CurrentPath
    movementFeature = "Z9351_���H��_L.shp"
    arcpy.Copy_management(movementFeature, CurrentPath + "\���H�ς�\\" + movementFeature)
    arcpy.Delete_management(movementFeature)
    
    # �i���\��
    print("3301_���H_���H" "�̏������I��")
else:
    # �i���\��
    print("3301_���H_���H" "�K�v�t�@�C�����������ߏ��������܂���")

# ������������������������������������������������������������������

# ��ƃt�H���_��ύX
arcpy.env.workspace = CurrentPath

# ��3336_���_��ԁ�����������������������������������������������������
# �i���\��
print("3336_���_���" "�̏������J�n")

# shp�t�@�C���������Ă���ꍇ�̂ݏ������s��
if arcpy.Exists("Z9302_���H��_P.shp"):
    
    outFeature = "3336_���_���.shp"
    
    arcpy.env.workspace = CurrentPath + "\�G���A"
    arcpy.Delete_management("3336_���_���.shp")
    arcpy.env.workspace = CurrentPath
    
    arcpy.env.workspace = CurrentPath + "\������"
    arcpy.Delete_management("3336_���_���.csv")
    arcpy.env.workspace = CurrentPath
    
    # unicode�����ƘA������̂ŘA�����镶����unicode�ɂ���
    OutputShape = CurrentPath + "\�G���A\\" + outFeature
    
    # �R�s�[���s
    arcpy.Copy_management("Z9302_���H��_P.shp", OutputShape)
    
    # ��ƃt�H���_��ύX
    arcpy.env.workspace = CurrentPath + "\�G���A"
    
    # �t�B�[���h��ǉ�
    arcpy.AddField_management(outFeature, "UserID", "LONG")
    
    # ���Z�����i�[
    Expression = "!FID! + 1"
    
    # ���Z
    arcpy.CalculateField_management(outFeature, "UserID", Expression, "PYTHON")
    
    # SLINKID��UserID�����̃t�B�[�`���ɂ��邽�߂ɃR�s�[����
    arcpy.Copy_management("3336_���_���.shp", CurrentPath + r"\������\3336_���_���.shp")
    arcpy.env.workspace = CurrentPath + "\������"
    
    # �s�v�ȃt�B�[���h���폜
    arcpy.DeleteField_management(CurrentPath + r"\������\3336_���_���.shp", ["CHIBUTSU", "NLEVEL"])
    
    # �O���c�[�����g����DBF��CSV�ɕϊ�����
    subprocess.call([CurrentPath + r"\dbf2csv.exe", CurrentPath + r"\������\3336_���_���.dbf"])
    
    # CSV�o�͗p�ɃR�s�[�����t�B�[�`���͍폜����
    arcpy.Delete_management(outFeature)
    
    # �ꉞ�O�̃R�[�h�͎c���Ă���
    # arcpy.TableToTable_conversion("3336_���_���.dbf", CurrentPath + "\������", "3336_���_���.csv")
    
    
    # �������I��������̂����H�ς݃t�H���_�Ɉړ�
    arcpy.env.workspace = CurrentPath
    movementFeature = "Z9302_���H��_P.shp"
    arcpy.Copy_management(movementFeature, CurrentPath + "\���H�ς�\\" + movementFeature)
    arcpy.Delete_management(movementFeature)
    
    # �i���\��
    print("3336_���_���" "�̏������I��")
else:
    # �i���\��
    print("3336_���_���" "�K�v�t�@�C�����������ߏ��������܂���")

# ������������������������������������������������������������������

# ��ƃt�H���_��ύX
arcpy.env.workspace = CurrentPath + "\�G���A"

# ��3337_���_�ԍ���������������������������������������������������
# �i���\��
print("3337_���_�ԍ�" "�̏������J�n")

# shp�t�@�C���������Ă���ꍇ�̂ݏ������s��
if arcpy.Exists("3336_���_���.shp"):
    
    outFeature = "3337_���_�ԍ�.shp"
    
    arcpy.env.workspace = CurrentPath + "\�e�L�X�g"
    arcpy.Delete_management("3337_���_�ԍ�.shp")
    arcpy.env.workspace = CurrentPath + "\�G���A"
    
    # unicode�����ƘA������̂ŘA�����镶����unicode�ɂ���
    OutputShape = CurrentPath + "\�e�L�X�g\\" + outFeature
    
    # ��ԃ|���S�����|�C���g�ɕϊ�
    arcpy.FeatureToPoint_management("3336_���_���.shp", OutputShape, "CENTROID")
    
    # ��ƃt�H���_��ύX
    arcpy.env.workspace = CurrentPath + "\�e�L�X�g"
    
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
    arcpy.CalculateField_management(outFeature, "CHIBUTSU", "921200", "PYTHON")
    arcpy.CalculateField_management(outFeature, "NFONTSIZE", "30", "PYTHON")
    arcpy.CalculateField_management(outFeature, "NLABELANGL", "0", "PYTHON")
    arcpy.CalculateField_management(outFeature, "NLEVEL", "500", "PYTHON")
    arcpy.CalculateField_management(outFeature, "NSYMBOLID", "6", "PYTHON")
    arcpy.CalculateField_management(outFeature, "SFONTNAME", "\"�l�r �S�V�b�N\"", "PYTHON")
    
    CodeBlock = """def mid(text, n, m):
  return text[n-1:n+m-1]"""
    
    arcpy.CalculateField_management(outFeature, "SLABEL", "mid( !SLINKID! , 8 , len( !SLINKID! ) -7 )", "PYTHON", CodeBlock)
    arcpy.CalculateField_management(outFeature, "kukan", "!SLABEL!", "PYTHON")
    
    # �i���\��
    print("3337_���_�ԍ�" "�̏������I��")
else:
    # �i���\��
    print("3337_���_�ԍ�" "�K�v�t�@�C�����������ߏ��������܂���")

# ������������������������������������������������������������������
print("���������I�����܂����B������������������������������������������")
