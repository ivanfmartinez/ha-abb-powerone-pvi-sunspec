from homeassistant.const import (
    DEVICE_CLASS_CURRENT,
    DEVICE_CLASS_ENERGY,
    DEVICE_CLASS_POWER,
    DEVICE_CLASS_TEMPERATURE,
    DEVICE_CLASS_VOLTAGE,
)

DOMAIN = "abb_powerone_pvi_sunspec"
CONF_NAME = "ABB Power-One"
DEFAULT_NAME = "ABB Power-One"
CONF_HOST = ""
CONF_PORT = 502
DEFAULT_PORT = 502
CONF_SLAVE_ID = 2
DEFAULT_SLAVE_ID = 2
CONF_SCAN_INTERVAL = 60
DEFAULT_SCAN_INTERVAL = 60
MANUFACTURER = "ABB Power-One"
ATTR_STATUS_DESCRIPTION = "status_description"
ATTR_MANUFACTURER = "ABB Power-One"

SENSOR_TYPES = {
    "Manufacturer": ["Manufacturer", "comm_manufact", None, "mdi:information-outline", None],
    "Model": ["Model", "comm_model", None, "mdi:information-outline", None],
    "Options": ["Options", "comm_options", None, "mdi:information-outline", None],
    "Version": ["Firmware Version", "comm_version", None, "mdi:information-outline", None],
    "Serial": ["Serial", "comm_sernum", None, "mdi:information-outline", None],
    "AC_Current": ["AC Current", "accurrent", "A", "mdi:current-ac", DEVICE_CLASS_CURRENT],
    "AC_CurrentA": ["AC Current A", "accurrenta", "A", "mdi:current-ac", DEVICE_CLASS_CURRENT],
    "AC_CurrentB": ["AC Current B", "accurrentb", "A", "mdi:current-ac", DEVICE_CLASS_CURRENT],
    "AC_CurrentC": ["AC Current C", "accurrentc", "A", "mdi:current-ac", DEVICE_CLASS_CURRENT],
    "AC_VoltageAB": ["AC Voltage AB", "acvoltageab", "V", "mdi:lightning-bolt", DEVICE_CLASS_VOLTAGE],
    "AC_VoltageBC": ["AC Voltage BC", "acvoltagebc", "V", "mdi:lightning-bolt", DEVICE_CLASS_VOLTAGE],
    "AC_VoltageCA": ["AC Voltage CA", "acvoltageca", "V", "mdi:lightning-bolt", DEVICE_CLASS_VOLTAGE],
    "AC_VoltageAN": ["AC Voltage AN", "acvoltagean", "V", "mdi:lightning-bolt", DEVICE_CLASS_VOLTAGE],
    "AC_VoltageBN": ["AC Voltage BN", "acvoltagebn", "V", "mdi:lightning-bolt", DEVICE_CLASS_VOLTAGE],
    "AC_VoltageCN": ["AC Voltage CN", "acvoltagecn", "V", "mdi:lightning-bolt", DEVICE_CLASS_VOLTAGE],
    "AC_Power": ["AC Power", "acpower", "W", "mdi:solar-power", DEVICE_CLASS_POWER],
    "AC_Frequency": ["AC Frequency", "acfreq", "Hz", "mdi:sine-wave", None],
    "AC_Energy": ["AC Energy", "acenergy", "kWh", "mdi:solar-power", DEVICE_CLASS_ENERGY],
    "DC_Power": ["DC Power", "dcpower", "W", "mdi:solar-power", DEVICE_CLASS_POWER],
    "DC1_Curr": ["DC1 current", "dc1curr", "A", "mdi:current-ac", DEVICE_CLASS_CURRENT],
    "DC1_Volt": ["DC1 voltage", "dc1volt", "V", "mdi:lightning-bolt", DEVICE_CLASS_VOLTAGE],
    "DC1_Power": ["DC1 power", "dc1power", "W", "mdi:solar-power", DEVICE_CLASS_POWER],
    "DC2_Curr": ["DC2 current", "dc2curr", "A", "mdi:current-ac", DEVICE_CLASS_CURRENT],
    "DC2_Volt": ["DC2 voltage", "dc2volt", "V", "mdi:lightning-bolt", DEVICE_CLASS_VOLTAGE],
    "DC2_Power": ["DC2 power", "dc2power", "W", "mdi:solar-power", DEVICE_CLASS_POWER],
    "Status": ["Operating State", "status", None, "mdi:information-outline", None],
    "Status_Vendor": ["Vendor Operating State", "statusvendor", None, "mdi:information-outline", None],
    "Temp_Cab": ["Ambient Temperature", "tempcab", "°C", "mdi:temperature-celsius", DEVICE_CLASS_TEMPERATURE],
    "Temp_Oth": ["Inverter Temperature", "tempoth", "°C", "mdi:temperature-celsius", DEVICE_CLASS_TEMPERATURE],
}

