import FWCore.ParameterSet.Config as cms


########################reconstruction_step
###added for cmssw_11_1

TrackProducer = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('undefAlgorithm'),
    Fitter = cms.string('KFFittingSmootherWithOutliersRejectionAndRK'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithAngleAndTemplate'), # this will be changed in the main file for now to "WithTrackAngle"
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("ckfTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)

###added for cmssw_10_6

SiStripClusterChargeCutNone = cms.PSet(  value = cms.double( -1.0 ) )
SiStripClusterChargeCutLoose = cms.PSet(  value = cms.double( 1620.0 ) )
SiStripClusterChargeCutTight = cms.PSet(  value = cms.double( 1945.0 ) )
#####################################################

CkfBaseTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

bunchSpacingProducer = cms.EDProducer("BunchSpacingProducer")

csc2DRecHits = cms.EDProducer("CSCRecHitDProducer",
    CSCDebug = cms.untracked.bool(False),
    CSCNoOfTimeBinsForDynamicPedestal = cms.int32(2),
    CSCStripClusterChargeCut = cms.double(25.0),
    CSCStripClusterSize = cms.untracked.int32(3),
    CSCStripPeakThreshold = cms.double(10.0),
    CSCStripxtalksOffset = cms.double(0.03),
    CSCUseCalibrations = cms.bool(True),
    CSCUseGasGainCorrections = cms.bool(False),
    CSCUseReducedWireTimeWindow = cms.bool(False),
    CSCUseStaticPedestals = cms.bool(False),
    CSCUseTimingCorrections = cms.bool(True),
    CSCWireClusterDeltaT = cms.int32(1),
    CSCWireTimeWindowHigh = cms.int32(15),
    CSCWireTimeWindowLow = cms.int32(0),
    CSCstripWireDeltaTime = cms.int32(8),
    ConstSyst_ME12 = cms.double(0.02),
    ConstSyst_ME13 = cms.double(0.03),
    ConstSyst_ME1a = cms.double(0.01),
    ConstSyst_ME1b = cms.double(0.02),
    ConstSyst_ME21 = cms.double(0.03),
    ConstSyst_ME22 = cms.double(0.03),
    ConstSyst_ME31 = cms.double(0.03),
    ConstSyst_ME32 = cms.double(0.03),
    ConstSyst_ME41 = cms.double(0.03),
    NoiseLevel_ME12 = cms.double(7.0),
    NoiseLevel_ME13 = cms.double(4.0),
    NoiseLevel_ME1a = cms.double(9.0),
    NoiseLevel_ME1b = cms.double(6.0),
    NoiseLevel_ME21 = cms.double(5.0),
    NoiseLevel_ME22 = cms.double(7.0),
    NoiseLevel_ME31 = cms.double(5.0),
    NoiseLevel_ME32 = cms.double(7.0),
    NoiseLevel_ME41 = cms.double(5.0),
    UseAverageTime = cms.bool(False),
    UseFivePoleFit = cms.bool(True),
    UseParabolaFit = cms.bool(False),
    XTasymmetry_ME12 = cms.double(0.015),
    XTasymmetry_ME13 = cms.double(0.02),
    XTasymmetry_ME1a = cms.double(0.023),
    XTasymmetry_ME1b = cms.double(0.01),
    XTasymmetry_ME21 = cms.double(0.023),
    XTasymmetry_ME22 = cms.double(0.023),
    XTasymmetry_ME31 = cms.double(0.023),
    XTasymmetry_ME32 = cms.double(0.023),
    XTasymmetry_ME41 = cms.double(0.023),
    readBadChambers = cms.bool(True),
    readBadChannels = cms.bool(False),
    stripDigiTag = cms.InputTag("muonCSCDigis","MuonCSCStripDigi"),
    wireDigiTag = cms.InputTag("muonCSCDigis","MuonCSCWireDigi")
)

cscSegments = cms.EDProducer("CSCSegmentProducer",
    algo_psets = cms.VPSet(
        cms.PSet(
            algo_name = cms.string('CSCSegAlgoSK'),
            algo_psets = cms.VPSet(
                cms.PSet(
                    chi2Max = cms.double(99999.0),
                    dPhiFineMax = cms.double(0.025),
                    dPhiMax = cms.double(0.003),
                    dRPhiFineMax = cms.double(8.0),
                    dRPhiMax = cms.double(8.0),
                    minLayersApart = cms.int32(2),
                    verboseInfo = cms.untracked.bool(True),
                    wideSeg = cms.double(3.0)
                ), 
                cms.PSet(
                    chi2Max = cms.double(99999.0),
                    dPhiFineMax = cms.double(0.025),
                    dPhiMax = cms.double(0.025),
                    dRPhiFineMax = cms.double(3.0),
                    dRPhiMax = cms.double(8.0),
                    minLayersApart = cms.int32(2),
                    verboseInfo = cms.untracked.bool(True),
                    wideSeg = cms.double(3.0)
                )
            ),
            chamber_types = cms.vstring(
                'ME1/a', 
                'ME1/b', 
                'ME1/2', 
                'ME1/3', 
                'ME2/1', 
                'ME2/2', 
                'ME3/1', 
                'ME3/2', 
                'ME4/1', 
                'ME4/2'
            ),
            parameters_per_chamber_type = cms.vint32(
                2, 1, 1, 1, 1, 
                1, 1, 1, 1, 1
            )
        ), 
        cms.PSet(
            algo_name = cms.string('CSCSegAlgoTC'),
            algo_psets = cms.VPSet(
                cms.PSet(
                    SegmentSorting = cms.int32(1),
                    chi2Max = cms.double(6000.0),
                    chi2ndfProbMin = cms.double(0.0001),
                    dPhiFineMax = cms.double(0.02),
                    dPhiMax = cms.double(0.003),
                    dRPhiFineMax = cms.double(6.0),
                    dRPhiMax = cms.double(1.2),
                    minLayersApart = cms.int32(2),
                    verboseInfo = cms.untracked.bool(True)
                ), 
                cms.PSet(
                    SegmentSorting = cms.int32(1),
                    chi2Max = cms.double(6000.0),
                    chi2ndfProbMin = cms.double(0.0001),
                    dPhiFineMax = cms.double(0.013),
                    dPhiMax = cms.double(0.00198),
                    dRPhiFineMax = cms.double(3.0),
                    dRPhiMax = cms.double(0.6),
                    minLayersApart = cms.int32(2),
                    verboseInfo = cms.untracked.bool(True)
                )
            ),
            chamber_types = cms.vstring(
                'ME1/a', 
                'ME1/b', 
                'ME1/2', 
                'ME1/3', 
                'ME2/1', 
                'ME2/2', 
                'ME3/1', 
                'ME3/2', 
                'ME4/1', 
                'ME4/2'
            ),
            parameters_per_chamber_type = cms.vint32(
                2, 1, 1, 1, 1, 
                1, 1, 1, 1, 1
            )
        ), 
        cms.PSet(
            algo_name = cms.string('CSCSegAlgoDF'),
            algo_psets = cms.VPSet(
                cms.PSet(
                    CSCSegmentDebug = cms.untracked.bool(False),
                    Pruning = cms.untracked.bool(False),
                    chi2Max = cms.double(5000.0),
                    dPhiFineMax = cms.double(0.025),
                    dRPhiFineMax = cms.double(8.0),
                    dXclusBoxMax = cms.double(8.0),
                    dYclusBoxMax = cms.double(8.0),
                    maxDPhi = cms.double(999.0),
                    maxDTheta = cms.double(999.0),
                    maxRatioResidualPrune = cms.double(3.0),
                    minHitsForPreClustering = cms.int32(10),
                    minHitsPerSegment = cms.int32(3),
                    minLayersApart = cms.int32(2),
                    nHitsPerClusterIsShower = cms.int32(20),
                    preClustering = cms.untracked.bool(False),
                    tanPhiMax = cms.double(0.5),
                    tanThetaMax = cms.double(1.2)
                ), 
                cms.PSet(
                    CSCSegmentDebug = cms.untracked.bool(False),
                    Pruning = cms.untracked.bool(False),
                    chi2Max = cms.double(5000.0),
                    dPhiFineMax = cms.double(0.025),
                    dRPhiFineMax = cms.double(12.0),
                    dXclusBoxMax = cms.double(8.0),
                    dYclusBoxMax = cms.double(12.0),
                    maxDPhi = cms.double(999.0),
                    maxDTheta = cms.double(999.0),
                    maxRatioResidualPrune = cms.double(3.0),
                    minHitsForPreClustering = cms.int32(10),
                    minHitsPerSegment = cms.int32(3),
                    minLayersApart = cms.int32(2),
                    nHitsPerClusterIsShower = cms.int32(20),
                    preClustering = cms.untracked.bool(False),
                    tanPhiMax = cms.double(0.8),
                    tanThetaMax = cms.double(2.0)
                ), 
                cms.PSet(
                    CSCSegmentDebug = cms.untracked.bool(False),
                    Pruning = cms.untracked.bool(False),
                    chi2Max = cms.double(5000.0),
                    dPhiFineMax = cms.double(0.025),
                    dRPhiFineMax = cms.double(8.0),
                    dXclusBoxMax = cms.double(8.0),
                    dYclusBoxMax = cms.double(8.0),
                    maxDPhi = cms.double(999.0),
                    maxDTheta = cms.double(999.0),
                    maxRatioResidualPrune = cms.double(3.0),
                    minHitsForPreClustering = cms.int32(30),
                    minHitsPerSegment = cms.int32(3),
                    minLayersApart = cms.int32(2),
                    nHitsPerClusterIsShower = cms.int32(20),
                    preClustering = cms.untracked.bool(False),
                    tanPhiMax = cms.double(0.5),
                    tanThetaMax = cms.double(1.2)
                )
            ),
            chamber_types = cms.vstring(
                'ME1/a', 
                'ME1/b', 
                'ME1/2', 
                'ME1/3', 
                'ME2/1', 
                'ME2/2', 
                'ME3/1', 
                'ME3/2', 
                'ME4/1', 
                'ME4/2'
            ),
            parameters_per_chamber_type = cms.vint32(
                3, 1, 2, 2, 1, 
                2, 1, 2, 1, 2
            )
        ), 
        cms.PSet(
            algo_name = cms.string('CSCSegAlgoST'),
            algo_psets = cms.VPSet(
                cms.PSet(
                    BPMinImprovement = cms.double(10000.0),
                    BrutePruning = cms.bool(True),
                    CSCDebug = cms.untracked.bool(False),
                    CorrectTheErrors = cms.bool(True),
                    Covariance = cms.double(0.0),
                    ForceCovariance = cms.bool(False),
                    ForceCovarianceAll = cms.bool(False),
                    NormChi2Cut2D = cms.double(20.0),
                    NormChi2Cut3D = cms.double(10.0),
                    Pruning = cms.bool(True),
                    SeedBig = cms.double(0.0015),
                    SeedSmall = cms.double(0.0002),
                    curvePenalty = cms.double(2.0),
                    curvePenaltyThreshold = cms.double(0.85),
                    dPhiFineMax = cms.double(0.025),
                    dRPhiFineMax = cms.double(8.0),
                    dXclusBoxMax = cms.double(4.0),
                    dYclusBoxMax = cms.double(8.0),
                    hitDropLimit4Hits = cms.double(0.6),
                    hitDropLimit5Hits = cms.double(0.8),
                    hitDropLimit6Hits = cms.double(0.3333),
                    maxDPhi = cms.double(999.0),
                    maxDTheta = cms.double(999.0),
                    maxRatioResidualPrune = cms.double(3),
                    maxRecHitsInCluster = cms.int32(20),
                    minHitsPerSegment = cms.int32(3),
                    onlyBestSegment = cms.bool(False),
                    preClustering = cms.bool(True),
                    preClusteringUseChaining = cms.bool(True),
                    prePrun = cms.bool(True),
                    prePrunLimit = cms.double(3.17),
                    tanPhiMax = cms.double(0.5),
                    tanThetaMax = cms.double(1.2),
                    useShowering = cms.bool(False),
                    yweightPenalty = cms.double(1.5),
                    yweightPenaltyThreshold = cms.double(1.0)
                ), 
                cms.PSet(
                    BPMinImprovement = cms.double(10000.0),
                    BrutePruning = cms.bool(True),
                    CSCDebug = cms.untracked.bool(False),
                    CorrectTheErrors = cms.bool(True),
                    Covariance = cms.double(0.0),
                    ForceCovariance = cms.bool(False),
                    ForceCovarianceAll = cms.bool(False),
                    NormChi2Cut2D = cms.double(20.0),
                    NormChi2Cut3D = cms.double(10.0),
                    Pruning = cms.bool(True),
                    SeedBig = cms.double(0.0015),
                    SeedSmall = cms.double(0.0002),
                    curvePenalty = cms.double(2.0),
                    curvePenaltyThreshold = cms.double(0.85),
                    dPhiFineMax = cms.double(0.025),
                    dRPhiFineMax = cms.double(8.0),
                    dXclusBoxMax = cms.double(4.0),
                    dYclusBoxMax = cms.double(8.0),
                    hitDropLimit4Hits = cms.double(0.6),
                    hitDropLimit5Hits = cms.double(0.8),
                    hitDropLimit6Hits = cms.double(0.3333),
                    maxDPhi = cms.double(999.0),
                    maxDTheta = cms.double(999.0),
                    maxRatioResidualPrune = cms.double(3),
                    maxRecHitsInCluster = cms.int32(24),
                    minHitsPerSegment = cms.int32(3),
                    onlyBestSegment = cms.bool(False),
                    preClustering = cms.bool(True),
                    preClusteringUseChaining = cms.bool(True),
                    prePrun = cms.bool(True),
                    prePrunLimit = cms.double(3.17),
                    tanPhiMax = cms.double(0.5),
                    tanThetaMax = cms.double(1.2),
                    useShowering = cms.bool(False),
                    yweightPenalty = cms.double(1.5),
                    yweightPenaltyThreshold = cms.double(1.0)
                )
            ),
            chamber_types = cms.vstring(
                'ME1/a', 
                'ME1/b', 
                'ME1/2', 
                'ME1/3', 
                'ME2/1', 
                'ME2/2', 
                'ME3/1', 
                'ME3/2', 
                'ME4/1', 
                'ME4/2'
            ),
            parameters_per_chamber_type = cms.vint32(
                2, 1, 1, 1, 1, 
                1, 1, 1, 1, 1
            )
        ), 
        cms.PSet(
            algo_name = cms.string('CSCSegAlgoRU'),
            algo_psets = cms.VPSet(
                cms.PSet(
                    chi2Max = cms.double(100.0),
                    chi2Norm_2D_ = cms.double(35),
                    chi2_str = cms.double(50.0),
                    dPhiIntMax = cms.double(0.005),
                    dPhiMax = cms.double(0.006),
                    dRIntMax = cms.double(2.0),
                    dRMax = cms.double(1.5),
                    doCollisions = cms.bool(True),
                    minLayersApart = cms.int32(1),
                    wideSeg = cms.double(3.0)
                ), 
                cms.PSet(
                    chi2Max = cms.double(100.0),
                    chi2Norm_2D_ = cms.double(35),
                    chi2_str = cms.double(50.0),
                    dPhiIntMax = cms.double(0.004),
                    dPhiMax = cms.double(0.005),
                    dRIntMax = cms.double(2.0),
                    dRMax = cms.double(1.5),
                    doCollisions = cms.bool(True),
                    minLayersApart = cms.int32(1),
                    wideSeg = cms.double(3.0)
                ), 
                cms.PSet(
                    chi2Max = cms.double(100.0),
                    chi2Norm_2D_ = cms.double(35),
                    chi2_str = cms.double(50.0),
                    dPhiIntMax = cms.double(0.003),
                    dPhiMax = cms.double(0.004),
                    dRIntMax = cms.double(2.0),
                    dRMax = cms.double(1.5),
                    doCollisions = cms.bool(True),
                    minLayersApart = cms.int32(1),
                    wideSeg = cms.double(3.0)
                ), 
                cms.PSet(
                    chi2Max = cms.double(60.0),
                    chi2Norm_2D_ = cms.double(20),
                    chi2_str = cms.double(30.0),
                    dPhiIntMax = cms.double(0.002),
                    dPhiMax = cms.double(0.003),
                    dRIntMax = cms.double(2.0),
                    dRMax = cms.double(1.5),
                    doCollisions = cms.bool(True),
                    minLayersApart = cms.int32(1),
                    wideSeg = cms.double(3.0)
                ), 
                cms.PSet(
                    chi2Max = cms.double(180.0),
                    chi2Norm_2D_ = cms.double(60),
                    chi2_str = cms.double(80.0),
                    dPhiIntMax = cms.double(0.005),
                    dPhiMax = cms.double(0.007),
                    dRIntMax = cms.double(2.0),
                    dRMax = cms.double(1.5),
                    doCollisions = cms.bool(True),
                    minLayersApart = cms.int32(1),
                    wideSeg = cms.double(3.0)
                ), 
                cms.PSet(
                    chi2Max = cms.double(100.0),
                    chi2Norm_2D_ = cms.double(35),
                    chi2_str = cms.double(50.0),
                    dPhiIntMax = cms.double(0.004),
                    dPhiMax = cms.double(0.006),
                    dRIntMax = cms.double(2.0),
                    dRMax = cms.double(1.5),
                    doCollisions = cms.bool(True),
                    minLayersApart = cms.int32(1),
                    wideSeg = cms.double(3.0)
                )
            ),
            chamber_types = cms.vstring(
                'ME1/a', 
                'ME1/b', 
                'ME1/2', 
                'ME1/3', 
                'ME2/1', 
                'ME2/2', 
                'ME3/1', 
                'ME3/2', 
                'ME4/1', 
                'ME4/2'
            ),
            parameters_per_chamber_type = cms.vint32(
                1, 2, 3, 4, 5, 
                6, 5, 6, 5, 6
            )
        )
    ),
    algo_type = cms.int32(5),
    inputObjects = cms.InputTag("csc2DRecHits")
)

dt1DRecHits = cms.EDProducer("DTRecHitProducer",
    debug = cms.untracked.bool(False),
    dtDigiLabel = cms.InputTag("muonDTDigis"),
    recAlgo = cms.string('DTLinearDriftFromDBAlgo'),
    recAlgoConfig = cms.PSet(
        debug = cms.untracked.bool(False),
        doVdriftCorr = cms.bool(True),
        maxTime = cms.double(420.0),
        minTime = cms.double(-3.0),
        stepTwoFromDigi = cms.bool(False),
        tTrigMode = cms.string('DTTTrigSyncFromDB'),
        tTrigModeConfig = cms.PSet(
            debug = cms.untracked.bool(False),
            doT0Correction = cms.bool(True),
            doTOFCorrection = cms.bool(True),
            doWirePropCorrection = cms.bool(True),
            tTrigLabel = cms.string(''),
            tofCorrType = cms.int32(0),
            vPropWire = cms.double(24.4),
            wirePropCorrType = cms.int32(0)
        ),
        useUncertDB = cms.bool(True)
    )
)

dt4DSegments = cms.EDProducer("DTRecSegment4DProducer",
    Reco4DAlgoConfig = cms.PSet(
        AllDTRecHits = cms.bool(True),
        Reco2DAlgoConfig = cms.PSet(
            AlphaMaxPhi = cms.double(1.0),
            AlphaMaxTheta = cms.double(0.9),
            MaxAllowedHits = cms.uint32(50),
            MaxChi2 = cms.double(4.0),
            debug = cms.untracked.bool(False),
            hit_afterT0_resolution = cms.double(0.03),
            nSharedHitsMax = cms.int32(2),
            nUnSharedHitsMin = cms.int32(2),
            performT0SegCorrection = cms.bool(False),
            performT0_vdriftSegCorrection = cms.bool(False),
            perform_delta_rejecting = cms.bool(False),
            recAlgo = cms.string('DTLinearDriftFromDBAlgo'),
            recAlgoConfig = cms.PSet(
                debug = cms.untracked.bool(False),
                doVdriftCorr = cms.bool(True),
                maxTime = cms.double(420.0),
                minTime = cms.double(-3.0),
                stepTwoFromDigi = cms.bool(False),
                tTrigMode = cms.string('DTTTrigSyncFromDB'),
                tTrigModeConfig = cms.PSet(
                    debug = cms.untracked.bool(False),
                    doT0Correction = cms.bool(True),
                    doTOFCorrection = cms.bool(True),
                    doWirePropCorrection = cms.bool(True),
                    tTrigLabel = cms.string(''),
                    tofCorrType = cms.int32(0),
                    vPropWire = cms.double(24.4),
                    wirePropCorrType = cms.int32(0)
                ),
                useUncertDB = cms.bool(True)
            ),
            segmCleanerMode = cms.int32(2)
        ),
        Reco2DAlgoName = cms.string('DTMeantimerPatternReco'),
        debug = cms.untracked.bool(False),
        hit_afterT0_resolution = cms.double(0.03),
        nUnSharedHitsMin = cms.int32(2),
        performT0SegCorrection = cms.bool(False),
        performT0_vdriftSegCorrection = cms.bool(False),
        perform_delta_rejecting = cms.bool(False),
        recAlgo = cms.string('DTLinearDriftFromDBAlgo'),
        recAlgoConfig = cms.PSet(
            debug = cms.untracked.bool(False),
            doVdriftCorr = cms.bool(True),
            maxTime = cms.double(420.0),
            minTime = cms.double(-3.0),
            stepTwoFromDigi = cms.bool(False),
            tTrigMode = cms.string('DTTTrigSyncFromDB'),
            tTrigModeConfig = cms.PSet(
                debug = cms.untracked.bool(False),
                doT0Correction = cms.bool(True),
                doTOFCorrection = cms.bool(True),
                doWirePropCorrection = cms.bool(True),
                tTrigLabel = cms.string(''),
                tofCorrType = cms.int32(0),
                vPropWire = cms.double(24.4),
                wirePropCorrType = cms.int32(0)
            ),
            useUncertDB = cms.bool(True)
        )
    ),
    Reco4DAlgoName = cms.string('DTMeantimerPatternReco4D'),
    debug = cms.untracked.bool(False),
    recHits1DLabel = cms.InputTag("dt1DRecHits"),
    recHits2DLabel = cms.InputTag("dt2DSegments")
)

ecalDetIdToBeRecovered = cms.EDProducer("EcalDetIdToBeRecoveredProducer",
    ebDetIdToBeRecovered = cms.string('ebDetId'),
    ebFEToBeRecovered = cms.string('ebFE'),
    ebIntegrityChIdErrors = cms.InputTag("ecalDigis","EcalIntegrityChIdErrors"),
    ebIntegrityGainErrors = cms.InputTag("ecalDigis","EcalIntegrityGainErrors"),
    ebIntegrityGainSwitchErrors = cms.InputTag("ecalDigis","EcalIntegrityGainSwitchErrors"),
    ebSrFlagCollection = cms.InputTag("ecalDigis"),
    eeDetIdToBeRecovered = cms.string('eeDetId'),
    eeFEToBeRecovered = cms.string('eeFE'),
    eeIntegrityChIdErrors = cms.InputTag("ecalDigis","EcalIntegrityChIdErrors"),
    eeIntegrityGainErrors = cms.InputTag("ecalDigis","EcalIntegrityGainErrors"),
    eeIntegrityGainSwitchErrors = cms.InputTag("ecalDigis","EcalIntegrityGainSwitchErrors"),
    eeSrFlagCollection = cms.InputTag("ecalDigis"),
    integrityBlockSizeErrors = cms.InputTag("ecalDigis","EcalIntegrityBlockSizeErrors"),
    integrityTTIdErrors = cms.InputTag("ecalDigis","EcalIntegrityTTIdErrors")
)

ecalMultiFitUncalibRecHit = cms.EDProducer("EcalUncalibRecHitProducer",
    EBdigiCollection = cms.InputTag("ecalDigis","ebDigis"),
    EBhitCollection = cms.string('EcalUncalibRecHitsEB'),
    EEdigiCollection = cms.InputTag("ecalDigis","eeDigis"),
    EEhitCollection = cms.string('EcalUncalibRecHitsEE'),
    algo = cms.string('EcalUncalibRecHitWorkerMultiFit'),
    algoPSet = cms.PSet(
        EBamplitudeFitParameters = cms.vdouble(1.138, 1.652),
        EBtimeConstantTerm = cms.double(0.6),
        EBtimeFitLimits_Lower = cms.double(0.2),
        EBtimeFitLimits_Upper = cms.double(1.4),
        EBtimeFitParameters = cms.vdouble(
            -2.015452, 3.130702, -12.3473, 41.88921, -82.83944, 
            91.01147, -50.35761, 11.05621
        ),
        EBtimeNconst = cms.double(28.5),
        EEamplitudeFitParameters = cms.vdouble(1.89, 1.4),
        EEtimeConstantTerm = cms.double(1.0),
        EEtimeFitLimits_Lower = cms.double(0.2),
        EEtimeFitLimits_Upper = cms.double(1.4),
        EEtimeFitParameters = cms.vdouble(
            -2.390548, 3.553628, -17.62341, 67.67538, -133.213, 
            140.7432, -75.41106, 16.20277
        ),
        EEtimeNconst = cms.double(31.8),
        EcalPulseShapeParameters = cms.PSet(
            EBCorrNoiseMatrixG01 = cms.vdouble(
                1.0, 0.73354, 0.64442, 0.58851, 0.55425, 
                0.53082, 0.51916, 0.51097, 0.50732, 0.50409
            ),
            EBCorrNoiseMatrixG06 = cms.vdouble(
                1.0, 0.70946, 0.58021, 0.49846, 0.45006, 
                0.41366, 0.39699, 0.38478, 0.37847, 0.37055
            ),
            EBCorrNoiseMatrixG12 = cms.vdouble(
                1.0, 0.71073, 0.55721, 0.46089, 0.40449, 
                0.35931, 0.33924, 0.32439, 0.31581, 0.30481
            ),
            EBPulseShapeCovariance = cms.vdouble(
                3.001e-06, 1.233e-05, 0.0, -4.416e-06, -4.571e-06, 
                -3.614e-06, -2.636e-06, -1.286e-06, -8.41e-07, -5.296e-07, 
                0.0, 0.0, 1.233e-05, 6.154e-05, 0.0, 
                -2.2e-05, -2.309e-05, -1.838e-05, -1.373e-05, -7.334e-06, 
                -5.088e-06, -3.745e-06, -2.428e-06, 0.0, 0.0, 
                0.0, 0.0, 0.0, 0.0, 0.0, 
                0.0, 0.0, 0.0, 0.0, 0.0, 
                0.0, -4.416e-06, -2.2e-05, 0.0, 8.319e-06, 
                8.545e-06, 6.792e-06, 5.059e-06, 2.678e-06, 1.816e-06, 
                1.223e-06, 8.245e-07, 5.589e-07, -4.571e-06, -2.309e-05, 
                0.0, 8.545e-06, 9.182e-06, 7.219e-06, 5.388e-06, 
                2.853e-06, 1.944e-06, 1.324e-06, 9.083e-07, 6.335e-07, 
                -3.614e-06, -1.838e-05, 0.0, 6.792e-06, 7.219e-06, 
                6.016e-06, 4.437e-06, 2.385e-06, 1.636e-06, 1.118e-06, 
                7.754e-07, 5.556e-07, -2.636e-06, -1.373e-05, 0.0, 
                5.059e-06, 5.388e-06, 4.437e-06, 3.602e-06, 1.917e-06, 
                1.322e-06, 9.079e-07, 6.529e-07, 4.752e-07, -1.286e-06, 
                -7.334e-06, 0.0, 2.678e-06, 2.853e-06, 2.385e-06, 
                1.917e-06, 1.375e-06, 9.1e-07, 6.455e-07, 4.693e-07, 
                3.657e-07, -8.41e-07, -5.088e-06, 0.0, 1.816e-06, 
                1.944e-06, 1.636e-06, 1.322e-06, 9.1e-07, 9.115e-07, 
                6.062e-07, 4.436e-07, 3.422e-07, -5.296e-07, -3.745e-06, 
                0.0, 1.223e-06, 1.324e-06, 1.118e-06, 9.079e-07, 
                6.455e-07, 6.062e-07, 7.217e-07, 4.862e-07, 3.768e-07, 
                0.0, -2.428e-06, 0.0, 8.245e-07, 9.083e-07, 
                7.754e-07, 6.529e-07, 4.693e-07, 4.436e-07, 4.862e-07, 
                6.509e-07, 4.418e-07, 0.0, 0.0, 0.0, 
                5.589e-07, 6.335e-07, 5.556e-07, 4.752e-07, 3.657e-07, 
                3.422e-07, 3.768e-07, 4.418e-07, 6.142e-07
            ),
            EBPulseShapeTemplate = cms.vdouble(
                0.0113979, 0.758151, 1.0, 0.887744, 0.673548, 
                0.474332, 0.319561, 0.215144, 0.147464, 0.101087, 
                0.0693181, 0.0475044
            ),
            EBdigiCollection = cms.string(''),
            EECorrNoiseMatrixG01 = cms.vdouble(
                1.0, 0.72698, 0.62048, 0.55691, 0.51848, 
                0.49147, 0.47813, 0.47007, 0.46621, 0.46265
            ),
            EECorrNoiseMatrixG06 = cms.vdouble(
                1.0, 0.71217, 0.47464, 0.34056, 0.26282, 
                0.20287, 0.17734, 0.16256, 0.15618, 0.14443
            ),
            EECorrNoiseMatrixG12 = cms.vdouble(
                1.0, 0.71373, 0.44825, 0.30152, 0.21609, 
                0.14786, 0.11772, 0.10165, 0.09465, 0.08098
            ),
            EEPulseShapeCovariance = cms.vdouble(
                3.941e-05, 3.333e-05, 0.0, -1.449e-05, -1.661e-05, 
                -1.424e-05, -1.183e-05, -6.842e-06, -4.915e-06, -3.411e-06, 
                0.0, 0.0, 3.333e-05, 2.862e-05, 0.0, 
                -1.244e-05, -1.431e-05, -1.233e-05, -1.032e-05, -5.883e-06, 
                -4.154e-06, -2.902e-06, -2.128e-06, 0.0, 0.0, 
                0.0, 0.0, 0.0, 0.0, 0.0, 
                0.0, 0.0, 0.0, 0.0, 0.0, 
                0.0, -1.449e-05, -1.244e-05, 0.0, 5.84e-06, 
                6.649e-06, 5.72e-06, 4.812e-06, 2.708e-06, 1.869e-06, 
                1.33e-06, 9.186e-07, 6.446e-07, -1.661e-05, -1.431e-05, 
                0.0, 6.649e-06, 7.966e-06, 6.898e-06, 5.794e-06, 
                3.157e-06, 2.184e-06, 1.567e-06, 1.084e-06, 7.575e-07, 
                -1.424e-05, -1.233e-05, 0.0, 5.72e-06, 6.898e-06, 
                6.341e-06, 5.347e-06, 2.859e-06, 1.991e-06, 1.431e-06, 
                9.839e-07, 6.886e-07, -1.183e-05, -1.032e-05, 0.0, 
                4.812e-06, 5.794e-06, 5.347e-06, 4.854e-06, 2.628e-06, 
                1.809e-06, 1.289e-06, 9.02e-07, 6.146e-07, -6.842e-06, 
                -5.883e-06, 0.0, 2.708e-06, 3.157e-06, 2.859e-06, 
                2.628e-06, 1.863e-06, 1.296e-06, 8.882e-07, 6.108e-07, 
                4.283e-07, -4.915e-06, -4.154e-06, 0.0, 1.869e-06, 
                2.184e-06, 1.991e-06, 1.809e-06, 1.296e-06, 1.217e-06, 
                8.669e-07, 5.751e-07, 3.882e-07, -3.411e-06, -2.902e-06, 
                0.0, 1.33e-06, 1.567e-06, 1.431e-06, 1.289e-06, 
                8.882e-07, 8.669e-07, 9.522e-07, 6.717e-07, 4.293e-07, 
                0.0, -2.128e-06, 0.0, 9.186e-07, 1.084e-06, 
                9.839e-07, 9.02e-07, 6.108e-07, 5.751e-07, 6.717e-07, 
                7.911e-07, 5.493e-07, 0.0, 0.0, 0.0, 
                6.446e-07, 7.575e-07, 6.886e-07, 6.146e-07, 4.283e-07, 
                3.882e-07, 4.293e-07, 5.493e-07, 7.027e-07
            ),
            EEPulseShapeTemplate = cms.vdouble(
                0.116442, 0.756246, 1.0, 0.897182, 0.686831, 
                0.491506, 0.344111, 0.245731, 0.174115, 0.123361, 
                0.0874288, 0.061957
            ),
            EEdigiCollection = cms.string(''),
            ESdigiCollection = cms.string(''),
            EcalPreMixStage1 = cms.bool(False),
            EcalPreMixStage2 = cms.bool(False),
            UseLCcorrection = cms.untracked.bool(True)
        ),
        activeBXs = cms.vint32(
            -5, -4, -3, -2, -1, 
            0, 1, 2, 3, 4
        ),
        addPedestalUncertaintyEB = cms.double(0.0),
        addPedestalUncertaintyEE = cms.double(0.0),
        ampErrorCalculation = cms.bool(True),
        amplitudeThresholdEB = cms.double(10),
        amplitudeThresholdEE = cms.double(10),
        chi2ThreshEB_ = cms.double(65.0),
        chi2ThreshEE_ = cms.double(50.0),
        doPrefitEB = cms.bool(False),
        doPrefitEE = cms.bool(False),
        dynamicPedestalsEB = cms.bool(False),
        dynamicPedestalsEE = cms.bool(False),
        ebPulseShape = cms.vdouble(
            5.2e-05, -5.26e-05, 6.66e-05, 0.1168, 0.7575, 
            1.0, 0.8876, 0.6732, 0.4741, 0.3194
        ),
        ebSpikeThreshold = cms.double(1.042),
        eePulseShape = cms.vdouble(
            5.2e-05, -5.26e-05, 6.66e-05, 0.1168, 0.7575, 
            1.0, 0.8876, 0.6732, 0.4741, 0.3194
        ),
        gainSwitchUseMaxSampleEB = cms.bool(True),
        gainSwitchUseMaxSampleEE = cms.bool(False),
        kPoorRecoFlagEB = cms.bool(True),
        kPoorRecoFlagEE = cms.bool(False),
        mitigateBadSamplesEB = cms.bool(False),
        mitigateBadSamplesEE = cms.bool(False),
        outOfTimeThresholdGain12mEB = cms.double(5),
        outOfTimeThresholdGain12mEE = cms.double(1000),
        outOfTimeThresholdGain12pEB = cms.double(5),
        outOfTimeThresholdGain12pEE = cms.double(1000),
        outOfTimeThresholdGain61mEB = cms.double(5),
        outOfTimeThresholdGain61mEE = cms.double(1000),
        outOfTimeThresholdGain61pEB = cms.double(5),
        outOfTimeThresholdGain61pEE = cms.double(1000),
        prefitMaxChiSqEB = cms.double(25.0),
        prefitMaxChiSqEE = cms.double(10.0),
        selectiveBadSampleCriteriaEB = cms.bool(False),
        selectiveBadSampleCriteriaEE = cms.bool(False),
        simplifiedNoiseModelForGainSwitch = cms.bool(True),
        timealgo = cms.string('RatioMethod'),
        useLumiInfoRunHeader = cms.bool(True)
    )
)

ecalRecHit = cms.EDProducer("EcalRecHitProducer",
    ChannelStatusToBeExcluded = cms.vstring(
        'kDAC', 
        'kNoisy', 
        'kNNoisy', 
        'kFixedG6', 
        'kFixedG1', 
        'kFixedG0', 
        'kNonRespondingIsolated', 
        'kDeadVFE', 
        'kDeadFE', 
        'kNoDataNoTP'
    ),
    EBLaserMAX = cms.double(3.0),
    EBLaserMIN = cms.double(0.5),
    EBrechitCollection = cms.string('EcalRecHitsEB'),
    EBuncalibRecHitCollection = cms.InputTag("ecalMultiFitUncalibRecHit","EcalUncalibRecHitsEB"),
    EELaserMAX = cms.double(8.0),
    EELaserMIN = cms.double(0.5),
    EErechitCollection = cms.string('EcalRecHitsEE'),
    EEuncalibRecHitCollection = cms.InputTag("ecalMultiFitUncalibRecHit","EcalUncalibRecHitsEE"),
    algo = cms.string('EcalRecHitWorkerSimple'),
    algoRecover = cms.string('EcalRecHitWorkerRecover'),
    cleaningConfig = cms.PSet(
        cThreshold_barrel = cms.double(4),
        cThreshold_double = cms.double(10),
        cThreshold_endcap = cms.double(15),
        e4e1Threshold_barrel = cms.double(0.08),
        e4e1Threshold_endcap = cms.double(0.3),
        e4e1_a_barrel = cms.double(0.02),
        e4e1_a_endcap = cms.double(0.02),
        e4e1_b_barrel = cms.double(0.02),
        e4e1_b_endcap = cms.double(-0.0125),
        e6e2thresh = cms.double(0.04),
        ignoreOutOfTimeThresh = cms.double(1000000000.0),
        tightenCrack_e1_double = cms.double(2),
        tightenCrack_e1_single = cms.double(1),
        tightenCrack_e4e1_single = cms.double(2.5),
        tightenCrack_e6e2_double = cms.double(3)
    ),
    dbStatusToBeExcludedEB = cms.vint32(14, 78, 142),
    dbStatusToBeExcludedEE = cms.vint32(14, 78, 142),
    ebDetIdToBeRecovered = cms.InputTag("ecalDetIdToBeRecovered","ebDetId"),
    ebFEToBeRecovered = cms.InputTag("ecalDetIdToBeRecovered","ebFE"),
    eeDetIdToBeRecovered = cms.InputTag("ecalDetIdToBeRecovered","eeDetId"),
    eeFEToBeRecovered = cms.InputTag("ecalDetIdToBeRecovered","eeFE"),
    flagsMapDBReco = cms.PSet(
        kDead = cms.vstring('kNoDataNoTP'),
        kGood = cms.vstring(
            'kOk', 
            'kDAC', 
            'kNoLaser', 
            'kNoisy'
        ),
        kNeighboursRecovered = cms.vstring(
            'kFixedG0', 
            'kNonRespondingIsolated', 
            'kDeadVFE'
        ),
        kNoisy = cms.vstring(
            'kNNoisy', 
            'kFixedG6', 
            'kFixedG1'
        ),
        kTowerRecovered = cms.vstring('kDeadFE')
    ),
    killDeadChannels = cms.bool(True),
    laserCorrection = cms.bool(True),
    logWarningEtThreshold_EB_FE = cms.double(50),
    logWarningEtThreshold_EE_FE = cms.double(50),
    recoverEBFE = cms.bool(True),
    recoverEBIsolatedChannels = cms.bool(False),
    recoverEBVFE = cms.bool(False),
    recoverEEFE = cms.bool(True),
    recoverEEIsolatedChannels = cms.bool(False),
    recoverEEVFE = cms.bool(False),
    singleChannelRecoveryMethod = cms.string('NeuralNetworks'),
    singleChannelRecoveryThreshold = cms.double(8),
    skipTimeCalib = cms.bool(False),
    triggerPrimitiveDigiCollection = cms.InputTag("ecalDigis","EcalTriggerPrimitives")
)


gemRecHits = cms.EDProducer("GEMRecHitProducer",
    gemDigiLabel = cms.InputTag("muonGEMDigis"),
    recAlgo = cms.string('GEMRecHitStandardAlgo'),
    recAlgoConfig = cms.PSet(

    )
)

gemSegments = cms.EDProducer("GEMSegmentProducer",
    algo_name = cms.string('GEMSegmentAlgorithm'),
    algo_pset = cms.PSet(
        GEMDebug = cms.untracked.bool(True),
        clusterOnlySameBXRecHits = cms.bool(True),
        dEtaChainBoxMax = cms.double(0.05),
        dPhiChainBoxMax = cms.double(0.02),
        dXclusBoxMax = cms.double(1.0),
        dYclusBoxMax = cms.double(5.0),
        maxRecHitsInCluster = cms.int32(4),
        minHitsPerSegment = cms.uint32(2),
        preClustering = cms.bool(True),
        preClusteringUseChaining = cms.bool(True)
    ),
    gemRecHitLabel = cms.InputTag("gemRecHits")
)

hbhereco = cms.EDProducer("HBHEPhase1Reconstructor",
    algoConfigClass = cms.string(''),
    algorithm = cms.PSet(
        Class = cms.string('SimpleHBHEPhase1Algo'),
        activeBXs = cms.vint32(
            -3, -2, -1, 0, 1, 
            2, 3, 4
        ),
        applyPedConstraint = cms.bool(True),
        applyPulseJitter = cms.bool(False),
        applyTimeConstraint = cms.bool(True),
        applyTimeSlew = cms.bool(True),
        applyTimeSlewM3 = cms.bool(True),
        chiSqSwitch = cms.double(15.0),
        correctForPhaseContainment = cms.bool(True),
        correctionPhaseNS = cms.double(6.0),
        deltaChiSqThresh = cms.double(0.001),
        dynamicPed = cms.bool(False),
        firstSampleShift = cms.int32(0),
        fitTimes = cms.int32(1),
        meanPed = cms.double(0.0),
        meanTime = cms.double(0.0),
        nMaxItersMin = cms.int32(500),
        nMaxItersNNLS = cms.int32(500),
        nnlsThresh = cms.double(1e-11),
        pulseJitter = cms.double(1.0),
        respCorrM3 = cms.double(1.0),
        samplesToAdd = cms.int32(2),
        tdcTimeShift = cms.double(0.0),
        timeMax = cms.double(12.5),
        timeMin = cms.double(-12.5),
        timeSigmaHPD = cms.double(5.0),
        timeSigmaSiPM = cms.double(2.5),
        timeSlewParsType = cms.int32(3),
        ts4Max = cms.vdouble(100.0, 20000.0, 30000),
        ts4Min = cms.double(0.0),
        ts4Thresh = cms.double(0.0),
        ts4chi2 = cms.vdouble(15.0, 15.0),
        useM2 = cms.bool(False),
        useM3 = cms.bool(True),
        useMahi = cms.bool(True)
    ),
    digiLabelQIE11 = cms.InputTag("hcalDigis"),
    digiLabelQIE8 = cms.InputTag("hcalDigis"),
    dropZSmarkedPassed = cms.bool(True),
    flagParametersQIE11 = cms.PSet(

    ),
    flagParametersQIE8 = cms.PSet(
        hitEnergyMinimum = cms.double(1.0),
        hitMultiplicityThreshold = cms.int32(17),
        nominalPedestal = cms.double(3.0),
        pulseShapeParameterSets = cms.VPSet(
            cms.PSet(
                pulseShapeParameters = cms.vdouble(
                    0.0, 100.0, -50.0, 0.0, -15.0, 
                    0.15
                )
            ), 
            cms.PSet(
                pulseShapeParameters = cms.vdouble(
                    100.0, 2000.0, -50.0, 0.0, -5.0, 
                    0.05
                )
            ), 
            cms.PSet(
                pulseShapeParameters = cms.vdouble(
                    2000.0, 1000000.0, -50.0, 0.0, 95.0, 
                    0.0
                )
            ), 
            cms.PSet(
                pulseShapeParameters = cms.vdouble(
                    -1000000.0, 1000000.0, 45.0, 0.1, 1000000.0, 
                    0.0
                )
            )
        )
    ),
    makeRecHits = cms.bool(True),
    processQIE11 = cms.bool(True),
    processQIE8 = cms.bool(True),
    pulseShapeParametersQIE11 = cms.PSet(

    ),
    pulseShapeParametersQIE8 = cms.PSet(
        LeftSlopeCut = cms.vdouble(5, 2.55, 2.55),
        LeftSlopeThreshold = cms.vdouble(250, 500, 100000),
        LinearCut = cms.vdouble(-3, -0.054, -0.054),
        LinearThreshold = cms.vdouble(20, 100, 100000),
        MinimumChargeThreshold = cms.double(20),
        MinimumTS4TS5Threshold = cms.double(100),
        R45MinusOneRange = cms.double(0.2),
        R45PlusOneRange = cms.double(0.2),
        RMS8MaxCut = cms.vdouble(-13.5, -11.5, -11.5),
        RMS8MaxThreshold = cms.vdouble(20, 100, 100000),
        RightSlopeCut = cms.vdouble(5, 4.15, 4.15),
        RightSlopeSmallCut = cms.vdouble(1.08, 1.16, 1.16),
        RightSlopeSmallThreshold = cms.vdouble(150, 200, 100000),
        RightSlopeThreshold = cms.vdouble(250, 400, 100000),
        TS3TS4ChargeThreshold = cms.double(70),
        TS3TS4UpperChargeThreshold = cms.double(20),
        TS4TS5ChargeThreshold = cms.double(70),
        TS4TS5LowerCut = cms.vdouble(
            -1, -0.7, -0.5, -0.4, -0.3, 
            0.1
        ),
        TS4TS5LowerThreshold = cms.vdouble(
            100, 120, 160, 200, 300, 
            500
        ),
        TS4TS5UpperCut = cms.vdouble(1, 0.8, 0.75, 0.72),
        TS4TS5UpperThreshold = cms.vdouble(70, 90, 100, 400),
        TS5TS6ChargeThreshold = cms.double(70),
        TS5TS6UpperChargeThreshold = cms.double(20),
        TriangleIgnoreSlow = cms.bool(False),
        TrianglePeakTS = cms.uint32(10000),
        UseDualFit = cms.bool(True)
    ),
    recoParamsFromDB = cms.bool(True),
    saveDroppedInfos = cms.bool(False),
    saveEffectivePedestal = cms.bool(True),
    saveInfos = cms.bool(False),
    setLegacyFlagsQIE11 = cms.bool(False),
    setLegacyFlagsQIE8 = cms.bool(True),
    setNegativeFlagsQIE11 = cms.bool(False),
    setNegativeFlagsQIE8 = cms.bool(True),
    setNoiseFlagsQIE11 = cms.bool(False),
    setNoiseFlagsQIE8 = cms.bool(True),
    setPulseShapeFlagsQIE11 = cms.bool(False),
    setPulseShapeFlagsQIE8 = cms.bool(True),
    sipmQNTStoSum = cms.int32(3),
    sipmQTSShift = cms.int32(0),
    tsFromDB = cms.bool(False),
    use8ts = cms.bool(True)
)


hfprereco = cms.EDProducer("HFPreReconstructor",
    digiLabel = cms.InputTag("hcalDigis"),
    dropZSmarkedPassed = cms.bool(False),
    forceSOI = cms.int32(-1),
    soiShift = cms.int32(0),
    sumAllTimeSlices = cms.bool(False),
    tsFromDB = cms.bool(False)
)

hfreco = cms.EDProducer("HFPhase1Reconstructor",
    PETstat = cms.PSet(
        HcalAcceptSeverityLevel = cms.int32(9),
        longETParams = cms.vdouble(
            0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 
            0, 0, 0
        ),
        longEnergyParams = cms.vdouble(
            43.5, 45.7, 48.32, 51.36, 54.82, 
            58.7, 63.0, 67.72, 72.86, 78.42, 
            84.4, 90.8, 97.62
        ),
        long_R = cms.vdouble(0.98),
        long_R_29 = cms.vdouble(0.8),
        shortETParams = cms.vdouble(
            0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 
            0, 0, 0
        ),
        shortEnergyParams = cms.vdouble(
            35.1773, 35.37, 35.7933, 36.4472, 37.3317, 
            38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 
            47.4813, 49.98, 52.7093
        ),
        short_R = cms.vdouble(0.8),
        short_R_29 = cms.vdouble(0.8)
    ),
    S8S1stat = cms.PSet(
        HcalAcceptSeverityLevel = cms.int32(9),
        isS8S1 = cms.bool(True),
        longETParams = cms.vdouble(
            0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 
            0, 0, 0
        ),
        longEnergyParams = cms.vdouble(
            40, 100, 100, 100, 100, 
            100, 100, 100, 100, 100, 
            100, 100, 100
        ),
        long_optimumSlope = cms.vdouble(
            0.3, 0.1, 0.1, 0.1, 0.1, 
            0.1, 0.1, 0.1, 0.1, 0.1, 
            0.1, 0.1, 0.1
        ),
        shortETParams = cms.vdouble(
            0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 
            0, 0, 0
        ),
        shortEnergyParams = cms.vdouble(
            40, 100, 100, 100, 100, 
            100, 100, 100, 100, 100, 
            100, 100, 100
        ),
        short_optimumSlope = cms.vdouble(
            0.3, 0.1, 0.1, 0.1, 0.1, 
            0.1, 0.1, 0.1, 0.1, 0.1, 
            0.1, 0.1, 0.1
        )
    ),
    S9S1stat = cms.PSet(
        HcalAcceptSeverityLevel = cms.int32(9),
        isS8S1 = cms.bool(False),
        longETParams = cms.vdouble(
            0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 
            0, 0, 0
        ),
        longEnergyParams = cms.vdouble(
            43.5, 45.7, 48.32, 51.36, 54.82, 
            58.7, 63.0, 67.72, 72.86, 78.42, 
            84.4, 90.8, 97.62
        ),
        long_optimumSlope = cms.vdouble(
            -99999, 0.0164905, 0.0238698, 0.0321383, 0.041296, 
            0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 
            0.135313, 0.136289, 0.0589927
        ),
        shortETParams = cms.vdouble(
            0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 
            0, 0, 0
        ),
        shortEnergyParams = cms.vdouble(
            35.1773, 35.37, 35.7933, 36.4472, 37.3317, 
            38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 
            47.4813, 49.98, 52.7093
        ),
        short_optimumSlope = cms.vdouble(
            -99999, 0.0164905, 0.0238698, 0.0321383, 0.041296, 
            0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 
            0.135313, 0.136289, 0.0589927
        )
    ),
    algoConfigClass = cms.string('HFPhase1PMTParams'),
    algorithm = cms.PSet(
        Class = cms.string('HFFlexibleTimeCheck'),
        alwaysCalculateQAsymmetry = cms.bool(False),
        energyWeights = cms.vdouble(
            1.0, 1.0, 1.0, 0.0, 1.0, 
            0.0, 2.0, 0.0, 2.0, 0.0, 
            2.0, 0.0, 1.0, 0.0, 0.0, 
            1.0, 0.0, 1.0, 0.0, 2.0, 
            0.0, 2.0, 0.0, 2.0, 0.0, 
            1.0
        ),
        minChargeForOvershoot = cms.double(10000000000.0),
        minChargeForUndershoot = cms.double(10000000000.0),
        rejectAllFailures = cms.bool(True),
        soiPhase = cms.uint32(1),
        tfallIfNoTDC = cms.double(-101.0),
        timeShift = cms.double(0.0),
        tlimits = cms.vdouble(-1000.0, 1000.0, -1000.0, 1000.0),
        triseIfNoTDC = cms.double(-100.0)
    ),
    checkChannelQualityForDepth3and4 = cms.bool(True),
    inputLabel = cms.InputTag("hfprereco"),
    setNoiseFlags = cms.bool(True),
    useChannelQualityFromDB = cms.bool(True)
)

horeco = cms.EDProducer("HcalHitReconstructor",
    Subdetector = cms.string('HO'),
    correctForPhaseContainment = cms.bool(True),
    correctForTimeslew = cms.bool(True),
    correctTiming = cms.bool(True),
    correctionPhaseNS = cms.double(13.0),
    dataOOTCorrectionCategory = cms.string('Data'),
    dataOOTCorrectionName = cms.string(''),
    digiLabel = cms.InputTag("hcalDigis"),
    dropZSmarkedPassed = cms.bool(True),
    firstAuxTS = cms.int32(4),
    firstSample = cms.int32(4),
    mcOOTCorrectionCategory = cms.string('MC'),
    mcOOTCorrectionName = cms.string(''),
    recoParamsFromDB = cms.bool(True),
    samplesToAdd = cms.int32(4),
    saturationParameters = cms.PSet(
        maxADCvalue = cms.int32(127)
    ),
    setHSCPFlags = cms.bool(True),
    setNegativeFlags = cms.bool(False),
    setNoiseFlags = cms.bool(True),
    setPulseShapeFlags = cms.bool(False),
    setSaturationFlags = cms.bool(True),
    setTimingTrustFlags = cms.bool(False),
    tsFromDB = cms.bool(True),
    useLeakCorrection = cms.bool(False)
)

me0RecHits = cms.EDProducer("ME0RecHitProducer",
    me0DigiLabel = cms.InputTag("simMuonME0PseudoReDigis"),
    recAlgo = cms.string('ME0RecHitStandardAlgo'),
    recAlgoConfig = cms.PSet(

    )
)

me0Segments = cms.EDProducer("ME0SegmentProducer",
    algo_psets = cms.VPSet(
        cms.PSet(
            algo_name = cms.string('ME0SegmentAlgorithm'),
            algo_pset = cms.PSet(
                ME0Debug = cms.untracked.bool(True),
                dEtaChainBoxMax = cms.double(0.05),
                dPhiChainBoxMax = cms.double(0.02),
                dTimeChainBoxMax = cms.double(15.0),
                dXclusBoxMax = cms.double(1.0),
                dYclusBoxMax = cms.double(5.0),
                maxRecHitsInCluster = cms.int32(6),
                minHitsPerSegment = cms.uint32(3),
                preClustering = cms.bool(True),
                preClusteringUseChaining = cms.bool(True)
            )
        ), 
        cms.PSet(
            algo_name = cms.string('ME0SegAlgoRU'),
            algo_pset = cms.PSet(
                allowWideSegments = cms.bool(True),
                doCollisions = cms.bool(True),
                maxChi2Additional = cms.double(100.0),
                maxChi2GoodSeg = cms.double(50),
                maxChi2Prune = cms.double(50),
                maxETASeeds = cms.double(0.1),
                maxPhiAdditional = cms.double(0.001096605744),
                maxPhiSeeds = cms.double(0.001096605744),
                maxTOFDiff = cms.double(25),
                minNumberOfHits = cms.uint32(4),
                requireCentralBX = cms.bool(True)
            )
        )
    ),
    algo_type = cms.int32(2),
    me0RecHitLabel = cms.InputTag("me0RecHits")
)


offlineBeamSpot = cms.EDProducer("BeamSpotProducer")

particleFlowClusterHGCal = cms.EDProducer("PFClusterProducer",
    energyCorrector = cms.PSet(

    ),
    initialClusteringStep = cms.PSet(
        algoName = cms.string('RealisticSimClusterMapper'),
        calibMaxEta = cms.double(3.0),
        calibMinEta = cms.double(1.4),
        egammaCalib = cms.vdouble(
            1.0, 1.0, 1.01, 1.01, 1.02, 
            1.03, 1.04, 1.04
        ),
        exclusiveFraction = cms.double(0.6),
        hadronCalib = cms.vdouble(
            1.24, 1.24, 1.24, 1.23, 1.24, 
            1.25, 1.29, 1.29
        ),
        invisibleFraction = cms.double(0.6),
        maxDforTimingSquared = cms.double(4.0),
        maxDistance = cms.double(10.0),
        maxDistanceFilter = cms.bool(True),
        minNHitsforTiming = cms.uint32(3),
        simClusterSrc = cms.InputTag("mix","MergedCaloTruth"),
        thresholdsByDetector = cms.VPSet(),
        timeOffset = cms.double(5),
        useMCFractionsForExclEnergy = cms.bool(False)
    ),
    pfClusterBuilder = cms.PSet(

    ),
    positionReCalc = cms.PSet(
        algoName = cms.string('Cluster3DPCACalculator'),
        minFractionInCalc = cms.double(1e-09),
        updateTiming = cms.bool(False)
    ),
    recHitCleaners = cms.VPSet(),
    recHitsSource = cms.InputTag("particleFlowRecHitHGC"),
    seedFinder = cms.PSet(
        algoName = cms.string('PassThruSeedFinder'),
        nNeighbours = cms.int32(8),
        thresholdsByDetector = cms.VPSet()
    )
)

rpcRecHits = cms.EDProducer("RPCRecHitProducer",
    deadSource = cms.string('File'),
    deadvecfile = cms.FileInPath('RecoLocalMuon/RPCRecHit/data/RPCDeadVec.dat'),
    maskSource = cms.string('File'),
    maskvecfile = cms.FileInPath('RecoLocalMuon/RPCRecHit/data/RPCMaskVec.dat'),
    recAlgo = cms.string('RPCRecHitStandardAlgo'),
    recAlgoConfig = cms.PSet(

    ),
    rpcDigiLabel = cms.InputTag("simMuonRPCDigis")
)

MeasurementTrackerEvent = cms.EDProducer("MeasurementTrackerEventProducer",
    Phase2TrackerCluster1DProducer = cms.string('siPhase2Clusters'),
    badPixelFEDChannelCollectionLabels = cms.VInputTag("siPixelDigis"),
    inactivePixelDetectorLabels = cms.VInputTag(),
    inactiveStripDetectorLabels = cms.VInputTag("siStripDigis"),
    measurementTracker = cms.string(''),
    pixelCablingMapLabel = cms.string(''),
    pixelClusterProducer = cms.string('siPixelClusters'),
    skipClusters = cms.InputTag(""),
    stripClusterProducer = cms.string(''),
    switchOffPixelsIfEmpty = cms.bool(True)
)

ak4CaloJetsForTrk = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(True),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(10.0),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    puPtMin = cms.double(10),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("caloTowerForTrk"),
    srcPVs = cms.InputTag("firstStepPrimaryVerticesUnsorted"),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)

caloTowerForTrk = cms.EDProducer("CaloTowersCreator",
    AllowMissingInputs = cms.bool(False),
    EBGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    EBSumThreshold = cms.double(0.2),
    EBThreshold = cms.double(0.07),
    EBWeight = cms.double(1.0),
    EBWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    EEGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    EESumThreshold = cms.double(0.45),
    EEThreshold = cms.double(0.3),
    EEWeight = cms.double(1.0),
    EEWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    EcalRecHitSeveritiesToBeExcluded = cms.vstring(
        'kTime', 
        'kWeird', 
        'kBad'
    ),
    EcalSeveritiesToBeUsedInBadTowers = cms.vstring(),
    EcutTower = cms.double(-1000.0),
    HBGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HBThreshold = cms.double(0.3),
    HBThreshold1 = cms.double(0.1),
    HBThreshold2 = cms.double(0.2),
    HBWeight = cms.double(1.0),
    HBWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HEDGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HEDThreshold = cms.double(0.2),
    HEDThreshold1 = cms.double(0.1),
    HEDWeight = cms.double(1.0),
    HEDWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HESGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HESThreshold = cms.double(0.2),
    HESThreshold1 = cms.double(0.1),
    HESWeight = cms.double(1.0),
    HESWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HF1Grid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HF1Threshold = cms.double(0.5),
    HF1Weight = cms.double(1.0),
    HF1Weights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HF2Grid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HF2Threshold = cms.double(0.85),
    HF2Weight = cms.double(1.0),
    HF2Weights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HOGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HOThreshold0 = cms.double(1.1),
    HOThresholdMinus1 = cms.double(3.5),
    HOThresholdMinus2 = cms.double(3.5),
    HOThresholdPlus1 = cms.double(3.5),
    HOThresholdPlus2 = cms.double(3.5),
    HOWeight = cms.double(1.0),
    HOWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HcalAcceptSeverityLevel = cms.uint32(9),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32(9999),
    HcalPhase = cms.int32(1),
    HcalThreshold = cms.double(-1000.0),
    MomConstrMethod = cms.int32(1),
    MomEBDepth = cms.double(0.3),
    MomEEDepth = cms.double(0.0),
    MomHBDepth = cms.double(0.2),
    MomHEDepth = cms.double(0.4),
    UseEcalRecoveredHits = cms.bool(False),
    UseEtEBTreshold = cms.bool(False),
    UseEtEETreshold = cms.bool(False),
    UseHO = cms.bool(True),
    UseHcalRecoveredHits = cms.bool(True),
    UseRejectedHitsOnly = cms.bool(False),
    UseRejectedRecoveredEcalHits = cms.bool(False),
    UseRejectedRecoveredHcalHits = cms.bool(True),
    UseSymEBTreshold = cms.bool(True),
    UseSymEETreshold = cms.bool(True),
    ecalInputs = cms.VInputTag(cms.InputTag("ecalRecHit","EcalRecHitsEB"), cms.InputTag("ecalRecHit","EcalRecHitsEE")),
    hbheInput = cms.InputTag("hbhereco"),
    hfInput = cms.InputTag("hfreco"),
    hoInput = cms.InputTag("horeco"),
    missingHcalRescaleFactorForEcal = cms.double(0)
)

trackAlgoPriorityOrder = cms.ESProducer("TrackAlgoPriorityOrderESProducer",
    ComponentName = cms.string('trackAlgoPriorityOrder'),
    algoOrder = cms.vstring(
        'initialStep', 
        'highPtTripletStep'### v2
    ),
    appendToDataLabel = cms.string('')
)


trackCleaner = cms.ESProducer("TrackCleanerESProducer",
    ComponentName = cms.string('trackCleaner'),
    appendToDataLabel = cms.string('')
)

#earlyGeneralTracks = cms.EDProducer("TrackListMerger",
generalTracks = cms.EDProducer("TrackListMerger",  ### v1
    Epsilon = cms.double(-0.001),
    FoundHitBonus = cms.double(5.0),
    LostHitPenalty = cms.double(5.0),
    MaxNormalizedChisq = cms.double(1000.0),
    MinFound = cms.int32(3),
    MinPT = cms.double(0.05),
    ShareFrac = cms.double(0.19),
    TrackProducers = cms.VInputTag(
        "initialStepTracks", "highPtTripletStepTracks" ### v2
    ),
    allowFirstHitShare = cms.bool(True),
    copyExtras = cms.untracked.bool(True),
    copyMVA = cms.bool(True),
    hasSelector = cms.vint32(
        1, 1#, 1#, 1, 1,  ### v2
        #1
    ),
    indivShareFrac = cms.vdouble(
        1.0, 0.16#, 0.095, 0.09, 0.09, ### v2
        #0.09
    ),
    makeReKeyedSeeds = cms.untracked.bool(False),
    newQuality = cms.string('confirmed'),
    selectedTrackQuals = cms.VInputTag(
        cms.InputTag("initialStepSelector","initialStep"), cms.InputTag("highPtTripletStepSelector","highPtTripletStep")### v2
    ),
    setsToMerge = cms.VPSet(cms.PSet(
        pQual = cms.bool(True),
        tLists = cms.vint32(
            0, 1#, 2#, 3, 4, ### v2
            #5
        )
    )),
    trackAlgoPriorityOrder = cms.string('trackAlgoPriorityOrder'),
    writeOnlyTrkQuals = cms.bool(False)
)

firstStepPrimaryVertices = cms.EDProducer("RecoChargedRefCandidatePrimaryVertexSorter",
    assignment = cms.PSet(
        maxDistanceToJetAxis = cms.double(0.07),
        maxDtSigForPrimaryAssignment = cms.double(4.0),
        maxDxyForJetAxisAssigment = cms.double(0.1),
        maxDxyForNotReconstructedPrimary = cms.double(0.01),
        maxDxySigForNotReconstructedPrimary = cms.double(2),
        maxDzErrorForPrimaryAssignment = cms.double(0.05),
        maxDzForJetAxisAssigment = cms.double(0.1),
        maxDzForPrimaryAssignment = cms.double(0.1),
        maxDzSigForPrimaryAssignment = cms.double(5.0),
        maxJetDeltaR = cms.double(0.5),
        minJetPt = cms.double(25),
        preferHighRanked = cms.bool(False),
        useTiming = cms.bool(False)
    ),
    jets = cms.InputTag("ak4CaloJetsForTrk"),
    particles = cms.InputTag("initialStepTrackRefsForJets"),
    produceAssociationToOriginalVertices = cms.bool(False),
    produceNoPileUpCollection = cms.bool(False),
    producePileUpCollection = cms.bool(False),
    produceSortedVertices = cms.bool(True),
    qualityForPrimary = cms.int32(3),
    sorting = cms.PSet(

    ),
    trackTimeResoTag = cms.InputTag(""),
    trackTimeTag = cms.InputTag(""),
    usePVMET = cms.bool(True),
    vertices = cms.InputTag("firstStepPrimaryVerticesUnsorted")
)

firstStepPrimaryVerticesUnsorted = cms.EDProducer("PrimaryVertexProducer",
    TkClusParameters = cms.PSet(
        TkDAClusParameters = cms.PSet(
            Tmin = cms.double(2.0),
            Tpurge = cms.double(2.0),
            Tstop = cms.double(0.5),
            coolingFactor = cms.double(0.6),
            d0CutOff = cms.double(3.0),
            dzCutOff = cms.double(3.0),
            uniquetrkweight = cms.double(0.8),
            vertexSize = cms.double(0.006),
            zmerge = cms.double(0.01)
        ),
        algorithm = cms.string('DA_vect')
    ),
    TkFilterParameters = cms.PSet(
        algorithm = cms.string('filter'),
        maxD0Significance = cms.double(4.0),
        maxEta = cms.double(4.0),
        maxNormalizedChi2 = cms.double(10.0),
        minPixelLayersWithHits = cms.int32(2),
        minPt = cms.double(0.0),
        minSiliconLayersWithHits = cms.int32(5),
        trackQuality = cms.string('any')
    ),
    TrackLabel = cms.InputTag("initialStepTracks"),
    beamSpotLabel = cms.InputTag("offlineBeamSpot"),
    verbose = cms.untracked.bool(False),
    vertexCollections = cms.VPSet(cms.PSet(
        algorithm = cms.string('AdaptiveVertexFitter'),
        chi2cutoff = cms.double(2.5),
        label = cms.string(''),
        maxDistanceToBeam = cms.double(1.0),
        minNdof = cms.double(0.0),
        useBeamConstraint = cms.bool(False)
    ))
)

generalV0Candidates = cms.EDProducer("V0Producer",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    cosThetaXYCut = cms.double(0.998),
    cosThetaXYZCut = cms.double(-2.0),
    doKShorts = cms.bool(True),
    doLambdas = cms.bool(True),
    innerHitPosCut = cms.double(4.0),
    kShortMassCut = cms.double(0.07),
    lambdaMassCut = cms.double(0.05),
    mPiPiCut = cms.double(0.6),
    tkChi2Cut = cms.double(10.0),
    tkDCACut = cms.double(1.0),
    tkIPSigXYCut = cms.double(2.0),
    tkIPSigZCut = cms.double(-1.0),
    tkNHitsCut = cms.int32(3),
    tkPtCut = cms.double(0.35),
    trackRecoAlgorithm = cms.InputTag("generalTracks"),
    useRefTracks = cms.bool(True),
    useVertex = cms.bool(False),
    vertexFitter = cms.bool(True),
    vertices = cms.InputTag("offlinePrimaryVertices"),
    vtxChi2Cut = cms.double(6.63),
    vtxDecaySigXYCut = cms.double(15.0),
    vtxDecaySigXYZCut = cms.double(-1.0)
)


highPtTripletStepClusters = cms.EDProducer("TrackClusterRemoverPhase2",
    TrackQuality = cms.string('highPurity'),
    maxChi2 = cms.double(9.0),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    oldClusterRemovalInfo = cms.InputTag(""),
    overrideTrkQuals = cms.InputTag("initialStepSelector","initialStep"),
    phase2OTClusters = cms.InputTag("siPhase2Clusters"),
    phase2pixelClusters = cms.InputTag("siPixelClusters"),
    trackClassifier = cms.InputTag("","QualityMasks"),
    trajectories = cms.InputTag("initialStepTracks")
)


highPtTripletStepHitDoublets = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    layerPairs = cms.vuint32(0, 1),
    maxElement = cms.uint32(50000000),
    maxElementTotal = cms.uint32(50000000),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(False),
    seedingLayers = cms.InputTag("highPtTripletStepSeedLayers"),
    trackingRegions = cms.InputTag("highPtTripletStepTrackingRegions"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


highPtTripletStepHitTriplets = cms.EDProducer("CAHitTripletEDProducer",
    CAHardPtCut = cms.double(0.5),
    CAPhiCut = cms.double(0.06),
    CAThetaCut = cms.double(0.003),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
    ),
    doublets = cms.InputTag("highPtTripletStepHitDoublets"),
    extraHitRPhitolerance = cms.double(0.032),
    maxChi2 = cms.PSet(
        enabled = cms.bool(True),
        pt1 = cms.double(0.8),
        pt2 = cms.double(8),
        value1 = cms.double(100),
        value2 = cms.double(6)
    ),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_highPtTripletStepHitDoublets__RECO'),
    useBendingCorrection = cms.bool(True)
)

highPtTripletStepSeedClusterMask = cms.EDProducer("SeedClusterRemoverPhase2",
    oldClusterRemovalInfo = cms.InputTag("initialStepSeedClusterMask"),
    phase2OTClusters = cms.InputTag("siPhase2Clusters"),
    pixelClusters = cms.InputTag("siPixelClusters"),
    trajectories = cms.InputTag("highPtTripletStepSeeds")
)


highPtTripletStepSeedLayers = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("highPtTripletStepClusters")
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("highPtTripletStepClusters")
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(

    ),
    TIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    layerList = cms.vstring(
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
        'FPix6_neg+FPix7_neg+FPix8_neg'
    )
)


