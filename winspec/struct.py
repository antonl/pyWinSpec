from ctypes import *

# Definitions of types
BYTE = c_ubyte
WORD = c_ushort
DWORD = c_uint

# long is 4 bytes in the manual. It is 8 bytes on my machine

# Lengths of arrays used in header
HDRNAMEMAX = 120
USERINFOMAX = 1000
COMMENTMAX = 80
LABELMAX = 16
FILEVERMAX = 16
DATEMAX = 10
ROIMAX = 10
TIMEMAX = 7

class ROIinfo(Structure):
    _pack_ = 1

    _fields_ = [
        ('startx', WORD), 
        ('endx', WORD),
        ('groupx', WORD),
        ('starty', WORD),
        ('endy', WORD),
        ('groupy', WORD)]

class AxisCalibration(Structure):
    _pack_ = 1

    _fields_ = [
        ('offset', c_double), 
        ('factor', c_double),
        ('current_unit', c_char),
        ('reserved1', c_char),
        ('string', c_char * 40),
        ('reserved2', c_char * 40), 
        ('calib_valid', c_char),
        ('input_unit', c_char),
        ('polynom_unit', c_char),
        ('polynom_order', c_char),
        ('calib_count', c_char),
        ('pixel_position', c_double * 10),
        ('calib_value', c_double * 10), 
        ('polynom_coeff', c_double * 6),
        ('laser_position', c_double),
        ('reserved3', c_char),
        ('new_calib_flag', BYTE),
        ('calib_label', c_char * 81),
        ('expansion', c_char * 87)]

