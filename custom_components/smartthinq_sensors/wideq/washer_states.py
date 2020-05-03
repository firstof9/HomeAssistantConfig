import enum

from .device import STATE_OPTIONITEM_NONE


# Washer State
class STATE_WASHER(enum.Enum):
    POWER_OFF = STATE_OPTIONITEM_NONE
    ADD_DRAIN = "Add Drain"
    COOLDOWN = "Cooldown"
    DETECTING = "Detecting"
    DETERGENT_AMOUNT = "Detergent Amount"
    DRYING = "Drying"
    END = "End"
    ERROR = "Error"
    ERRORSTATE = "An error occurred"
    ERROR_AUTO_OFF = "Automatic Poweroff Error"
    FROZEN_PREVENT_INITIAL = "Error during initialization"
    FROZEN_PREVENT_PAUSE = "System is being unfrozen, you cannot pause this operation."
    FROZEN_PREVENT_RUNNING = "Unfreezing system, please wait"
    INITIAL = "Select Course"
    PAUSE = "Paused"
    PREWASH = "Pre-Wash"
    REFRESHWITHSTEAM = "Refreshing with steam"
    RESERVE = "Reserved"
    RINSING = "Rinsing"
    RINSE_HOLD = "Rinsing [On Hold]"
    RUNNING = "Washing"
    SPINNING = "Spinning"
    STEAMSOFTENING = "Using softener with steam"
    TCL_ALARM_NORMAL = "Pipe Clogged"


# Washer Temp
class STATE_WASHER_WATERTEMP(enum.Enum):
    OFF = STATE_OPTIONITEM_NONE
    NO_SELECT = "Not selected"
    COLD = "Cold"
    EXTRA_HOT = "Extra Hot"
    HOT = "Hot"
    TAP_COLD = "Tap Cold"
    TEMP_20 = "20℃"
    TEMP_30 = "30℃"
    TEMP_40 = "40℃"
    TEMP_50 = "50℃"
    TEMP_60 = "60℃"
    TEMP_95 = "95℃"
    WARM = "Warm"


# Washesr Spin
class STATE_WASHER_SPINSPEED(enum.Enum):
    OFF = STATE_OPTIONITEM_NONE
    NO_SPIN = "No Spin"
    SPEED_EXTRA_HIGH = "Extra High"
    SPEED_HIGH = "High"
    SPEED_LOW = "Low"
    SPEED_MAX = "Max"
    SPEED_MEDIUM = "Medium"
    SPEED_400 = "400 RPM"
    SPEED_600 = "600 RPM"
    SPEED_700 = "700 RPM"
    SPEED_800 = "800 RPM"
    SPEED_1000 = "1000 RPM"
    SPEED_1100 = "1100 RPM"
    SPEED_1200 = "1200 RPM"
    SPEED_1400 = "1400 RPM"
    SPEED_1600 = "1600 RPM"


# Washer Error
class STATE_WASHER_ERROR(enum.Enum):
    OFF = STATE_OPTIONITEM_NONE
    NO_ERROR = "Normal"
    ERROR_AE = "AE - AquaLock"
    ERROR_CE = "CE - Contact Service Center"
    ERROR_dE1 = "Door open - Please close the door"
    ERROR_dE2 = "Door open - Please close the door"
    ERROR_dE4 = "DE4 - Door open - Please close the door"
    ERROR_dCE = "dCE - Contact Service Center"
    ERROR_dHE = "dHE - Contact Service Center"
    ERROR_EE = "EE - Contact Service Center"
    ERROR_FE = "FE - Contact Service Center"
    ERROR_FF = "The washer is frozen, please warm up the surrounding area."
    ERROR_IE = "No water - Please make sure the water has enough pressure to reach the washer."
    ERROR_LE = "LE - Contact Service Center"
    ERROR_LOE = "Detergent door is open - Please close the detergent door"
    ERROR_OE = "Drain error - Please make sure the pipe is not clogged/frozen"
    ERROR_PE = "PE - Contact Service Center"
    ERROR_PF = "PF - Contact Service Center"
    ERROR_PS = "PS - Contact Service Center"
    ERROR_TE = "tE - Contact Service Center"
    ERROR_UE = "Laundry trim"