highPtTripletStepSeeds = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsEDProducer",
    MinOneOverPtError = cms.double(1),
    OriginTransverseErrorMultiplier = cms.double(1),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    SeedMomentumForBOFF = cms.double(5),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string(''),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_highPtTripletStepHitTriplets__RECO'),
    propagator = cms.string('PropagatorWithMaterial'),
    seedingHitSets = cms.InputTag("highPtTripletStepHitTriplets")
)


highPtTripletStepSelector = cms.EDProducer("MultiTrackSelector",
    beamspot = cms.InputTag("offlineBeamSpot"),
    src = cms.InputTag("highPtTripletStepTracks"),
    trackSelectors = cms.VPSet(
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(2.0),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(0.7, 4.0),
            d0_par2 = cms.vdouble(0.6, 4.0),
            dz_par1 = cms.vdouble(0.8, 4.0),
            dz_par2 = cms.vdouble(0.6, 4.0),
            keepAllTracks = cms.bool(False),
            maxNumberLostLayers = cms.uint32(3),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(3),
            minNumberLayers = cms.uint32(3),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('highPtTripletStepLoose'),
            preFilterName = cms.string(''),
            qualityBit = cms.string('loose'),
            res_par = cms.vdouble(0.003, 0.002),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(1.0),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(0.6, 4.0),
            d0_par2 = cms.vdouble(0.5, 4.0),
            dz_par1 = cms.vdouble(0.7, 4.0),
            dz_par2 = cms.vdouble(0.6, 4.0),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(2),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(3),
            minNumberLayers = cms.uint32(3),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('highPtTripletStepTight'),
            preFilterName = cms.string('highPtTripletStepLoose'),
            qualityBit = cms.string('tight'),
            res_par = cms.vdouble(0.003, 0.002),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(0.8),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(0.6, 4.0),
            d0_par2 = cms.vdouble(0.45, 4.0),
            dz_par1 = cms.vdouble(0.7, 4.0),
            dz_par2 = cms.vdouble(0.55, 4.0),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(2),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(4),
            minNumberLayers = cms.uint32(4),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(4),
            nSigmaZ = cms.double(4.0),
            name = cms.string('highPtTripletStep'),
            preFilterName = cms.string('highPtTripletStepTight'),
            qualityBit = cms.string('highPurity'),
            res_par = cms.vdouble(0.003, 0.001),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        )
    ),
    useVertices = cms.bool(True),
    useVtxError = cms.bool(False),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)

highPtTripletStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet(
        cms.PSet(
            refToPSet_ = cms.string('highPtTripletStepTrajectoryFilterBase')
        ), 
        cms.PSet(
            refToPSet_ = cms.string('ClusterShapeTrajectoryFilter')
        )
    )
    )

highPtTripletStepTrajectoryFilterBase = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.2),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)



highPtTripletStepTrajectoryFilterInOut = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.4),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(1),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

highPtTripletStepChi2Est = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('highPtTripletStepChi2Est'),
    MaxChi2 = cms.double(20.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    ),
    nSigma = cms.double(3),
    pTChargeCutThreshold = cms.double(15.0)
)


highPtTripletStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('highPtTripletStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.16)
)



highPtTripletStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('highPtTripletStepChi2Est'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('highPtTripletStepTrajectoryFilterInOut')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False), #cmssw_11_0
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('highPtTripletStepTrajectoryFilter')
    ),
    updator = cms.string('KFUpdator'),
    useSameTrajFilter = cms.bool(False)
)


highPtTripletStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('highPtTripletStepTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('highPtTripletStepTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    numHitsForSeedCleaner = cms.int32(50),
    onlyPixelHitsForSeedCleaner = cms.bool(True),
    phase2clustersToSkip = cms.InputTag("highPtTripletStepClusters"),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("highPtTripletStepSeeds"),
    useHitsSplitting = cms.bool(True)
)