DEVICE_MODEL = {
    49: "PVI-3.0-OUTD",
    50: "PVI-3.3-OUTD",
    51: "PVI-3.6-OUTD",
    52: "PVI-4.2-OUTD",
    53: "PVI-5000-OUTD",
    54: "PVI-6000-OUTD",
    65: "PVI-CENTRAL-350 Liquid Cooled (AC gathering)",
    66: "PVI-CENTRAL-350 Liquid Cooled (display board)",
    67: "PVI-CENTRAL-50 module",
    68: "PVI-12.5-OUTD",
    69: "PVI-CENTRAL-67 module",
    70: "TRIO-27.6-TL-OUTD (output 480 VAC)",
    71: "UNO-2.5-OUTD",
    72: "PVI-4.6-OUTD-I",
    74: "PVI-1700-OUTD",
    76: "PVI-CENTRAL-350 Liquid Cooled (control board)",
    77: "PVI-CENTRAL-250",
    78: "PVI-12.5-OUTD Universal (output 400 VAC)",
    79: "PVI-3600-OUTD",
    80: "3-phase interface (3G74)",
    81: "PVI-8.0-OUTD Universal PLUS (output 400 VAC)",
    84: "PVI-12.5-OUTD-I (output 480 VAC)",
    85: "PVI-12.5-OUTD-I (output 208 VAC)",
    86: "PVI-12.5-OUTD-I (output 380 VAC)",
    88: "PVI-10.0-OUTD",
    89: "TRIO-27.6-TL-OUTD (output 400 VAC)",
    90: "PVI-12.5-OUTD-I (output 600 VAC)",
    99: "CDD",
    102: "TRIO-20-TL-OUTD (output 480 VAC)",
    103: "UNO-2.0-OUTD",
    104: "PVI-3.8-OUTD-I",
    105: "PVI-2000-IND",
    106: "PVI-1700-IND",
    108: "PVI-3600-IND",
    110: "PVI-10.0-OUTD Universal (output 400 VAC)",
    111: "PVI-2000-OUTD",
    113: "PVI-8.0-OUTD Universal (output 400 VAC)",
    116: "PVI-10.0-OUTD-I (output 480 VAC)",
    117: "PVI-10.0-OUTD-I (output 208 VAC)",
    118: "PVI-10.0-OUTD-I (output 380 VAC)",
    119: "PVI-10.0-I-OUTD (output 480 VAC – current limit 12 A)",
    121: "TRIO-20-TL-OUTD (output 400 VAC)",
    122: "PVI-10.0-OUTD-I (output 600 VAC)",
}

DEVICE_GLOBAL_STATUS = {
    0: "Sending Parameters",
    1: "Wait Sun/Grid",
    2: "Checking Grid",
    3: "Measuring Riso",
    4: "DcDc Start",
    5: "Inverter Start",
    6: "Run",
    7: "Recovery",
    8: "Pause",
    9: "Ground Fault",
    10: "OTH Fault",
    11: "Address Setting",
    12: "Self Test",
    13: "Self Test Fail",
    14: "Sensor Test + Measure Riso",
    15: "Leak Fault",
    16: "Waiting for manual reset",
    17: "Internal Error E026",
    18: "Internal Error E027",
    19: "Internal Error E028",
    20: "Internal Error E029",
    21: "Internal Error E030",
    22: "Sending Wind Table",
    23: "Failed Sending table",
    24: "UTH Fault",
    25: "Remote OFF",
    26: "Interlock Fail",
    27: "Executing Autotest",
    30: "Waiting Sun",
    31: "Temperature Fault",
    32: "Fan Staucked",
    33: "Int. Com. Fault",
    34: "Slave Insertion",
    35: "DC Switch Open",
    36: "TRAS Switch Open",
    37: "MASTER Exclusion",
    38: "Auto Exclusion",
    98: "Erasing Internal EEprom",
    99: "Erasing External EEprom",
    100: "Counting EEprom",
    101: "Freeze",
    200: "Dsp Programming",
}

DEVICE_STATUS = {
    0: "Stand By",
    1: "Checking Grid",
    2: "Run",
    3: "Bulk OV",
    4: "Out OC",
    5: "IGBT Sat",
    6: "Bulk UV",
    7: "Degauss Error",
    8: "No Parameters",
    9: "Bulk Low",
    10: "Grid OV",
    11: "Communication Error",
    12: "Degaussing",
    13: "Starting",
    14: "Bulk Cap Fail",
    15: "Leak Fail",
    16: "DcDc Fail",
    17: "Ileak Sensor Fail",
    18: "SelfTest: relay inverter",
    19: "SelfTest: wait for sensor test",
    20: "SelfTest: test relay DcDc + sensor",
    21: "SelfTest: relay inverter fail",
    22: "SelfTest timeout fail",
    23: "SelfTest: relay DcDc fail",
    24: "Self Test 1",
    25: "Waiting self test start",
    26: "Dc Injection",
    27: "Self Test 2",
    28: "Self Test 3",
    29: "Self Test 4",
    30: "Internal Error",
    31: "Internal Error",
    40: "Forbidden State",
    41: "Input UC",
    42: "Zero Power",
    43: "Grid Not Present",
    44: "Waiting Start",
    45: "MPPT",
    46: "Grid Fail",
    47: "Input OC",
    255: "Inverter Dsp not programmed",
}