"""------------------for Washer"""
WASHERSTATES = {
    "ERROR": STATE_WASHER.ERROR,
    "@WM_STATE_POWER_OFF_W": STATE_WASHER.POWER_OFF,
    "@WM_STATE_ADD_DRAIN_W": STATE_WASHER.ADD_DRAIN,
    "@WM_STATE_COMPLETE_W": STATE_WASHER.END,
    "@WM_STATE_COOLDOWN_W": STATE_WASHER.COOLDOWN,
    "@WM_STATE_DETECTING_W": STATE_WASHER.DETECTING,
    "@WM_STATE_DETERGENT_AMOUNT_W": STATE_WASHER.DETERGENT_AMOUNT,
    "@WM_STATE_DRYING_W": STATE_WASHER.DRYING,
    "@WM_STATE_END_W": STATE_WASHER.END,
    "@WM_STATE_ERROR_W": STATE_WASHER.ERRORSTATE,
    "@WM_STATE_ERROR_AUTO_OFF_W": STATE_WASHER.ERROR_AUTO_OFF,
    "@WM_STATE_FROZEN_PREVENT_INITIAL_W": STATE_WASHER.FROZEN_PREVENT_INITIAL,
    "@WM_STATE_FROZEN_PREVENT_PAUSE_W": STATE_WASHER.FROZEN_PREVENT_PAUSE,
    "@WM_STATE_FROZEN_PREVENT_RUNNING_W": STATE_WASHER.FROZEN_PREVENT_RUNNING,
    "@WM_STATE_INITIAL_W": STATE_WASHER.INITIAL,
    "@WM_STATE_PAUSE_W": STATE_WASHER.PAUSE,
    "@WM_STATE_PREWASH_W": STATE_WASHER.PREWASH,
    "@WM_STATE_REFRESHING_W": STATE_WASHER.REFRESHWITHSTEAM,
    "@WM_STATE_RESERVE_W": STATE_WASHER.RESERVE,
    "@WM_STATE_RINSEHOLD_W": STATE_WASHER.RINSE_HOLD,
    "@WM_STATE_RINSING_W": STATE_WASHER.RINSING,
    "@WM_STATE_RUNNING_W": STATE_WASHER.RUNNING,
    "@WM_STATE_SPINNING_W": STATE_WASHER.SPINNING,
    "@WM_STATE_STEAMSOFTENING_W": STATE_WASHER.STEAMSOFTENING,
    "TCL_ALARM_NORMAL": STATE_WASHER.TCL_ALARM_NORMAL,
}

WASHERWATERTEMPS = {
    "-": STATE_WASHER_WATERTEMP.OFF,
    "OFF": STATE_WASHER_WATERTEMP.OFF,
    "@WM_TERM_NO_SELECT_W": STATE_WASHER_WATERTEMP.NO_SELECT,
    "@WM_OPTION_TEMP_COLD_W": STATE_WASHER_WATERTEMP.COLD,
    "@WM_OPTION_TEMP_TAP_COLD_W": STATE_WASHER_WATERTEMP.TAP_COLD,
    "@WM_OPTION_TEMP_WARM_W": STATE_WASHER_WATERTEMP.WARM,
    "@WM_OPTION_TEMP_HOT_W": STATE_WASHER_WATERTEMP.HOT,
    "@WM_OPTION_TEMP_EXTRA_HOT_W": STATE_WASHER_WATERTEMP.EXTRA_HOT,
    "@WM_TITAN2_OPTION_TEMP_COLD_W": STATE_WASHER_WATERTEMP.COLD,
    "@WM_TITAN2_OPTION_TEMP_20_W": STATE_WASHER_WATERTEMP.TEMP_20,
    "@WM_TITAN2_OPTION_TEMP_30_W": STATE_WASHER_WATERTEMP.TEMP_30,
    "@WM_TITAN2_OPTION_TEMP_40_W": STATE_WASHER_WATERTEMP.TEMP_40,
    "@WM_TITAN2_OPTION_TEMP_50_W": STATE_WASHER_WATERTEMP.TEMP_50,
    "@WM_TITAN2_OPTION_TEMP_60_W": STATE_WASHER_WATERTEMP.TEMP_60,
    "@WM_TITAN2_OPTION_TEMP_95_W": STATE_WASHER_WATERTEMP.TEMP_95,
    "@WM_FL24_TITAN_TEMP_COLD_W": STATE_WASHER_WATERTEMP.COLD,
    "@WM_FL24_TITAN_TEMP_20_W": STATE_WASHER_WATERTEMP.TEMP_20,
    "@WM_FL24_TITAN_TEMP_30_W": STATE_WASHER_WATERTEMP.TEMP_30,
    "@WM_FL24_TITAN_TEMP_40_W": STATE_WASHER_WATERTEMP.TEMP_40,
    "@WM_FL24_TITAN_TEMP_50_W": STATE_WASHER_WATERTEMP.TEMP_50,
    "@WM_FL24_TITAN_TEMP_60_W": STATE_WASHER_WATERTEMP.TEMP_60,
    "@WM_FL24_TITAN_TEMP_95_W": STATE_WASHER_WATERTEMP.TEMP_95,
}