highPtTripletStepTrackingRegions = cms.EDProducer("GlobalTrackingRegionFromBeamSpotEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        nSigmaZ = cms.double(4),
        originHalfLength = cms.double(0),
        originRadius = cms.double(0.02),
        precise = cms.bool(True),
        ptMin = cms.double(0.7),
        useMultipleScattering = cms.bool(False)
    )
)


highPtTripletStepTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('highPtTripletStep'),
    Fitter = cms.string('FlexibleKFFittingSmoother'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("highPtTripletStepTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


inclusiveSecondaryVertices = cms.EDProducer("VertexMerger",
    maxFraction = cms.double(0.2),
    minSignificance = cms.double(10.0),
    secondaryVertices = cms.InputTag("trackVertexArbitrator")
)


inclusiveVertexFinder = cms.EDProducer("InclusiveVertexFinder",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterizer = cms.PSet(
        clusterMaxDistance = cms.double(0.05),
        clusterMaxSignificance = cms.double(4.5),
        clusterMinAngleCosine = cms.double(0.5),
        distanceRatio = cms.double(20),
        maxTimeSignificance = cms.double(3.5),
        seedMax3DIPSignificance = cms.double(9999),
        seedMax3DIPValue = cms.double(9999),
        seedMin3DIPSignificance = cms.double(1.2),
        seedMin3DIPValue = cms.double(0.005)
    ),
    fitterRatio = cms.double(0.25),
    fitterSigmacut = cms.double(3),
    fitterTini = cms.double(256),
    maxNTracks = cms.uint32(30),
    maximumLongitudinalImpactParameter = cms.double(0.3),
    maximumTimeSignificance = cms.double(3),
    minHits = cms.uint32(8),
    minPt = cms.double(0.8),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("generalTracks"),
    useDirectVertexFitter = cms.bool(True),
    useVertexReco = cms.bool(True),
    vertexMinAngleCosine = cms.double(0.95),
    vertexMinDLen2DSig = cms.double(2.5),
    vertexMinDLenSig = cms.double(0.5),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        primcut = cms.double(1),
        seccut = cms.double(3),
        smoothing = cms.bool(True)
    )
)



initialStepHitDoublets = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    layerPairs = cms.vuint32(0, 1, 2),
    maxElement = cms.uint32(50000000),
    maxElementTotal = cms.uint32(50000000),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(False),
    seedingLayers = cms.InputTag("initialStepSeedLayers"),
    trackingRegions = cms.InputTag("initialStepTrackingRegions"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


initialStepHitQuadruplets = cms.EDProducer("CAHitQuadrupletEDProducer",
    CAHardPtCut = cms.double(0),
    CAPhiCut = cms.double(0.175),
    CAThetaCut = cms.double(0.001),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
    ),
    doublets = cms.InputTag("initialStepHitDoublets"),
    extraHitRPhitolerance = cms.double(0.032),
    fitFastCircle = cms.bool(True),
    fitFastCircleChi2Cut = cms.bool(True),
    maxChi2 = cms.PSet(
        enabled = cms.bool(True),
        pt1 = cms.double(0.7),
        pt2 = cms.double(2),
        value1 = cms.double(200),
        value2 = cms.double(50)
    ),
    mightGet = cms.untracked.vstring('IntermediateHitDoublets_initialStepHitDoublets__RECO'),
    useBendingCorrection = cms.bool(True)
)

initialStepSeedClusterMask = cms.EDProducer("SeedClusterRemoverPhase2",
    oldClusterRemovalInfo = cms.InputTag("highPtTripletStepClusters"),
    phase2OTClusters = cms.InputTag("siPhase2Clusters"),
    pixelClusters = cms.InputTag("siPixelClusters"),
    trajectories = cms.InputTag("initialStepSeeds")
) 


initialStepSeedLayers = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle')
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle')
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(

    ),
    TIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    layerList = cms.vstring(
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
        'FPix5_neg+FPix6_neg+FPix7_neg+FPix8_neg'
    )
)

