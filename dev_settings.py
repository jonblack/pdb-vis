# Flask
DEBUG = True
SECRET_KEY = 'development_key'

# Debug toolbar
DEBUG_TB_ENABLED = DEBUG
DEBUG_TB_INTERCEPT_REDIRECTS = False

# Email logging settings
MAIL_SERVER = "smtp.umcn.nl"
MAIL_SMTP_PORT = 25
MAIL_FROM = "pdb-vis@cmbi.umcn.nl"
MAIL_TO = ["Jon.Black@radboudumc.nl"]

# Databank paths
ACC_ROOT_PDB = '/mnt/cmbi4/wi-lists/pdb/acc/'
ACC_ROOT_PDB_REDO = '/mnt/cmbi4/wi-lists/redo/acc/'
DSP_ROOT_PDB = '/mnt/cmbi4/wi-lists/pdb/dsp/'
DSP_ROOT_PDB_REDO = '/mnt/cmbi4/wi-lists/redo/dsp/'
SCE_ROOT_PDB = '/mnt/cmbi4/wi-lists/pdb/scenes/'
SCE_ROOT_PDB_REDO = '/mnt/cmbi4/wi-lists/redo/scenes/'
SCE_TYPES = {'ss2': 'sym-contacts', 'iod': 'ion-sites'}
