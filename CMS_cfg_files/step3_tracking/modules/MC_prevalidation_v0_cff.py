import FWCore.ParameterSet.Config as cms

###################### prevalidation_step


trackValidatorTrackingOnly = cms.EDProducer("MultiTrackValidator", #cmssw_11_1 previous cms.EDAnalyzer
    cores = cms.InputTag("highPtJetsForTrk"), #cmssw_10_6    # cmssw_11_1 
    UseAssociators = cms.bool(False),
    associators = cms.untracked.VInputTag("trackingParticleRecoTrackAsssociation"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    calculateDrSingleCollection = cms.untracked.bool(True),
    chargedOnlyTP = cms.bool(True),
    dEdx1Tag = cms.InputTag("dedxHarmonic2"),
    dEdx2Tag = cms.InputTag("dedxTruncated40"),
    dirName = cms.string('Tracking/Track/'),
    doMVAPlots = cms.untracked.bool(False),
    doPVAssociationPlots = cms.untracked.bool(True),
    doPlotsOnlyForTruePV = cms.untracked.bool(False),
    doRecoTrackPlots = cms.untracked.bool(True),
    doResolutionPlotsForLabels = cms.VInputTag("generalTracks", "cutsRecoTracksHp", "generalTracksPt09", "cutsRecoTracksBtvLike"),
    doSeedPlots = cms.untracked.bool(False),
    doSimPlots = cms.untracked.bool(True),
    doSimTrackPlots = cms.untracked.bool(True),
    doSummaryPlots = cms.untracked.bool(True),
    dodEdxPlots = cms.untracked.bool(False),
    histoProducerAlgoBlock = cms.PSet(
	mindrj = cms.double(0.001),#cmssw_10_6 
        maxdrj = cms.double(0.1),#cmssw_10_6
        nintdrj = cms.int32(100), #cmssw_10_6
        GpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5 
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.05),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 30.0
        ),
        GpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(35.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.05),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 60.0
        ),
        TpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        cotThetaRes_nbin = cms.int32(300),
        cotThetaRes_rangeMax = cms.double(0.02),
        cotThetaRes_rangeMin = cms.double(-0.02),
        doMTDPlots = cms.untracked.bool(True), # cmssw_11_1
        dxyDzZoom = cms.double(25),
        dxyRes_nbin = cms.int32(500),
        dxyRes_rangeMax = cms.double(0.1),
        dxyRes_rangeMin = cms.double(-0.1),
        dzRes_nbin = cms.int32(150),
        dzRes_rangeMax = cms.double(0.05),
        dzRes_rangeMin = cms.double(-0.05),
        generalGpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        generalTpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        maxChi2 = cms.double(20),
        maxDeDx = cms.double(10.0),
        maxDxy = cms.double(25),
        maxDz = cms.double(30),
        maxDzpvCumulative = cms.double(0.6),
        maxDzpvsigCumulative = cms.double(10),
        maxEta = cms.double(4.5),
        maxHit = cms.double(80.5),
        maxLayers = cms.double(25.5),
        maxMVA = cms.double(1),
        maxPVz = cms.double(60),
        maxPhi = cms.double(3.1416),
        maxPt = cms.double(1000),
        maxPu = cms.double(259.5),
        maxTracks = cms.double(2000),
        maxVertcount = cms.double(160.5),
        maxVertpos = cms.double(100),
        maxZpos = cms.double(30),
        maxdr = cms.double(1),
        minChi2 = cms.double(0),
        minDeDx = cms.double(0.0),
        minDxy = cms.double(-25),
        minDz = cms.double(-30),
        minEta = cms.double(-4.5),
        minHit = cms.double(-0.5),
        minLayers = cms.double(-0.5),
        minMVA = cms.double(-1),
        minPVz = cms.double(-60),
        minPhi = cms.double(-3.1416),
        minPt = cms.double(0.1),
        minPu = cms.double(-0.5),
        minTracks = cms.double(0),
        minVertcount = cms.double(-0.5),
        minVertpos = cms.double(0.01),
        minZpos = cms.double(-30),
        mindr = cms.double(0.001),
        nintChi2 = cms.int32(40),
        nintDeDx = cms.int32(40),
        nintDxy = cms.int32(100),
        nintDz = cms.int32(60),
        nintDzpvCumulative = cms.int32(240),
        nintDzpvsigCumulative = cms.int32(200),
        nintEta = cms.int32(90),
        nintHit = cms.int32(81),
        nintLayers = cms.int32(26),
        nintMVA = cms.int32(100),
        nintPVz = cms.int32(120),
        nintPhi = cms.int32(36),
        nintPt = cms.int32(40),
        nintPu = cms.int32(130),
        nintTracks = cms.int32(200),
        nintVertcount = cms.int32(161),
        nintVertpos = cms.int32(40),
        nintZpos = cms.int32(60),
        nintdr = cms.int32(100),
        phiRes_nbin = cms.int32(300),
        phiRes_rangeMax = cms.double(0.01),
        phiRes_rangeMin = cms.double(-0.01),
        ptRes_nbin = cms.int32(100),
        ptRes_rangeMax = cms.double(0.1),
        ptRes_rangeMin = cms.double(-0.1),
        seedingLayerSets = cms.vstring(
            'BPix1+BPix2+BPix3+BPix4', 
            'BPix1+BPix2+BPix3+FPix1_pos', 
            'BPix1+BPix2+BPix3+FPix1_neg', 
            'BPix1+BPix2+FPix1_pos+FPix2_pos', 
            'BPix1+BPix2+FPix1_neg+FPix2_neg', 
            'BPix1+FPix1_pos+FPix2_pos+FPix3_pos', 
            'BPix1+FPix1_neg+FPix2_neg+FPix3_neg', 
            'FPix1_pos+FPix2_pos+FPix3_pos+FPix4_pos', 
            'FPix1_neg+FPix2_neg+FPix3_neg+FPix4_neg', 
            'FPix2_pos+FPix3_pos+FPix4_pos+FPix5_pos', 
            'FPix2_neg+FPix3_neg+FPix4_neg+FPix5_neg', 
            'FPix3_pos+FPix4_pos+FPix5_pos+FPix6_pos', 
            'FPix3_neg+FPix4_neg+FPix5_neg+FPix6_neg', 
            'FPix4_pos+FPix5_pos+FPix6_pos+FPix7_pos', 
            'FPix4_neg+FPix5_neg+FPix6_neg+FPix7_neg', 
            'FPix5_pos+FPix6_pos+FPix7_pos+FPix8_pos', 
            'FPix5_neg+FPix6_neg+FPix7_neg+FPix8_neg', 
            'BPix1+BPix2+BPix3', 
            'BPix2+BPix3+BPix4', 
            'BPix1+BPix3+BPix4', 
            'BPix1+BPix2+BPix4', 
            'BPix2+BPix3+FPix1_pos', 
            'BPix2+BPix3+FPix1_neg', 
            'BPix1+BPix2+FPix1_pos', 
            'BPix1+BPix2+FPix1_neg', 
            'BPix2+FPix1_pos+FPix2_pos', 
            'BPix2+FPix1_neg+FPix2_neg', 
            'BPix1+FPix1_pos+FPix2_pos', 
            'BPix1+FPix1_neg+FPix2_neg', 
            'FPix1_pos+FPix2_pos+FPix3_pos', 
            'FPix1_neg+FPix2_neg+FPix3_neg', 
            'BPix1+FPix2_pos+FPix3_pos', 
            'BPix1+FPix2_neg+FPix3_neg', 
            'FPix2_pos+FPix3_pos+FPix4_pos', 
            'FPix2_neg+FPix3_neg+FPix4_neg', 
            'FPix3_pos+FPix4_pos+FPix5_pos', 
            'FPix3_neg+FPix4_neg+FPix5_neg', 
            'FPix4_pos+FPix5_pos+FPix6_pos', 
            'FPix4_neg+FPix5_neg+FPix6_neg', 
            'FPix5_pos+FPix6_pos+FPix7_pos', 
            'FPix5_neg+FPix6_neg+FPix7_neg', 
            'FPix6_pos+FPix7_pos+FPix8_pos', 
            'FPix6_neg+FPix7_neg+FPix8_neg', 
            'BPix1+BPix2', 
            'BPix1+BPix3', 
            'BPix2+BPix3', 
            'BPix1+FPix1_pos', 
            'BPix1+FPix1_neg', 
            'BPix2+FPix1_pos', 
            'BPix2+FPix1_neg'
        ),
        useFabsEta = cms.bool(False),
        useInvPt = cms.bool(False),
        useLogPt = cms.untracked.bool(True),
        useLogVertpos = cms.untracked.bool(True)
    ),
    ignoremissingtrackcollection = cms.untracked.bool(False),
    intimeOnlyTP = cms.bool(True),
    invertRapidityCutTP = cms.bool(False), # cmssw_11_1
    label = cms.VInputTag(
        "generalTracks", "cutsRecoTracksHp", "cutsRecoTracksInitialStep", "cutsRecoTracksHighPtTripletStep",   "cutsRecoTracksInitialStepHp", "cutsRecoTracksHighPtTripletStepHp",   
        "cutsRecoTracksInitialStepByOriginalAlgo", "cutsRecoTracksHighPtTripletStepByOriginalAlgo",   "cutsRecoTracksInitialStepByOriginalAlgoHp", "cutsRecoTracksHighPtTripletStepByOriginalAlgoHp", 
        "generalTracksPt09", "cutsRecoTracksPt09Hp", "cutsRecoTracksBtvLike", "cutsRecoTracksInitialStepByAlgoMask", 
        "cutsRecoTracksHighPtTripletStepByAlgoMask",  "cutsRecoTracksInitialStepByAlgoMaskHp", "cutsRecoTracksHighPtTripletStepByAlgoMaskHp", 
        "cutsRecoTracksPt09InitialStep", "cutsRecoTracksPt09HighPtTripletStep", "cutsRecoTracksPt09InitialStepHp", "cutsRecoTracksPt09HighPtTripletStepHp"
    ),
    label_pileupinfo = cms.InputTag("addPileupInfo"),
    label_tp_effic = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_effic_refvector = cms.bool(False),
    label_tp_fake = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_fake_refvector = cms.bool(False),
    label_tp_nlayers = cms.InputTag("trackingParticleNumberOfLayersProducer","trackerLayers"),
    label_tp_npixellayers = cms.InputTag("trackingParticleNumberOfLayersProducer","pixelLayers"),
    label_tp_nstripstereolayers = cms.InputTag("trackingParticleNumberOfLayersProducer","stripStereoLayers"),
    label_tv = cms.InputTag("mix","MergedTrackTruth"),
    label_vertex = cms.untracked.InputTag("offlinePrimaryVertices"),
    lipTP = cms.double(30.0),
    maxRapidityTP = cms.double(4.5),
    minHitTP = cms.int32(0),
    minRapidityTP = cms.double(-4.5),
    mvaLabels = cms.untracked.PSet(

    ),
    parametersDefiner = cms.string('LhcParametersDefinerForTP'),
    pdgIdTP = cms.vint32(),
    ptMaxTP = cms.double(1e+100),
    ptMinTP = cms.double(0.005),
    signalOnlyTP = cms.bool(False),
    sim = cms.VInputTag(
        cms.InputTag("g4SimHits","TrackerHitsPixelBarrelLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelBarrelHighTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIBLowTof"), 
        cms.InputTag("g4SimHits","TrackerHitsTIBHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIDLowTof"), cms.InputTag("g4SimHits","TrackerHitsTIDHighTof"), cms.InputTag("g4SimHits","TrackerHitsTOBLowTof"), cms.InputTag("g4SimHits","TrackerHitsTOBHighTof"), 
        cms.InputTag("g4SimHits","TrackerHitsTECLowTof"), cms.InputTag("g4SimHits","TrackerHitsTECHighTof")
    ),
    simHitTpMapTag = cms.InputTag("simHitTPAssocProducer"),
    simPVMaxZ = cms.untracked.double(-1),
    stableOnlyTP = cms.bool(False),
    tipTP = cms.double(2.5), #previous 60
    trackCollectionForDrCalculation = cms.InputTag("generalTracks"),
    useGsf = cms.bool(False),
    useLogPt = cms.untracked.bool(True),
    vertexAssociator = cms.untracked.InputTag("VertexAssociatorByPositionAndTracks")
)


trackValidatorTPPtLess09Standalone = cms.EDProducer("MultiTrackValidator", #cmssw_11_1 previous cms.EDAnalyzer 
    cores = cms.InputTag("highPtJets"), #cmssw_10_6  #cmssw_11_1
    UseAssociators = cms.bool(False),
    associators = cms.untracked.VInputTag("trackingParticleRecoTrackAsssociation"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    calculateDrSingleCollection = cms.untracked.bool(True),
    chargedOnlyTP = cms.bool(True),
    dEdx1Tag = cms.InputTag("dedxHarmonic2"),
    dEdx2Tag = cms.InputTag("dedxTruncated40"),
    dirName = cms.string('Tracking/TrackTPPtLess09/'),
    doMVAPlots = cms.untracked.bool(False),
    doPVAssociationPlots = cms.untracked.bool(True),
    doPlotsOnlyForTruePV = cms.untracked.bool(False),
    doRecoTrackPlots = cms.untracked.bool(False),
    doResolutionPlotsForLabels = cms.VInputTag("disabled"),
    doSeedPlots = cms.untracked.bool(False),
    doSimPlots = cms.untracked.bool(False),
    doSimTrackPlots = cms.untracked.bool(True),
    doSummaryPlots = cms.untracked.bool(True),
    dodEdxPlots = cms.untracked.bool(False),
    histoProducerAlgoBlock = cms.PSet(
	mindrj = cms.double(0.001),#cmssw_10_6 
        maxdrj = cms.double(0.1),#cmssw_10_6
        nintdrj = cms.int32(100), #cmssw_10_6
        GpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
   	    invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5 
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.05),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 30.0
        ),
        GpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(35.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.05),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.05),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.05),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.05),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 60.0
        ),
        TpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.05),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        cotThetaRes_nbin = cms.int32(300),
        cotThetaRes_rangeMax = cms.double(0.02),
        cotThetaRes_rangeMin = cms.double(-0.02),
        doMTDPlots = cms.untracked.bool(True), # cmssw_11_1
        dxyDzZoom = cms.double(25),
        dxyRes_nbin = cms.int32(500),
        dxyRes_rangeMax = cms.double(0.1),
        dxyRes_rangeMin = cms.double(-0.1),
        dzRes_nbin = cms.int32(150),
        dzRes_rangeMax = cms.double(0.05),
        dzRes_rangeMin = cms.double(-0.05),
        generalGpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        generalTpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        maxChi2 = cms.double(20),
        maxDeDx = cms.double(10.0),
        maxDxy = cms.double(25),
        maxDz = cms.double(30),
        maxDzpvCumulative = cms.double(0.6),
        maxDzpvsigCumulative = cms.double(10),
        maxEta = cms.double(4.5),
        maxHit = cms.double(80.5),
        maxLayers = cms.double(25.5),
        maxMVA = cms.double(1),
        maxPVz = cms.double(60),
        maxPhi = cms.double(3.1416),
        maxPt = cms.double(1000),
        maxPu = cms.double(259.5),
        maxTracks = cms.double(2000),
        maxVertcount = cms.double(160.5),
        maxVertpos = cms.double(100),
        maxZpos = cms.double(30),
        maxdr = cms.double(1),
        minChi2 = cms.double(0),
        minDeDx = cms.double(0.0),
        minDxy = cms.double(-25),
        minDz = cms.double(-30),
        minEta = cms.double(-4.5),
        minHit = cms.double(-0.5),
        minLayers = cms.double(-0.5),
        minMVA = cms.double(-1),
        minPVz = cms.double(-60),
        minPhi = cms.double(-3.1416),
        minPt = cms.double(0.1),
        minPu = cms.double(-0.5),
        minTracks = cms.double(0),
        minVertcount = cms.double(-0.5),
        minVertpos = cms.double(0.01),
        minZpos = cms.double(-30),
        mindr = cms.double(0.001),
        nintChi2 = cms.int32(40),
        nintDeDx = cms.int32(40),
        nintDxy = cms.int32(100),
        nintDz = cms.int32(60),
        nintDzpvCumulative = cms.int32(240),
        nintDzpvsigCumulative = cms.int32(200),
        nintEta = cms.int32(90),
        nintHit = cms.int32(81),
        nintLayers = cms.int32(26),
        nintMVA = cms.int32(100),
        nintPVz = cms.int32(120),
        nintPhi = cms.int32(36),
        nintPt = cms.int32(40),
        nintPu = cms.int32(130),
        nintTracks = cms.int32(200),
        nintVertcount = cms.int32(161),
        nintVertpos = cms.int32(40),
        nintZpos = cms.int32(60),
        nintdr = cms.int32(100),
        phiRes_nbin = cms.int32(300),
        phiRes_rangeMax = cms.double(0.01),
        phiRes_rangeMin = cms.double(-0.01),
        ptRes_nbin = cms.int32(100),
        ptRes_rangeMax = cms.double(0.1),
        ptRes_rangeMin = cms.double(-0.1),
        seedingLayerSets = cms.vstring(
            'BPix1+BPix2+BPix3+BPix4', 
            'BPix1+BPix2+BPix3+FPix1_pos', 
            'BPix1+BPix2+BPix3+FPix1_neg', 
            'BPix1+BPix2+FPix1_pos+FPix2_pos', 
            'BPix1+BPix2+FPix1_neg+FPix2_neg', 
            'BPix1+FPix1_pos+FPix2_pos+FPix3_pos', 
            'BPix1+FPix1_neg+FPix2_neg+FPix3_neg', 
            'FPix1_pos+FPix2_pos+FPix3_pos+FPix4_pos', 
            'FPix1_neg+FPix2_neg+FPix3_neg+FPix4_neg', 
            'FPix2_pos+FPix3_pos+FPix4_pos+FPix5_pos', 
            'FPix2_neg+FPix3_neg+FPix4_neg+FPix5_neg', 
            'FPix3_pos+FPix4_pos+FPix5_pos+FPix6_pos', 
            'FPix3_neg+FPix4_neg+FPix5_neg+FPix6_neg', 
            'FPix4_pos+FPix5_pos+FPix6_pos+FPix7_pos', 
            'FPix4_neg+FPix5_neg+FPix6_neg+FPix7_neg', 
            'FPix5_pos+FPix6_pos+FPix7_pos+FPix8_pos', 
            'FPix5_neg+FPix6_neg+FPix7_neg+FPix8_neg', 
            'BPix1+BPix2+BPix3', 
            'BPix2+BPix3+BPix4', 
            'BPix1+BPix3+BPix4', 
            'BPix1+BPix2+BPix4', 
            'BPix2+BPix3+FPix1_pos', 
            'BPix2+BPix3+FPix1_neg', 
            'BPix1+BPix2+FPix1_pos', 
            'BPix1+BPix2+FPix1_neg', 
            'BPix2+FPix1_pos+FPix2_pos', 
            'BPix2+FPix1_neg+FPix2_neg', 
            'BPix1+FPix1_pos+FPix2_pos', 
            'BPix1+FPix1_neg+FPix2_neg', 
            'FPix1_pos+FPix2_pos+FPix3_pos', 
            'FPix1_neg+FPix2_neg+FPix3_neg', 
            'BPix1+FPix2_pos+FPix3_pos', 
            'BPix1+FPix2_neg+FPix3_neg', 
            'FPix2_pos+FPix3_pos+FPix4_pos', 
            'FPix2_neg+FPix3_neg+FPix4_neg', 
            'FPix3_pos+FPix4_pos+FPix5_pos', 
            'FPix3_neg+FPix4_neg+FPix5_neg', 
            'FPix4_pos+FPix5_pos+FPix6_pos', 
            'FPix4_neg+FPix5_neg+FPix6_neg', 
            'FPix5_pos+FPix6_pos+FPix7_pos', 
            'FPix5_neg+FPix6_neg+FPix7_neg', 
            'FPix6_pos+FPix7_pos+FPix8_pos', 
            'FPix6_neg+FPix7_neg+FPix8_neg', 
            'BPix1+BPix2', 
            'BPix1+BPix3', 
            'BPix2+BPix3', 
            'BPix1+FPix1_pos', 
            'BPix1+FPix1_neg', 
            'BPix2+FPix1_pos', 
            'BPix2+FPix1_neg'
        ),
        useFabsEta = cms.bool(False),
        useInvPt = cms.bool(False),
        useLogPt = cms.untracked.bool(True),
        useLogVertpos = cms.untracked.bool(True)
    ),
    ignoremissingtrackcollection = cms.untracked.bool(False),
    intimeOnlyTP = cms.bool(True),
    invertRapidityCutTP = cms.bool(False), # cmssw_11_1
    label = cms.VInputTag(
        "generalTracks", "cutsRecoTracksHp", "cutsRecoTracksInitialStep", "cutsRecoTracksHighPtTripletStep",  
        "cutsRecoTracksInitialStepHp", "cutsRecoTracksHighPtTripletStepHp",   
        "cutsRecoTracksInitialStepByOriginalAlgo", "cutsRecoTracksHighPtTripletStepByOriginalAlgo",   "cutsRecoTracksInitialStepByOriginalAlgoHp", "cutsRecoTracksHighPtTripletStepByOriginalAlgoHp", 
        "cutsRecoTracksInitialStepByAlgoMask", "cutsRecoTracksHighPtTripletStepByAlgoMask",   
        "cutsRecoTracksInitialStepByAlgoMaskHp", "cutsRecoTracksHighPtTripletStepByAlgoMaskHp",   
        "cutsRecoTracksPt09InitialStep", 
        "cutsRecoTracksPt09HighPtTripletStep", "cutsRecoTracksPt09InitialStepHp", "cutsRecoTracksPt09HighPtTripletStepHp"
    ),
    label_pileupinfo = cms.InputTag("addPileupInfo"),
    label_tp_effic = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_effic_refvector = cms.bool(False),
    label_tp_fake = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_fake_refvector = cms.bool(False),
    label_tp_nlayers = cms.InputTag("trackingParticleNumberOfLayersProducer","trackerLayers"),
    label_tp_npixellayers = cms.InputTag("trackingParticleNumberOfLayersProducer","pixelLayers"),
    label_tp_nstripstereolayers = cms.InputTag("trackingParticleNumberOfLayersProducer","stripStereoLayers"),
    label_tv = cms.InputTag("mix","MergedTrackTruth"),
    label_vertex = cms.untracked.InputTag("offlinePrimaryVertices"),
    lipTP = cms.double(30.0),
    maxRapidityTP = cms.double(4.5),
    minHitTP = cms.int32(0),
    minRapidityTP = cms.double(-4.5),
    mvaLabels = cms.untracked.PSet(

    ),
    parametersDefiner = cms.string('LhcParametersDefinerForTP'),
    pdgIdTP = cms.vint32(),
    ptMaxTP = cms.double(0.9),
    ptMinTP = cms.double(0.005),
    signalOnlyTP = cms.bool(False),
    sim = cms.VInputTag(
        cms.InputTag("g4SimHits","TrackerHitsPixelBarrelLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelBarrelHighTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIBLowTof"), 
        cms.InputTag("g4SimHits","TrackerHitsTIBHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIDLowTof"), cms.InputTag("g4SimHits","TrackerHitsTIDHighTof"), cms.InputTag("g4SimHits","TrackerHitsTOBLowTof"), cms.InputTag("g4SimHits","TrackerHitsTOBHighTof"), 
        cms.InputTag("g4SimHits","TrackerHitsTECLowTof"), cms.InputTag("g4SimHits","TrackerHitsTECHighTof")
    ),
    simHitTpMapTag = cms.InputTag("simHitTPAssocProducer"),
    simPVMaxZ = cms.untracked.double(-1),
    stableOnlyTP = cms.bool(False),
    tipTP = cms.double(2.5), #previous 60
    trackCollectionForDrCalculation = cms.InputTag("generalTracks"),
    useGsf = cms.bool(False),
    useLogPt = cms.untracked.bool(True),
    vertexAssociator = cms.untracked.InputTag("VertexAssociatorByPositionAndTracks")
)