initialStepSeeds = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsTripletOnlyEDProducer",
    MinOneOverPtError = cms.double(1),
    OriginTransverseErrorMultiplier = cms.double(1),
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(False),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False)
    ),
    SeedMomentumForBOFF = cms.double(5),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string(''),
    mightGet = cms.untracked.vstring('RegionsSeedingHitSets_initialStepHitQuadruplets__RECO'),
    propagator = cms.string('PropagatorWithMaterial'),
    seedingHitSets = cms.InputTag("initialStepHitQuadruplets")
)

initialStepSelector = cms.EDProducer("MultiTrackSelector",
    beamspot = cms.InputTag("offlineBeamSpot"),
    src = cms.InputTag("initialStepTracks"),
    trackSelectors = cms.VPSet(
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(2.0),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(0.8, 4.0),
            d0_par2 = cms.vdouble(0.6, 4.0),
            dz_par1 = cms.vdouble(0.9, 4.0),
            dz_par2 = cms.vdouble(0.8, 4.0),
            keepAllTracks = cms.bool(False),
            maxNumberLostLayers = cms.uint32(3),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(3),
            minNumberLayers = cms.uint32(3),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('initialStepLoose'),
            preFilterName = cms.string(''),
            qualityBit = cms.string('loose'),
            res_par = cms.vdouble(0.003, 0.002),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(1.4),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(0.7, 4.0),
            d0_par2 = cms.vdouble(0.5, 4.0),
            dz_par1 = cms.vdouble(0.8, 4.0),
            dz_par2 = cms.vdouble(0.7, 4.0),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(2),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(3),
            minNumberLayers = cms.uint32(3),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('initialStepTight'),
            preFilterName = cms.string('initialStepLoose'),
            qualityBit = cms.string('tight'),
            res_par = cms.vdouble(0.003, 0.002),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(1.2),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(0.6, 4.0),
            d0_par2 = cms.vdouble(0.45, 4.0),
            dz_par1 = cms.vdouble(0.7, 4.0),
            dz_par2 = cms.vdouble(0.55, 4.0),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(2),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(3),
            minNumberLayers = cms.uint32(3),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('initialStep'),
            preFilterName = cms.string('initialStepTight'),
            qualityBit = cms.string('highPurity'),
            res_par = cms.vdouble(0.003, 0.001),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        )
    ),
    useVertices = cms.bool(True),
    useVtxError = cms.bool(False),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