WASHERSPINSPEEDS = {
    "-": STATE_WASHER_SPINSPEED.OFF,
    "OFF": STATE_WASHER_SPINSPEED.OFF,
    "@WM_OPTION_SPIN_NO_SPIN_W": STATE_WASHER_SPINSPEED.NO_SPIN,
    "@WM_OPTION_SPIN_LOW_W": STATE_WASHER_SPINSPEED.SPEED_LOW,
    "@WM_OPTION_SPIN_MEDIUM_W": STATE_WASHER_SPINSPEED.SPEED_MEDIUM,
    "@WM_OPTION_SPIN_HIGH_W": STATE_WASHER_SPINSPEED.SPEED_HIGH,
    "@WM_OPTION_SPIN_EXTRA_HIGH_W": STATE_WASHER_SPINSPEED.SPEED_EXTRA_HIGH,
    "@WM_TITAN2_OPTION_SPIN_NO_SPIN_W": STATE_WASHER_SPINSPEED.NO_SPIN,
    "@WM_TITAN2_OPTION_SPIN_400_W": STATE_WASHER_SPINSPEED.SPEED_400,
    "@WM_TITAN2_OPTION_SPIN_600_W": STATE_WASHER_SPINSPEED.SPEED_600,
    "@WM_TITAN2_OPTION_SPIN_700_W": STATE_WASHER_SPINSPEED.SPEED_700,
    "@WM_TITAN2_OPTION_SPIN_800_W": STATE_WASHER_SPINSPEED.SPEED_800,
    "@WM_TITAN2_OPTION_SPIN_1000_W": STATE_WASHER_SPINSPEED.SPEED_1000,
    "@WM_TITAN2_OPTION_SPIN_1100_W": STATE_WASHER_SPINSPEED.SPEED_1100,
    "@WM_TITAN2_OPTION_SPIN_1200_W": STATE_WASHER_SPINSPEED.SPEED_1200,
    "@WM_TITAN2_OPTION_SPIN_1400_W": STATE_WASHER_SPINSPEED.SPEED_1400,
    "@WM_TITAN2_OPTION_SPIN_1600_W": STATE_WASHER_SPINSPEED.SPEED_1600,
    "@WM_TITAN2_OPTION_SPIN_MAX_W": STATE_WASHER_SPINSPEED.SPEED_MAX,
    "@WM_FL24_TITAN_SPIN_NO_SPIN_W": STATE_WASHER_SPINSPEED.NO_SPIN,
    "@WM_FL24_TITAN_SPIN_SPEED_400_W": STATE_WASHER_SPINSPEED.SPEED_400,
    "@WM_FL24_TITAN_SPIN_SPEED_600_W": STATE_WASHER_SPINSPEED.SPEED_600,
    "@WM_FL24_TITAN_SPIN_SPEED_700_W": STATE_WASHER_SPINSPEED.SPEED_700,
    "@WM_FL24_TITAN_SPIN_SPEED_800_W": STATE_WASHER_SPINSPEED.SPEED_800,
    "@WM_FL24_TITAN_SPIN_SPEED_1000_W": STATE_WASHER_SPINSPEED.SPEED_1000,
    "@WM_FL24_TITAN_SPIN_SPEED_1100_W": STATE_WASHER_SPINSPEED.SPEED_1100,
    "@WM_FL24_TITAN_SPIN_SPEED_1200_W": STATE_WASHER_SPINSPEED.SPEED_1200,
    "@WM_FL24_TITAN_SPIN_SPEED_1400_W": STATE_WASHER_SPINSPEED.SPEED_1400,
    "@WM_FL24_TITAN_SPIN_SPEED_1600_W": STATE_WASHER_SPINSPEED.SPEED_1600,
    "@WM_FL24_TITAN_SPIN_SPEED_MAX_W": STATE_WASHER_SPINSPEED.SPEED_MAX,
}

