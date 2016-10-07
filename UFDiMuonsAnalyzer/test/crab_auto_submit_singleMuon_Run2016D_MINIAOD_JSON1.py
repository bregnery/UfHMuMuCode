from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'singleMuon_Run2016D_MINIAOD_JSON1'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'dimu_singleMuon_Run2016D_MINIAOD1_for_crab.py'
#config.JobType.outputFiles = ['outputfile.root']

config.Data.inputDataset = '/SingleMuon/Run2016D-PromptReco-v2/MINIAOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
#config.Data.splitting = 'LumiBased' # Must use this with JSON file
config.Data.lumiMask = 's.jsonfiles[1]'
config.Data.unitsPerJob = 10
config.Data.outLFNDirBase = '/store/user/bregnery/'
config.Data.publication = False
config.Data.outputDatasetTag = 'singleMuon_Run2016D_MINIAOD_JSON1'

config.Site.storageSite = 'T2_US_Florida'