initialStepChi2Est = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('initialStepChi2Est'),
    MaxChi2 = cms.double(30.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
)


initialStepChi2EstPreSplitting = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('initialStepChi2EstPreSplitting'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1)
)


initialStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('initialStepChi2Est'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('CkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(True),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(1),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    seedAs5DHit = cms.bool(False), #cmssw_11_0
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('initialStepTrajectoryFilter')
    ),
    updator = cms.string('KFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

initialStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.2),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)


initialStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('initialStepTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    numHitsForSeedCleaner = cms.int32(50),
    onlyPixelHitsForSeedCleaner = cms.bool(True),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("initialStepSeeds"),
    useHitsSplitting = cms.bool(True)
)



initialStepTrackRefsForJets = cms.EDProducer("ChargedRefCandidateProducer",
    particleType = cms.string('pi+'),
    src = cms.InputTag("initialStepTracks")
)



initialStepTrackingRegions = cms.EDProducer("GlobalTrackingRegionFromBeamSpotEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        nSigmaZ = cms.double(4),
        originHalfLength = cms.double(0),
        originRadius = cms.double(0.03),
        precise = cms.bool(True),
        ptMin = cms.double(0.6),
        useMultipleScattering = cms.bool(False)
    )
)

initialStepTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('initialStep'),
    Fitter = cms.string('FlexibleKFFittingSmoother'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("initialStepTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)

lowPtTripletStepStandardTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.075),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)



ClusterShapeTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('ClusterShapeTrajectoryFilter'),
    cacheSrc = cms.InputTag("siPixelClusterShapeCache")
)

offlinePrimaryVertices = cms.EDProducer("RecoChargedRefCandidatePrimaryVertexSorter",
    assignment = cms.PSet(
        maxDistanceToJetAxis = cms.double(0.07),
        maxDtSigForPrimaryAssignment = cms.double(4.0),
        maxDxyForJetAxisAssigment = cms.double(0.1),
        maxDxyForNotReconstructedPrimary = cms.double(0.01),
        maxDxySigForNotReconstructedPrimary = cms.double(2),
        maxDzErrorForPrimaryAssignment = cms.double(0.05),
        maxDzForJetAxisAssigment = cms.double(0.1),
        maxDzForPrimaryAssignment = cms.double(0.1),
        maxDzSigForPrimaryAssignment = cms.double(5.0),
        maxJetDeltaR = cms.double(0.5),
        minJetPt = cms.double(25),
        preferHighRanked = cms.bool(False),
        useTiming = cms.bool(False)
    ),
    jets = cms.InputTag("ak4CaloJetsForTrk"),
    particles = cms.InputTag("trackRefsForJetsBeforeSorting"),
    produceAssociationToOriginalVertices = cms.bool(False),
    produceNoPileUpCollection = cms.bool(False),
    producePileUpCollection = cms.bool(False),
    produceSortedVertices = cms.bool(True),
    qualityForPrimary = cms.int32(3),
    sorting = cms.PSet(

    ),
    trackTimeResoTag = cms.InputTag(""),
    trackTimeTag = cms.InputTag(""),
    usePVMET = cms.bool(True),
    vertices = cms.InputTag("unsortedOfflinePrimaryVertices")
)

offlinePrimaryVerticesWithBS = cms.EDProducer("RecoChargedRefCandidatePrimaryVertexSorter",
    assignment = cms.PSet(
        maxDistanceToJetAxis = cms.double(0.07),
        maxDtSigForPrimaryAssignment = cms.double(4.0),
        maxDxyForJetAxisAssigment = cms.double(0.1),
        maxDxyForNotReconstructedPrimary = cms.double(0.01),
        maxDxySigForNotReconstructedPrimary = cms.double(2),
        maxDzErrorForPrimaryAssignment = cms.double(0.05),
        maxDzForJetAxisAssigment = cms.double(0.1),
        maxDzForPrimaryAssignment = cms.double(0.1),
        maxDzSigForPrimaryAssignment = cms.double(5.0),
        maxJetDeltaR = cms.double(0.5),
        minJetPt = cms.double(25),
        preferHighRanked = cms.bool(False),
        useTiming = cms.bool(False)
    ),
    jets = cms.InputTag("ak4CaloJetsForTrk"),
    particles = cms.InputTag("trackRefsForJetsBeforeSorting"),
    produceAssociationToOriginalVertices = cms.bool(False),
    produceNoPileUpCollection = cms.bool(False),
    producePileUpCollection = cms.bool(False),
    produceSortedVertices = cms.bool(True),
    qualityForPrimary = cms.int32(3),
    sorting = cms.PSet(

    ),
    trackTimeResoTag = cms.InputTag(""),
    trackTimeTag = cms.InputTag(""),
    usePVMET = cms.bool(True),
    vertices = cms.InputTag("unsortedOfflinePrimaryVertices","WithBS")
)

siPhase2Clusters = cms.EDProducer("Phase2TrackerClusterizer",
    maxClusterSize = cms.uint32(0),
    maxNumberClusters = cms.uint32(0),
    src = cms.InputTag("mix","Tracker")
)

