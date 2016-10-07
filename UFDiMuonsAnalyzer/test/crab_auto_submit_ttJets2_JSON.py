from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'ttJets2'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'dimu_ttJets2_for_crab.py'
#config.JobType.outputFiles = ['outputfile.root']

config.Data.inputDataset = '/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
#config.Data.splitting = 'LumiBased' # Must use this with JSON file
#config.Data.lumiMask = 's.jsonfiles[1]'
config.Data.unitsPerJob = 10
config.Data.outLFNDirBase = '/store/user/bregnery/'
config.Data.publication = False
config.Data.outputDatasetTag = 'ttJets2'

config.Site.storageSite = 'T2_US_Florida'