trackValidatorFromPVStandalone = cms.EDProducer("MultiTrackValidator", #cmssw_11_1 previous cms.EDAnalyzer
    cores = cms.InputTag("highPtJets"), #cmssw_10_6  #cmssw_11_1
    UseAssociators = cms.bool(False),
    associators = cms.untracked.VInputTag("trackingParticleRecoTrackAsssociation"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    calculateDrSingleCollection = cms.untracked.bool(True),
    chargedOnlyTP = cms.bool(True),
    dEdx1Tag = cms.InputTag("dedxHarmonic2"),
    dEdx2Tag = cms.InputTag("dedxTruncated40"),
    dirName = cms.string('Tracking/TrackFromPV/'),
    doMVAPlots = cms.untracked.bool(False),
    doPVAssociationPlots = cms.untracked.bool(False),
    doPlotsOnlyForTruePV = cms.untracked.bool(True),
    doRecoTrackPlots = cms.untracked.bool(True),
    doResolutionPlotsForLabels = cms.VInputTag(),
    doSeedPlots = cms.untracked.bool(False),
    doSimPlots = cms.untracked.bool(True),
    doSimTrackPlots = cms.untracked.bool(True),
    doSummaryPlots = cms.untracked.bool(True),
    dodEdxPlots = cms.untracked.bool(False),
    histoProducerAlgoBlock = cms.PSet(
	mindrj = cms.double(0.001),#cmssw_10_6 
        maxdrj = cms.double(0.1),#cmssw_10_6
        nintdrj = cms.int32(100), #cmssw_10_6
        GpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), #cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5 
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), #cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), #cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.05),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), #cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 30.0
        ),
        GpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), #cmssw_11_1
            lip = cms.double(35.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), #cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), #cmssw_11_1
            intimeOnly = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False), #cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.05),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False), #cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 60.0
        ),
        TpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False), #cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        cotThetaRes_nbin = cms.int32(300),
        cotThetaRes_rangeMax = cms.double(0.02),
        cotThetaRes_rangeMin = cms.double(-0.02),
        doMTDPlots = cms.untracked.bool(True), # cmssw_11_1
        dxyDzZoom = cms.double(25),
        dxyRes_nbin = cms.int32(500),
        dxyRes_rangeMax = cms.double(0.1),
        dxyRes_rangeMin = cms.double(-0.1),
        dzRes_nbin = cms.int32(150),
        dzRes_rangeMax = cms.double(0.05),
        dzRes_rangeMin = cms.double(-0.05),
        generalGpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), #cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        generalTpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False), #cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        maxChi2 = cms.double(20),
        maxDeDx = cms.double(10.0),
        maxDxy = cms.double(25),
        maxDz = cms.double(30),
        maxDzpvCumulative = cms.double(0.6),
        maxDzpvsigCumulative = cms.double(10),
        maxEta = cms.double(4.5),
        maxHit = cms.double(80.5),
        maxLayers = cms.double(25.5),
        maxMVA = cms.double(1),
        maxPVz = cms.double(60),
        maxPhi = cms.double(3.1416),
        maxPt = cms.double(1000),
        maxPu = cms.double(259.5),
        maxTracks = cms.double(2000),
        maxVertcount = cms.double(160.5),
        maxVertpos = cms.double(100),
        maxZpos = cms.double(30),
        maxdr = cms.double(1),
        minChi2 = cms.double(0),
        minDeDx = cms.double(0.0),
        minDxy = cms.double(-25),
        minDz = cms.double(-30),
        minEta = cms.double(-4.5),
        minHit = cms.double(-0.5),
        minLayers = cms.double(-0.5),
        minMVA = cms.double(-1),
        minPVz = cms.double(-60),
        minPhi = cms.double(-3.1416),
        minPt = cms.double(0.1),
        minPu = cms.double(-0.5),
        minTracks = cms.double(0),
        minVertcount = cms.double(-0.5),
        minVertpos = cms.double(0.01),
        minZpos = cms.double(-30),
        mindr = cms.double(0.001),
        nintChi2 = cms.int32(40),
        nintDeDx = cms.int32(40),
        nintDxy = cms.int32(100),
        nintDz = cms.int32(60),
        nintDzpvCumulative = cms.int32(240),
        nintDzpvsigCumulative = cms.int32(200),
        nintEta = cms.int32(90),
        nintHit = cms.int32(81),
        nintLayers = cms.int32(26),
        nintMVA = cms.int32(100),
        nintPVz = cms.int32(120),
        nintPhi = cms.int32(36),
        nintPt = cms.int32(40),
        nintPu = cms.int32(130),
        nintTracks = cms.int32(200),
        nintVertcount = cms.int32(161),
        nintVertpos = cms.int32(40),
        nintZpos = cms.int32(60),
        nintdr = cms.int32(100),
        phiRes_nbin = cms.int32(300),
        phiRes_rangeMax = cms.double(0.01),
        phiRes_rangeMin = cms.double(-0.01),
        ptRes_nbin = cms.int32(100),
        ptRes_rangeMax = cms.double(0.1),
        ptRes_rangeMin = cms.double(-0.1),
        seedingLayerSets = cms.vstring(
            'BPix1+BPix2+BPix3+BPix4', 
            'BPix1+BPix2+BPix3+FPix1_pos', 
            'BPix1+BPix2+BPix3+FPix1_neg', 
            'BPix1+BPix2+FPix1_pos+FPix2_pos', 
            'BPix1+BPix2+FPix1_neg+FPix2_neg', 
            'BPix1+FPix1_pos+FPix2_pos+FPix3_pos', 
            'BPix1+FPix1_neg+FPix2_neg+FPix3_neg', 
            'FPix1_pos+FPix2_pos+FPix3_pos+FPix4_pos', 
            'FPix1_neg+FPix2_neg+FPix3_neg+FPix4_neg', 
            'FPix2_pos+FPix3_pos+FPix4_pos+FPix5_pos', 
            'FPix2_neg+FPix3_neg+FPix4_neg+FPix5_neg', 
            'FPix3_pos+FPix4_pos+FPix5_pos+FPix6_pos', 
            'FPix3_neg+FPix4_neg+FPix5_neg+FPix6_neg', 
            'FPix4_pos+FPix5_pos+FPix6_pos+FPix7_pos', 
            'FPix4_neg+FPix5_neg+FPix6_neg+FPix7_neg', 
            'FPix5_pos+FPix6_pos+FPix7_pos+FPix8_pos', 
            'FPix5_neg+FPix6_neg+FPix7_neg+FPix8_neg', 
            'BPix1+BPix2+BPix3', 
            'BPix2+BPix3+BPix4', 
            'BPix1+BPix3+BPix4', 
            'BPix1+BPix2+BPix4', 
            'BPix2+BPix3+FPix1_pos', 
            'BPix2+BPix3+FPix1_neg', 
            'BPix1+BPix2+FPix1_pos', 
            'BPix1+BPix2+FPix1_neg', 
            'BPix2+FPix1_pos+FPix2_pos', 
            'BPix2+FPix1_neg+FPix2_neg', 
            'BPix1+FPix1_pos+FPix2_pos', 
            'BPix1+FPix1_neg+FPix2_neg', 
            'FPix1_pos+FPix2_pos+FPix3_pos', 
            'FPix1_neg+FPix2_neg+FPix3_neg', 
            'BPix1+FPix2_pos+FPix3_pos', 
            'BPix1+FPix2_neg+FPix3_neg', 
            'FPix2_pos+FPix3_pos+FPix4_pos', 
            'FPix2_neg+FPix3_neg+FPix4_neg', 
            'FPix3_pos+FPix4_pos+FPix5_pos', 
            'FPix3_neg+FPix4_neg+FPix5_neg', 
            'FPix4_pos+FPix5_pos+FPix6_pos', 
            'FPix4_neg+FPix5_neg+FPix6_neg', 
            'FPix5_pos+FPix6_pos+FPix7_pos', 
            'FPix5_neg+FPix6_neg+FPix7_neg', 
            'FPix6_pos+FPix7_pos+FPix8_pos', 
            'FPix6_neg+FPix7_neg+FPix8_neg', 
            'BPix1+BPix2', 
            'BPix1+BPix3', 
            'BPix2+BPix3', 
            'BPix1+FPix1_pos', 
            'BPix1+FPix1_neg', 
            'BPix2+FPix1_pos', 
            'BPix2+FPix1_neg'
        ),
        useFabsEta = cms.bool(False),
        useInvPt = cms.bool(False),
        useLogPt = cms.untracked.bool(True),
        useLogVertpos = cms.untracked.bool(True)
    ),
    ignoremissingtrackcollection = cms.untracked.bool(False),
    intimeOnlyTP = cms.bool(True),
    invertRapidityCutTP = cms.bool(False), # cmssw_11_1
    label = cms.VInputTag(
        "generalTracksFromPV", "cutsRecoTracksFromPVHp", "generalTracksFromPVPt09", "cutsRecoTracksFromPVPt09Hp", "cutsRecoTracksFromPVInitialStep", 
        "cutsRecoTracksFromPVHighPtTripletStep", "cutsRecoTracksFromPVInitialStepHp", "cutsRecoTracksFromPVHighPtTripletStepHp", 
        "cutsRecoTracksFromPVPt09InitialStep", "cutsRecoTracksFromPVPt09HighPtTripletStep", 
        "cutsRecoTracksFromPVPt09InitialStepHp", "cutsRecoTracksFromPVPt09HighPtTripletStepHp",
    ),
    label_pileupinfo = cms.InputTag("addPileupInfo"),
    label_tp_effic = cms.InputTag("trackingParticlesSignal"),
    label_tp_effic_refvector = cms.bool(True),
    label_tp_fake = cms.InputTag("trackingParticlesSignal"),
    label_tp_fake_refvector = cms.bool(True),
    label_tp_nlayers = cms.InputTag("trackingParticleNumberOfLayersProducer","trackerLayers"),
    label_tp_npixellayers = cms.InputTag("trackingParticleNumberOfLayersProducer","pixelLayers"),
    label_tp_nstripstereolayers = cms.InputTag("trackingParticleNumberOfLayersProducer","stripStereoLayers"),
    label_tv = cms.InputTag("mix","MergedTrackTruth"),
    label_vertex = cms.untracked.InputTag("offlinePrimaryVertices"),
    lipTP = cms.double(30.0),
    maxRapidityTP = cms.double(4.5),
    minHitTP = cms.int32(0),
    minRapidityTP = cms.double(-4.5),
    mvaLabels = cms.untracked.PSet(

    ),
    parametersDefiner = cms.string('LhcParametersDefinerForTP'),
    pdgIdTP = cms.vint32(),
    ptMaxTP = cms.double(1e+100),
    ptMinTP = cms.double(0.005),
    signalOnlyTP = cms.bool(False),
    sim = cms.VInputTag(
        cms.InputTag("g4SimHits","TrackerHitsPixelBarrelLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelBarrelHighTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIBLowTof"), 
        cms.InputTag("g4SimHits","TrackerHitsTIBHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIDLowTof"), cms.InputTag("g4SimHits","TrackerHitsTIDHighTof"), cms.InputTag("g4SimHits","TrackerHitsTOBLowTof"), cms.InputTag("g4SimHits","TrackerHitsTOBHighTof"), 
        cms.InputTag("g4SimHits","TrackerHitsTECLowTof"), cms.InputTag("g4SimHits","TrackerHitsTECHighTof")
    ),
    simHitTpMapTag = cms.InputTag("simHitTPAssocProducer"),
    simPVMaxZ = cms.untracked.double(-1),
    stableOnlyTP = cms.bool(False),
    tipTP = cms.double(2.5), #previous 60
    trackCollectionForDrCalculation = cms.InputTag("generalTracksFromPV"),
    useGsf = cms.bool(False),
    useLogPt = cms.untracked.bool(True),
    vertexAssociator = cms.untracked.InputTag("VertexAssociatorByPositionAndTracks")
)


