import FWCore.ParameterSet.Config as cms

################# process.raw2digi_step

ecalDigis = cms.EDProducer("EcalRawToDigi",
    DoRegional = cms.bool(False),
    FEDs = cms.vint32(
        601, 602, 603, 604, 605, 
        606, 607, 608, 609, 610, 
        611, 612, 613, 614, 615, 
        616, 617, 618, 619, 620, 
        621, 622, 623, 624, 625, 
        626, 627, 628, 629, 630, 
        631, 632, 633, 634, 635, 
        636, 637, 638, 639, 640, 
        641, 642, 643, 644, 645, 
        646, 647, 648, 649, 650, 
        651, 652, 653, 654
    ),
    FedLabel = cms.InputTag("listfeds"),
    InputLabel = cms.InputTag("rawDataCollector"),
    eventPut = cms.bool(True),
    feIdCheck = cms.bool(True),
    feUnpacking = cms.bool(True),
    forceToKeepFRData = cms.bool(False),
    headerUnpacking = cms.bool(True),
    memUnpacking = cms.bool(True),
    numbTriggerTSamples = cms.int32(1),
    numbXtalTSamples = cms.int32(10),
    orderedDCCIdList = cms.vint32(
        1, 2, 3, 4, 5, 
        6, 7, 8, 9, 10, 
        11, 12, 13, 14, 15, 
        16, 17, 18, 19, 20, 
        21, 22, 23, 24, 25, 
        26, 27, 28, 29, 30, 
        31, 32, 33, 34, 35, 
        36, 37, 38, 39, 40, 
        41, 42, 43, 44, 45, 
        46, 47, 48, 49, 50, 
        51, 52, 53, 54
    ),
    orderedFedList = cms.vint32(
        601, 602, 603, 604, 605, 
        606, 607, 608, 609, 610, 
        611, 612, 613, 614, 615, 
        616, 617, 618, 619, 620, 
        621, 622, 623, 624, 625, 
        626, 627, 628, 629, 630, 
        631, 632, 633, 634, 635, 
        636, 637, 638, 639, 640, 
        641, 642, 643, 644, 645, 
        646, 647, 648, 649, 650, 
        651, 652, 653, 654
    ),
    silentMode = cms.untracked.bool(True),
    srpUnpacking = cms.bool(True),
    syncCheck = cms.bool(True),
    tccUnpacking = cms.bool(True)
)

hcalDigis = cms.EDProducer("HcalRawToDigi",
    ComplainEmptyData = cms.untracked.bool(False),
    ElectronicsMap = cms.string(''),
    ExpectedOrbitMessageTime = cms.untracked.int32(-1),
    FEDs = cms.untracked.vint32(),
    FilterDataQuality = cms.bool(True),
    HcalFirstFED = cms.untracked.int32(700),
    InputLabel = cms.InputTag("rawDataCollector"),
    UnpackCalib = cms.untracked.bool(True),
    UnpackTTP = cms.untracked.bool(True),
    UnpackUMNio = cms.untracked.bool(True),
    UnpackZDC = cms.untracked.bool(True),
    UnpackerMode = cms.untracked.int32(0),
    firstSample = cms.int32(0),
    lastSample = cms.int32(9),
    saveQIE10DataNSamples = cms.untracked.vint32(),
    saveQIE10DataTags = cms.untracked.vstring(),
    saveQIE11DataNSamples = cms.untracked.vint32(),
    saveQIE11DataTags = cms.untracked.vstring(),
    silent = cms.untracked.bool(True)
)

muonCSCDigis = cms.EDProducer("CSCDCCUnpacker",
    Debug = cms.untracked.bool(False),
    ErrorMask = cms.uint32(0),
    ExaminerMask = cms.uint32(535558134),
    FormatedEventDump = cms.untracked.bool(False),
    InputObjects = cms.InputTag("rawDataCollector"),
    PrintEventNumber = cms.untracked.bool(False),
    SuppressZeroLCT = cms.untracked.bool(True),
    UnpackStatusDigis = cms.bool(False),
    UseExaminer = cms.bool(True),
    UseFormatStatus = cms.bool(True),
    UseSelectiveUnpacking = cms.bool(True),
    VisualFEDInspect = cms.untracked.bool(False),
    VisualFEDShort = cms.untracked.bool(False),
    runDQM = cms.untracked.bool(False)
)

muonDTDigis = cms.EDProducer("DTuROSRawToDigi",
    debug = cms.untracked.bool(False),
    inputLabel = cms.InputTag("rawDataCollector")
)

muonGEMDigis = cms.EDProducer("GEMRawToDigiModule",
    InputLabel = cms.InputTag("rawDataCollector"),
    unPackStatusDigis = cms.bool(False),
    useDBEMap = cms.bool(False)
)

muonRPCDigis = cms.EDProducer("RPCUnpackingModule",
    InputLabel = cms.InputTag("rawDataCollector"),
    doSynchro = cms.bool(True)
)


muonRPCNewDigis = cms.EDProducer("RPCDigiMerger",
    inputTagCPPFDigis = cms.InputTag("rpcCPPFRawToDigi"),
    inputTagOMTFDigis = cms.InputTag("omtfStage2Digis"),
    inputTagTwinMuxDigis = cms.InputTag("rpcTwinMuxRawToDigi")
)


scalersRawToDigi = cms.EDProducer("ScalersRawToDigi",
    scalersInputTag = cms.InputTag("rawDataCollector")
)

#process.raw2digi_step
raw2digi_step = cms.Path(cms.Task(ecalDigis, hcalDigis, muonCSCDigis, muonDTDigis, muonGEMDigis, muonRPCDigis, muonRPCNewDigis, scalersRawToDigi))
