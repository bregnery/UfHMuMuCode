from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'singleMuon_RunDOct_v1_MINIAOD_JSON1'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'dimu_singleMuon_RunDOct_v1_MINIAOD1_for_crab.py'
#config.JobType.outputFiles = ['outputfile.root']

config.Data.inputDataset = '/SingleMuon/Run2015D-05Oct2015-v1/MINIAOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
#config.Data.splitting = 'LumiBased' # Must use this with JSON file
config.Data.lumiMask = 'sample_file_lists/data/json/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_v2.txt'
config.Data.unitsPerJob = 10
config.Data.outLFNDirBase = '/store/user/acarnes/'
config.Data.publication = False
config.Data.outputDatasetTag = 'singleMuon_RunDOct_v1_MINIAOD_JSON1'

config.Site.storageSite = 'T2_US_Florida'