trackValidatorFromPVAllTPStandalone = cms.EDProducer("MultiTrackValidator", #cmssw_11_1 previous cms.EDAnalyzer
    cores = cms.InputTag("highPtJets"), #cmssw_10_6 #cmssw_11_1
    UseAssociators = cms.bool(False),
    associators = cms.untracked.VInputTag("trackingParticleRecoTrackAsssociation"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    calculateDrSingleCollection = cms.untracked.bool(True),
    chargedOnlyTP = cms.bool(True),
    dEdx1Tag = cms.InputTag("dedxHarmonic2"),
    dEdx2Tag = cms.InputTag("dedxTruncated40"),
    dirName = cms.string('Tracking/TrackFromPVAllTP/'),
    doMVAPlots = cms.untracked.bool(False),
    doPVAssociationPlots = cms.untracked.bool(False),
    doPlotsOnlyForTruePV = cms.untracked.bool(True),
    doRecoTrackPlots = cms.untracked.bool(True),
    doResolutionPlotsForLabels = cms.VInputTag("disabled"),
    doSeedPlots = cms.untracked.bool(False),
    doSimPlots = cms.untracked.bool(False),
    doSimTrackPlots = cms.untracked.bool(False),
    doSummaryPlots = cms.untracked.bool(True),
    dodEdxPlots = cms.untracked.bool(False),
    histoProducerAlgoBlock = cms.PSet(
	mindrj = cms.double(0.001),#cmssw_10_6 
        maxdrj = cms.double(0.1),#cmssw_10_6
        nintdrj = cms.int32(100), #cmssw_10_6
        GpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5 
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.05),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 30.0
        ),
        GpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(35.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.05),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 60.0
        ),
        TpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        cotThetaRes_nbin = cms.int32(300),
        cotThetaRes_rangeMax = cms.double(0.02),
        cotThetaRes_rangeMin = cms.double(-0.02),
        doMTDPlots = cms.untracked.bool(True), # cmssw_11_1
        dxyDzZoom = cms.double(25),
        dxyRes_nbin = cms.int32(500),
        dxyRes_rangeMax = cms.double(0.1),
        dxyRes_rangeMin = cms.double(-0.1),
        dzRes_nbin = cms.int32(150),
        dzRes_rangeMax = cms.double(0.05),
        dzRes_rangeMin = cms.double(-0.05),
        generalGpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        generalTpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        maxChi2 = cms.double(20),
        maxDeDx = cms.double(10.0),
        maxDxy = cms.double(25),
        maxDz = cms.double(30),
        maxDzpvCumulative = cms.double(0.6),
        maxDzpvsigCumulative = cms.double(10),
        maxEta = cms.double(4.5),
        maxHit = cms.double(80.5),
        maxLayers = cms.double(25.5),
        maxMVA = cms.double(1),
        maxPVz = cms.double(60),
        maxPhi = cms.double(3.1416),
        maxPt = cms.double(1000),
        maxPu = cms.double(259.5),
        maxTracks = cms.double(2000),
        maxVertcount = cms.double(160.5),
        maxVertpos = cms.double(100),
        maxZpos = cms.double(30),
        maxdr = cms.double(1),
        minChi2 = cms.double(0),
        minDeDx = cms.double(0.0),
        minDxy = cms.double(-25),
        minDz = cms.double(-30),
        minEta = cms.double(-4.5),
        minHit = cms.double(-0.5),
        minLayers = cms.double(-0.5),
        minMVA = cms.double(-1),
        minPVz = cms.double(-60),
        minPhi = cms.double(-3.1416),
        minPt = cms.double(0.1),
        minPu = cms.double(-0.5),
        minTracks = cms.double(0),
        minVertcount = cms.double(-0.5),
        minVertpos = cms.double(0.01),
        minZpos = cms.double(-30),
        mindr = cms.double(0.001),
        nintChi2 = cms.int32(40),
        nintDeDx = cms.int32(40),
        nintDxy = cms.int32(100),
        nintDz = cms.int32(60),
        nintDzpvCumulative = cms.int32(240),
        nintDzpvsigCumulative = cms.int32(200),
        nintEta = cms.int32(90),
        nintHit = cms.int32(81),
        nintLayers = cms.int32(26),
        nintMVA = cms.int32(100),
        nintPVz = cms.int32(120),
        nintPhi = cms.int32(36),
        nintPt = cms.int32(40),
        nintPu = cms.int32(130),
        nintTracks = cms.int32(200),
        nintVertcount = cms.int32(161),
        nintVertpos = cms.int32(40),
        nintZpos = cms.int32(60),
        nintdr = cms.int32(100),
        phiRes_nbin = cms.int32(300),
        phiRes_rangeMax = cms.double(0.01),
        phiRes_rangeMin = cms.double(-0.01),
        ptRes_nbin = cms.int32(100),
        ptRes_rangeMax = cms.double(0.1),
        ptRes_rangeMin = cms.double(-0.1),
        seedingLayerSets = cms.vstring(
            'BPix1+BPix2+BPix3+BPix4', 
            'BPix1+BPix2+BPix3+FPix1_pos', 
            'BPix1+BPix2+BPix3+FPix1_neg', 
            'BPix1+BPix2+FPix1_pos+FPix2_pos', 
            'BPix1+BPix2+FPix1_neg+FPix2_neg', 
            'BPix1+FPix1_pos+FPix2_pos+FPix3_pos', 
            'BPix1+FPix1_neg+FPix2_neg+FPix3_neg', 
            'FPix1_pos+FPix2_pos+FPix3_pos+FPix4_pos', 
            'FPix1_neg+FPix2_neg+FPix3_neg+FPix4_neg', 
            'FPix2_pos+FPix3_pos+FPix4_pos+FPix5_pos', 
            'FPix2_neg+FPix3_neg+FPix4_neg+FPix5_neg', 
            'FPix3_pos+FPix4_pos+FPix5_pos+FPix6_pos', 
            'FPix3_neg+FPix4_neg+FPix5_neg+FPix6_neg', 
            'FPix4_pos+FPix5_pos+FPix6_pos+FPix7_pos', 
            'FPix4_neg+FPix5_neg+FPix6_neg+FPix7_neg', 
            'FPix5_pos+FPix6_pos+FPix7_pos+FPix8_pos', 
            'FPix5_neg+FPix6_neg+FPix7_neg+FPix8_neg', 
            'BPix1+BPix2+BPix3', 
            'BPix2+BPix3+BPix4', 
            'BPix1+BPix3+BPix4', 
            'BPix1+BPix2+BPix4', 
            'BPix2+BPix3+FPix1_pos', 
            'BPix2+BPix3+FPix1_neg', 
            'BPix1+BPix2+FPix1_pos', 
            'BPix1+BPix2+FPix1_neg', 
            'BPix2+FPix1_pos+FPix2_pos', 
            'BPix2+FPix1_neg+FPix2_neg', 
            'BPix1+FPix1_pos+FPix2_pos', 
            'BPix1+FPix1_neg+FPix2_neg', 
            'FPix1_pos+FPix2_pos+FPix3_pos', 
            'FPix1_neg+FPix2_neg+FPix3_neg', 
            'BPix1+FPix2_pos+FPix3_pos', 
            'BPix1+FPix2_neg+FPix3_neg', 
            'FPix2_pos+FPix3_pos+FPix4_pos', 
            'FPix2_neg+FPix3_neg+FPix4_neg', 
            'FPix3_pos+FPix4_pos+FPix5_pos', 
            'FPix3_neg+FPix4_neg+FPix5_neg', 
            'FPix4_pos+FPix5_pos+FPix6_pos', 
            'FPix4_neg+FPix5_neg+FPix6_neg', 
            'FPix5_pos+FPix6_pos+FPix7_pos', 
            'FPix5_neg+FPix6_neg+FPix7_neg', 
            'FPix6_pos+FPix7_pos+FPix8_pos', 
            'FPix6_neg+FPix7_neg+FPix8_neg', 
            'BPix1+BPix2', 
            'BPix1+BPix3', 
            'BPix2+BPix3', 
            'BPix1+FPix1_pos', 
            'BPix1+FPix1_neg', 
            'BPix2+FPix1_pos', 
            'BPix2+FPix1_neg'
        ),
        useFabsEta = cms.bool(False),
        useInvPt = cms.bool(False),
        useLogPt = cms.untracked.bool(True),
        useLogVertpos = cms.untracked.bool(True)
    ),
    ignoremissingtrackcollection = cms.untracked.bool(False),
    intimeOnlyTP = cms.bool(True),
    invertRapidityCutTP = cms.bool(False), # cmssw_11_1
    label = cms.VInputTag(
        "generalTracksFromPV", "cutsRecoTracksFromPVHp", "generalTracksFromPVPt09", "cutsRecoTracksFromPVPt09Hp", "cutsRecoTracksFromPVInitialStep", 
        "cutsRecoTracksFromPVHighPtTripletStep", "cutsRecoTracksFromPVInitialStepHp", "cutsRecoTracksFromPVHighPtTripletStepHp", 
        "cutsRecoTracksFromPVPt09InitialStep", "cutsRecoTracksFromPVPt09HighPtTripletStep",  
        "cutsRecoTracksFromPVPt09InitialStepHp", "cutsRecoTracksFromPVPt09HighPtTripletStepHp"
    ),
    label_pileupinfo = cms.InputTag("addPileupInfo"),
    label_tp_effic = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_effic_refvector = cms.bool(False),
    label_tp_fake = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_fake_refvector = cms.bool(False),
    label_tp_nlayers = cms.InputTag("trackingParticleNumberOfLayersProducer","trackerLayers"),
    label_tp_npixellayers = cms.InputTag("trackingParticleNumberOfLayersProducer","pixelLayers"),
    label_tp_nstripstereolayers = cms.InputTag("trackingParticleNumberOfLayersProducer","stripStereoLayers"),
    label_tv = cms.InputTag("mix","MergedTrackTruth"),
    label_vertex = cms.untracked.InputTag("offlinePrimaryVertices"),
    lipTP = cms.double(30.0),
    maxRapidityTP = cms.double(4.5),
    minHitTP = cms.int32(0),
    minRapidityTP = cms.double(-4.5),
    mvaLabels = cms.untracked.PSet(

    ),
    parametersDefiner = cms.string('LhcParametersDefinerForTP'),
    pdgIdTP = cms.vint32(),
    ptMaxTP = cms.double(1e+100),
    ptMinTP = cms.double(0.005),
    signalOnlyTP = cms.bool(False),
    sim = cms.VInputTag(
        cms.InputTag("g4SimHits","TrackerHitsPixelBarrelLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelBarrelHighTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIBLowTof"), 
        cms.InputTag("g4SimHits","TrackerHitsTIBHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIDLowTof"), cms.InputTag("g4SimHits","TrackerHitsTIDHighTof"), cms.InputTag("g4SimHits","TrackerHitsTOBLowTof"), cms.InputTag("g4SimHits","TrackerHitsTOBHighTof"), 
        cms.InputTag("g4SimHits","TrackerHitsTECLowTof"), cms.InputTag("g4SimHits","TrackerHitsTECHighTof")
    ),
    simHitTpMapTag = cms.InputTag("simHitTPAssocProducer"),
    simPVMaxZ = cms.untracked.double(-1),
    stableOnlyTP = cms.bool(False),
    tipTP = cms.double(2.5), #previous 60
    trackCollectionForDrCalculation = cms.InputTag("generalTracksFromPV"),
    useGsf = cms.bool(False),
    useLogPt = cms.untracked.bool(True),
    vertexAssociator = cms.untracked.InputTag("VertexAssociatorByPositionAndTracks")
)


trackValidatorAllTPEfficStandalone = cms.EDProducer("MultiTrackValidator", #cmssw_11_1 previous cms.EDAnalyzer
    cores = cms.InputTag("highPtJets"), #cmssw_10_6  #cmssw_11_1
    UseAssociators = cms.bool(False),
    associators = cms.untracked.VInputTag("trackingParticleRecoTrackAsssociation"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    calculateDrSingleCollection = cms.untracked.bool(True),
    chargedOnlyTP = cms.bool(True),
    dEdx1Tag = cms.InputTag("dedxHarmonic2"),
    dEdx2Tag = cms.InputTag("dedxTruncated40"),
    dirName = cms.string('Tracking/TrackAllTPEffic/'),
    doMVAPlots = cms.untracked.bool(False),
    doPVAssociationPlots = cms.untracked.bool(False),
    doPlotsOnlyForTruePV = cms.untracked.bool(False),
    doRecoTrackPlots = cms.untracked.bool(True),
    doResolutionPlotsForLabels = cms.VInputTag("disabled"),
    doSeedPlots = cms.untracked.bool(False),
    doSimPlots = cms.untracked.bool(False),
    doSimTrackPlots = cms.untracked.bool(True),
    doSummaryPlots = cms.untracked.bool(True),
    dodEdxPlots = cms.untracked.bool(False),
    histoProducerAlgoBlock = cms.PSet(
	mindrj = cms.double(0.001),#cmssw_10_6 
        maxdrj = cms.double(0.1),#cmssw_10_6
        nintdrj = cms.int32(100), #cmssw_10_6
        GpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5 
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.05),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 30.0
        ),
        GpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(35.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(False),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(False),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.05),
            signalOnly = cms.bool(False),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(False),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 60.0
        ),
        TpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(False),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        cotThetaRes_nbin = cms.int32(300),
        cotThetaRes_rangeMax = cms.double(0.02),
        cotThetaRes_rangeMin = cms.double(-0.02),
        doMTDPlots = cms.untracked.bool(True), # cmssw_11_1
        dxyDzZoom = cms.double(25),
        dxyRes_nbin = cms.int32(500),
        dxyRes_rangeMax = cms.double(0.1),
        dxyRes_rangeMin = cms.double(-0.1),
        dzRes_nbin = cms.int32(150),
        dzRes_rangeMax = cms.double(0.05),
        dzRes_rangeMin = cms.double(-0.05),
        generalGpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        generalTpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(False),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        maxChi2 = cms.double(20),
        maxDeDx = cms.double(10.0),
        maxDxy = cms.double(25),
        maxDz = cms.double(30),
        maxDzpvCumulative = cms.double(0.6),
        maxDzpvsigCumulative = cms.double(10),
        maxEta = cms.double(4.5),
        maxHit = cms.double(80.5),
        maxLayers = cms.double(25.5),
        maxMVA = cms.double(1),
        maxPVz = cms.double(60),
        maxPhi = cms.double(3.1416),
        maxPt = cms.double(1000),
        maxPu = cms.double(259.5),
        maxTracks = cms.double(2000),
        maxVertcount = cms.double(160.5),
        maxVertpos = cms.double(100),
        maxZpos = cms.double(30),
        maxdr = cms.double(1),
        minChi2 = cms.double(0),
        minDeDx = cms.double(0.0),
        minDxy = cms.double(-25),
        minDz = cms.double(-30),
        minEta = cms.double(-4.5),
        minHit = cms.double(-0.5),
        minLayers = cms.double(-0.5),
        minMVA = cms.double(-1),
        minPVz = cms.double(-60),
        minPhi = cms.double(-3.1416),
        minPt = cms.double(0.1),
        minPu = cms.double(-0.5),
        minTracks = cms.double(0),
        minVertcount = cms.double(-0.5),
        minVertpos = cms.double(0.01),
        minZpos = cms.double(-30),
        mindr = cms.double(0.001),
        nintChi2 = cms.int32(40),
        nintDeDx = cms.int32(40),
        nintDxy = cms.int32(100),
        nintDz = cms.int32(60),
        nintDzpvCumulative = cms.int32(240),
        nintDzpvsigCumulative = cms.int32(200),
        nintEta = cms.int32(90),
        nintHit = cms.int32(81),
        nintLayers = cms.int32(26),
        nintMVA = cms.int32(100),
        nintPVz = cms.int32(120),
        nintPhi = cms.int32(36),
        nintPt = cms.int32(40),
        nintPu = cms.int32(130),
        nintTracks = cms.int32(200),
        nintVertcount = cms.int32(161),
        nintVertpos = cms.int32(40),
        nintZpos = cms.int32(60),
        nintdr = cms.int32(100),
        phiRes_nbin = cms.int32(300),
        phiRes_rangeMax = cms.double(0.01),
        phiRes_rangeMin = cms.double(-0.01),
        ptRes_nbin = cms.int32(100),
        ptRes_rangeMax = cms.double(0.1),
        ptRes_rangeMin = cms.double(-0.1),
        seedingLayerSets = cms.vstring(
            'BPix1+BPix2+BPix3+BPix4', 
            'BPix1+BPix2+BPix3+FPix1_pos', 
            'BPix1+BPix2+BPix3+FPix1_neg', 
            'BPix1+BPix2+FPix1_pos+FPix2_pos', 
            'BPix1+BPix2+FPix1_neg+FPix2_neg', 
            'BPix1+FPix1_pos+FPix2_pos+FPix3_pos', 
            'BPix1+FPix1_neg+FPix2_neg+FPix3_neg', 
            'FPix1_pos+FPix2_pos+FPix3_pos+FPix4_pos', 
            'FPix1_neg+FPix2_neg+FPix3_neg+FPix4_neg', 
            'FPix2_pos+FPix3_pos+FPix4_pos+FPix5_pos', 
            'FPix2_neg+FPix3_neg+FPix4_neg+FPix5_neg', 
            'FPix3_pos+FPix4_pos+FPix5_pos+FPix6_pos', 
            'FPix3_neg+FPix4_neg+FPix5_neg+FPix6_neg', 
            'FPix4_pos+FPix5_pos+FPix6_pos+FPix7_pos', 
            'FPix4_neg+FPix5_neg+FPix6_neg+FPix7_neg', 
            'FPix5_pos+FPix6_pos+FPix7_pos+FPix8_pos', 
            'FPix5_neg+FPix6_neg+FPix7_neg+FPix8_neg', 
            'BPix1+BPix2+BPix3', 
            'BPix2+BPix3+BPix4', 
            'BPix1+BPix3+BPix4', 
            'BPix1+BPix2+BPix4', 
            'BPix2+BPix3+FPix1_pos', 
            'BPix2+BPix3+FPix1_neg', 
            'BPix1+BPix2+FPix1_pos', 
            'BPix1+BPix2+FPix1_neg', 
            'BPix2+FPix1_pos+FPix2_pos', 
            'BPix2+FPix1_neg+FPix2_neg', 
            'BPix1+FPix1_pos+FPix2_pos', 
            'BPix1+FPix1_neg+FPix2_neg', 
            'FPix1_pos+FPix2_pos+FPix3_pos', 
            'FPix1_neg+FPix2_neg+FPix3_neg', 
            'BPix1+FPix2_pos+FPix3_pos', 
            'BPix1+FPix2_neg+FPix3_neg', 
            'FPix2_pos+FPix3_pos+FPix4_pos', 
            'FPix2_neg+FPix3_neg+FPix4_neg', 
            'FPix3_pos+FPix4_pos+FPix5_pos', 
            'FPix3_neg+FPix4_neg+FPix5_neg', 
            'FPix4_pos+FPix5_pos+FPix6_pos', 
            'FPix4_neg+FPix5_neg+FPix6_neg', 
            'FPix5_pos+FPix6_pos+FPix7_pos', 
            'FPix5_neg+FPix6_neg+FPix7_neg', 
            'FPix6_pos+FPix7_pos+FPix8_pos', 
            'FPix6_neg+FPix7_neg+FPix8_neg', 
            'BPix1+BPix2', 
            'BPix1+BPix3', 
            'BPix2+BPix3', 
            'BPix1+FPix1_pos', 
            'BPix1+FPix1_neg', 
            'BPix2+FPix1_pos', 
            'BPix2+FPix1_neg'
        ),
        useFabsEta = cms.bool(False),
        useInvPt = cms.bool(False),
        useLogPt = cms.untracked.bool(True),
        useLogVertpos = cms.untracked.bool(True)
    ),
    ignoremissingtrackcollection = cms.untracked.bool(False),
    intimeOnlyTP = cms.bool(True),
    invertRapidityCutTP = cms.bool(False), # cmssw_11_1
    label = cms.VInputTag(
        "generalTracks", "cutsRecoTracksHp", "cutsRecoTracksInitialStep", "cutsRecoTracksHighPtTripletStep", 
        "cutsRecoTracksInitialStepHp", "cutsRecoTracksHighPtTripletStepHp", 
        "cutsRecoTracksInitialStepByOriginalAlgo", "cutsRecoTracksHighPtTripletStepByOriginalAlgo",  "cutsRecoTracksInitialStepByOriginalAlgoHp", "cutsRecoTracksHighPtTripletStepByOriginalAlgoHp"
    ),
    label_pileupinfo = cms.InputTag("addPileupInfo"),
    label_tp_effic = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_effic_refvector = cms.bool(False),
    label_tp_fake = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_fake_refvector = cms.bool(False),
    label_tp_nlayers = cms.InputTag("trackingParticleNumberOfLayersProducer","trackerLayers"),
    label_tp_npixellayers = cms.InputTag("trackingParticleNumberOfLayersProducer","pixelLayers"),
    label_tp_nstripstereolayers = cms.InputTag("trackingParticleNumberOfLayersProducer","stripStereoLayers"),
    label_tv = cms.InputTag("mix","MergedTrackTruth"),
    label_vertex = cms.untracked.InputTag("offlinePrimaryVertices"),
    lipTP = cms.double(30.0),
    maxRapidityTP = cms.double(4.5),
    minHitTP = cms.int32(0),
    minRapidityTP = cms.double(-4.5),
    mvaLabels = cms.untracked.PSet(

    ),
    parametersDefiner = cms.string('LhcParametersDefinerForTP'),
    pdgIdTP = cms.vint32(),
    ptMaxTP = cms.double(1e+100),
    ptMinTP = cms.double(0.005),
    signalOnlyTP = cms.bool(False),
    sim = cms.VInputTag(
        cms.InputTag("g4SimHits","TrackerHitsPixelBarrelLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelBarrelHighTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIBLowTof"), 
        cms.InputTag("g4SimHits","TrackerHitsTIBHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIDLowTof"), cms.InputTag("g4SimHits","TrackerHitsTIDHighTof"), cms.InputTag("g4SimHits","TrackerHitsTOBLowTof"), cms.InputTag("g4SimHits","TrackerHitsTOBHighTof"), 
        cms.InputTag("g4SimHits","TrackerHitsTECLowTof"), cms.InputTag("g4SimHits","TrackerHitsTECHighTof")
    ),
    simHitTpMapTag = cms.InputTag("simHitTPAssocProducer"),
    simPVMaxZ = cms.untracked.double(-1),
    stableOnlyTP = cms.bool(False),
    tipTP = cms.double(2.5), #previous 60
    trackCollectionForDrCalculation = cms.InputTag("generalTracks"),
    useGsf = cms.bool(False),
    useLogPt = cms.untracked.bool(True),
    vertexAssociator = cms.untracked.InputTag("VertexAssociatorByPositionAndTracks")
)