class Header(Structure):
    _pack_ = 1

    # Header fields
    _fields_ = [
        ('ControllerVersion', c_short),
        ('LogicOutput', c_short),
        ('AmpHiCapLowNoise', WORD),
        ('xDimDet', WORD),
        ('mode', c_short),
        ('exp_sec', c_float),
        ('VChipXdim', c_short),
        ('VChipYdim', c_short),
        ('yDimDet', WORD),
        ('date', c_char * DATEMAX),
        ('VirtualChipFlag', c_short),
        ('Spare_1', c_char * 2), # Unused data
        ('noscan', c_short),
        ('DetTemperature', c_float),
        ('DetType', c_short),
        ('xdim', WORD),
        ('stdiode', c_short),
        ('DelayTime', c_float),
        ('ShutterControl', WORD),
        ('AbsorbLive', c_short),
        ('AbsorbMode', WORD),
        ('CanDoVirtualChipFlag', c_short),
        ('ThresholdMinLive', c_short),
        ('ThresholdMinVal', c_float), 
        ('ThresholdMaxLive', c_short), 
        ('ThresholdMaxVal', c_float),
        ('SpecAutoSpectroMode', c_short),
        ('SpecCenterWlNm', c_float),
        ('SpecGlueFlag', c_short),
        ('SpecGlueStartWlNm', c_float),
        ('SpecGlueEndWlNm', c_float),
        ('SpecGlueMinOvrlpNm', c_float),
        ('SpecGlueFinalResNm', c_float),
        ('PulserType', c_short),
        ('CustomChipFlag', c_short),
        ('XPrePixels', c_short),
        ('XPostPixels', c_short),
        ('YPrePixels', c_short),
        ('YPostPixels', c_short),
        ('asynen', c_short),
        ('datatype', c_short), # 0 - float, 1 - long, 2 - short, 3 - ushort
        ('PulserMode', c_short),
        ('PulserOnChipAccums', WORD),
        ('PulserRepeatExp', DWORD),
        ('PulseRepWidth', c_float),
        ('PulseRepDelay', c_float),
        ('PulseSeqStartWidth', c_float),
        ('PulseSeqEndWidth', c_float),
        ('PulseSeqStartDelay', c_float),
        ('PulseSeqEndDelay', c_float),
        ('PulseSeqIncMode', c_short),
        ('PImaxUsed', c_short),
        ('PImaxMode', c_short),
        ('PImaxGain', c_short),
        ('BackGrndApplied', c_short),
        ('PImax2nsBrdUsed', c_short),
        ('minblk', WORD),
        ('numminblk', WORD),
        ('SpecMirrorLocation', c_short * 2),
        ('SpecSlitLocation', c_short * 4),
        ('CustomTimingFlag', c_short),
        ('ExperimentTimeLocal', c_char * TIMEMAX),
        ('ExperimentTimeUTC', c_char * TIMEMAX),
        ('ExposUnits', c_short),
        ('ADCoffset', WORD),
        ('ADCrate', WORD),
        ('ADCtype', WORD),
        ('ADCresolution', WORD),
        ('ADCbitAdjust', WORD),
        ('gain', WORD),
        ('Comments', c_char * 5 * COMMENTMAX),
        ('geometric', WORD), # x01 - rotate, x02 - reverse, x04 flip
        ('xlabel', c_char * LABELMAX),
        ('cleans', WORD),
        ('NumSkpPerCln', WORD),
        ('SpecMirrorPos', c_short * 2),
        ('SpecSlitPos', c_float * 4), 
        ('AutoCleansActive', c_short),
        ('UseContCleansInst', c_short),
        ('AbsorbStripNum', c_short), 
        ('SpecSlipPosUnits', c_short),
        ('SpecGrooves', c_float),
        ('srccmp', c_short),
        ('ydim', WORD), 
        ('scramble', c_short),
        ('ContinuousCleansFlag', c_short), 
        ('ExternalTriggerFlag', c_short), 
        ('lnoscan', c_int), # Longs are 4 bytes  
        ('lavgexp', c_int), # 4 bytes
        ('ReadoutTime', c_float), 
        ('TriggeredModeFlag', c_short), 
        ('Spare_2', c_char * 10), 
        ('sw_version', c_char * FILEVERMAX), 
        ('type', c_short),
        ('flatFieldApplied', c_short), 
        ('Spare_3', c_char * 16), 
        ('kin_trig_mode', c_short), 
        ('dlabel', c_char * LABELMAX), 
        ('Spare_4', c_char * 436), 
        ('PulseFileName', c_char * HDRNAMEMAX), 
        ('AbsorbFileName', c_char * HDRNAMEMAX),
        ('NumExpRepeats', DWORD),
        ('NumExpAccums', DWORD),
        ('YT_Flag', c_short), 
        ('clkspd_us', c_float),
        ('HWaccumFlag', c_short),
        ('StoreSync', c_short),
        ('BlemishApplied', c_short),
        ('CosmicApplied', c_short), 
        ('CosmicType', c_short),
        ('CosmicThreshold', c_float), 
        ('NumFrames', c_int),
        ('MaxIntensity', c_float),
        ('MinIntensity', c_float),
        ('ylabel', c_char * LABELMAX),
        ('ShutterType', WORD),
        ('shutterComp', c_float),
        ('readoutMode', WORD),
        ('WindowSize', WORD),
        ('clkspd', WORD),
        ('interface_type', WORD),
        ('NumROIsInExperiment', c_short),
        ('Spare_5', c_char * 16),
        ('controllerNum', WORD),
        ('SWmade', WORD),
        ('NumROI', c_short),
        ('ROIinfblk', ROIinfo * ROIMAX),
        ('FlatField', c_char * HDRNAMEMAX),
        ('background', c_char * HDRNAMEMAX),
        ('blemish', c_char * HDRNAMEMAX),
        ('file_header_ver', c_float),
        ('YT_Info', c_char * 1000),
        ('WinView_id', c_int),
        ('xcalibration', Calibration),
        ('ycalibration', Calibration),
        ('Istring', c_char * 40),
        ('Spare_6', c_char * 25),
        ('SpecType', BYTE),
        ('SpecModel', BYTE),
        ('PulseBurstUsed', BYTE),
        ('PulseBurstCount', DWORD),
        ('PulseBurstPeriod', c_double),
        ('PulseBracketUsed', BYTE),
        ('PulseBracketType', BYTE),
        ('PulseTimeConstFast', c_double),
        ('PulseAmplitudeFast', c_double),
        ('PulseTimeConstSlow', c_double),
        ('PulseAmplitudeSlow', c_double),
        ('AnalogGain', c_short),
        ('AvGainUsed', c_short),
        ('AvGain', c_short),
        ('lastvalue', c_short)]

    def __repr__(self):
        return 'SPE File\n\t{:d}x{:d} area, {:d} frames\n\tTaken on {:s}'\
                .format(self.xdim, self.ydim, self.NumFrames, self.date)