WASHREFERRORS = {
    "OFF": STATE_WASHER_ERROR.OFF,
    "No Error": STATE_WASHER_ERROR.NO_ERROR,
    "AE Error (AquaLock)": STATE_WASHER_ERROR.ERROR_AE,
    "CE Error": STATE_WASHER_ERROR.ERROR_CE,
    "DE1 Error": STATE_WASHER_ERROR.ERROR_dE1,
    "DE2 Error": STATE_WASHER_ERROR.ERROR_dE2,
    "DE4 Error": STATE_WASHER_ERROR.ERROR_dE4,
    "DCE Error": STATE_WASHER_ERROR.ERROR_dCE,
    "DHE Error": STATE_WASHER_ERROR.ERROR_dHE,
    "EE Error": STATE_WASHER_ERROR.ERROR_EE,
    "FE Error": STATE_WASHER_ERROR.ERROR_FE,
    "FF Error": STATE_WASHER_ERROR.ERROR_FF,
    "IE Error": STATE_WASHER_ERROR.ERROR_IE,
    "LE Error": STATE_WASHER_ERROR.ERROR_LE,
    "LOE Error": STATE_WASHER_ERROR.ERROR_LOE,
    "OE Error": STATE_WASHER_ERROR.ERROR_OE,
    "PE Error": STATE_WASHER_ERROR.ERROR_PE,
    "PF Error": STATE_WASHER_ERROR.ERROR_PF,
    "PS Error": STATE_WASHER_ERROR.ERROR_PS,
    "TE Error": STATE_WASHER_ERROR.ERROR_TE,
    "UE Error": STATE_WASHER_ERROR.ERROR_UE,
}

# this is not used
WASHERERRORS = {
    "OFF": STATE_WASHER_ERROR.OFF,
    "ERROR_NOERROR": STATE_WASHER_ERROR.NO_ERROR,
    "@WM_WW_FL_ERROR_AE_W": STATE_WASHER_ERROR.ERROR_AE,
    "@WM_WW_FL_ERROR_CE_W": STATE_WASHER_ERROR.ERROR_CE,
    "@WM_WW_FL_ERROR_DE1_W": STATE_WASHER_ERROR.ERROR_dE1,
    "@WM_WW_FL_ERROR_DE2_W": STATE_WASHER_ERROR.ERROR_dE2,
    "@WM_WW_FL_ERROR_DE4_W": STATE_WASHER_ERROR.ERROR_dE4,
    "@WM_WW_FL_ERROR_DCE_W": STATE_WASHER_ERROR.ERROR_dCE,
    "@WM_WW_FL_ERROR_DHE_W": STATE_WASHER_ERROR.ERROR_dHE,
    "@WM_WW_FL_ERROR_EE_W": STATE_WASHER_ERROR.ERROR_EE,
    "@WM_WW_FL_ERROR_FE_W": STATE_WASHER_ERROR.ERROR_FE,
    "@WM_WW_FL_ERROR_FF_W": STATE_WASHER_ERROR.ERROR_FF,
    "@WM_WW_FL_ERROR_IE_W": STATE_WASHER_ERROR.ERROR_IE,
    "@WM_WW_FL_ERROR_LE_W": STATE_WASHER_ERROR.ERROR_LE,
    "@WM_WW_FL_ERROR_LOE_W": STATE_WASHER_ERROR.ERROR_LOE,
    "@WM_WW_FL_ERROR_OE_W": STATE_WASHER_ERROR.ERROR_OE,
    "@WM_WW_FL_ERROR_PE_W": STATE_WASHER_ERROR.ERROR_PE,
    "@WM_WW_FL_ERROR_PF_W": STATE_WASHER_ERROR.ERROR_PF,
    "@WM_WW_FL_ERROR_PS_W": STATE_WASHER_ERROR.ERROR_PS,
    "@WM_WW_FL_ERROR_TE_W": STATE_WASHER_ERROR.ERROR_TE,
    "@WM_WW_FL_ERROR_UE_W": STATE_WASHER_ERROR.ERROR_UE,
}