trackValidatorBHadronTrackingOnly = cms.EDProducer("MultiTrackValidator", #cmssw_11_1 previous cms.EDAnalyzer
    cores = cms.InputTag("highPtJetsForTrk"), #cmssw_10_6 #cmssw_11_1
    UseAssociators = cms.bool(False),
    associators = cms.untracked.VInputTag("trackingParticleRecoTrackAsssociation"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    calculateDrSingleCollection = cms.untracked.bool(True),
    chargedOnlyTP = cms.bool(True),
    dEdx1Tag = cms.InputTag("dedxHarmonic2"),
    dEdx2Tag = cms.InputTag("dedxTruncated40"),
    dirName = cms.string('Tracking/TrackBHadron/'),
    doMVAPlots = cms.untracked.bool(False),
    doPVAssociationPlots = cms.untracked.bool(True),
    doPlotsOnlyForTruePV = cms.untracked.bool(False),
    doRecoTrackPlots = cms.untracked.bool(False),
    doResolutionPlotsForLabels = cms.VInputTag("generalTracks", "cutsRecoTracksHp", "generalTracksPt09", "cutsRecoTracksBtvLike"),
    doSeedPlots = cms.untracked.bool(False),
    doSimPlots = cms.untracked.bool(True),
    doSimTrackPlots = cms.untracked.bool(True),
    doSummaryPlots = cms.untracked.bool(True),
    dodEdxPlots = cms.untracked.bool(False),
    histoProducerAlgoBlock = cms.PSet(
	mindrj = cms.double(0.001),#cmssw_10_6 
        maxdrj = cms.double(0.1),#cmssw_10_6
        nintdrj = cms.int32(100), #cmssw_10_6
        GpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5 
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.05),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 30.0
        ),
        GpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(35.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.05),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 60.0
        ),
        TpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        cotThetaRes_nbin = cms.int32(300),
        cotThetaRes_rangeMax = cms.double(0.02),
        cotThetaRes_rangeMin = cms.double(-0.02),
        doMTDPlots = cms.untracked.bool(True), # cmssw_11_1
        dxyDzZoom = cms.double(25),
        dxyRes_nbin = cms.int32(500),
        dxyRes_rangeMax = cms.double(0.1),
        dxyRes_rangeMin = cms.double(-0.1),
        dzRes_nbin = cms.int32(150),
        dzRes_rangeMax = cms.double(0.05),
        dzRes_rangeMin = cms.double(-0.05),
        generalGpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        generalTpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False), # cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        maxChi2 = cms.double(20),
        maxDeDx = cms.double(10.0),
        maxDxy = cms.double(25),
        maxDz = cms.double(30),
        maxDzpvCumulative = cms.double(0.6),
        maxDzpvsigCumulative = cms.double(10),
        maxEta = cms.double(4.5),
        maxHit = cms.double(80.5),
        maxLayers = cms.double(25.5),
        maxMVA = cms.double(1),
        maxPVz = cms.double(60),
        maxPhi = cms.double(3.1416),
        maxPt = cms.double(1000),
        maxPu = cms.double(259.5),
        maxTracks = cms.double(2000),
        maxVertcount = cms.double(160.5),
        maxVertpos = cms.double(100),
        maxZpos = cms.double(30),
        maxdr = cms.double(1),
        minChi2 = cms.double(0),
        minDeDx = cms.double(0.0),
        minDxy = cms.double(-25),
        minDz = cms.double(-30),
        minEta = cms.double(-4.5),
        minHit = cms.double(-0.5),
        minLayers = cms.double(-0.5),
        minMVA = cms.double(-1),
        minPVz = cms.double(-60),
        minPhi = cms.double(-3.1416),
        minPt = cms.double(0.1),
        minPu = cms.double(-0.5),
        minTracks = cms.double(0),
        minVertcount = cms.double(-0.5),
        minVertpos = cms.double(0.01),
        minZpos = cms.double(-30),
        mindr = cms.double(0.001),
        nintChi2 = cms.int32(40),
        nintDeDx = cms.int32(40),
        nintDxy = cms.int32(100),
        nintDz = cms.int32(60),
        nintDzpvCumulative = cms.int32(240),
        nintDzpvsigCumulative = cms.int32(200),
        nintEta = cms.int32(90),
        nintHit = cms.int32(81),
        nintLayers = cms.int32(26),
        nintMVA = cms.int32(100),
        nintPVz = cms.int32(120),
        nintPhi = cms.int32(36),
        nintPt = cms.int32(40),
        nintPu = cms.int32(130),
        nintTracks = cms.int32(200),
        nintVertcount = cms.int32(161),
        nintVertpos = cms.int32(40),
        nintZpos = cms.int32(60),
        nintdr = cms.int32(100),
        phiRes_nbin = cms.int32(300),
        phiRes_rangeMax = cms.double(0.01),
        phiRes_rangeMin = cms.double(-0.01),
        ptRes_nbin = cms.int32(100),
        ptRes_rangeMax = cms.double(0.1),
        ptRes_rangeMin = cms.double(-0.1),
        seedingLayerSets = cms.vstring(
            'BPix1+BPix2+BPix3+BPix4', 
            'BPix1+BPix2+BPix3+FPix1_pos', 
            'BPix1+BPix2+BPix3+FPix1_neg', 
            'BPix1+BPix2+FPix1_pos+FPix2_pos', 
            'BPix1+BPix2+FPix1_neg+FPix2_neg', 
            'BPix1+FPix1_pos+FPix2_pos+FPix3_pos', 
            'BPix1+FPix1_neg+FPix2_neg+FPix3_neg', 
            'FPix1_pos+FPix2_pos+FPix3_pos+FPix4_pos', 
            'FPix1_neg+FPix2_neg+FPix3_neg+FPix4_neg', 
            'FPix2_pos+FPix3_pos+FPix4_pos+FPix5_pos', 
            'FPix2_neg+FPix3_neg+FPix4_neg+FPix5_neg', 
            'FPix3_pos+FPix4_pos+FPix5_pos+FPix6_pos', 
            'FPix3_neg+FPix4_neg+FPix5_neg+FPix6_neg', 
            'FPix4_pos+FPix5_pos+FPix6_pos+FPix7_pos', 
            'FPix4_neg+FPix5_neg+FPix6_neg+FPix7_neg', 
            'FPix5_pos+FPix6_pos+FPix7_pos+FPix8_pos', 
            'FPix5_neg+FPix6_neg+FPix7_neg+FPix8_neg', 
            'BPix1+BPix2+BPix3', 
            'BPix2+BPix3+BPix4', 
            'BPix1+BPix3+BPix4', 
            'BPix1+BPix2+BPix4', 
            'BPix2+BPix3+FPix1_pos', 
            'BPix2+BPix3+FPix1_neg', 
            'BPix1+BPix2+FPix1_pos', 
            'BPix1+BPix2+FPix1_neg', 
            'BPix2+FPix1_pos+FPix2_pos', 
            'BPix2+FPix1_neg+FPix2_neg', 
            'BPix1+FPix1_pos+FPix2_pos', 
            'BPix1+FPix1_neg+FPix2_neg', 
            'FPix1_pos+FPix2_pos+FPix3_pos', 
            'FPix1_neg+FPix2_neg+FPix3_neg', 
            'BPix1+FPix2_pos+FPix3_pos', 
            'BPix1+FPix2_neg+FPix3_neg', 
            'FPix2_pos+FPix3_pos+FPix4_pos', 
            'FPix2_neg+FPix3_neg+FPix4_neg', 
            'FPix3_pos+FPix4_pos+FPix5_pos', 
            'FPix3_neg+FPix4_neg+FPix5_neg', 
            'FPix4_pos+FPix5_pos+FPix6_pos', 
            'FPix4_neg+FPix5_neg+FPix6_neg', 
            'FPix5_pos+FPix6_pos+FPix7_pos', 
            'FPix5_neg+FPix6_neg+FPix7_neg', 
            'FPix6_pos+FPix7_pos+FPix8_pos', 
            'FPix6_neg+FPix7_neg+FPix8_neg', 
            'BPix1+BPix2', 
            'BPix1+BPix3', 
            'BPix2+BPix3', 
            'BPix1+FPix1_pos', 
            'BPix1+FPix1_neg', 
            'BPix2+FPix1_pos', 
            'BPix2+FPix1_neg'
        ),
        useFabsEta = cms.bool(False),
        useInvPt = cms.bool(False),
        useLogPt = cms.untracked.bool(True),
        useLogVertpos = cms.untracked.bool(True)
    ),
    ignoremissingtrackcollection = cms.untracked.bool(False),
    intimeOnlyTP = cms.bool(True),
    invertRapidityCutTP = cms.bool(False), # cmssw_11_1
    label = cms.VInputTag(
        "generalTracks", "cutsRecoTracksHp", "cutsRecoTracksInitialStep", "cutsRecoTracksHighPtTripletStep", 
        "cutsRecoTracksInitialStepHp", "cutsRecoTracksHighPtTripletStepHp",
        "cutsRecoTracksInitialStepByOriginalAlgo", "cutsRecoTracksHighPtTripletStepByOriginalAlgo",  "cutsRecoTracksInitialStepByOriginalAlgoHp", "cutsRecoTracksHighPtTripletStepByOriginalAlgoHp", 
        "cutsRecoTracksBtvLike", "cutsRecoTracksInitialStepByAlgoMask", "cutsRecoTracksHighPtTripletStepByAlgoMask", 
        "cutsRecoTracksInitialStepByAlgoMaskHp", "cutsRecoTracksHighPtTripletStepByAlgoMaskHp"
    ),
    label_pileupinfo = cms.InputTag("addPileupInfo"),
    label_tp_effic = cms.InputTag("trackingParticlesBHadron"),
    label_tp_effic_refvector = cms.bool(True),
    label_tp_fake = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_fake_refvector = cms.bool(False),
    label_tp_nlayers = cms.InputTag("trackingParticleNumberOfLayersProducer","trackerLayers"),
    label_tp_npixellayers = cms.InputTag("trackingParticleNumberOfLayersProducer","pixelLayers"),
    label_tp_nstripstereolayers = cms.InputTag("trackingParticleNumberOfLayersProducer","stripStereoLayers"),
    label_tv = cms.InputTag("mix","MergedTrackTruth"),
    label_vertex = cms.untracked.InputTag("offlinePrimaryVertices"),
    lipTP = cms.double(30.0),
    maxRapidityTP = cms.double(4.5),
    minHitTP = cms.int32(0),
    minRapidityTP = cms.double(-4.5),
    mvaLabels = cms.untracked.PSet(

    ),
    parametersDefiner = cms.string('LhcParametersDefinerForTP'),
    pdgIdTP = cms.vint32(),
    ptMaxTP = cms.double(1e+100),
    ptMinTP = cms.double(0.005),
    signalOnlyTP = cms.bool(False),
    sim = cms.VInputTag(
        cms.InputTag("g4SimHits","TrackerHitsPixelBarrelLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelBarrelHighTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIBLowTof"), 
        cms.InputTag("g4SimHits","TrackerHitsTIBHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIDLowTof"), cms.InputTag("g4SimHits","TrackerHitsTIDHighTof"), cms.InputTag("g4SimHits","TrackerHitsTOBLowTof"), cms.InputTag("g4SimHits","TrackerHitsTOBHighTof"), 
        cms.InputTag("g4SimHits","TrackerHitsTECLowTof"), cms.InputTag("g4SimHits","TrackerHitsTECHighTof")
    ),
    simHitTpMapTag = cms.InputTag("simHitTPAssocProducer"),
    simPVMaxZ = cms.untracked.double(-1),
    stableOnlyTP = cms.bool(False),
    tipTP = cms.double(2.5), #previous 60
    trackCollectionForDrCalculation = cms.InputTag("generalTracks"),
    useGsf = cms.bool(False),
    useLogPt = cms.untracked.bool(True),
    vertexAssociator = cms.untracked.InputTag("VertexAssociatorByPositionAndTracks")
)


