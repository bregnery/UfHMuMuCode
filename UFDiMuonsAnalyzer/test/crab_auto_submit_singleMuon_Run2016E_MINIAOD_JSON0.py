from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'singleMuon_Run2016E_MINIAOD_JSON0'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'dimu_singleMuon_Run2016E_MINIAOD0_for_crab.py'
#config.JobType.outputFiles = ['outputfile.root']

config.Data.inputDataset = '/SingleMuon/Run2016E-PromptReco-v2/MINIAOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
#config.Data.splitting = 'LumiBased' # Must use this with JSON file
config.Data.lumiMask = 'sample_file_lists/data/json/Cert_271036-280385_13TeV_PromptReco_Collisions16_JSON_NoL1T_v2.txt'
config.Data.unitsPerJob = 10
config.Data.outLFNDirBase = '/store/user/bregnery/'
config.Data.publication = False
config.Data.outputDatasetTag = 'singleMuon_Run2016E_MINIAOD_JSON0'

config.Site.storageSite = 'T2_US_Florida'