siPixelClusterShapeCache = cms.EDProducer("SiPixelClusterShapeCacheProducer",
    onDemand = cms.bool(False),
    src = cms.InputTag("siPixelClusters")
)


siPixelClusters = cms.EDProducer("SiPixelClusterProducer",
    ChannelThreshold = cms.int32(1000),
    ClusterThreshold = cms.int32(4000),
    ClusterThreshold_L1 = cms.int32(4000),
    ElectronPerADCGain = cms.double(600.0),
    MissCalibrate = cms.bool(False), #cmssw_10_6 untracked --> tracked
    Phase2Calibration = cms.bool(True),
    Phase2DigiBaseline = cms.double(1200.0),
    Phase2KinkADC = cms.int32(8),
    Phase2ReadoutMode = cms.int32(-1),
    SeedThreshold = cms.int32(1000),
    SplitClusters = cms.bool(False),
    VCaltoElectronGain = cms.int32(65),
    VCaltoElectronGain_L1 = cms.int32(65),
    VCaltoElectronOffset = cms.int32(-414),
    VCaltoElectronOffset_L1 = cms.int32(-414),
    maxNumberOfClusters = cms.int32(-1),
    payloadType = cms.string('Offline'),
    src = cms.InputTag("simSiPixelDigis","Pixel")
)



siPixelClustersPreSplitting = cms.EDProducer("SiPixelClusterProducer",
    ChannelThreshold = cms.int32(1000),
    ClusterThreshold = cms.int32(4000),
    ClusterThreshold_L1 = cms.int32(4000),
    ElectronPerADCGain = cms.double(600.0),
    MissCalibrate = cms.bool(False), #cmssw_10_6 untracked --> tracked
    Phase2Calibration = cms.bool(True),
    Phase2DigiBaseline = cms.double(1200.0),
    Phase2KinkADC = cms.int32(8),
    Phase2ReadoutMode = cms.int32(-1),
    SeedThreshold = cms.int32(1000),
    SplitClusters = cms.bool(False),
    VCaltoElectronGain = cms.int32(65),
    VCaltoElectronGain_L1 = cms.int32(65),
    VCaltoElectronOffset = cms.int32(-414),
    VCaltoElectronOffset_L1 = cms.int32(-414),
    maxNumberOfClusters = cms.int32(-1),
    payloadType = cms.string('Offline'),
    src = cms.InputTag("simSiPixelDigis","Pixel")
)


siPixelRecHits = cms.EDProducer("SiPixelRecHitConverter",
    CPE = cms.string('PixelCPEGeneric'),
    VerboseLevel = cms.untracked.int32(0),
    src = cms.InputTag("siPixelClusters")
)

siPixelRecHitsPreSplitting = cms.EDProducer("SiPixelRecHitConverter",
    CPE = cms.string('PixelCPEGeneric'),
    VerboseLevel = cms.untracked.int32(0),
    src = cms.InputTag("siPixelClustersPreSplitting")
)

trackRefsForJetsBeforeSorting = cms.EDProducer("ChargedRefCandidateProducer",
    particleType = cms.string('pi+'),
    src = cms.InputTag("trackWithVertexRefSelectorBeforeSorting")
)

trackVertexArbitrator = cms.EDProducer("TrackVertexArbitrator",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    dLenFraction = cms.double(0.333),
    dRCut = cms.double(0.4),
    distCut = cms.double(0.04),
    fitterRatio = cms.double(0.25),
    fitterSigmacut = cms.double(3),
    fitterTini = cms.double(256),
    maxTimeSignificance = cms.double(3.5),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    secondaryVertices = cms.InputTag("vertexMerger"),
    sigCut = cms.double(5),
    trackMinLayers = cms.int32(4),
    trackMinPixels = cms.int32(1),
    trackMinPt = cms.double(0.4),
    tracks = cms.InputTag("generalTracks")
)

trackWithVertexRefSelectorBeforeSorting = cms.EDProducer("TrackWithVertexRefSelector",
    copyExtras = cms.untracked.bool(False),
    copyTrajectories = cms.untracked.bool(False),
    d0Max = cms.double(999.0),
    dzMax = cms.double(999.0),
    etaMax = cms.double(5.0),
    etaMin = cms.double(0.0),
    nSigmaDtVertex = cms.double(0),
    nVertices = cms.uint32(0),
    normalizedChi2 = cms.double(999999.0),
    numberOfLostHits = cms.uint32(999),
    numberOfValidHits = cms.uint32(0),
    numberOfValidPixelHits = cms.uint32(0),
    ptErrorCut = cms.double(9e+99),
    ptMax = cms.double(9e+99),
    ptMin = cms.double(0.3),
    quality = cms.string('highPurity'),
    rhoVtx = cms.double(0.2),
    src = cms.InputTag("generalTracks"),
    timeResosTag = cms.InputTag(""),
    timesTag = cms.InputTag(""),
    useVtx = cms.bool(True),
    vertexTag = cms.InputTag("unsortedOfflinePrimaryVertices"),
    vtxFallback = cms.bool(True),
    zetaVtx = cms.double(1.0)
)

trackerClusterCheck = cms.EDProducer("ClusterCheckerEDProducer",
    ClusterCollectionLabel = cms.InputTag("siStripClusters"),
    MaxNumberOfCosmicClusters = cms.uint32(400000),
    MaxNumberOfPixelClusters = cms.uint32(40000),
    PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
    cut = cms.string('strip < 400000 && pixel < 40000 && (strip < 50000 + 10*pixel) && (pixel < 5000 + 0.1*strip)'),
    doClusterCheck = cms.bool(False),
    silentClusterCheck = cms.untracked.bool(False)
)


unsortedOfflinePrimaryVertices = cms.EDProducer("PrimaryVertexProducer",
    TkClusParameters = cms.PSet(
        TkDAClusParameters = cms.PSet(
            Tmin = cms.double(2.0),
            Tpurge = cms.double(2.0),
            Tstop = cms.double(0.5),
            coolingFactor = cms.double(0.6),
            d0CutOff = cms.double(3.0),
            dzCutOff = cms.double(3.0),
            uniquetrkweight = cms.double(0.8),
            vertexSize = cms.double(0.006),
            zmerge = cms.double(0.01)
        ),
        algorithm = cms.string('DA_vect')
    ),
    TkFilterParameters = cms.PSet(
        algorithm = cms.string('filter'),
        maxD0Significance = cms.double(4.0),
        maxEta = cms.double(4.0),
        maxNormalizedChi2 = cms.double(10.0),
        minPixelLayersWithHits = cms.int32(2),
        minPt = cms.double(0.0),
        minSiliconLayersWithHits = cms.int32(5),
        trackQuality = cms.string('any')
    ),
    TrackLabel = cms.InputTag("generalTracks"),
    beamSpotLabel = cms.InputTag("offlineBeamSpot"),
    verbose = cms.untracked.bool(False),
    vertexCollections = cms.VPSet(
        cms.PSet(
            algorithm = cms.string('AdaptiveVertexFitter'),
            chi2cutoff = cms.double(2.5),
            label = cms.string(''),
            maxDistanceToBeam = cms.double(1.0),
            minNdof = cms.double(0.0),
            useBeamConstraint = cms.bool(False)
        ), 
        cms.PSet(
            algorithm = cms.string('AdaptiveVertexFitter'),
            chi2cutoff = cms.double(2.5),
            label = cms.string('WithBS'),
            maxDistanceToBeam = cms.double(1.0),
            minNdof = cms.double(2.0),
            useBeamConstraint = cms.bool(True)
        )
    )
)


vertexMerger = cms.EDProducer("VertexMerger",
    maxFraction = cms.double(0.7),
    minSignificance = cms.double(2),
    secondaryVertices = cms.InputTag("inclusiveVertexFinder")
)

############# ordered setup

ecalUncalibRecHitSequence = cms.Sequence(
    bunchSpacingProducer +
    ecalMultiFitUncalibRecHit +
    ecalDetIdToBeRecovered
)

caloLocalReco = cms.Sequence(
    hbhereco +
    hfprereco + #####
    hfreco +
    horeco +
    ecalUncalibRecHitSequence +
    ecalRecHit
)

itLocalReco = cms.Sequence(
    siPhase2Clusters + 
    siPixelClusters + 
    siPixelClusterShapeCache + 
    siPixelClustersPreSplitting + 
    siPixelRecHits + 
    siPixelRecHitsPreSplitting
)
otLocalReco = cms.Sequence(
    MeasurementTrackerEvent #+
    #clusterSummaryProducer     # not sure what it is :(
)

initialStepPVSequence = cms.Sequence(
    firstStepPrimaryVerticesUnsorted + #uses beamspot
    initialStepTrackRefsForJets +
    caloTowerForTrk +
    ak4CaloJetsForTrk +
    firstStepPrimaryVertices
)
initialStepSequence = cms.Sequence(
    initialStepSeedLayers + 
    initialStepTrackingRegions + 
    initialStepHitDoublets + 
    initialStepHitQuadruplets + 
    initialStepSeeds + 
    initialStepTrackCandidates + 
    initialStepTracks +
    initialStepPVSequence + #uses beamspot
    initialStepSelector
)

highPtTripletStepSequence = cms.Sequence(
    highPtTripletStepClusters +
    highPtTripletStepSeedLayers +
    highPtTripletStepTrackingRegions +
    highPtTripletStepHitDoublets +
    highPtTripletStepHitTriplets +
    highPtTripletStepSeedLayers +
    highPtTripletStepSeeds +
    highPtTripletStepTrackCandidates +
    highPtTripletStepTracks +
    highPtTripletStepSelector +
    initialStepSeedClusterMask + # needed by electron, but also by highPtTripletStepSeedClusterMask
    highPtTripletStepSeedClusterMask
)

vertexReco = cms.Sequence(
    caloTowerForTrk +
    ak4CaloJetsForTrk +
    firstStepPrimaryVertices
)
initialStepSequence = cms.Sequence(
    initialStepSeedLayers + 
    initialStepTrackingRegions + 
    initialStepHitDoublets + 
    initialStepHitQuadruplets + 
    initialStepSeeds + 
    initialStepTrackCandidates + 
    initialStepTracks +
    initialStepPVSequence + #uses beamspot
    initialStepSelector
)

highPtTripletStepSequence = cms.Sequence(
    highPtTripletStepClusters +
    highPtTripletStepSeedLayers +
    highPtTripletStepTrackingRegions +
    highPtTripletStepHitDoublets +
    highPtTripletStepHitTriplets +
    highPtTripletStepSeedLayers +
    highPtTripletStepSeeds +
    highPtTripletStepTrackCandidates +
    highPtTripletStepTracks +
    highPtTripletStepSelector +
    initialStepSeedClusterMask + # needed by electron, but also by highPtTripletStepSeedClusterMask
    highPtTripletStepSeedClusterMask
)

vertexReco = cms.Sequence(
    ak4CaloJetsForTrk +
    unsortedOfflinePrimaryVertices +
    trackWithVertexRefSelectorBeforeSorting +
    trackRefsForJetsBeforeSorting +
    offlinePrimaryVertices + 
    offlinePrimaryVerticesWithBS +
    inclusiveVertexFinder +
    vertexMerger +
    trackVertexArbitrator +
    inclusiveSecondaryVertices
)

MC_Tracking_v2 = cms.Path(
    itLocalReco +
    offlineBeamSpot + #cmssw_10_6
    otLocalReco +
    caloLocalReco +
    trackerClusterCheck + 
##############################################
    initialStepSequence +
    highPtTripletStepSequence +
##############################################
    generalTracks +
##############################################
#    inclusiveSecondaryVertices + # it would be nice to keep !
#    inclusiveVertexFinder +      # it would be nice to keep !
##############################################
#    newCombinedSeeds +           # used by electron  #defs are in v0
##############################################
    vertexReco
##############################################
#    photonConvTrajSeedFromSingleLeg + #not in v0 or v1 #defs are in v0 just in case
##############################################
#    tripletElectronHitDoublets + #defs are in v0
#    tripletElectronHitTriplets + 
#    tripletElectronSeedLayers + 
#    tripletElectronSeeds + 
#    tripletElectronTrackingRegions + 
)