trackValidatorSeedingTrackingOnly = cms.EDProducer("MultiTrackValidator", #cmssw_11_1 previous cms.EDAnalyzer
    cores = cms.InputTag("highPtJetsForTrk"), #cmssw_10_6 #cmssw_11_1
    UseAssociators = cms.bool(True),
    associators = cms.untracked.VInputTag("quickTrackAssociatorByHits"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    calculateDrSingleCollection = cms.untracked.bool(True),
    chargedOnlyTP = cms.bool(True),
    dEdx1Tag = cms.InputTag("dedxHarmonic2"),
    dEdx2Tag = cms.InputTag("dedxTruncated40"),
    dirName = cms.string('Tracking/TrackSeeding/'),
    doMVAPlots = cms.untracked.bool(False),
    doPVAssociationPlots = cms.untracked.bool(False),
    doPlotsOnlyForTruePV = cms.untracked.bool(False),
    doRecoTrackPlots = cms.untracked.bool(True),
    doResolutionPlotsForLabels = cms.VInputTag("disabled"),
    doSeedPlots = cms.untracked.bool(True),
    doSimPlots = cms.untracked.bool(False),
    doSimTrackPlots = cms.untracked.bool(True),
    doSummaryPlots = cms.untracked.bool(True),
    dodEdxPlots = cms.untracked.bool(False),
    histoProducerAlgoBlock = cms.PSet(
	mindrj = cms.double(0.001),#cmssw_10_6 
        maxdrj = cms.double(0.1),#cmssw_10_6
        nintdrj = cms.int32(100), #cmssw_10_6
        GpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), #cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5 
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False), #cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False),
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.05),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 30.0
        ),
        GpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(35.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.05),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False), #cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 60.0
        ),
        TpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False), #cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        cotThetaRes_nbin = cms.int32(300),
        cotThetaRes_rangeMax = cms.double(0.02),
        cotThetaRes_rangeMin = cms.double(-0.02),
        doMTDPlots = cms.untracked.bool(True), # cmssw_11_1
        dxyDzZoom = cms.double(25),
        dxyRes_nbin = cms.int32(500),
        dxyRes_rangeMax = cms.double(0.1),
        dxyRes_rangeMin = cms.double(-0.1),
        dzRes_nbin = cms.int32(150),
        dzRes_rangeMax = cms.double(0.05),
        dzRes_rangeMin = cms.double(-0.05),
        generalGpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        generalTpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        maxChi2 = cms.double(20),
        maxDeDx = cms.double(10.0),
        maxDxy = cms.double(25),
        maxDz = cms.double(30),
        maxDzpvCumulative = cms.double(0.6),
        maxDzpvsigCumulative = cms.double(10),
        maxEta = cms.double(4.5),
        maxHit = cms.double(80.5),
        maxLayers = cms.double(25.5),
        maxMVA = cms.double(1),
        maxPVz = cms.double(60),
        maxPhi = cms.double(3.1416),
        maxPt = cms.double(1000),
        maxPu = cms.double(259.5),
        maxTracks = cms.double(2000),
        maxVertcount = cms.double(160.5),
        maxVertpos = cms.double(100),
        maxZpos = cms.double(30),
        maxdr = cms.double(1),
        minChi2 = cms.double(0),
        minDeDx = cms.double(0.0),
        minDxy = cms.double(-25),
        minDz = cms.double(-30),
        minEta = cms.double(-4.5),
        minHit = cms.double(-0.5),
        minLayers = cms.double(-0.5),
        minMVA = cms.double(-1),
        minPVz = cms.double(-60),
        minPhi = cms.double(-3.1416),
        minPt = cms.double(0.1),
        minPu = cms.double(-0.5),
        minTracks = cms.double(0),
        minVertcount = cms.double(-0.5),
        minVertpos = cms.double(0.01),
        minZpos = cms.double(-30),
        mindr = cms.double(0.001),
        nintChi2 = cms.int32(40),
        nintDeDx = cms.int32(40),
        nintDxy = cms.int32(100),
        nintDz = cms.int32(60),
        nintDzpvCumulative = cms.int32(240),
        nintDzpvsigCumulative = cms.int32(200),
        nintEta = cms.int32(90),
        nintHit = cms.int32(81),
        nintLayers = cms.int32(26),
        nintMVA = cms.int32(100),
        nintPVz = cms.int32(120),
        nintPhi = cms.int32(36),
        nintPt = cms.int32(40),
        nintPu = cms.int32(130),
        nintTracks = cms.int32(200),
        nintVertcount = cms.int32(161),
        nintVertpos = cms.int32(40),
        nintZpos = cms.int32(60),
        nintdr = cms.int32(100),
        phiRes_nbin = cms.int32(300),
        phiRes_rangeMax = cms.double(0.01),
        phiRes_rangeMin = cms.double(-0.01),
        ptRes_nbin = cms.int32(100),
        ptRes_rangeMax = cms.double(0.1),
        ptRes_rangeMin = cms.double(-0.1),
        seedingLayerSets = cms.vstring(
            'BPix1+BPix2+BPix3+BPix4', 
            'BPix1+BPix2+BPix3+FPix1_pos', 
            'BPix1+BPix2+BPix3+FPix1_neg', 
            'BPix1+BPix2+FPix1_pos+FPix2_pos', 
            'BPix1+BPix2+FPix1_neg+FPix2_neg', 
            'BPix1+FPix1_pos+FPix2_pos+FPix3_pos', 
            'BPix1+FPix1_neg+FPix2_neg+FPix3_neg', 
            'FPix1_pos+FPix2_pos+FPix3_pos+FPix4_pos', 
            'FPix1_neg+FPix2_neg+FPix3_neg+FPix4_neg', 
            'FPix2_pos+FPix3_pos+FPix4_pos+FPix5_pos', 
            'FPix2_neg+FPix3_neg+FPix4_neg+FPix5_neg', 
            'FPix3_pos+FPix4_pos+FPix5_pos+FPix6_pos', 
            'FPix3_neg+FPix4_neg+FPix5_neg+FPix6_neg', 
            'FPix4_pos+FPix5_pos+FPix6_pos+FPix7_pos', 
            'FPix4_neg+FPix5_neg+FPix6_neg+FPix7_neg', 
            'FPix5_pos+FPix6_pos+FPix7_pos+FPix8_pos', 
            'FPix5_neg+FPix6_neg+FPix7_neg+FPix8_neg', 
            'BPix1+BPix2+BPix3', 
            'BPix2+BPix3+BPix4', 
            'BPix1+BPix3+BPix4', 
            'BPix1+BPix2+BPix4', 
            'BPix2+BPix3+FPix1_pos', 
            'BPix2+BPix3+FPix1_neg', 
            'BPix1+BPix2+FPix1_pos', 
            'BPix1+BPix2+FPix1_neg', 
            'BPix2+FPix1_pos+FPix2_pos', 
            'BPix2+FPix1_neg+FPix2_neg', 
            'BPix1+FPix1_pos+FPix2_pos', 
            'BPix1+FPix1_neg+FPix2_neg', 
            'FPix1_pos+FPix2_pos+FPix3_pos', 
            'FPix1_neg+FPix2_neg+FPix3_neg', 
            'BPix1+FPix2_pos+FPix3_pos', 
            'BPix1+FPix2_neg+FPix3_neg', 
            'FPix2_pos+FPix3_pos+FPix4_pos', 
            'FPix2_neg+FPix3_neg+FPix4_neg', 
            'FPix3_pos+FPix4_pos+FPix5_pos', 
            'FPix3_neg+FPix4_neg+FPix5_neg', 
            'FPix4_pos+FPix5_pos+FPix6_pos', 
            'FPix4_neg+FPix5_neg+FPix6_neg', 
            'FPix5_pos+FPix6_pos+FPix7_pos', 
            'FPix5_neg+FPix6_neg+FPix7_neg', 
            'FPix6_pos+FPix7_pos+FPix8_pos', 
            'FPix6_neg+FPix7_neg+FPix8_neg', 
            'BPix1+BPix2', 
            'BPix1+BPix3', 
            'BPix2+BPix3', 
            'BPix1+FPix1_pos', 
            'BPix1+FPix1_neg', 
            'BPix2+FPix1_pos', 
            'BPix2+FPix1_neg'
        ),
        useFabsEta = cms.bool(False),
        useInvPt = cms.bool(False),
        useLogPt = cms.untracked.bool(True),
        useLogVertpos = cms.untracked.bool(True)
    ),
    ignoremissingtrackcollection = cms.untracked.bool(False),
    intimeOnlyTP = cms.bool(True),
    invertRapidityCutTP = cms.bool(False), # cmssw_11_1
    label = cms.VInputTag(
        "seedTracksinitialStepSeeds", "seedTrackshighPtTripletStepSeeds" ### v2
    ),
    label_pileupinfo = cms.InputTag("addPileupInfo"),
    label_tp_effic = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_effic_refvector = cms.bool(False),
    label_tp_fake = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_fake_refvector = cms.bool(False),
    label_tp_nlayers = cms.InputTag("trackingParticleNumberOfLayersProducer","trackerLayers"),
    label_tp_npixellayers = cms.InputTag("trackingParticleNumberOfLayersProducer","pixelLayers"),
    label_tp_nstripstereolayers = cms.InputTag("trackingParticleNumberOfLayersProducer","stripStereoLayers"),
    label_tv = cms.InputTag("mix","MergedTrackTruth"),
    label_vertex = cms.untracked.InputTag("offlinePrimaryVertices"),
    lipTP = cms.double(30.0),
    maxRapidityTP = cms.double(4.5),
    minHitTP = cms.int32(0),
    minRapidityTP = cms.double(-4.5),
    mvaLabels = cms.untracked.PSet(

    ),
    parametersDefiner = cms.string('LhcParametersDefinerForTP'),
    pdgIdTP = cms.vint32(),
    ptMaxTP = cms.double(1e+100),
    ptMinTP = cms.double(0.005),
    signalOnlyTP = cms.bool(False),
    sim = cms.VInputTag(
        cms.InputTag("g4SimHits","TrackerHitsPixelBarrelLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelBarrelHighTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIBLowTof"), 
        cms.InputTag("g4SimHits","TrackerHitsTIBHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIDLowTof"), cms.InputTag("g4SimHits","TrackerHitsTIDHighTof"), cms.InputTag("g4SimHits","TrackerHitsTOBLowTof"), cms.InputTag("g4SimHits","TrackerHitsTOBHighTof"), 
        cms.InputTag("g4SimHits","TrackerHitsTECLowTof"), cms.InputTag("g4SimHits","TrackerHitsTECHighTof")
    ),
    simHitTpMapTag = cms.InputTag("simHitTPAssocProducer"),
    simPVMaxZ = cms.untracked.double(-1),
    stableOnlyTP = cms.bool(False),
    tipTP = cms.double(2.5), #previous 60
    trackCollectionForDrCalculation = cms.InputTag("generalTracks"),
    useGsf = cms.bool(False),
    useLogPt = cms.untracked.bool(True),
    vertexAssociator = cms.untracked.InputTag("VertexAssociatorByPositionAndTracks")
)

trackValidatorSeedingPreSplittingTrackingOnly = cms.EDProducer("MultiTrackValidator", #cmssw_11_1 previous cms.EDAnalyzer
    cores = cms.InputTag("highPtJetsForTrk"), #cmssw_10_6 #cmssw_11_1
    UseAssociators = cms.bool(True),
    associators = cms.untracked.VInputTag("quickTrackAssociatorByHitsPreSplitting"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    calculateDrSingleCollection = cms.untracked.bool(True),
    chargedOnlyTP = cms.bool(True),
    dEdx1Tag = cms.InputTag("dedxHarmonic2"),
    dEdx2Tag = cms.InputTag("dedxTruncated40"),
    dirName = cms.string('Tracking/TrackSeeding/'),
    doMVAPlots = cms.untracked.bool(False),
    doPVAssociationPlots = cms.untracked.bool(False),
    doPlotsOnlyForTruePV = cms.untracked.bool(False),
    doRecoTrackPlots = cms.untracked.bool(True),
    doResolutionPlotsForLabels = cms.VInputTag("disabled"),
    doSeedPlots = cms.untracked.bool(True),
    doSimPlots = cms.untracked.bool(False),
    doSimTrackPlots = cms.untracked.bool(True),
    doSummaryPlots = cms.untracked.bool(False),
    dodEdxPlots = cms.untracked.bool(False),
    histoProducerAlgoBlock = cms.PSet(
	mindrj = cms.double(0.001),#cmssw_10_6 
        maxdrj = cms.double(0.1),#cmssw_10_6
        nintdrj = cms.int32(100), #cmssw_10_6
        GpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5 
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.05),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 30.0
        ),
        GpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(35.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.05),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 60.0
        ),
        TpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        cotThetaRes_nbin = cms.int32(300),
        cotThetaRes_rangeMax = cms.double(0.02),
        cotThetaRes_rangeMin = cms.double(-0.02),
        doMTDPlots = cms.untracked.bool(True), # cmssw_11_1
        dxyDzZoom = cms.double(25),
        dxyRes_nbin = cms.int32(500),
        dxyRes_rangeMax = cms.double(0.1),
        dxyRes_rangeMin = cms.double(-0.1),
        dzRes_nbin = cms.int32(150),
        dzRes_rangeMax = cms.double(0.05),
        dzRes_rangeMin = cms.double(-0.05),
        generalGpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        generalTpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        maxChi2 = cms.double(20),
        maxDeDx = cms.double(10.0),
        maxDxy = cms.double(25),
        maxDz = cms.double(30),
        maxDzpvCumulative = cms.double(0.6),
        maxDzpvsigCumulative = cms.double(10),
        maxEta = cms.double(4.5),
        maxHit = cms.double(80.5),
        maxLayers = cms.double(25.5),
        maxMVA = cms.double(1),
        maxPVz = cms.double(60),
        maxPhi = cms.double(3.1416),
        maxPt = cms.double(1000),
        maxPu = cms.double(259.5),
        maxTracks = cms.double(2000),
        maxVertcount = cms.double(160.5),
        maxVertpos = cms.double(100),
        maxZpos = cms.double(30),
        maxdr = cms.double(1),
        minChi2 = cms.double(0),
        minDeDx = cms.double(0.0),
        minDxy = cms.double(-25),
        minDz = cms.double(-30),
        minEta = cms.double(-4.5),
        minHit = cms.double(-0.5),
        minLayers = cms.double(-0.5),
        minMVA = cms.double(-1),
        minPVz = cms.double(-60),
        minPhi = cms.double(-3.1416),
        minPt = cms.double(0.1),
        minPu = cms.double(-0.5),
        minTracks = cms.double(0),
        minVertcount = cms.double(-0.5),
        minVertpos = cms.double(0.01),
        minZpos = cms.double(-30),
        mindr = cms.double(0.001),
        nintChi2 = cms.int32(40),
        nintDeDx = cms.int32(40),
        nintDxy = cms.int32(100),
        nintDz = cms.int32(60),
        nintDzpvCumulative = cms.int32(240),
        nintDzpvsigCumulative = cms.int32(200),
        nintEta = cms.int32(90),
        nintHit = cms.int32(81),
        nintLayers = cms.int32(26),
        nintMVA = cms.int32(100),
        nintPVz = cms.int32(120),
        nintPhi = cms.int32(36),
        nintPt = cms.int32(40),
        nintPu = cms.int32(130),
        nintTracks = cms.int32(200),
        nintVertcount = cms.int32(161),
        nintVertpos = cms.int32(40),
        nintZpos = cms.int32(60),
        nintdr = cms.int32(100),
        phiRes_nbin = cms.int32(300),
        phiRes_rangeMax = cms.double(0.01),
        phiRes_rangeMin = cms.double(-0.01),
        ptRes_nbin = cms.int32(100),
        ptRes_rangeMax = cms.double(0.1),
        ptRes_rangeMin = cms.double(-0.1),
        seedingLayerSets = cms.vstring(
            'BPix1+BPix2+BPix3+BPix4', 
            'BPix1+BPix2+BPix3+FPix1_pos', 
            'BPix1+BPix2+BPix3+FPix1_neg', 
            'BPix1+BPix2+FPix1_pos+FPix2_pos', 
            'BPix1+BPix2+FPix1_neg+FPix2_neg', 
            'BPix1+FPix1_pos+FPix2_pos+FPix3_pos', 
            'BPix1+FPix1_neg+FPix2_neg+FPix3_neg', 
            'FPix1_pos+FPix2_pos+FPix3_pos+FPix4_pos', 
            'FPix1_neg+FPix2_neg+FPix3_neg+FPix4_neg', 
            'FPix2_pos+FPix3_pos+FPix4_pos+FPix5_pos', 
            'FPix2_neg+FPix3_neg+FPix4_neg+FPix5_neg', 
            'FPix3_pos+FPix4_pos+FPix5_pos+FPix6_pos', 
            'FPix3_neg+FPix4_neg+FPix5_neg+FPix6_neg', 
            'FPix4_pos+FPix5_pos+FPix6_pos+FPix7_pos', 
            'FPix4_neg+FPix5_neg+FPix6_neg+FPix7_neg', 
            'FPix5_pos+FPix6_pos+FPix7_pos+FPix8_pos', 
            'FPix5_neg+FPix6_neg+FPix7_neg+FPix8_neg', 
            'BPix1+BPix2+BPix3', 
            'BPix2+BPix3+BPix4', 
            'BPix1+BPix3+BPix4', 
            'BPix1+BPix2+BPix4', 
            'BPix2+BPix3+FPix1_pos', 
            'BPix2+BPix3+FPix1_neg', 
            'BPix1+BPix2+FPix1_pos', 
            'BPix1+BPix2+FPix1_neg', 
            'BPix2+FPix1_pos+FPix2_pos', 
            'BPix2+FPix1_neg+FPix2_neg', 
            'BPix1+FPix1_pos+FPix2_pos', 
            'BPix1+FPix1_neg+FPix2_neg', 
            'FPix1_pos+FPix2_pos+FPix3_pos', 
            'FPix1_neg+FPix2_neg+FPix3_neg', 
            'BPix1+FPix2_pos+FPix3_pos', 
            'BPix1+FPix2_neg+FPix3_neg', 
            'FPix2_pos+FPix3_pos+FPix4_pos', 
            'FPix2_neg+FPix3_neg+FPix4_neg', 
            'FPix3_pos+FPix4_pos+FPix5_pos', 
            'FPix3_neg+FPix4_neg+FPix5_neg', 
            'FPix4_pos+FPix5_pos+FPix6_pos', 
            'FPix4_neg+FPix5_neg+FPix6_neg', 
            'FPix5_pos+FPix6_pos+FPix7_pos', 
            'FPix5_neg+FPix6_neg+FPix7_neg', 
            'FPix6_pos+FPix7_pos+FPix8_pos', 
            'FPix6_neg+FPix7_neg+FPix8_neg', 
            'BPix1+BPix2', 
            'BPix1+BPix3', 
            'BPix2+BPix3', 
            'BPix1+FPix1_pos', 
            'BPix1+FPix1_neg', 
            'BPix2+FPix1_pos', 
            'BPix2+FPix1_neg'
        ),
        useFabsEta = cms.bool(False),
        useInvPt = cms.bool(False),
        useLogPt = cms.untracked.bool(True),
        useLogVertpos = cms.untracked.bool(True)
    ),
    ignoremissingtrackcollection = cms.untracked.bool(False),
    intimeOnlyTP = cms.bool(True),
    invertRapidityCutTP = cms.bool(False), # cmssw_11_1
    label = cms.VInputTag(),
    label_pileupinfo = cms.InputTag("addPileupInfo"),
    label_tp_effic = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_effic_refvector = cms.bool(False),
    label_tp_fake = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_fake_refvector = cms.bool(False),
    label_tp_nlayers = cms.InputTag("trackingParticleNumberOfLayersProducer","trackerLayers"),
    label_tp_npixellayers = cms.InputTag("trackingParticleNumberOfLayersProducer","pixelLayers"),
    label_tp_nstripstereolayers = cms.InputTag("trackingParticleNumberOfLayersProducer","stripStereoLayers"),
    label_tv = cms.InputTag("mix","MergedTrackTruth"),
    label_vertex = cms.untracked.InputTag("offlinePrimaryVertices"),
    lipTP = cms.double(30.0),
    maxRapidityTP = cms.double(4.5),
    minHitTP = cms.int32(0),
    minRapidityTP = cms.double(-4.5),
    mvaLabels = cms.untracked.PSet(

    ),
    parametersDefiner = cms.string('LhcParametersDefinerForTP'),
    pdgIdTP = cms.vint32(),
    ptMaxTP = cms.double(1e+100),
    ptMinTP = cms.double(0.005),
    signalOnlyTP = cms.bool(False),
    sim = cms.VInputTag(
        cms.InputTag("g4SimHits","TrackerHitsPixelBarrelLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelBarrelHighTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIBLowTof"), 
        cms.InputTag("g4SimHits","TrackerHitsTIBHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIDLowTof"), cms.InputTag("g4SimHits","TrackerHitsTIDHighTof"), cms.InputTag("g4SimHits","TrackerHitsTOBLowTof"), cms.InputTag("g4SimHits","TrackerHitsTOBHighTof"), 
        cms.InputTag("g4SimHits","TrackerHitsTECLowTof"), cms.InputTag("g4SimHits","TrackerHitsTECHighTof")
    ),
    simHitTpMapTag = cms.InputTag("simHitTPAssocProducer"),
    simPVMaxZ = cms.untracked.double(-1),
    stableOnlyTP = cms.bool(False),
    tipTP = cms.double(2.5), #previous 60
    trackCollectionForDrCalculation = cms.InputTag("generalTracks"),
    useGsf = cms.bool(False),
    useLogPt = cms.untracked.bool(True),
    vertexAssociator = cms.untracked.InputTag("VertexAssociatorByPositionAndTracks")
)

