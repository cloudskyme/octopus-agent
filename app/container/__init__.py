# -*- coding: UTF-8 -*-
#*************************************
#author:zhengqs
#create:201707
#desc: 
#**********************************

from flask import Blueprint

container=Blueprint('container',
        __name__,
        #template_folder='/opt/auras/templates/',   #ָ��ģ��·��
         #static_folder='/opt/auras/flask_bootstrap/static/',#ָ����̬�ļ�·��
      )
  
from app.container import views