trackValidatorBuilding = cms.EDProducer("MultiTrackValidator", #cmssw_11_1 previous cms.EDAnalyzer
    cores = cms.InputTag("highPtJetsForTrk"), #cmssw_10_6 #cmssw_11_1
    UseAssociators = cms.bool(True),
    associators = cms.untracked.VInputTag("quickTrackAssociatorByHits"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    calculateDrSingleCollection = cms.untracked.bool(True),
    chargedOnlyTP = cms.bool(True),
    dEdx1Tag = cms.InputTag("dedxHarmonic2"),
    dEdx2Tag = cms.InputTag("dedxTruncated40"),
    dirName = cms.string('Tracking/TrackBuilding/'),
    doMVAPlots = cms.untracked.bool(True),
    doPVAssociationPlots = cms.untracked.bool(False),
    doPlotsOnlyForTruePV = cms.untracked.bool(False),
    doRecoTrackPlots = cms.untracked.bool(True),
    doResolutionPlotsForLabels = cms.VInputTag("disabled"),
    doSeedPlots = cms.untracked.bool(False),
    doSimPlots = cms.untracked.bool(False),
    doSimTrackPlots = cms.untracked.bool(True),
    doSummaryPlots = cms.untracked.bool(True),
    dodEdxPlots = cms.untracked.bool(False),
    histoProducerAlgoBlock = cms.PSet(
	mindrj = cms.double(0.001),#cmssw_10_6 
        maxdrj = cms.double(0.1),#cmssw_10_6
        nintdrj = cms.int32(100), #cmssw_10_6
        GpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5 
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.05),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 30.0
        ),
        GpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(35.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.05),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 60.0
        ),
        TpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        cotThetaRes_nbin = cms.int32(300),
        cotThetaRes_rangeMax = cms.double(0.02),
        cotThetaRes_rangeMin = cms.double(-0.02),
        doMTDPlots = cms.untracked.bool(True), # cmssw_11_1
        dxyDzZoom = cms.double(25),
        dxyRes_nbin = cms.int32(500),
        dxyRes_rangeMax = cms.double(0.1),
        dxyRes_rangeMin = cms.double(-0.1),
        dzRes_nbin = cms.int32(150),
        dzRes_rangeMax = cms.double(0.05),
        dzRes_rangeMin = cms.double(-0.05),
        generalGpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        generalTpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        maxChi2 = cms.double(20),
        maxDeDx = cms.double(10.0),
        maxDxy = cms.double(25),
        maxDz = cms.double(30),
        maxDzpvCumulative = cms.double(0.6),
        maxDzpvsigCumulative = cms.double(10),
        maxEta = cms.double(4.5),
        maxHit = cms.double(80.5),
        maxLayers = cms.double(25.5),
        maxMVA = cms.double(1),
        maxPVz = cms.double(60),
        maxPhi = cms.double(3.1416),
        maxPt = cms.double(1000),
        maxPu = cms.double(259.5),
        maxTracks = cms.double(2000),
        maxVertcount = cms.double(160.5),
        maxVertpos = cms.double(100),
        maxZpos = cms.double(30),
        maxdr = cms.double(1),
        minChi2 = cms.double(0),
        minDeDx = cms.double(0.0),
        minDxy = cms.double(-25),
        minDz = cms.double(-30),
        minEta = cms.double(-4.5),
        minHit = cms.double(-0.5),
        minLayers = cms.double(-0.5),
        minMVA = cms.double(-1),
        minPVz = cms.double(-60),
        minPhi = cms.double(-3.1416),
        minPt = cms.double(0.1),
        minPu = cms.double(-0.5),
        minTracks = cms.double(0),
        minVertcount = cms.double(-0.5),
        minVertpos = cms.double(0.01),
        minZpos = cms.double(-30),
        mindr = cms.double(0.001),
        nintChi2 = cms.int32(40),
        nintDeDx = cms.int32(40),
        nintDxy = cms.int32(100),
        nintDz = cms.int32(60),
        nintDzpvCumulative = cms.int32(240),
        nintDzpvsigCumulative = cms.int32(200),
        nintEta = cms.int32(90),
        nintHit = cms.int32(81),
        nintLayers = cms.int32(26),
        nintMVA = cms.int32(100),
        nintPVz = cms.int32(120),
        nintPhi = cms.int32(36),
        nintPt = cms.int32(40),
        nintPu = cms.int32(130),
        nintTracks = cms.int32(200),
        nintVertcount = cms.int32(161),
        nintVertpos = cms.int32(40),
        nintZpos = cms.int32(60),
        nintdr = cms.int32(100),
        phiRes_nbin = cms.int32(300),
        phiRes_rangeMax = cms.double(0.01),
        phiRes_rangeMin = cms.double(-0.01),
        ptRes_nbin = cms.int32(100),
        ptRes_rangeMax = cms.double(0.1),
        ptRes_rangeMin = cms.double(-0.1),
        seedingLayerSets = cms.vstring(
            'BPix1+BPix2+BPix3+BPix4', 
            'BPix1+BPix2+BPix3+FPix1_pos', 
            'BPix1+BPix2+BPix3+FPix1_neg', 
            'BPix1+BPix2+FPix1_pos+FPix2_pos', 
            'BPix1+BPix2+FPix1_neg+FPix2_neg', 
            'BPix1+FPix1_pos+FPix2_pos+FPix3_pos', 
            'BPix1+FPix1_neg+FPix2_neg+FPix3_neg', 
            'FPix1_pos+FPix2_pos+FPix3_pos+FPix4_pos', 
            'FPix1_neg+FPix2_neg+FPix3_neg+FPix4_neg', 
            'FPix2_pos+FPix3_pos+FPix4_pos+FPix5_pos', 
            'FPix2_neg+FPix3_neg+FPix4_neg+FPix5_neg', 
            'FPix3_pos+FPix4_pos+FPix5_pos+FPix6_pos', 
            'FPix3_neg+FPix4_neg+FPix5_neg+FPix6_neg', 
            'FPix4_pos+FPix5_pos+FPix6_pos+FPix7_pos', 
            'FPix4_neg+FPix5_neg+FPix6_neg+FPix7_neg', 
            'FPix5_pos+FPix6_pos+FPix7_pos+FPix8_pos', 
            'FPix5_neg+FPix6_neg+FPix7_neg+FPix8_neg', 
            'BPix1+BPix2+BPix3', 
            'BPix2+BPix3+BPix4', 
            'BPix1+BPix3+BPix4', 
            'BPix1+BPix2+BPix4', 
            'BPix2+BPix3+FPix1_pos', 
            'BPix2+BPix3+FPix1_neg', 
            'BPix1+BPix2+FPix1_pos', 
            'BPix1+BPix2+FPix1_neg', 
            'BPix2+FPix1_pos+FPix2_pos', 
            'BPix2+FPix1_neg+FPix2_neg', 
            'BPix1+FPix1_pos+FPix2_pos', 
            'BPix1+FPix1_neg+FPix2_neg', 
            'FPix1_pos+FPix2_pos+FPix3_pos', 
            'FPix1_neg+FPix2_neg+FPix3_neg', 
            'BPix1+FPix2_pos+FPix3_pos', 
            'BPix1+FPix2_neg+FPix3_neg', 
            'FPix2_pos+FPix3_pos+FPix4_pos', 
            'FPix2_neg+FPix3_neg+FPix4_neg', 
            'FPix3_pos+FPix4_pos+FPix5_pos', 
            'FPix3_neg+FPix4_neg+FPix5_neg', 
            'FPix4_pos+FPix5_pos+FPix6_pos', 
            'FPix4_neg+FPix5_neg+FPix6_neg', 
            'FPix5_pos+FPix6_pos+FPix7_pos', 
            'FPix5_neg+FPix6_neg+FPix7_neg', 
            'FPix6_pos+FPix7_pos+FPix8_pos', 
            'FPix6_neg+FPix7_neg+FPix8_neg', 
            'BPix1+BPix2', 
            'BPix1+BPix3', 
            'BPix2+BPix3', 
            'BPix1+FPix1_pos', 
            'BPix1+FPix1_neg', 
            'BPix2+FPix1_pos', 
            'BPix2+FPix1_neg'
        ),
        useFabsEta = cms.bool(False),
        useInvPt = cms.bool(False),
        useLogPt = cms.untracked.bool(True),
        useLogVertpos = cms.untracked.bool(True)
    ),
    ignoremissingtrackcollection = cms.untracked.bool(False),
    intimeOnlyTP = cms.bool(True),
    invertRapidityCutTP = cms.bool(False), # cmssw_11_1
    label = cms.VInputTag(
        "initialStepTracks", "highPtTripletStepTracks" ### v2
    ),
    label_pileupinfo = cms.InputTag("addPileupInfo"),
    label_tp_effic = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_effic_refvector = cms.bool(False),
    label_tp_fake = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_fake_refvector = cms.bool(False),
    label_tp_nlayers = cms.InputTag("trackingParticleNumberOfLayersProducer","trackerLayers"),
    label_tp_npixellayers = cms.InputTag("trackingParticleNumberOfLayersProducer","pixelLayers"),
    label_tp_nstripstereolayers = cms.InputTag("trackingParticleNumberOfLayersProducer","stripStereoLayers"),
    label_tv = cms.InputTag("mix","MergedTrackTruth"),
    label_vertex = cms.untracked.InputTag("offlinePrimaryVertices"),
    lipTP = cms.double(30.0),
    maxRapidityTP = cms.double(4.5),
    minHitTP = cms.int32(0),
    minRapidityTP = cms.double(-4.5),
    mvaLabels = cms.untracked.PSet(

    ),
    parametersDefiner = cms.string('LhcParametersDefinerForTP'),
    pdgIdTP = cms.vint32(),
    ptMaxTP = cms.double(1e+100),
    ptMinTP = cms.double(0.005),
    signalOnlyTP = cms.bool(False),
    sim = cms.VInputTag(
        cms.InputTag("g4SimHits","TrackerHitsPixelBarrelLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelBarrelHighTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIBLowTof"), 
        cms.InputTag("g4SimHits","TrackerHitsTIBHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIDLowTof"), cms.InputTag("g4SimHits","TrackerHitsTIDHighTof"), cms.InputTag("g4SimHits","TrackerHitsTOBLowTof"), cms.InputTag("g4SimHits","TrackerHitsTOBHighTof"), 
        cms.InputTag("g4SimHits","TrackerHitsTECLowTof"), cms.InputTag("g4SimHits","TrackerHitsTECHighTof")
    ),
    simHitTpMapTag = cms.InputTag("simHitTPAssocProducer"),
    simPVMaxZ = cms.untracked.double(-1),
    stableOnlyTP = cms.bool(False),
    tipTP = cms.double(2.5), #previous 60
    trackCollectionForDrCalculation = cms.InputTag("generalTracks"),
    useGsf = cms.bool(False),
    useLogPt = cms.untracked.bool(True),
    vertexAssociator = cms.untracked.InputTag("VertexAssociatorByPositionAndTracks")
)


trackValidatorBuildingPreSplitting = cms.EDProducer("MultiTrackValidator", #cmssw_11_1 previous cms.EDAnalyzer
    cores = cms.InputTag("highPtJetsForTrk"), #cmssw_10_6 #cmssw_11_1
    UseAssociators = cms.bool(True),
    associators = cms.untracked.VInputTag("quickTrackAssociatorByHitsPreSplitting"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    calculateDrSingleCollection = cms.untracked.bool(True),
    chargedOnlyTP = cms.bool(True),
    dEdx1Tag = cms.InputTag("dedxHarmonic2"),
    dEdx2Tag = cms.InputTag("dedxTruncated40"),
    dirName = cms.string('Tracking/TrackBuilding/'),
    doMVAPlots = cms.untracked.bool(False),
    doPVAssociationPlots = cms.untracked.bool(False),
    doPlotsOnlyForTruePV = cms.untracked.bool(False),
    doRecoTrackPlots = cms.untracked.bool(True),
    doResolutionPlotsForLabels = cms.VInputTag("disabled"),
    doSeedPlots = cms.untracked.bool(False),
    doSimPlots = cms.untracked.bool(False),
    doSimTrackPlots = cms.untracked.bool(True),
    doSummaryPlots = cms.untracked.bool(False),
    dodEdxPlots = cms.untracked.bool(False),
    histoProducerAlgoBlock = cms.PSet(
	mindrj = cms.double(0.001),#cmssw_10_6 
        maxdrj = cms.double(0.1),#cmssw_10_6
        nintdrj = cms.int32(100), #cmssw_10_6
        GpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5 
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.05),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        GpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 30.0
        ),
        GpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(35.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsEta = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPhi = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsPt = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.05),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        TpSelectorForEfficiencyVsVTXR = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 60.0
        ),
        TpSelectorForEfficiencyVsVTXZ = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        cotThetaRes_nbin = cms.int32(300),
        cotThetaRes_rangeMax = cms.double(0.02),
        cotThetaRes_rangeMin = cms.double(-0.02),
        doMTDPlots = cms.untracked.bool(True), # cmssw_11_1
        dxyDzZoom = cms.double(25),
        dxyRes_nbin = cms.int32(500),
        dxyRes_rangeMax = cms.double(0.1),
        dxyRes_rangeMin = cms.double(-0.1),
        dzRes_nbin = cms.int32(150),
        dzRes_rangeMax = cms.double(0.05),
        dzRes_rangeMin = cms.double(-0.05),
        generalGpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2), # cmssw_11_1
            minPhi = cms.double(-3.2), # cmssw_11_1
            maxRapidity = cms.double(4.5), #previous 2.5
            minRapidity = cms.double(-4.5), #previous -2.5
            pdgId = cms.vint32(),
            ptMin = cms.double(0.9),
            status = cms.int32(1),
            tip = cms.double(2.5) #previous 3.5
        ),
        generalTpSelector = cms.PSet(
            chargedOnly = cms.bool(True),
            intimeOnly = cms.bool(False),
            invertRapidityCut = cms.bool(False),#cmssw_11_1
            lip = cms.double(30.0),
            maxPhi = cms.double(3.2),
            maxRapidity = cms.double(4.5),
            minHit = cms.int32(0),
            minPhi = cms.double(-3.2),
            minRapidity = cms.double(-4.5),
            pdgId = cms.vint32(),
            ptMax = cms.double(1e+100),
            ptMin = cms.double(0.9),
            signalOnly = cms.bool(True),
            stableOnly = cms.bool(False),
            tip = cms.double(2.5) #previous 3.5
        ),
        maxChi2 = cms.double(20),
        maxDeDx = cms.double(10.0),
        maxDxy = cms.double(25),
        maxDz = cms.double(30),
        maxDzpvCumulative = cms.double(0.6),
        maxDzpvsigCumulative = cms.double(10),
        maxEta = cms.double(4.5),
        maxHit = cms.double(80.5),
        maxLayers = cms.double(25.5),
        maxMVA = cms.double(1),
        maxPVz = cms.double(60),
        maxPhi = cms.double(3.1416),
        maxPt = cms.double(1000),
        maxPu = cms.double(259.5),
        maxTracks = cms.double(2000),
        maxVertcount = cms.double(160.5),
        maxVertpos = cms.double(100),
        maxZpos = cms.double(30),
        maxdr = cms.double(1),
        minChi2 = cms.double(0),
        minDeDx = cms.double(0.0),
        minDxy = cms.double(-25),
        minDz = cms.double(-30),
        minEta = cms.double(-4.5),
        minHit = cms.double(-0.5),
        minLayers = cms.double(-0.5),
        minMVA = cms.double(-1),
        minPVz = cms.double(-60),
        minPhi = cms.double(-3.1416),
        minPt = cms.double(0.1),
        minPu = cms.double(-0.5),
        minTracks = cms.double(0),
        minVertcount = cms.double(-0.5),
        minVertpos = cms.double(0.01),
        minZpos = cms.double(-30),
        mindr = cms.double(0.001),
        nintChi2 = cms.int32(40),
        nintDeDx = cms.int32(40),
        nintDxy = cms.int32(100),
        nintDz = cms.int32(60),
        nintDzpvCumulative = cms.int32(240),
        nintDzpvsigCumulative = cms.int32(200),
        nintEta = cms.int32(90),
        nintHit = cms.int32(81),
        nintLayers = cms.int32(26),
        nintMVA = cms.int32(100),
        nintPVz = cms.int32(120),
        nintPhi = cms.int32(36),
        nintPt = cms.int32(40),
        nintPu = cms.int32(130),
        nintTracks = cms.int32(200),
        nintVertcount = cms.int32(161),
        nintVertpos = cms.int32(40),
        nintZpos = cms.int32(60),
        nintdr = cms.int32(100),
        phiRes_nbin = cms.int32(300),
        phiRes_rangeMax = cms.double(0.01),
        phiRes_rangeMin = cms.double(-0.01),
        ptRes_nbin = cms.int32(100),
        ptRes_rangeMax = cms.double(0.1),
        ptRes_rangeMin = cms.double(-0.1),
        seedingLayerSets = cms.vstring(
            'BPix1+BPix2+BPix3+BPix4', 
            'BPix1+BPix2+BPix3+FPix1_pos', 
            'BPix1+BPix2+BPix3+FPix1_neg', 
            'BPix1+BPix2+FPix1_pos+FPix2_pos', 
            'BPix1+BPix2+FPix1_neg+FPix2_neg', 
            'BPix1+FPix1_pos+FPix2_pos+FPix3_pos', 
            'BPix1+FPix1_neg+FPix2_neg+FPix3_neg', 
            'FPix1_pos+FPix2_pos+FPix3_pos+FPix4_pos', 
            'FPix1_neg+FPix2_neg+FPix3_neg+FPix4_neg', 
            'FPix2_pos+FPix3_pos+FPix4_pos+FPix5_pos', 
            'FPix2_neg+FPix3_neg+FPix4_neg+FPix5_neg', 
            'FPix3_pos+FPix4_pos+FPix5_pos+FPix6_pos', 
            'FPix3_neg+FPix4_neg+FPix5_neg+FPix6_neg', 
            'FPix4_pos+FPix5_pos+FPix6_pos+FPix7_pos', 
            'FPix4_neg+FPix5_neg+FPix6_neg+FPix7_neg', 
            'FPix5_pos+FPix6_pos+FPix7_pos+FPix8_pos', 
            'FPix5_neg+FPix6_neg+FPix7_neg+FPix8_neg', 
            'BPix1+BPix2+BPix3', 
            'BPix2+BPix3+BPix4', 
            'BPix1+BPix3+BPix4', 
            'BPix1+BPix2+BPix4', 
            'BPix2+BPix3+FPix1_pos', 
            'BPix2+BPix3+FPix1_neg', 
            'BPix1+BPix2+FPix1_pos', 
            'BPix1+BPix2+FPix1_neg', 
            'BPix2+FPix1_pos+FPix2_pos', 
            'BPix2+FPix1_neg+FPix2_neg', 
            'BPix1+FPix1_pos+FPix2_pos', 
            'BPix1+FPix1_neg+FPix2_neg', 
            'FPix1_pos+FPix2_pos+FPix3_pos', 
            'FPix1_neg+FPix2_neg+FPix3_neg', 
            'BPix1+FPix2_pos+FPix3_pos', 
            'BPix1+FPix2_neg+FPix3_neg', 
            'FPix2_pos+FPix3_pos+FPix4_pos', 
            'FPix2_neg+FPix3_neg+FPix4_neg', 
            'FPix3_pos+FPix4_pos+FPix5_pos', 
            'FPix3_neg+FPix4_neg+FPix5_neg', 
            'FPix4_pos+FPix5_pos+FPix6_pos', 
            'FPix4_neg+FPix5_neg+FPix6_neg', 
            'FPix5_pos+FPix6_pos+FPix7_pos', 
            'FPix5_neg+FPix6_neg+FPix7_neg', 
            'FPix6_pos+FPix7_pos+FPix8_pos', 
            'FPix6_neg+FPix7_neg+FPix8_neg', 
            'BPix1+BPix2', 
            'BPix1+BPix3', 
            'BPix2+BPix3', 
            'BPix1+FPix1_pos', 
            'BPix1+FPix1_neg', 
            'BPix2+FPix1_pos', 
            'BPix2+FPix1_neg'
        ),
        useFabsEta = cms.bool(False),
        useInvPt = cms.bool(False),
        useLogPt = cms.untracked.bool(True),
        useLogVertpos = cms.untracked.bool(True)
    ),
    ignoremissingtrackcollection = cms.untracked.bool(False),
    intimeOnlyTP = cms.bool(True),
    invertRapidityCutTP = cms.bool(False), # cmssw_11_1
    label = cms.VInputTag(),
    label_pileupinfo = cms.InputTag("addPileupInfo"),
    label_tp_effic = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_effic_refvector = cms.bool(False),
    label_tp_fake = cms.InputTag("mix","MergedTrackTruth"),
    label_tp_fake_refvector = cms.bool(False),
    label_tp_nlayers = cms.InputTag("trackingParticleNumberOfLayersProducer","trackerLayers"),
    label_tp_npixellayers = cms.InputTag("trackingParticleNumberOfLayersProducer","pixelLayers"),
    label_tp_nstripstereolayers = cms.InputTag("trackingParticleNumberOfLayersProducer","stripStereoLayers"),
    label_tv = cms.InputTag("mix","MergedTrackTruth"),
    label_vertex = cms.untracked.InputTag("offlinePrimaryVertices"),
    lipTP = cms.double(30.0),
    maxRapidityTP = cms.double(4.5),
    minHitTP = cms.int32(0),
    minRapidityTP = cms.double(-4.5),
    mvaLabels = cms.untracked.PSet(

    ),
    parametersDefiner = cms.string('LhcParametersDefinerForTP'),
    pdgIdTP = cms.vint32(),
    ptMaxTP = cms.double(1e+100),
    ptMinTP = cms.double(0.005),
    signalOnlyTP = cms.bool(False),
    sim = cms.VInputTag(
        cms.InputTag("g4SimHits","TrackerHitsPixelBarrelLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelBarrelHighTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapLowTof"), cms.InputTag("g4SimHits","TrackerHitsPixelEndcapHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIBLowTof"), 
        cms.InputTag("g4SimHits","TrackerHitsTIBHighTof"), cms.InputTag("g4SimHits","TrackerHitsTIDLowTof"), cms.InputTag("g4SimHits","TrackerHitsTIDHighTof"), cms.InputTag("g4SimHits","TrackerHitsTOBLowTof"), cms.InputTag("g4SimHits","TrackerHitsTOBHighTof"), 
        cms.InputTag("g4SimHits","TrackerHitsTECLowTof"), cms.InputTag("g4SimHits","TrackerHitsTECHighTof")
    ),
    simHitTpMapTag = cms.InputTag("simHitTPAssocProducer"),
    simPVMaxZ = cms.untracked.double(-1),
    stableOnlyTP = cms.bool(False),
    tipTP = cms.double(2.5), #previous 60
    trackCollectionForDrCalculation = cms.InputTag("generalTracks"),
    useGsf = cms.bool(False),
    useLogPt = cms.untracked.bool(True),
    vertexAssociator = cms.untracked.InputTag("VertexAssociatorByPositionAndTracks")
)
VertexAssociatorByPositionAndTracks = cms.EDProducer("VertexAssociatorByPositionAndTracksProducer",
    absT = cms.double(-1),
    absZ = cms.double(0.1),
    maxRecoT = cms.double(-1),
    maxRecoZ = cms.double(1000),
    sharedTrackFraction = cms.double(-1),
    sigmaT = cms.double(-1),
    sigmaZ = cms.double(3),
    trackAssociation = cms.InputTag("trackingParticleRecoTrackAsssociation")
)


cutsRecoTracksBtvLike = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(17.0),
    maxChi2 = cms.double(5.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(9.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(0),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(1),
    minRapidity = cms.double(-9.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(1.0),
    quality = cms.vstring(),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(0.2),
    usePV = cms.bool(True),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksDetachedQuadStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('detachedQuadStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)

cutsRecoTracksDetachedQuadStepByAlgoMask = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring('detachedQuadStep'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)

cutsRecoTracksDetachedQuadStepByAlgoMaskHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring('detachedQuadStep'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)

cutsRecoTracksDetachedQuadStepByOriginalAlgo = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring('detachedQuadStep'),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)

cutsRecoTracksDetachedQuadStepByOriginalAlgoHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring('detachedQuadStep'),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)

cutsRecoTracksDetachedQuadStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('detachedQuadStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)

cutsRecoTracksDuplicateMerge = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('duplicateMerge'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksDuplicateMergeByAlgoMask = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring('duplicateMerge'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)

cutsRecoTracksDuplicateMergeByAlgoMaskHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring('duplicateMerge'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)
cutsRecoTracksDuplicateMergeHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('duplicateMerge'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)

cutsRecoTracksFromPVDetachedQuadStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('detachedQuadStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracksFromPV"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksFromPVDetachedQuadStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('detachedQuadStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracksFromPV"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)

cutsRecoTracksFromPVDuplicateMerge = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('duplicateMerge'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracksFromPV"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)

cutsRecoTracksFromPVDuplicateMergeHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('duplicateMerge'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracksFromPV"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)

cutsRecoTracksFromPVHighPtTripletStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('highPtTripletStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracksFromPV"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksFromPVHighPtTripletStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('highPtTripletStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracksFromPV"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)

cutsRecoTracksFromPVHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracksFromPV"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksFromPVInitialStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('initialStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracksFromPV"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksFromPVInitialStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('initialStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracksFromPV"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)

cutsRecoTracksFromPVLowPtQuadStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('lowPtQuadStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracksFromPV"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksFromPVLowPtQuadStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('lowPtQuadStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracksFromPV"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksFromPVLowPtTripletStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('lowPtTripletStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracksFromPV"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksFromPVLowPtTripletStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('lowPtTripletStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracksFromPV"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)

cutsRecoTracksFromPVMuonSeededStepInOut = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('muonSeededStepInOut'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracksFromPV"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksFromPVMuonSeededStepInOutHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('muonSeededStepInOut'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracksFromPV"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksFromPVMuonSeededStepOutIn = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('muonSeededStepOutIn'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracksFromPV"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksFromPVMuonSeededStepOutInHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('muonSeededStepOutIn'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracksFromPV"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)

cutsRecoTracksFromPVPixelPairStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('pixelPairStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracksFromPV"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksFromPVPixelPairStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('pixelPairStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracksFromPV"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)

cutsRecoTracksFromPVPt09DetachedQuadStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('detachedQuadStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracksFromPVPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksFromPVPt09DetachedQuadStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('detachedQuadStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracksFromPVPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)

cutsRecoTracksFromPVPt09DuplicateMerge = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('duplicateMerge'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracksFromPVPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksFromPVPt09DuplicateMergeHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('duplicateMerge'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracksFromPVPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)

cutsRecoTracksFromPVPt09HighPtTripletStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('highPtTripletStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracksFromPVPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksFromPVPt09HighPtTripletStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('highPtTripletStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracksFromPVPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)

cutsRecoTracksFromPVPt09Hp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracksFromPVPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)

cutsRecoTracksFromPVPt09InitialStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('initialStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracksFromPVPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksFromPVPt09InitialStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('initialStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracksFromPVPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)

cutsRecoTracksFromPVPt09LowPtQuadStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('lowPtQuadStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracksFromPVPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksFromPVPt09LowPtQuadStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('lowPtQuadStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracksFromPVPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)

cutsRecoTracksFromPVPt09LowPtTripletStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('lowPtTripletStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracksFromPVPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksFromPVPt09LowPtTripletStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('lowPtTripletStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracksFromPVPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)

cutsRecoTracksFromPVPt09MuonSeededStepInOut = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('muonSeededStepInOut'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracksFromPVPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksFromPVPt09MuonSeededStepInOutHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('muonSeededStepInOut'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracksFromPVPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksFromPVPt09MuonSeededStepOutIn = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('muonSeededStepOutIn'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracksFromPVPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksFromPVPt09MuonSeededStepOutInHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('muonSeededStepOutIn'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracksFromPVPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)

cutsRecoTracksFromPVPt09PixelPairStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('pixelPairStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracksFromPVPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksFromPVPt09PixelPairStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('pixelPairStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracksFromPVPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)

cutsRecoTracksHighPtTripletStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('highPtTripletStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksHighPtTripletStepByAlgoMask = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring('highPtTripletStep'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksHighPtTripletStepByAlgoMaskHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring('highPtTripletStep'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksHighPtTripletStepByOriginalAlgo = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring('highPtTripletStep'),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksHighPtTripletStepByOriginalAlgoHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring('highPtTripletStep'),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksHighPtTripletStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('highPtTripletStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)

cutsRecoTracksHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksInitialStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('initialStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksInitialStepByAlgoMask = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring('initialStep'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksInitialStepByAlgoMaskHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring('initialStep'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksInitialStepByOriginalAlgo = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring('initialStep'),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksInitialStepByOriginalAlgoHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring('initialStep'),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksInitialStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('initialStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)

cutsRecoTracksLowPtQuadStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('lowPtQuadStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksLowPtQuadStepByAlgoMask = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring('lowPtQuadStep'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksLowPtQuadStepByAlgoMaskHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring('lowPtQuadStep'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksLowPtQuadStepByOriginalAlgo = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring('lowPtQuadStep'),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksLowPtQuadStepByOriginalAlgoHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring('lowPtQuadStep'),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksLowPtQuadStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('lowPtQuadStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)

cutsRecoTracksLowPtTripletStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('lowPtTripletStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksLowPtTripletStepByAlgoMask = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring('lowPtTripletStep'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksLowPtTripletStepByAlgoMaskHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring('lowPtTripletStep'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksLowPtTripletStepByOriginalAlgo = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring('lowPtTripletStep'),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksLowPtTripletStepByOriginalAlgoHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring('lowPtTripletStep'),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksLowPtTripletStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('lowPtTripletStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)



cutsRecoTracksMuonSeededStepInOut = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('muonSeededStepInOut'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksMuonSeededStepInOutByAlgoMask = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring('muonSeededStepInOut'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksMuonSeededStepInOutByAlgoMaskHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring('muonSeededStepInOut'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksMuonSeededStepInOutByOriginalAlgo = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring('muonSeededStepInOut'),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksMuonSeededStepInOutByOriginalAlgoHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring('muonSeededStepInOut'),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksMuonSeededStepInOutHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('muonSeededStepInOut'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksMuonSeededStepOutIn = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('muonSeededStepOutIn'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksMuonSeededStepOutInByAlgoMask = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring('muonSeededStepOutIn'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksMuonSeededStepOutInByAlgoMaskHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring('muonSeededStepOutIn'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksMuonSeededStepOutInByOriginalAlgo = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring('muonSeededStepOutIn'),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksMuonSeededStepOutInByOriginalAlgoHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring('muonSeededStepOutIn'),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksMuonSeededStepOutInHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('muonSeededStepOutIn'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)

cutsRecoTracksPixelPairStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('pixelPairStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksPixelPairStepByAlgoMask = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring('pixelPairStep'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksPixelPairStepByAlgoMaskHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring('pixelPairStep'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksPixelPairStepByOriginalAlgo = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring('pixelPairStep'),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksPixelPairStepByOriginalAlgoHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring('pixelPairStep'),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksPixelPairStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('pixelPairStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)

cutsRecoTracksPt09DetachedQuadStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('detachedQuadStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracksPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksPt09DetachedQuadStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('detachedQuadStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracksPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)

cutsRecoTracksPt09DuplicateMerge = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('duplicateMerge'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracksPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksPt09DuplicateMergeHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('duplicateMerge'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracksPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksPt09HighPtTripletStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('highPtTripletStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracksPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksPt09HighPtTripletStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('highPtTripletStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracksPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)

cutsRecoTracksPt09Hp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracksPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksPt09InitialStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('initialStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracksPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksPt09InitialStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('initialStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracksPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)

cutsRecoTracksPt09LowPtQuadStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('lowPtQuadStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracksPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksPt09LowPtQuadStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('lowPtQuadStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracksPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)

cutsRecoTracksPt09LowPtTripletStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('lowPtTripletStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracksPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksPt09LowPtTripletStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('lowPtTripletStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracksPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)

cutsRecoTracksPt09MuonSeededStepInOut = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('muonSeededStepInOut'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracksPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksPt09MuonSeededStepInOutHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('muonSeededStepInOut'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracksPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksPt09MuonSeededStepOutIn = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('muonSeededStepOutIn'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracksPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksPt09MuonSeededStepOutInHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('muonSeededStepOutIn'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracksPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)
cutsRecoTracksPt09PixelPairStep = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('pixelPairStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracksPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


cutsRecoTracksPt09PixelPairStepHp = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring('pixelPairStep'),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.1),
    quality = cms.vstring('highPurity'),
    src = cms.InputTag("generalTracksPt09"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)

generalTracksFromPV = cms.EDProducer("TrackWithVertexRefSelector",
    copyExtras = cms.untracked.bool(False),
    copyTrajectories = cms.untracked.bool(False),
    d0Max = cms.double(999.0),
    dzMax = cms.double(999.0),
    etaMax = cms.double(5.0),
    etaMin = cms.double(0.0),
    nSigmaDtVertex = cms.double(0),
    nVertices = cms.uint32(1),
    normalizedChi2 = cms.double(999999.0),
    numberOfLostHits = cms.uint32(999),
    numberOfValidHits = cms.uint32(0),
    numberOfValidPixelHits = cms.uint32(0),
    ptErrorCut = cms.double(10000000000.0),
    ptMax = cms.double(10000000000.0),
    ptMin = cms.double(0),
    quality = cms.string('loose'),
    rhoVtx = cms.double(10000000000.0),
    src = cms.InputTag("generalTracks"),
    timeResosTag = cms.InputTag(""),
    timesTag = cms.InputTag(""),
    useVtx = cms.bool(True),
    vertexTag = cms.InputTag("offlinePrimaryVertices"),
    vtxFallback = cms.bool(False),
    zetaVtx = cms.double(0.1)
)


generalTracksFromPVPt09 = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracksFromPV"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)


generalTracksPt09 = cms.EDProducer("RecoTrackViewRefSelector",
    algorithm = cms.vstring(),
    algorithmMaskContains = cms.vstring(),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    invertRapidityCut = cms.bool(False), # cmssw_11_1
    lip = cms.double(300.0),
    maxChi2 = cms.double(10000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(5.0),
    min3DLayer = cms.int32(0),
    minHit = cms.int32(0),
    minLayer = cms.int32(3),
    minPhi = cms.double(-3.2),
    minPixelHit = cms.int32(0),
    minRapidity = cms.double(-5.0),
    originalAlgorithm = cms.vstring(),
    ptMin = cms.double(0.9),
    quality = cms.vstring('loose'),
    src = cms.InputTag("generalTracks"),
    tip = cms.double(120.0),
    usePV = cms.bool(False),
    vertexTag = cms.InputTag("offlinePrimaryVertices")
)

quickTrackAssociatorByHits = cms.EDProducer("QuickTrackAssociatorByHitsProducer",
    AbsoluteNumberOfHits = cms.bool(False),
    Cut_RecoToSim = cms.double(0.75),
    PixelHitWeight = cms.double(1.0),
    Purity_SimToReco = cms.double(0.75),
    Quality_SimToReco = cms.double(0.5),
    SimToRecoDenominator = cms.string('reco'),
    ThreeHitTracksAreSpecial = cms.bool(True),
    cluster2TPSrc = cms.InputTag("tpClusterProducer"),
    useClusterTPAssociation = cms.bool(True)
)

quickTrackAssociatorByHitsPreSplitting = cms.EDProducer("QuickTrackAssociatorByHitsProducer",
    AbsoluteNumberOfHits = cms.bool(False),
    Cut_RecoToSim = cms.double(0.75),
    PixelHitWeight = cms.double(1.0),
    Purity_SimToReco = cms.double(0.75),
    Quality_SimToReco = cms.double(0.5),
    SimToRecoDenominator = cms.string('reco'),
    ThreeHitTracksAreSpecial = cms.bool(True),
    cluster2TPSrc = cms.InputTag("tpClusterProducerPreSplitting"),
    useClusterTPAssociation = cms.bool(True)
)

seedTracksdetachedQuadStepSeeds = cms.EDProducer("TrackFromSeedProducer",
    TTRHBuilder = cms.string('WithoutRefit'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    src = cms.InputTag("detachedQuadStepSeeds")
)

seedTrackshighPtTripletStepSeeds = cms.EDProducer("TrackFromSeedProducer",
    TTRHBuilder = cms.string('WithoutRefit'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    src = cms.InputTag("highPtTripletStepSeeds")
)


seedTracksinitialStepSeeds = cms.EDProducer("TrackFromSeedProducer",
    TTRHBuilder = cms.string('WithoutRefit'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    src = cms.InputTag("initialStepSeeds")
)

seedTrackslowPtQuadStepSeeds = cms.EDProducer("TrackFromSeedProducer",
    TTRHBuilder = cms.string('WithoutRefit'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    src = cms.InputTag("lowPtQuadStepSeeds")
)


seedTrackslowPtTripletStepSeeds = cms.EDProducer("TrackFromSeedProducer",
    TTRHBuilder = cms.string('WithoutRefit'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    src = cms.InputTag("lowPtTripletStepSeeds")
)

seedTracksmuonSeededSeedsInOut = cms.EDProducer("TrackFromSeedProducer",
    TTRHBuilder = cms.string('WithoutRefit'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    src = cms.InputTag("muonSeededSeedsInOut")
)


seedTracksmuonSeededSeedsOutIn = cms.EDProducer("TrackFromSeedProducer",
    TTRHBuilder = cms.string('WithoutRefit'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    src = cms.InputTag("muonSeededSeedsOutIn")
)

seedTrackspixelPairStepSeeds = cms.EDProducer("TrackFromSeedProducer",
    TTRHBuilder = cms.string('WithoutRefit'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    src = cms.InputTag("pixelPairStepSeeds")
)

tpClusterProducer = cms.EDProducer("ClusterTPAssociationProducer",
    phase2OTClusterSrc = cms.InputTag("siPhase2Clusters"),
    phase2OTSimLinkSrc = cms.InputTag("simSiPixelDigis","Tracker"),
    pixelClusterSrc = cms.InputTag("siPixelClusters"),
    pixelSimLinkSrc = cms.InputTag("simSiPixelDigis","Pixel"),
    simTrackSrc = cms.InputTag("g4SimHits"),
    stripClusterSrc = cms.InputTag("siStripClusters"),
    stripSimLinkSrc = cms.InputTag("simSiStripDigis"),
    trackingParticleSrc = cms.InputTag("mix","MergedTrackTruth")
)


tpClusterProducerPreSplitting = cms.EDProducer("ClusterTPAssociationProducer",
    phase2OTClusterSrc = cms.InputTag("siPhase2Clusters"),
    phase2OTSimLinkSrc = cms.InputTag("simSiPixelDigis","Tracker"),
    pixelClusterSrc = cms.InputTag("siPixelClustersPreSplitting"),
    pixelSimLinkSrc = cms.InputTag("simSiPixelDigis","Pixel"),
    simTrackSrc = cms.InputTag("g4SimHits"),
    stripClusterSrc = cms.InputTag("siStripClusters"),
    stripSimLinkSrc = cms.InputTag("simSiStripDigis"),
    trackingParticleSrc = cms.InputTag("mix","MergedTrackTruth")
)
trackingParticleNumberOfLayersProducer = cms.EDProducer("TrackingParticleNumberOfLayersProducer",
    simHits = cms.VInputTag("g4SimHits:TrackerHitsPixelBarrelLowTof", "g4SimHits:TrackerHitsPixelEndcapLowTof"),
    trackingParticles = cms.InputTag("mix","MergedTrackTruth")
)
trackingParticleRecoTrackAsssociation = cms.EDProducer("TrackAssociatorEDProducer",
    associator = cms.InputTag("quickTrackAssociatorByHits"),
    ignoremissingtrackcollection = cms.untracked.bool(False),
    label_tp = cms.InputTag("mix","MergedTrackTruth"),
    label_tr = cms.InputTag("generalTracks")
)

trackingParticlesBHadron = cms.EDProducer("TrackingParticleBHadronRefSelector",
    src = cms.InputTag("mix","MergedTrackTruth")
)

trackingParticlesConversion = cms.EDProducer("TrackingParticleConversionRefSelector",
    src = cms.InputTag("mix","MergedTrackTruth")
)
trackingParticlesElectron = cms.EDFilter("TrackingParticleRefSelector",
    chargedOnly = cms.bool(True),
    intimeOnly = cms.bool(False),
    invertRapidityCut = cms.bool(False),
    lip = cms.double(100000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5), # previous 10
    minHit = cms.int32(0),
    minPhi = cms.double(-3.2),
    minRapidity = cms.double(-4.5), # previous -10
    pdgId = cms.vint32(-11, 11),
    ptMax = cms.double(1e+100),
    ptMin = cms.double(0),
    signalOnly = cms.bool(False),
    src = cms.InputTag("mix","MergedTrackTruth"),
    stableOnly = cms.bool(False),
    tip = cms.double(100000.0)
)

trackingParticlesSignal = cms.EDFilter("TrackingParticleRefSelector",
    chargedOnly = cms.bool(False),
    intimeOnly = cms.bool(False),
    invertRapidityCut = cms.bool(False),
    lip = cms.double(100000.0),
    maxPhi = cms.double(3.2),
    maxRapidity = cms.double(4.5), # previous 10
    minHit = cms.int32(0),
    minPhi = cms.double(-3.2),
    minRapidity = cms.double(-4.5), # previous -10
    pdgId = cms.vint32(),
    ptMax = cms.double(1e+100),
    ptMin = cms.double(0),
    signalOnly = cms.bool(True),
    src = cms.InputTag("mix","MergedTrackTruth"),
    stableOnly = cms.bool(False),
    tip = cms.double(100000.0)
)


selectedOfflinePrimaryVertices = cms.EDFilter("VertexSelector",
    cut = cms.string('isValid & ndof > 4 & tracksSize > 0 & abs(z) <= 24 & abs(position.Rho) <= 2.'),
    filter = cms.bool(False),
    src = cms.InputTag("offlinePrimaryVertices")
)
selectedOfflinePrimaryVerticesWithBS = cms.EDFilter("VertexSelector",
    cut = cms.string('isValid & ndof > 4 & tracksSize > 0 & abs(z) <= 24 & abs(position.Rho) <= 2.'),
    filter = cms.bool(False),
    src = cms.InputTag("offlinePrimaryVerticesWithBS")
)
simHitTPAssocProducer = cms.EDProducer("SimHitTPAssociationProducer",
    simHitSrc = cms.VInputTag("g4SimHits:TrackerHitsPixelBarrelLowTof", "g4SimHits:TrackerHitsPixelEndcapLowTof"),
    trackingParticleSrc = cms.InputTag("mix","MergedTrackTruth")
)

v0Validator = cms.EDProducer("V0Validator",
    DQMRootFileName = cms.untracked.string(''),
    dirName = cms.untracked.string('Vertexing/V0V'),
    kShortCollection = cms.untracked.InputTag("generalV0Candidates","Kshort"),
    lambdaCollection = cms.untracked.InputTag("generalV0Candidates","Lambda"),
    trackAssociatorMap = cms.untracked.InputTag("trackingParticleRecoTrackAsssociation"),
    trackingVertexCollection = cms.untracked.InputTag("mix","MergedTrackTruth"),
    vertexCollection = cms.untracked.InputTag("offlinePrimaryVertices")
)

vertexAnalysisTrackingOnly = cms.EDProducer("PrimaryVertexAnalyzer4PUSlimmed",
    do_generic_sim_plots = cms.untracked.bool(True),
    root_folder = cms.untracked.string('Vertexing/PrimaryVertexV'),
    trackAssociatorMap = cms.untracked.InputTag("trackingParticleRecoTrackAsssociation"),
    trackingParticleCollection = cms.untracked.InputTag("mix","MergedTrackTruth"),
    trackingVertexCollection = cms.untracked.InputTag("mix","MergedTrackTruth"),
    use_only_charged_tracks = cms.untracked.bool(True),
    verbose = cms.untracked.bool(False),
    vertexAssociator = cms.untracked.InputTag("VertexAssociatorByPositionAndTracks"),
    vertexRecoCollections = cms.VInputTag("offlinePrimaryVertices", "offlinePrimaryVerticesWithBS", "selectedOfflinePrimaryVertices", "selectedOfflinePrimaryVerticesWithBS", "firstStepPrimaryVertices")
)


#########################################################################
MC_prevalidation_v0 = cms.Path(trackValidatorTrackingOnly+trackValidatorTPPtLess09Standalone+trackValidatorFromPVStandalone+trackValidatorFromPVAllTPStandalone+
trackValidatorAllTPEfficStandalone+trackValidatorBHadronTrackingOnly+trackValidatorSeedingTrackingOnly+trackValidatorSeedingPreSplittingTrackingOnly+trackValidatorBuilding+trackValidatorBuildingPreSplitting, cms.Task(VertexAssociatorByPositionAndTracks, cutsRecoTracksBtvLike, cutsRecoTracksDetachedQuadStep, cutsRecoTracksDetachedQuadStepByAlgoMask, cutsRecoTracksDetachedQuadStepByAlgoMaskHp, cutsRecoTracksDetachedQuadStepByOriginalAlgo, cutsRecoTracksDetachedQuadStepByOriginalAlgoHp, cutsRecoTracksDetachedQuadStepHp, cutsRecoTracksDuplicateMerge, cutsRecoTracksDuplicateMergeByAlgoMask, cutsRecoTracksDuplicateMergeByAlgoMaskHp, cutsRecoTracksDuplicateMergeHp, cutsRecoTracksFromPVDetachedQuadStep, cutsRecoTracksFromPVDetachedQuadStepHp, cutsRecoTracksFromPVDuplicateMerge, cutsRecoTracksFromPVDuplicateMergeHp, cutsRecoTracksFromPVHighPtTripletStep, cutsRecoTracksFromPVHighPtTripletStepHp, cutsRecoTracksFromPVHp, cutsRecoTracksFromPVInitialStep, cutsRecoTracksFromPVInitialStepHp, cutsRecoTracksFromPVLowPtQuadStep, cutsRecoTracksFromPVLowPtQuadStepHp, cutsRecoTracksFromPVLowPtTripletStep, cutsRecoTracksFromPVLowPtTripletStepHp, cutsRecoTracksFromPVMuonSeededStepInOut, cutsRecoTracksFromPVMuonSeededStepInOutHp, cutsRecoTracksFromPVMuonSeededStepOutIn, cutsRecoTracksFromPVMuonSeededStepOutInHp, cutsRecoTracksFromPVPixelPairStep, cutsRecoTracksFromPVPixelPairStepHp, cutsRecoTracksFromPVPt09DetachedQuadStep, cutsRecoTracksFromPVPt09DetachedQuadStepHp, cutsRecoTracksFromPVPt09DuplicateMerge, cutsRecoTracksFromPVPt09DuplicateMergeHp, cutsRecoTracksFromPVPt09HighPtTripletStep, cutsRecoTracksFromPVPt09HighPtTripletStepHp, cutsRecoTracksFromPVPt09Hp, cutsRecoTracksFromPVPt09InitialStep, cutsRecoTracksFromPVPt09InitialStepHp, cutsRecoTracksFromPVPt09LowPtQuadStep, cutsRecoTracksFromPVPt09LowPtQuadStepHp, cutsRecoTracksFromPVPt09LowPtTripletStep, cutsRecoTracksFromPVPt09LowPtTripletStepHp, cutsRecoTracksFromPVPt09MuonSeededStepInOut, cutsRecoTracksFromPVPt09MuonSeededStepInOutHp, cutsRecoTracksFromPVPt09MuonSeededStepOutIn, cutsRecoTracksFromPVPt09MuonSeededStepOutInHp, cutsRecoTracksFromPVPt09PixelPairStep, cutsRecoTracksFromPVPt09PixelPairStepHp, cutsRecoTracksHighPtTripletStep, cutsRecoTracksHighPtTripletStepByAlgoMask, cutsRecoTracksHighPtTripletStepByAlgoMaskHp, cutsRecoTracksHighPtTripletStepByOriginalAlgo, cutsRecoTracksHighPtTripletStepByOriginalAlgoHp, cutsRecoTracksHighPtTripletStepHp, cutsRecoTracksHp, cutsRecoTracksInitialStep, cutsRecoTracksInitialStepByAlgoMask, cutsRecoTracksInitialStepByAlgoMaskHp, cutsRecoTracksInitialStepByOriginalAlgo, cutsRecoTracksInitialStepByOriginalAlgoHp, cutsRecoTracksInitialStepHp, cutsRecoTracksLowPtQuadStep, cutsRecoTracksLowPtQuadStepByAlgoMask, cutsRecoTracksLowPtQuadStepByAlgoMaskHp, cutsRecoTracksLowPtQuadStepByOriginalAlgo, cutsRecoTracksLowPtQuadStepByOriginalAlgoHp, cutsRecoTracksLowPtQuadStepHp, cutsRecoTracksLowPtTripletStep, cutsRecoTracksLowPtTripletStepByAlgoMask, cutsRecoTracksLowPtTripletStepByAlgoMaskHp, cutsRecoTracksLowPtTripletStepByOriginalAlgo, cutsRecoTracksLowPtTripletStepByOriginalAlgoHp, cutsRecoTracksLowPtTripletStepHp, cutsRecoTracksMuonSeededStepInOut, cutsRecoTracksMuonSeededStepInOutByAlgoMask, cutsRecoTracksMuonSeededStepInOutByAlgoMaskHp, cutsRecoTracksMuonSeededStepInOutByOriginalAlgo, cutsRecoTracksMuonSeededStepInOutByOriginalAlgoHp, cutsRecoTracksMuonSeededStepInOutHp, cutsRecoTracksMuonSeededStepOutIn, cutsRecoTracksMuonSeededStepOutInByAlgoMask, cutsRecoTracksMuonSeededStepOutInByAlgoMaskHp, cutsRecoTracksMuonSeededStepOutInByOriginalAlgo, cutsRecoTracksMuonSeededStepOutInByOriginalAlgoHp, cutsRecoTracksMuonSeededStepOutInHp, cutsRecoTracksPixelPairStep, cutsRecoTracksPixelPairStepByAlgoMask, cutsRecoTracksPixelPairStepByAlgoMaskHp, cutsRecoTracksPixelPairStepByOriginalAlgo, cutsRecoTracksPixelPairStepByOriginalAlgoHp, cutsRecoTracksPixelPairStepHp, cutsRecoTracksPt09DetachedQuadStep, cutsRecoTracksPt09DetachedQuadStepHp, cutsRecoTracksPt09DuplicateMerge, cutsRecoTracksPt09DuplicateMergeHp, cutsRecoTracksPt09HighPtTripletStep, cutsRecoTracksPt09HighPtTripletStepHp, cutsRecoTracksPt09Hp, cutsRecoTracksPt09InitialStep, cutsRecoTracksPt09InitialStepHp, cutsRecoTracksPt09LowPtQuadStep, cutsRecoTracksPt09LowPtQuadStepHp, cutsRecoTracksPt09LowPtTripletStep, cutsRecoTracksPt09LowPtTripletStepHp, cutsRecoTracksPt09MuonSeededStepInOut, cutsRecoTracksPt09MuonSeededStepInOutHp, cutsRecoTracksPt09MuonSeededStepOutIn, cutsRecoTracksPt09MuonSeededStepOutInHp, cutsRecoTracksPt09PixelPairStep, cutsRecoTracksPt09PixelPairStepHp, generalTracksFromPV, generalTracksFromPVPt09, generalTracksPt09, quickTrackAssociatorByHits, quickTrackAssociatorByHitsPreSplitting, seedTracksdetachedQuadStepSeeds, seedTrackshighPtTripletStepSeeds, seedTracksinitialStepSeeds, seedTrackslowPtQuadStepSeeds, seedTrackslowPtTripletStepSeeds, seedTracksmuonSeededSeedsInOut, seedTracksmuonSeededSeedsOutIn, seedTrackspixelPairStepSeeds, tpClusterProducer, tpClusterProducerPreSplitting, trackingParticleNumberOfLayersProducer, trackingParticleRecoTrackAsssociation, trackingParticlesBHadron, trackingParticlesConversion, trackingParticlesElectron, trackingParticlesSignal), cms.Task(selectedOfflinePrimaryVertices, selectedOfflinePrimaryVerticesWithBS, simHitTPAssocProducer, v0Validator, vertexAnalysisTrackingOnly))



